---
type: link
source: notion
url: https://computer.rip/2025-05-11-air-traffic-control.html
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-05-13T02:47:00.000Z
---

# 2025-05-11 air traffic control

## Overview (from Notion)
- Air traffic control (ATC) is a complex system shaped by historical, technical, and social factors, reflecting how technology evolves alongside societal needs.
- The evolution of ATC illustrates the challenges of managing growth and safety in a rapidly advancing industry, which could resonate with your experiences in software engineering and entrepreneurship.
- The intertwining of military and civilian aviation highlights the impact of defense technologies on everyday life, showcasing how sectors can benefit from each other.
- Unique insights include the notion that air traffic control isn't just about safety; it's also about managing human interactions, which can inform your approach to team dynamics in your company.
- Alternate viewpoints could include critiques of how ATC has been shaped by bureaucracy and underfunding, raising questions about how innovation is stifled in both aviation and tech sectors.
- The historical context of ATC might inspire thoughts on how to build a resilient startup—acknowledging past mistakes and learning from them can lead to better management practices.

## AI Summary (from Notion)
Air traffic control has evolved from minimal communication in early aviation to a complex system influenced by military practices, with significant advancements during and after WWII. The integration of radar and the establishment of the FAA marked key developments, while ongoing challenges include automation and the relationship between flight service stations and ATC.

## Content (from Notion)

```plain text
   _____                   _                  _____            _____       _
  |     |___ _____ ___ _ _| |_ ___ ___ ___   |  _  |___ ___   | __  |___ _| |
  |   --| . |     | . | | |  _| -_|  _|_ -|  |     |  _| -_|  | __ -| .'| . |
  |_____|___|_|_|_|  _|___|_| |___|_| |___|  |__|__|_| |___|  |_____|__,|___|
  a newsletter by |_|j. b. crawfordhomearchivesubscriberss
```

Air traffic control has been in the news lately, on account of my country's declining ability to do it. Well, that's a long-term trend, resulting from decades of under-investment, severe capture by our increasingly incompetent defense-industrial complex, no small degree of management incompetence in the FAA, and long-lasting effects of Reagan crushing the PATCO strike. But that's just my opinion, you know, maybe airplanes got too woke. In any case, it's an interesting time to consider how weird parts of air traffic control are. The technical, administrative, and social aspects of ATC all seem two notches more complicated than you would expect. ATC is heavily influenced by its peculiar and often accidental development, a product of necessity that perpetually trails behind the need, and a beneficiary of hand-me-down military practices and technology.

## Aviation Radio

In the early days of aviation, there was little need for ATC---there just weren't many planes, and technology didn't allow ground-based controllers to do much of value. There was some use of flags and signal lights to clear aircraft to land, but for the most part ATC had to wait for the development of aviation radio. The impetus for that work came mostly from the First World War.

Here we have to note that the history of aviation is very closely intertwined with the history of warfare. Aviation technology has always rapidly advanced during major conflicts, and as we will see, ATC is no exception.

By 1913, the US Army Signal Corps was experimenting with the use of radio to communicate with aircraft. This was pretty early in radio technology, and the aircraft radios were huge and awkward to operate, but it was also early in aviation and "huge and awkward to operate" could be similarly applied to the aircraft of the day. Even so, radio had obvious potential in aviation. The first military application for aircraft was reconnaissance. Pilots could fly past the front to find artillery positions and otherwise provide useful information, and then return with maps. Well, even better than returning with a map was providing the information in real-time, and by the end of the war medium-frequency AM radios were well developed for aircraft.

Radios in aircraft lead naturally to another wartime innovation: ground control. Military personnel on the ground used radio to coordinate the schedules and routes of reconnaissance planes, and later to inform on the positions of fighters and other enemy assets. Without any real way to know where the planes were, this was all pretty primitive, but it set the basic pattern that people on the ground could keep track of aircraft and provide useful information.

Post-war, civil aviation rapidly advanced. The early 1920s saw numerous commercial airlines adopting radio, mostly for business purposes like schedule coordination. Once you were in contact with someone on the ground, though, it was only logical to ask about weather and conditions. Many of our modern practices like weather briefings, flight plans, and route clearances originated as more or less formal practices within individual airlines.

