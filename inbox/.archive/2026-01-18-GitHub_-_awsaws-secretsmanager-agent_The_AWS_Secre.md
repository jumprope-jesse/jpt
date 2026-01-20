---
type: link
source: notion
url: https://github.com/aws/aws-secretsmanager-agent
notion_type: Software Repo
tags: ['Running']
created: 2024-07-12T04:16:00.000Z
---

# GitHub - aws/aws-secretsmanager-agent: The AWS Secrets Manager Agent is a local HTTP service that you can install and use in your compute environments to read secrets from Secrets Manager and cache them in memory.

## AI Summary (from Notion)
- Overview: AWS Secrets Manager Agent is a local HTTP service for reading and caching secrets from AWS Secrets Manager.
- Functionality:
- Provides a standardized way to access secrets across various AWS services (e.g., Lambda, ECS, EKS).
- Caches secrets in memory for quick access, reducing the need to repeatedly call Secrets Manager.
- Only supports read requests; cannot modify secrets.
- Configuration:
- Configurable settings include connection limits, cache size, TTL, and HTTP port.
- Requires AWS credentials to make calls to Secrets Manager.
- Security:
- Protects against SSRF by requiring a token for requests.
- Secrets are not encrypted in cache, which raises security considerations.
- Installation Options:
- Can be installed on various platforms including Docker containers, Amazon EKS, ECS, or as a Lambda extension.
- Build Process:
- Detailed steps provided for building the agent on RPM-based, Debian-based systems, and Windows.
- Cross-compilation instructions are available for different environments.
- Usage:
- Secrets can be retrieved via local HTTP endpoints using tools like curl and programming languages like Python.
- Logging:
- Logs errors locally and does not integrate with cloud logging services.
- Each log file is capped at 10 MB, with a maximum of five log files retained.
- Interesting Facts:
- Default TTL for cached secrets is 300 seconds but is configurable.
- The agent architecture allows legacy applications to access secrets securely.
- The performance and security of the agent can be improved by using appropriate IAM roles and policies.

## Content (from Notion)

# AWS Secrets Manager Agent

The AWS Secrets Manager Agent is a client-side HTTP service that you can use to standardize consumption of secrets from Secrets Manager across environments such as AWS Lambda, Amazon Elastic Container Service, Amazon Elastic Kubernetes Service, and Amazon Elastic Compute Cloud. The Secrets Manager Agent can retrieve and cache secrets in memory so that your applications can consume secrets directly from the cache. That means you can fetch the secrets your application needs from the localhost instead of making calls to Secrets Manager. The Secrets Manager Agent can only make read requests to Secrets Manager - it can't modify secrets.

The Secrets Manager Agent uses the AWS credentials you provide in your environment to make calls to Secrets Manager. The Secrets Manager Agent offers protection against Server Side Request Forgery (SSRF) to help improve secret security. You can configure the Secrets Manager Agent by setting the maximum number of connections, the time to live (TTL), the localhost HTTP port, and the cache size.

Because the Secrets Manager Agent uses an in-memory cache, it resets when the Secrets Manager Agent restarts. The Secrets Manager Agent periodically refreshes the cached secret value. The refresh happens when you try to read a secret from the Secrets Manager Agent after the TTL has expired. The default refresh frequency (TTL) is 300 seconds, and you can change it by using a Configuration file which you pass to the Secrets Manager Agent using the --config command line argument. The Secrets Manager Agent does not include cache invalidation. For example, if a secret rotates before the cache entry expires, the Secrets Manager Agent might return a stale secret value.

The Secrets Manager Agent returns secret values in the same format as the response of GetSecretValue. Secret values are not encrypted in the cache.

To download the source code, see https://github.com/aws/aws-secretsmanager-agent on GitHub.

Topics

- AWS Secrets Manager Agent 
## Step 1: Build the Secrets Manager Agent binary

To build the Secrets Manager Agent binary natively, you need the standard development tools and the Rust tools. Alternatively, you can cross-compile for systems that support it, or you can use Rust cross to cross-compile.

