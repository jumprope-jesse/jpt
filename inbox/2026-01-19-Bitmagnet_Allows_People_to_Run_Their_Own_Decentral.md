---
type: link
source: notion
url: https://torrentfreak.com/bitmagnet-allows-people-to-run-their-own-decentralized-torrent-indexer-locally-240218/
notion_type: Software Repo
tags: ['Running']
created: 2024-02-18T21:32:00.000Z
---

# Bitmagnet Allows People to Run Their Own Decentralized Torrent Indexer Locally * TorrentFreak

## AI Summary (from Notion)
- Decentralization of BitTorrent: Bitmagnet allows users to run their own decentralized torrent index, reducing reliance on centralized torrent sites.
- DHT and BEP51 Protocol: Uses Distributed Hash Table (DHT) and BEP51 protocol to discover and collect infohashes without needing a central tracker.
- User-Controlled Index: Users can create a private BitTorrent index, making it possible to have a personal search engine for torrents.
- Rapid Content Discovery: After running Bitmagnet for a month, users can build extensive personal indexes that may surpass traditional torrent sites.
- Curation Challenges: Bitmagnet lacks moderation, potentially indexing mislabeled files and illegal content, though it attempts to filter out harmful material.
- Growing Popularity: The Docker image has been downloaded nearly 25,000 times, indicating strong interest despite its "alpha" release status.
- Legal Risks: Running a public-facing search engine with Bitmagnet carries legal risks, as it may attract anti-piracy scrutiny.
- Potential for Abuse: While designed for personal use, there are risks associated with public usage, including tracking by anti-piracy tools.
- Future Developments: Plans to enhance curation and community features are in progress, aiming for better content management.
- Immunity from Takedown: The developer asserts that Bitmagnet is a content-neutral tool, and the software cannot be easily shut down.

## Content (from Notion)

BitTorrent is often characterized as a decentralized file-sharing technology. However, its reliance on centralized indexes runs contrary to this idea. Over the years, several 'indestructible' alternatives have been proposed, including the relatively new Bitmagnet software. With Bitmagnet, people can run their own private BitTorrent index, relying on DHT and the BEP51 protocol.

When Bram Cohen released the first version of BitTorrent in 2002, it sparked a file-sharing revolution.

At the time bandwidth was a scarce resource, making it impossible to simultaneously share large files with millions of people over the Internet. BitTorrent not only thrived in that environment, the protocol remains effective even to this day.

BitTorrent transfers rely on peer-to-peer file-sharing without a central storage location. With updated additions to the protocol, such as the BitTorrent Distributed Hash Table (DHT), torrent files no longer require a tracker server either, making it decentralized by nature.

In theory, it doesn’t always work like that though. People who use BitTorrent, for research purposes or to grab the latest Linux distros, often use centralized search engines or indexes. If these go offline, the .torrent files they offer go offline too.

## Decentralizing Torrents

This problem isn’t new and solutions have been around for quite a few years. There’s the University-sponsored Tribler torrent client, for example, and the BitTorrent protocol extension (BEP51), developed by ‘The 8472’, that also helps to tackle this exact problem.

BEP51 makes it possible to discover and collect infohashes through DHT, without the need for a central tracker. These infohashes can be converted to magnet links and when paired with relevant metadata, it’s possible to create a full BitTorrent index that easily rivals most centralized torrent sites.

Some centralized torrent sites, such as BTDigg, have already done just that. However, the beauty of the proposition involving DHT is that centralized sites are not required to act as search engines. With the right code, anyone can set up their own personalized and private DHT crawler, torrent index, and search engine.

## Bitmagnet: A Private Decentralized Torrent Index

Bitmagnet is a relatively new self-hosted tool that does exactly that. The software, which is still in an early stage of development, was launched publicly a few months ago.

“The project aims to reduce reliance on public torrent sites that are prone to takedown and expose users to ads and malware,” Mike, the lead developer, tells us.

Those who know how to create a Docker container can have an instance up and running in minutes and for the privacy conscious, the docker-compose file on GitHub supports VPNs via Gluetun. Once Bitmagnet is up and running, it starts collecting torrent data from DHT, neatly classifies what it finds, and makes everything discoverable through its own search engine.

Bitmagnet UI

Decentralization is just one of the stated advantages. The developer was also positively surprised by the sheer amount of content that was discovered and categorized through Bitmagnet. This easily exceeds the libraries of most traditional torrent sites.

“Run it for a month and you’ll have a personal index and search engine that dwarfs the popular torrent websites, and includes much content that can often only be found on difficult-to-join private trackers,” Mike tells us.

After running the software for four months, the developer now has more than 12 million indexed torrents. However, other users with more bandwidth and better connections have many more already. This also brings us to one of the main drawbacks; a lack of curation.

## Curation

Unlike well-moderated torrent sites, Bitmagnet adds almost any torrent it finds to its database. This includes mislabeled files, malware-ridden releases, and potentially illegal content. The software tries to limit abuse by filtering metadata for CSAM content, however.

There are plans to add more curation by adding support for manual postings and federation. That would allow people with similar interests to connect, acting more like a trusted community. However, this is still work in progress.

Another downside is that it could take longer to index rare content, as it has to be discovered first. Widely shared torrents tend to distribute quickly over DHT, but rare releases will take much longer to be picked up. In addition, users may occasionally stumble upon dead or incomplete torrents.

Thus far, these drawbacks are not stopping people from trying the software.

While Bitmagnet is only out as an “alpha” release it’s getting plenty of interest. The Docker image has been downloaded nearly 25k times and the repository has been starred by more than a thousand other developers so far.

## Caution is Advised!

Mike doesn’t know how many people are running an instance or how they’re using them. Bitmagnet is designed and intended for people to run on their own computer and network, but people could turn it into a public-facing search engine as well.

Running a public search engine comes with legal risks of course. Once there’s serious traffic, that will undoubtedly alert anti-piracy groups.

Even those who use the software privately to download legitimate content might receive complaints. By crawling the DHT, the software presents itself as a torrent client. While it doesn’t download any content automatically, some rudimentary anti-piracy tracking tools might still (incorrectly) flag this activity.

There are no examples of this happening at the moment, but the potential risk is why Bitmagnet advises users to opt for VPN routing.

## Impossible to Shut Down

All in all, Bitmagnet is an interesting tool that uses some of BitTorrent’s underutilized powers, which have become increasingly rare in recent years.

The idea behind Bitmagnet is similar to Magnetico, which first came out in 2017. While that no longer appears to be actively maintained, it remains available on GitHub. During these years, we haven’t seen any takedown notices targeting the software.

Mike hopes that his project will be spared from copyright complaints too. The developer sees it simply as a content-neutral tool, much like a web browser.

“I hope that the project is immune from such issues, because the source code contains no copyright infringing material. How people choose to use the app is up to them – if you access copyrighted content using a web browser or BitTorrent client, that does not make the vendors of those apps liable.”

“Bitmagnet cannot be ‘taken down’ – even if the GitHub repository were threatened by an illegitimate takedown request, the code can easily be hosted elsewhere,” Mike concludes.