## Air Mail

The government was not left out of the action. The Post Office operated what may have been the largest commercial aviation operation in the world during the early 1920s, in the form of Air Mail. The Post Office itself did not have any aircraft; all of the flying was contracted out---initially to the Army Air Service, and later to a long list of regional airlines. Air Mail was considered a high priority by the Post Office and proved very popular with the public. When the transcontinental route began proper operation in 1920, it became possible to get a letter from New York City to San Francisco in just 33 hours by transferring it between airplanes in a nearly non-stop relay race.

The Post Office's largesse in contracting the service to private operators provided not only the funding but the very motivation for much of our modern aviation industry. Air travel was not very popular at the time, being loud and uncomfortable, but the mail didn't complain. The many contract mail carriers of the 1920s grew and consolidated into what are now some of the United States' largest companies. For around a decade, the Post Office almost singlehandedly bankrolled civil aviation, and passengers were a side hustle [1].

Air mail ambition was not only of economic benefit. Air mail routes were often longer and more challenging than commercial passenger routes. Transcontinental service required regular flights through sparsely populated parts of the interior, challenging the navigation technology of the time and making rescue of downed pilots a major concern. Notably, air mail operators did far more nighttime flying than any other commercial aviation in the 1920s. The post office became the government's de facto technical leader in civil aviation. Besides the network of beacons and markers built to guide air mail between cities, the post office built 17 Air Mail Radio Stations along the transcontinental route.

The Air Mail Radio Stations were the company radio system for the entire air mail enterprise, and the closest thing to a nationwide, public air traffic control service to then exist. They did not, however, provide what we would now call control. Their role was mainly to provide pilots with information (including, critically, weather reports) and to keep loose tabs on air mail flights so that a disappearance would be noticed in time to send search and rescue.

In 1926, the Watres Act created the Aeronautic Branch of the Department of Commerce. The Aeronautic Branch assumed a number of responsibilities, but one of them was the maintenance of the Air Mail routes. Similarly, the Air Mail Radio Stations became Aeronautics Branch facilities, and took on the new name of Flight Service Stations. No longer just for the contract mail carriers, the Flight Service Stations made up a nationwide network of government-provided services to aviators. They were the first edifices in what we now call the National Airspace System (NAS): a complex combination of physical facilities, technologies, and operating practices that enable safe aviation.

In 1935, the first en-route air traffic control center opened, a facility in Newark owned by a group of airlines. The Aeronautic Branch, since renamed the Bureau of Air Commerce, supported the airlines in developing this new concept of en-route control that used radio communications and paperwork to track which aircraft were in which airways. The rising number of commercial aircraft made in-air collisions a bigger problem, so the Newark control center was quickly followed by more facilities built on the same pattern. In 1936, the Bureau of Air Commerce took ownership of these centers, and ATC became a government function alongside the advisory and safety services provided by the flight service stations.

En route center controllers worked off of position reports from pilots via radio, but needed a way to visualize and track aircraft's positions and their intended flight paths. Several techniques helped: first, airlines shared their flight planning paperwork with the control centers, establishing "flight plans" that corresponded to each aircraft in the sky. Controllers adopted a work aid called a "flight strip," a small piece of paper with the key information about an aircraft's identity and flight plan that could easily be handed between stations. By arranging the flight strips on display boards full of slots, controllers could visualize the ordering of aircraft in terms of altitude and airway.

Second, each center was equipped with a large plotting table map where controllers pushed markers around to correspond to the position reports from aircraft. A small flag on each marker gave the flight number, so it could easily be correlated to a flight strip on one of the boards mounted around the plotting table. This basic concept of air traffic control, of a flight strip and a position marker, is still in use today.

## Radar

The Second World War changed aviation more than any other event of history. Among the many advancements were two British inventions of particular significance: first, the jet engine, which would make modern passenger airliners practical. Second, the radar, and more specifically the magnetron. This was a development of such significance that the British government treated it as a secret akin to nuclear weapons; indeed, the UK effectively traded radar technology to the US in exchange for participation in US nuclear weapons research.

