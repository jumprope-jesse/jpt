# TeleMessage Signal Security Analysis

Source: Micah Lee's analysis (May 2025)
URL: https://micahflee.com/despite-misleading-marketing-israeli-company-telemessage-used-by-trump-officials-can-access-plaintext-chat-logs/

## Summary

TeleMessage makes modified versions of Signal, WhatsApp, Telegram, and WeChat for enterprise archival/compliance. Their Signal clone (TM SGNL) was used by senior Trump officials including Mike Waltz. Despite marketing claims of "end-to-end encryption from the mobile phone through to the corporate archive," the system sends **plaintext chat logs** to TeleMessage's servers.

## Key Technical Findings

### How TM SGNL Works
- Nearly identical to real Signal, interoperable with Signal users
- Every message stored in SQLite with `WaitingToBeDelivered` status
- Background sync sends plaintext messages to `https://archive.telemessage.com`
- Archive server forwards to customer destinations (Microsoft 365, SMTP, SFTP)

### Why E2EE Claims Are False
1. Messages are decrypted on the phone (as normal for Signal)
2. TM SGNL then sends **plaintext** copies to TeleMessage's archive server
3. The archive server (hosted on public AWS in Virginia) has full access to all message content
4. No encryption between the app and the archive destination

### Security Implications
- Archive server hosted on public AWS cloud (not approved for classified info)
- Server was publicly accessible - anyone could send HTTP requests
- TeleMessage is an Israeli company founded by former IDF intelligence officer
- Trivial for company to forward copies to Israeli intelligence (no evidence this happened, but architecture permits it)
- Server was subsequently hacked, confirming plaintext access

## The Hack (May 2025)

An anonymous hacker exploited the archive server and obtained:
- Plaintext Signal messages (including group chats, phone numbers, message content)
- Plaintext Telegram messages (including Coinbase employee communications)
- Plaintext WhatsApp messages (group names, member lists, content)
- Some encrypted WhatsApp messages (metadata still plaintext)
- Private key material
- Usernames and plaintext passwords (used to access list of 747 CBP employees)

## Code Analysis Details

Key components in the TM SGNL Android source:
- `SignalDatabase`: Stores all Signal data in SQLite
- `DataGrabber.setMessage()`: Inserts messages into staging DB, triggers sync
- `SyncAdapter.onPerformSync()`: Selects `WaitingToBeDelivered` messages, POSTs to archive server
- `NetworkManager.start()`: Makes HTTP POST to `archive.telemessage.com/api/rest/archive/telemessageincomingmessage/`
- `ArchiveMessagesProcessor`: Processes message creation, deletion, and edits for archival

## Reverse Engineering Notes

Useful for analyzing Android apps:
- TeleMessage published their own source code (required by AGPL license from Signal)
- Android archives (.aar) can be decompiled with online tools
- Apps are Java/Kotlin bytecode, easily decompiled to readable source
- Look for sync adapters, content providers, and network managers

## Lessons

1. **"Enterprise security" features often break actual security** - archival compliance defeats E2EE
2. **Marketing claims need verification** - "end-to-end encrypted" was demonstrably false
3. **Supply chain matters** - who runs your messaging infrastructure?
4. **Interoperability is a double-edged sword** - Signal users had no way to know they were talking to TM SGNL users
5. **Open source licensing enables auditing** - AGPL forced code disclosure that enabled this analysis

## Related

- Senator Ron Wyden requested DOJ investigation citing this analysis
- TeleMessage suspended service after the hacks
- NBC reported a second hacker breach with "large cache of files"
