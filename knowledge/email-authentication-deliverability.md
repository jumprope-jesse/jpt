# Email Authentication & Deliverability

Technical reference for email authentication standards (SPF, DKIM, DMARC) and deliverability best practices.

## Background

In late 2023, Google, Yahoo, and Outlook announced strict enforcement of email authentication standards starting 2024. Failure to comply results in emails being blocked.

## The Three Authentication Standards

### SPF (Sender Policy Framework)
Specifies which servers/domains are allowed to send email for your organization. Added as a DNS TXT record.

```
v=spf1 ip4:173.236.251.117 include:netblocks.dreamhost.com include:relay.mailchannels.net mx ~all
```

### DKIM (DomainKeys Identified Mail)
Digitally signs every outgoing message. Receiving server verifies authenticity using a public key in DNS.

```
v=DKIM1; k=rsa; h=sha256; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...
```

### DMARC (Domain-based Message Authentication, Reporting and Conformance)
Instructs receiving servers how to handle messages that fail SPF or DKIM. Also enables reporting.

```
v=DMARC1; p=reject; sp=none; fo=1; rua=mailto:dmarc_rua@domain.com; ruf=mailto:dmarc_ruf@domain.com
```

DMARC tags:
- `p` - policy (none, quarantine, reject)
- `sp` - subdomain policy
- `fo` - forensic options
- `rua` - aggregate report URI
- `ruf` - forensic report URI

## Email Journey

1. Sender composes and sends email
2. Sender's MTA adds DKIM signature to header
3. Recipient's MTA checks SPF and DKIM records
4. DMARC alignment verified, policy applied

## Bulk Sender Requirements (5,000+ emails/day to Gmail)

- Implement SPF, DKIM, and DMARC
- Keep spam rate below 0.10% (hard limit: 0.30%)
- One-click unsubscribe for marketing emails
- Process unsubscribe requests within 2 days
- Valid forward and reverse DNS (PTR) records
- TLS connection for transmitting email
- From: header aligned with SPF or DKIM domain
- Format per RFC 5322 (Internet Message Format)

## Free Tools

| Purpose | Tool |
|---------|------|
| SPF Generator | mxtoolbox.com/SPFRecordGenerator.aspx |
| DKIM Generator | easydmarc.com/tools/dkim-record-generator |
| DMARC Generator | mxtoolbox.com/DMARCRecordGenerator.aspx |
| SPF Check | mxtoolbox.com/spf.aspx |
| DKIM Check | mxtoolbox.com/dkim.aspx |
| DMARC Check | mxtoolbox.com/dmarc.aspx |
| SuperTool | mxtoolbox.com/SuperTool.aspx |
| Email Health | mxtoolbox.com/emailhealth |
| Blacklist Check | mxtoolbox.com/blacklists.aspx |
| DMARC Report Analyzer | mxtoolbox.com/DmarcReportAnalyzer.aspx |
| Google Safe Browsing | transparencyreport.google.com/safe-browsing |

## Monitoring Tools

- **Google Postmaster Tools** - insights for bulk senders on spam rates, authentication, reputation
- **Yahoo Sender Hub** - Yahoo's equivalent

## Legal Considerations

- **CAN-SPAM Act (USA)** - subject lines, sender ID, unsubscribe options
- **GDPR (EU)** - explicit consent required for marketing emails
- **CASL (Canada)** - opt-in consent, unsubscribe options

## Key RFCs

- SPF: RFC 7208
- DKIM: RFC 6376
- DMARC: RFC 7489
- Internet Message Format: RFC 5322
- SMTP: RFC 5321
- One-Click Unsubscribe: RFC 8058

---
*Source: XOMedia deep dive on email deliverability, April 2024*