Radar created radical new possibilities for air defense, and complimented previous air defense development in Britain. During WWI, the organization tasked with defending London from aerial attack had developed a method called "ground-controlled interception" or GCI. Under GCI, ground-based observers identify possible targets and then direct attack aircraft towards them via radio. The advent of radar made GCI tremendously more powerful, allowing a relatively small number of radar-assisted air defense centers to monitor for inbound attack and then direct defenders with real-time vectors.

In the first implementation, radar stations reported contacts via telephone to "filter centers" that correlated tracks from separate radars to create a unified view of the airspace---drawn in grease pencil on a preprinted map. Filter center staff took radar and visual reports and updated the map by moving the marks. This consolidated information was then provided to air defense bases, once again by telephone.

Later technical developments in the UK made the process more automated. The invention of the "plan position indicator" or PPI, the type of radar scope we are all familiar with today, made the radar far easier to operate and interpret. Radar sets that automatically swept over 360 degrees allowed each radar station to see all activity in its area, rather than just aircraft passing through a defensive line. These new capabilities eliminated the need for much of the manual work: radar stations could see attacking aircraft and defending aircraft on one PPI, and communicated directly with defenders by radio.

It became routine for a radar operator to give a pilot navigation vectors by radio, based on real-time observation of the pilot's position and heading. A controller took strategic command of the airspace, effectively steering the aircraft from a top-down view. The ease and efficiency of this workflow was a significant factor in the end of the Battle of Britain, and its remarkable efficacy was noticed in the US as well.

At the same time, changes were afoot in the US. WWII was tremendously disruptive to civil aviation; while aviation technology rapidly advanced due to wartime needs those same pressing demands lead to a slowdown in nonmilitary activity. A heavy volume of military logistics flights and flight training, as well as growing concerns about defending the US from an invasion, meant that ATC was still a priority. A reorganization of the Bureau of Air Commerce replaced it with the Civil Aeronautics Authority, or CAA. The CAA's role greatly expanded as it assumed responsibility for airport control towers and commissioned new en route centers.

As WWII came to a close, CAA en route control centers began to adopt GCI techniques. By 1955, the name Air Route Traffic Control Center (ARTCC) had been adopted for en route centers and the first air surveillance radars were installed. In a radar-equipped ARTCC, the map where controllers pushed markers around was replaced with a large tabletop PPI built to a Navy design. The controllers still pushed markers around to track the identities of aircraft, but they moved them based on their corresponding radar "blips" instead of radio position reports.

## Air Defense

After WWII, post-war prosperity and wartime technology like the jet engine lead to huge growth in commercial aviation. During the 1950s, radar was adopted by more and more ATC facilities (both "terminal" at airports and "en route" at ARTCCs), but there were few major changes in ATC procedure. With more and more planes in the air, tracking flight plans and their corresponding positions became labor intensive and error-prone. A particular problem was the increasing range and speed of aircraft, and corresponding longer passenger flights, that meant that many aircraft passed from the territory of one ARTCC into another. This required that controllers "hand off" the aircraft, informing the "next" ARTCC of the flight plan and position at which the aircraft would enter their airspace.

In 1956, 128 people died in a mid-air collision of two commercial airliners over the Grand Canyon. In 1958, 49 people died when a military fighter struck a commercial airliner over Nevada. These were not the only such incidents in the mid-1950s, and public trust in aviation started to decline. Something had to be done. First, in 1958 the CAA gave way to the Federal Aviation Administration. This was more than just a name change: the FAA's authority was greatly increased compared to the CAA, most notably by granting it authority over military aviation.

This is a difficult topic to explain succinctly, so I will only give broad strokes. Prior to 1958, military aviation was completely distinct from civil aviation, with no coordination and often no communication at all between the two. This was, of course, a factor in the 1958 collision. Further, the 1956 collision, while it did not involve the military, did result in part from communications issues between separate distinct CAA facilities and the airline's own control facilities. After 1958, ATC was completely unified into one organization, the FAA, which assumed the work of the military controllers of the time and some of the role of the airlines. The military continues to have its own air controllers to this day, and military aircraft continue to include privileges such as (practical but not legal) exemption from transponder requirements, but military flights over the US are still beholden to the same ATC as civil flights. Some exceptions apply, void where prohibited, etc.

