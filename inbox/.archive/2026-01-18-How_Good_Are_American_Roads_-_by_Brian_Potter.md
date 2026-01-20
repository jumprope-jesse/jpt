---
type: link
source: notion
url: https://www.construction-physics.com/p/how-good-are-american-roads
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-11-20T15:06:00.000Z
---

# How Good Are American Roads? - by Brian Potter

## Content (from Notion)

We’re in an era where US infrastructure is getting a lot of attention. We need a lot of energy infrastructure for decarbonization, and to enable the AI data center buildout. There’s lots of interest in building high-speed rail, mass transit infrastructure, desalination plants in arid regions, and better ports.

One facet of infrastructure that doesn’t get all that much attention is roads, despite the fact that they’re crucial transportation infrastructure, and probably the infrastructure that Americans interact with most directly and consistently. The US has the largest road network in the world, about 4.3 million miles of road, and Americans drive much more than residents in most other countries. Good-quality roads are important for a functioning economy, and rough roads inflict costs in the form of reduced vehicle speeds.

How good is American road infrastructure? How does it compare with roads built in other countries?

Overall, the quality of US interstates is very high, while the quality of roads in major cities is quite poor. And while there’s some anecdotal evidence that US roads are worse than European roads, I wasn’t able to find much international road quality data to compare. The limited data I found points to the US not being a huge outlier in road quality. But more data is needed to compare accurately.

### Measuring US road quality

The most common metric for measuring road quality is the International Roughness Index (IRI). The IRI measures how much a car moves vertically as it travels over a given distance, and is typically given in units like “inches per mile” or “millimeters per meter.” Lower IRI is better: the rougher the road, the more the car bounces up and down, and the higher the IRI. As we’ll see, standards for road quality vary from country to country, but a “good” IRI is generally in the neighborhood of 95 inches per mile / 1.5 millimeters per meter or less.

Data on US road quality is provided by the Bureau of Transportation Statistics and the Federal Highway Administration (FHWA) at the national, state, and city level. It’s not 100% clear to me what’s included in this data, or what the selection criteria is. It definitely includes essentially all of the Interstate System, as well as other major highways that make up the National Highway System. But the National Highway System has on the order of 160,000 miles, while there is quality data for around 800,000 miles worth of road. Presumably the other 640,000 miles are other important roads outside of the highway system. Regardless, the roads we have quality data for are only a fraction (around 19%) of the US’s total road network.

To start, let’s look at overall road quality, broken down by whether they’re interstate highways or not, and whether they’re urban or rural roads.

Note: The FHWA uses slightly different category breakdowns in different places. Some places it uses three categories, some places it uses five, and some places it uses a different five. I’ve used the categories given in the national level statistics. These are consistent with the three-level categorization used elsewhere, with an additional “very good” and “very poor” labels I’ve assigned to < 60 and > 220 IRI. Note that state DOTs might use their own, slightly different quality categories.

US interstates are fairly good quality, with more than 80% of mileage good or very good, and only a tiny fraction of mileage (around 3%) poor or very poor. Non-interstate roads are, unsurprisingly, less good, with only around 40% of measured mileage good or better, and 20% poor or worse. Interestingly, in all cases urban roads are worse quality than rural roads, presumably because they see higher traffic than rural roads. More than a third of non-interstate urban roads are poor quality or worse. And remember, this data is just a fraction of total US road mileage (which includes more than a million miles of unpaved roads). Presumably average quality of the total non-interstate road network is even worse.

We can also see how road quality has changed over time. Over the last 30 years, interstate quality has been steadily improving, while non-interstate has been fairly flat.

We can also look at a state-by-state breakdown. For interstates, there’s not a huge amount of variation: only four states have less than 60% of their roads good quality or better, and almost every state has less than 10% of its interstate mileage poor quality or worse.

With non-interstates, we see more variation. Broadly, highly rural states tend to have higher quality roads than more urbanized states, though there’s a decent amount of variation. California, which is reasonably rural, nevertheless comes in third from the bottom. Interestingly, I expected cold places to have lower road quality in general due to things like freeze-thaw cycles and the impact of road salting, but there doesn’t seem to be much correlation. Plenty of cold places (North Dakota, Wyoming, Minnesota) have good-quality roads, while plenty of warm places (Louisiana, New Mexico, California) have poor-quality roads.

