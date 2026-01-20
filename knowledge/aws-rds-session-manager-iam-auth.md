# Secure RDS Connectivity with Session Manager and IAM Auth

## Problem

Traditional bastion host approach has downsides:
- Increased attack surface when server exposed to public internet
- Need to store and maintain SSH keys
- Burden of managing database usernames/passwords

## Solution: Session Manager + IAM Database Authentication

Use AWS Systems Manager Session Manager with port forwarding to a remote host, combined with IAM database authentication. No bastion host exposed to internet, no SSH keys, no database passwords.

## Architecture Flow

1. Start Session Manager session to an EC2 instance in private subnet using `AWS-StartPortForwardingSessionToRemoteHost` document
2. SSM agent on EC2 processes request via SSM VPC endpoints
3. Port forwarding established - local traffic tunneled to remote host
4. Generate IAM database auth token using AWS CLI
5. Connect to RDS through tunnel using the token

## Prerequisites

- AWS CLI and Session Manager plugin installed locally
- EC2 instance in private subnet with SSM agent (Amazon Linux has it)
- VPC endpoints for Systems Manager API calls
- RDS instance with IAM database authentication enabled
- psql/mysql client locally

## Setup Steps

### 1. EC2 Instance (Bastion)

- Place in private subnet
- No public IP needed
- Security group: outbound 443 to VPC CIDR (for SSM endpoints)
- IAM role with `AmazonSSMManagedInstanceCore` policy
- No SSH key pair needed

### 2. RDS IAM Authentication

Enable IAM DB auth on RDS instance, then create database user with `rds_iam` role:

```sql
CREATE USER db_user WITH LOGIN;
GRANT rds_iam TO db_user;
```

### 3. IAM Policy for DB Access

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "rds-db:connect",
      "Resource": "arn:aws:rds-db:REGION:ACCOUNT:dbuser:DBI-RESOURCE-ID/db_user"
    }
  ]
}
```

### 4. Connect

```bash
# Set RDS endpoint
export RDSHOST="mydb.123456789012.eu-central-1.rds.amazonaws.com"

# Generate auth token (valid 15 min)
export PGPASSWORD="$(aws rds generate-db-auth-token \
  --hostname $RDSHOST --port 5432 --region eu-central-1 --username db_user)"

# Add to /etc/hosts (required for SSL cert verification)
echo "127.0.0.1 $RDSHOST" | sudo tee -a /etc/hosts

# Start port forwarding session (terminal 1)
aws ssm start-session \
  --target i-0123456789abcdef0 \
  --document-name AWS-StartPortForwardingSessionToRemoteHost \
  --parameters host="$RDSHOST",portNumber="5432",localPortNumber="1053"

# Connect via psql (terminal 2)
psql "host=$RDSHOST port=1053 sslmode=verify-full sslrootcert=rds-ca-bundle.pem dbname=postgres user=db_user"
```

## Key Points

- **Auth token lifetime**: 15 minutes, but doesn't affect existing connections
- **SSL verification**: Must use RDS endpoint hostname (not localhost) because cert CN matches endpoint
- **No internet exposure**: EC2 communicates with SSM via VPC endpoints only
- **Audit trail**: Session Manager logs all session activity

## Benefits Over Traditional Bastion

| Traditional Bastion | Session Manager Approach |
|---------------------|-------------------------|
| Public subnet, public IP | Private subnet, no public IP |
| SSH keys to manage | No keys needed |
| DB passwords | IAM tokens (auto-rotate) |
| Port 22 open | No inbound ports |
| Manual audit | CloudTrail + Session Manager logs |

## Source

https://aws.amazon.com/blogs/database/securely-connect-to-amazon-rds-for-postgresql-with-aws-session-manager-and-iam-authentication/