The FAA's suddenly increased scope only made the practical challenges of ATC more difficult, and commercial aviation numbers continued to rise. As soon as the FAA was formed, it was understood that there needed to be major investments in improving the National Airspace System. While the first couple of years were dominated by the transition, the FAA's second director (Najeeb Halaby) prepared two lengthy reports examining the situation and recommending improvements. One of these, the Beacon report (also called Project Beacon), specifically addressed ATC. The Beacon report's recommendations included massive expansion of radar-based control (called "positive control" because of the controller's access to real-time feedback on aircraft movements) and new control procedures for airways and airports. Even better, for our purposes, it recommended the adoption of general-purpose computers and software to automate ATC functions.

Meanwhile, the Cold War was heating up. US air defense, a minor concern in the few short years after WWII, became a higher priority than ever before. The Soviet Union had long-range aircraft capable of reaching the United States, and nuclear weapons meant that only a few such aircraft had to make it to cause massive destruction. Considering the vast size of the United States (and, considering the new unified air defense command between the United States and Canada, all of North America) made this a formidable challenge.

During the 1950s, the newly minted Air Force worked closely with MIT's Lincoln Laboratory (an important center of radar research) and IBM to design a computerized, integrated, networked system for GCI. When the Air Force committed to purchasing the system, it was christened the Semi-Automated Ground Environment, or SAGE. SAGE is a critical juncture in the history of the computer and computer communications, the first system to demonstrate many parts of modern computer technology and, moreover, perhaps the first large-scale computer system of any kind.

SAGE is an expansive topic that I will not take on here; I'm sure it will be the focus of a future article but it's a pretty well-known and well-covered topic. I have not so far felt like I had much new to contribute, despite it being the first item on my "list of topics" for the last five years. But one of the things I want to tell you about SAGE, that is perhaps not so well known, is that SAGE was not used for ATC. SAGE was a purely military system. It was commissioned by the Air Force, and its numerous operating facilities (called "direction centers") were located on Air Force bases along with the interceptor forces they would direct.

However, there was obvious overlap between the functionality of SAGE and the needs of ATC. SAGE direction centers continuously received tracks from remote data sites using modems over leased telephone lines, and automatically correlated multiple radar tracks to a single aircraft. Once an operator entered information about an aircraft, SAGE stored that information for retrieval by other radar operators. When an aircraft with associated data passed from the territory of one direction center to another, the aircraft's position and related information were automatically transmitted to the next direction center by modem.

One of the key demands of air defense is the identification of aircraft---any unknown track might be routine commercial activity, or it could be an inbound attack. The air defense command received flight plan data on commercial flights (and more broadly all flights entering North America) from the FAA and entered them into SAGE, allowing radar operators to retrieve "flight strip" data on any aircraft on their scope.

Recognizing this interconnection with ATC, as soon as SAGE direction centers were being installed the Air Force started work on an upgrade called SAGE Air Traffic Integration, or SATIN. SATIN would extend SAGE to serve the ATC use-case as well, providing SAGE consoles directly in ARTCCs and enhancing SAGE to perform non-military safety functions like conflict warning and forward projection of flight plans for scheduling. Flight strips would be replaced by teletype output, and in general made less necessary by the computer's ability to filter the radar scope.

Experimental trial installations were made, and the FAA participated readily in the research efforts. Enhancement of SAGE to meet ATC requirements seemed likely to meet the Beacon report's recommendations and radically improve ARTCC operations, sooner and cheaper than development of an FAA-specific system.

As it happened, well, it didn't happen. SATIN became interconnected with another planned SAGE upgrade to the Super Combat Centers (SCC), deep underground combat command centers with greatly enhanced SAGE computer equipment. SATIN and SCC planners were so confident that the last three Air Defense Sectors scheduled for SAGE installation, including my own Albuquerque, were delayed under the assumption that the improved SATIN/SCC equipment should be installed instead of the soon-obsolete original system. SCC cost estimates ballooned, and the program's ambitions were reduced month by month until it was canceled entirely in 1960. Albuquerque never got a SAGE installation, and the Albuquerque air defense sector was eliminated by reorganization later in 1960 anyway.

## Flight Service Stations

Remember those Flight Service Stations, the ones that were originally built by the Post Office? One of the oddities of ATC is that they never went away. FSS were transferred to the CAB, to the CAA, and then to the FAA. During the 1930s and 1940s many more were built, expanding coverage across much of the country.