### [ RPM-based systems ]

1.  
1.  
1.   
### [ Debian-based systems ]

1.  
1.  
1.   
### [ Windows ]

To build on Windows, follow the instructions at Set up your dev environment on Windows for Rust in the Microsoft Windows documentation.

### [ Cross-compile natively ]

On distributions where the mingw-w64 package is available such as Ubuntu, you can cross compile natively.

```plain text
# Install the cross compile tool chain
sudo add-apt-repository universe
sudo apt install -y mingw-w64

# Install the rust build targets
rustup target add x86_64-pc-windows-gnu

# Cross compile the agent for Windows
cargo build --release --target x86_64-pc-windows-gnu
```

You will find the executable at target/x86_64-pc-windows-gnu/release/aws-secrets-manager-agent.exe.

### [ Cross compile with Rust cross ]

If the cross compile tools are not available natively on the system, you can use the Rust cross project. For more information, see https://github.com/cross-rs/cross.

Important

We recommend 32GB disk space for the build environment.

```plain text
# Install and start docker
sudo yum -y install docker
sudo systemctl start docker
sudo systemctl enable docker # Make docker start after reboot

# Give ourselves permission to run the docker images without sudo
sudo usermod -aG docker $USER
newgrp docker

# Install cross and cross compile the executable
cargo install cross
cross build --release --target x86_64-pc-windows-gnu
```

## Step 2: Install the Secrets Manager Agent

Based on the type of compute, you have several options for installing the Secrets Manager Agent.

### [ Amazon EKS and Amazon ECS ]

To install the Secrets Manager Agent

1.  
1.  
### [ Docker ]

You can run the Secrets Manager Agent as a sidecar container alongside your application by using Docker. Then your application can retrieve secrets from the local HTTP server the Secrets Manager Agent provides. For information about Docker, see the Docker documentation.

To create a sidecar container for the Secrets Manager Agent with Docker

1.  
1. 
1.  
1. 
1.  
1. 
### [ AWS Lambda ]

You can package the Secrets Manager Agent as an AWS Lambda extension. Then you can add it to your Lambda function as a layer and call the Secrets Manager Agent from your Lambda function to get secrets. For an example script that shows how to run the Secrets Manager Agent as an extension, see secrets-manager-agent-extension.sh in https://github.com/aws/aws-secretsmanager-agent.

To create a Lambda extension that packages the Secrets Manager Agent

1. 
1. 
1. 
1. 
## Step 3: Retrieve secrets with the Secrets Manager Agent

To use the agent, you call the local Secrets Manager Agent endpoint and include the name or ARN of the secret as a query parameter. By default, the Secrets Manager Agent retrieves the AWSCURRENT version of the secret. To retrieve a different version, you can set versionStage or versionId.

To help protect the Secrets Manager Agent, you must include a SSRF token header as part of each request: X-Aws-Parameters-Secrets-Token. The Secrets Manager Agent denies requests that don't have this header or that have an invalid SSRF token. You can customize the SSRF header name in the Configuration file.

The Secrets Manager Agent uses the AWS SDK for Rust, which uses the https://docs.aws.amazon.com/sdk-for-rust/latest/dg/credentials.html. The identity of these IAM credentials determines the permissions the Secrets Manager Agent has to retrieve secrets.

- *Required permissions: **
- secretsmanager:DescribeSecret
- secretsmanager:GetSecretValue
For more information, see Permissions reference.

Important

After the secret value is pulled into the Secrets Manager Agent, any user with access to the compute environment and SSRF token can access the secret from the Secrets Manager Agent cache. For more information, see Security considerations.

### [ curl ]

The following curl example shows how to get a secret from the Secrets Manager Agent. The example relies on the SSRF being present in a file, which is where it is stored by the install script.

```plain text
curl -v -H \
    "X-Aws-Parameters-Secrets-Token: $(</var/run/awssmatoken)" \
    'http://localhost:2773/secretsmanager/get?secretId=<YOUR_SECRET_ID>}'; \
    echo
```