We can also look at the road quality of individual cities. Below is road quality (non-interstate) for the 19 largest metro areas in the US.1

While urban roads are poor in general, there’s a large amount of variation. Cities like Atlanta and Minneapolis have less than 10% of their roads are poor quality or worse, while more than 60% of the roads in San Francisco and Los Angeles are poor. But in general, most major cities aren’t doing great: in 13 of the 19 largest US cities, more than 1/3rd of the roads are poor quality. And here again we see that cold climate doesn’t seem to have much impact on road quality, with cold places like Minneapolis and New York near the top, while warm cities like Los Angeles, San Diego and Dallas are near the bottom.

### International comparisons in road quality

So US interstates seem high-quality, while urban roads are often quite poor. How does this compare to other countries?

It’s unfortunately not easy to tell. The US ranks very highly in the international Roads Quality Index (11th in the world, as of 2019), but this is based on a survey of the perceptions of business leaders about road quality, not actual road data. A 2022 IMF study of various countries’ road quality ranked the US best in the world, but it relied on estimated travel speeds between major cities using Google Maps data, not actual road roughness. While the IRI is commonly used by countries around the world to measure road quality, I had a very hard time finding any international datasets comparable to FHWA data.

But I was able to scrape together a few. This 2023 report from the UK compares highway quality in England, Wales, Scotland, and the Netherlands, and provides a high-level summary of IRI data.2 This Canadian website gives IRI data up to 2021 for the provincial highways in Ontario. This presentation gives some summary IRI statistics for Ireland’s national roads as of 2017, and this one gives some IRI data for Irish regional roads as of 2018.

Because these countries use somewhat different roughness categories, I graphed each of these, along with US interstate and non-interstate roads, using a cumulative distribution function, which gradually adds the fraction of roads at different IRI levels. The farther the curve is to the left, the larger the fraction of roads at a lower IRI, and the higher quality the road network.

For most of the international sources, the data is for the national or provincial highway network, major roads which (as far as I can tell) are roughly equivalent to the US National Highway System. The exception is the Irish regional road data, which I believe are a lower tier of road.3

We see that US interstates compare very well; as good or better than the national road networks in every other country for which there’s data. US non-interstates do less well: about 90% of Dutch national roads are “good” by US standards, for instance, whereas only around 40% of US non-interstates are. Nevertheless, the US doesn’t seem to be a huge outlier: its roads seem to be roughly as good as British national roads, for instance. I’m also assuming that the US data includes a lot of lower-importance/quality roads beyond the national system that drag its average down. My guess is that if you restricted US data to just the National Highway System roads, average quality would jump significantly.4

On the other hand, while Ireland has reasonably good motorways (interstate equivalents) and “engineered pavements” (whatever that means), it appears to have poor regional and legacy roads, to the point where I’d be sure there was an error in the data if I hadn’t already heard that Ireland has unusually poor roads.5

Unfortunately, this doesn’t include data from many countries we might be interested in, like the Nordics, Germany, France, or Spain (anecdotally, I’ve heard that Spain has exceptionally good roads). And it's only measuring a very small portion of each country’s road network: the Netherlands data, for instance, is based on about 7,000 kilometers of national highway network, a tiny fraction of the 139,000 kilometers of roads in the country.

Is there anything else we can look at that might prove illuminating? One thing we can do is compare the quality standards of different countries: how smooth does a road have to be to meet different quality thresholds? This 2016 paper compares International Roughness Index specifications around the world. This report from 2000 gives a few more, though unfortunately they’re quite old. Most countries have five different quality levels. For ease of comparison, we’ll use the same “very good," “good," “acceptable," “poor," and “very poor” descriptors that we used for US roads. We can compare these to quality thresholds in the US.6

Looking at this, we see that the US generally has fairly strict quality standards compared to other countries. The US for instance, has a higher threshold for what counts as “good” than any other country listed, and only Holland has a higher bar for what counts as “very good.”