Throughout the development of ATC, the FSS remained responsible for non-control functions like weather briefing and flight plan management. Because aircraft operating under instrument flight rules must closely comply with ATC, the involvement of FSS in IFR flights is very limited, and FSS mostly serve VFR traffic.

As ATC became common, the FSS gained a new and somewhat odd role: playing go-between for ATC. FSS were more numerous and often located in sparser areas between cities (while ATC facilities tended to be in cities), so especially in the mid-century, pilots were more likely to be able to reach an FSS than ATC. It was, for a time, routine for FSS to relay instructions between pilots and controllers. This is still done today, although improved communications have made the need much less common.

As weather dissemination improved (another topic for a future post), FSS gained access to extensive weather conditions and forecasting information from the Weather Service. This connectivity is bidirectional; during the midcentury FSS not only received weather forecasts by teletype but transmitted pilot reports of weather conditions back to the Weather Service. Today these communications have, of course, been computerized, although the legacy teletype format doggedly persists.

There has always been an odd schism between the FSS and ATC: they are operated by different departments, out of different facilities, with different functions and operating practices. In 2005, the FAA cut costs by privatizing the FSS function entirely. Flight service is now operated by Leidos, one of the largest government contractors. All FSS operations have been centralized to one facility that communicates via remote radio sites.

While flight service is still available, increasing automation has made the stations far less important, and the general perception is that flight service is in its last years. Last I looked, Leidos was not hiring for flight service and the expectation was that they would never hire again, retiring the service along with its staff.

Flight service does maintain one of my favorite internet phenomenon, the phone number domain name: 1800wxbrief.com. One of the odd manifestations of the FSS/ATC schism and the FAA's very partial privatization is that Leidos maintains an online aviation weather portal that is separate from, and competes with, the Weather Service's aviationweather.gov. Since Flight Service traditionally has the responsibility for weather briefings, it is honestly unclear to what extend Leidos vs. the National Weather Service should be investing in aviation weather information services. For its part, the FAA seems to consider aviationweather.gov the official source, while it pays for 1800wxbrief.com. There's also weathercams.faa.gov, which duplicates a very large portion (maybe all?) of the weather information on Leidos's portal and some of the NWS's. It's just one of those things. Or three of those things, rather. Speaking of duplication due to poor planning...

## The National Airspace System

Left in the lurch by the Air Force, the FAA launched its own program for ATC automation. While the Air Force was deploying SAGE, the FAA had mostly been waiting, and various ARTCCs had adopted a hodgepodge of methods ranging from one-off computer systems to completely paper-based tracking. By 1960 radar was ubiquitous, but different radar systems were used at different facilities, and correlation between radar contacts and flight plans was completely manual. The FAA needed something better, and with growing congressional support for ATC modernization, they had the money to fund what they called National Airspace System En Route Stage A.

Further bolstering historical confusion between SAGE and ATC, the FAA decided on a practical, if ironic, solution: buy their own SAGE.

In an upcoming article, we'll learn about the FAA's first fully integrated computerized air traffic control system. While the failed detour through SATIN delayed the development of this system, the nearly decade-long delay between the design of SAGE and the FAA's contract allowed significant technical improvements. This "New SAGE," while directly based on SAGE at a functional level, used later off-the-shelf computer equipment including the IBM System/360, giving it far more resemblance to our modern world of computing than SAGE with its enormous, bespoke AN/FSQ-7.

And we're still dealing with the consequences today!

[1] It also laid the groundwork for the consolidation of the industry, with a 1930 decision that took air mail contracts away from most of the smaller companies and awarded them instead to the precursors of United, TWA, and American Airlines.

```plain text
                                                 sincerely,
                                                 j. b. crawford
                                                 me@computer.rip

Support me on Ko-Fi and receive EYES ONLY, a monthly or more special edition.

Discuss this, complain, etc: #computer.rip:waffle.tech on Matrix
Me, elsewhere:Mastodon,Pixelfed,YouTube

This website is begrudgingly generated by the use of software. Letters to the
editor are welcome via facsimile to +1 (505) 926-5492 or mail to PO Box 26924,
Albuquerque, NM 87125.

```