### [ Python ]

The following Python example shows how to get a secret from the Secrets Manager Agent. The example relies on the SSRF being present in a file, which is where it is stored by the install script.

```plain text
import requests
import json

# Function that fetches the secret from Secrets Manager Agent for the provided secret id.
def get_secret():
    # Construct the URL for the GET request
    url = f"http://localhost:2773/secretsmanager/get?secretId=<YOUR_SECRET_ID>}"

    # Get the SSRF token from the token file
    with open('/var/run/awssmatoken') as fp:
        token = fp.read()

    headers = {
        "X-Aws-Parameters-Secrets-Token": token.strip()
    }

    try:
        # Send the GET request with headers
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Return the secret value
            return response.text
        else:
            # Handle error cases
            raise Exception(f"Status code {response.status_code} - {response.text}")

    except Exception as e:
        # Handle network errors
        raise Exception(f"Error: {e}")
```

## Configure the Secrets Manager Agent

To change the configuration of the Secrets Manager Agent, create a TOML config file, and then call ./aws-secrets-manager-agent --config config.toml.

The following list shows the options you can configure for the Secrets Manager Agent.

- log_level – The level of detail reported in logs for the Secrets Manager Agent: DEBUG, INFO, WARN, ERROR, or NONE. The default is INFO.
- http_port – The port for the local HTTP server, in the range 1024 to 65535. The default is 2773.
- region – The AWS Region to use for requests. If no Region is specified, the Secrets Manager Agent determines the Region from the SDK. For more information, see Specify your credentials and default Region in the AWS SDK for Rust Developer Guide.
- ttl_seconds – The TTL in seconds for the cached items, in the range 1 to 3600. The default is 300. This setting is not used if the cache size is 0.
- cache_size – The maximum number of secrets that can be stored in the cache, in the range 0 to 1000. 0 indicates that there is no caching. The default is 1000.
- ssrf_headers – A list of header names the Secrets Manager Agent checks for the SSRF token. The default is "X-Aws-Parameters-Secrets-Token, X-Vault-Token".
- ssrf_env_variables – A list of environment variable names the Secrets Manager Agent checks for the SSRF token. The environment variable can contain the token or a reference to the token file as in: AWS_TOKEN=file:///var/run/awssmatoken. The default is "AWS_TOKEN, AWS_SESSION_TOKEN".
- path_prefix – The URI prefix used to determine if the request is a path based request. The default is "/v1/".
- max_conn – The maximum number of connections from HTTP clients that the Secrets Manager Agent allows, in the range 1 to 1000. The default is 800.
## Logging

The Secrets Manager Agent logs errors locally to the file logs/secrets_manager_agent.log. When your application calls the Secrets Manager Agent to get a secret, those calls appear in the local log. They do not appear in the CloudTrail logs.

The Secrets Manager Agent creates a new log file when the file reaches 10 MB, and it stores up to five log files total.

The log does not go to Secrets Manager, CloudTrail, or CloudWatch. Requests to get secrets from the Secrets Manager Agent do not appear in those logs. When the Secrets Manager Agent makes a call to Secrets Manager to get a secret, that call is recorded in CloudTrail with a user agent string containing aws-secrets-manager-agent.

You can configure logging in the Configuration file.

## Security considerations

The Secrets Manager Agent provides compatibility for legacy applications that access secrets through an existing agent or that need caching for langages not supported through other solutions.

For an agent architecture, the domain of trust is where the agent endpoint and SSRF token are accessible, which is usually the entire host. The domain of trust for the Secrets Manager Agent should match the domain where the Secrets Manager credentials are available in order to maintain the same security posture. For example, on Amazon EC2 the domain of trust for the Secrets Manager Agent would be the same as the domain of the credentials when using roles for Amazon EC2.

Security conscious applications that are not already using an agent solution with the Secrets Manager credentials locked down to the application should consider using the language-specific AWS SDKs or caching solutions. For more information, see Get secrets.