There’s also slivers of information that can be found elsewhere. This 2014 EU report states that as of 2011, on average both national and local roads in Spain were “deficient” (though it doesn’t give an IRI rating). This article from 1992 discusses several US road experts and government representatives touring France, Austria, Germany, the Netherlands, and Belgium to examine their roadways. They found that European roads were much higher quality, noting that “the serious deterioration that exists on US highways and streets was virtually never seen in Europe,” likely because damage was repaired much sooner. It’s of course hard to weigh a report from more than 30 years ago too heavily, but the 2023 UK report mentioned above also notes that Dutch highways, which were of higher quality than UK highways, were resurfaced much more frequently. (I tried to find data on road maintenance schedules for various countries and came up short.)

A Time article from 2001 claims that European roads are superior to US ones because, in addition to more frequent maintenance, European countries build roads more durably:

> European highways actually carry more traffic and considerably heavier truck weights than US roads, yet they are smoother and far sturdier. European highways are designed by their builders to last 40 years; the projected life of American roads is half as long.

As far as I can tell, the most common way to build a road more durably is to use concrete construction. Most roads in the US are built using one or more layers of asphalt concrete (a mixture of aggregate and bitumen as a binder) over a layer of coarse aggregate like gravel. But you can also make pavement out of conventional Portland cement concrete, complete with steel reinforcing. Concrete pavement will generally have a longer lifespan than asphalt pavement, at the expense of greater upfront cost:

> The maximum service life of an asphalt service course is 20 years…compared with 30 to 50 years for concrete road surfaces. Indeed, subject to cost parameters a concrete road can be designed for however long it is required.

Cross sections of asphalt pavement from Massachusetts DOT.

Cross section of a continuously reinforced concrete pavement, via FHWA.

Most US roads are indeed made of asphalt rather than concrete, but so are most European roads, it seems. 80% of Dutch roads are made of multi-layered asphalt pavements, this presentation on the German highway network states that only 30% of Germany highways are made of concrete, and this report claims that more than 90% of European roads are surfaced with asphalt (though this is made somewhat more complicated by the fact that you can have a concrete road with a thin asphalt surface).

It’s also possible that European roads use the same basic construction methods, but are built more robustly. In 1993, the Michigan DOT experimented by rebuilding a concrete road using two methods: one section was built using its standard construction methods, and another was built using more robust German specifications. The German section had two layers of concrete instead of one, a gravel base course instead of sand, and tighter joint spacing. However, after 20 years of service, the German section was actually performing slightly worse than the one built to Michigan standards, despite costing twice as much to build.

### Conclusion

To sum up, US interstates seem high quality, and as good as comparable roads in Europe. Non-interstates are lower quality, particularly within major urban areas, but a lack of data makes it hard to do much international comparison. The limited data we have suggests that US roads are perhaps not a huge outlier in quality. It also seems likely that many European roads are maintained better than US roads and resurfaced more frequently, and that European roads are designed more robustly (though perhaps not in a way that results in better service life).

Overall, my main takeaway is that roads in major US cities are often shockingly bad, particularly in California, and that much more data is needed on road quality in other countries. If you know of good international road quality datasets (ideally IRI), please let me know!

1

Detroit is larger than some of these cities, but I excluded it from this list because of an error in its quality data (some of the mileage for different quality levels is anomalously high and doesn’t add up correctly.)

2

The Netherlands data measured IRI directly, while England, Wales, and Scotland had to be converted to IRI from another, similar quality metric, longitudinal profile variance (eLPV).

3

National roads in England, Scotland, and Wales were all at very similar levels of quality, so I’ve only included England here.

4

My suspicion that the non-interstate portions of the National Highway System are higher quality than most other roads is because there seems to be a similar level of stringency in monitoring the interstate and non-interstate parts of the National Highway System.

5

The linked presentation gives “engineered pavement” as its own subcategory of road network, but other sources describe “engineered pavement” as a design methodology, and I wasn’t able to determine when, specifically, it was used.

6

Not all countries use five quality levels: Canada has three and Germany seems to have four. For present purposes, I’ve assumed they (roughly) correspond to “good," “acceptable," and “poor” for Canada, and adding “very poor” for Germany.

### Subscribe to Construction Physics

By Brian Potter · Hundreds of paid subscribers

Essays about buildings, infrastructure, and industrial technology.


