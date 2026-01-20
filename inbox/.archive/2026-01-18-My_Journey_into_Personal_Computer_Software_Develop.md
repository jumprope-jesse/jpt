---
type: link
source: notion
url: https://farrs.substack.com/p/my-journey-into-personal-computer
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-04-21T03:01:00.000Z
---

# My Journey into Personal Computer Software Development in 1983

## AI Summary (from Notion)
- Historical Context: The document focuses on the author's experience in personal computer software development in 1983, a time when PCs were emerging but still viewed as toys by some professionals.
- Job Acquisition: The author took a risk to transition from Digital Equipment to Software Arts, motivated by the opportunity to work on VisiCalc, an original spreadsheet program.
- Key Figures: The author interacted with Bob Frankston, co-creator of VisiCalc, who proposed a segmentation strategy to overcome memory limitations in the program.
- Segmentation Success: The author successfully implemented the segmentation strategy, allowing the program to fit within the IBM PC's memory constraints.
- Bug Fixing: The author became a prolific bug fixer, clearing a long-standing bug list and adding new features, which contrasted with the slow pace of other programmers.
- Management Dynamics: The management's focus shifted away from VisiCalc to newer projects, leaving the author and a couple of others to work on the outdated program.
- Recognition and Misunderstanding: The author's rapid success led to skepticism from peers and management, who labeled the author as an "idiot savant," questioning their qualifications and intelligence.
- Support from Staff: Despite the derogatory label, the author gained respect and support from non-programming staff within the company.
- Exit from PC Software: Frustrated by the internal politics and labeling, the author chose to leave the personal computer software domain and return to more familiar programming environments like Unix and C.
- Takeaway: The narrative illustrates the challenges of workplace dynamics, the importance of recognizing talent regardless of background, and the impact of management perceptions on career progression.

## Content (from Notion)

In 1983, Personal Computers were quite the up and coming thing. You could buy your own for a few thousand dollars. Though they were mostly considered toys by many East Coast programmers (more expensive "workstations" were the rage), there had already been some interesting and promising applications developed for it.

I thought (along with a lot of other people) that these were definitely the thing of the future. I was considering a new job, so I decided to take a bit of a risk, and look for work writing Personal Computer Software.

I was able to get an interview at one of the top Personal Computer software development companies of the area. The company was called "Software Arts". It was the company of the creators of "VisiCalc", the original spreadsheet.

During the interview process, I actually met the creators of VisiCalc. People had scared me about one of them, Bob Frankston, as someone difficult to talk to, and quick to temper. But when I met him, I actually found a genuine pleasant programmer-type. His problem was that he didn't really internalize that he was one of the company bosses, and felt that he was just a super-cool programmer. As such, if he felt like yelling at you - it would be perfectly normal because, of course, if he was wrong - you would yell right back and tell him to stfu! The only problem was, as the company founder and chief programmer or something - nobody was actually going to yell back at him. But they would grumble a lot later on, thereby giving him a bad and undeserved reputation.

The work was one of those "improve performance" details. They were doing a version of VisiCalc for the newly emerged IBM PC. The program was "almost ready", but it wouldn't fit in the memory limit! If I recall correctly, the memory limit was 256K (that's K, not M) because the "floppy disks" could only hold that much.

Bob Frankston believed the program could be made to fit into the memory by using a "segmentation" strategy. Some people at Software Arts had given it a try, but had not been able to get much success or had decided the work was too boring. In any case, nobody wanted to do it, hence the job opening.

I heard out his ideas, and it made sense to me. They offered me a job with a 30% raise (I was working for Digital Equipment which was not known for best salaries) and I joined them.

Bob Frankston's ideas about segmentation were sound. As the original author of the program, he did have a good feel for VisiCalc code, and in fact I found it was very amenable to segmentation along the lines he had suggested.

So in 2-3 months, I was able to fit the program in the memory limits, with plenty of room to spare for new features.

That work having done, I became a regular part of the IBM PC VisiCalc team.

As I mentioned, the program was "almost ready". One of the "almost" parts involved the 256 K memory limit.

There was another part to the "almost". The bug list of the program had over 600 items. Most of the original programmers on the VisiCalc team had moved on to "better" stuff (more about that later.) Christine S and Joe B were the remaining programmers. Even if they solved 1 bug a day, it would take 60 weeks to clear the bug list. The actual rate was not 1 bug a day, some bugs took many days in fact. Not a very happy situation -- but the Software Arts management was already seeing VisiCalc as a "yesterday" thing. Dan Bricklin, a bright and friendly guy who had the original spreadsheet idea and then involved Bob Frankston for the coding, felt that since VisiCalc had already been done and they already owned the spreadsheet market, the best bet was to focus on more new ideas rather than wasting much resources on VisiCalc.

The management thought "TK!Solver", an algebra-type program, would be the next "spreadsheet" type revolution. So that's where the programmers that the company felt were the "best", went.

Which left two programmers on the VisiCalc team - Christine S and Joe B, and then also I, since I had finished the "segmentation" problem ahead of schedule.

Truth be told, the "segmentation" problem was indeed boring and routine after a while. So I was only too happy to get into something more exciting. Like, uh, bug-fixing.

The company had the perfect "bug" solving system as far as I was concerned. Nobody assigned you anything. You looked over the bug list, "checked out" a bug, solved it, and "checked in" the bug.

Naturally, the hairy bugs were left alone as nobody checked them out.

But being a natural programmer, I liked my bugs complex. The easy ones were good to perk me up while I finished my morning coffee, another entertaining couple by lunch, and then often I could get one or two more by the end of the day. So I started solving bugs at the rate of 5 or so, a day.

This caused problems.

The Quality Assurance staff was very happy. They were used to programmers trying to explain to them why something wasn't a bug, or telling them it would be solved any time soon, now. And here I was, announcing every day that these 3-5 bugs were off the list. Christine P, who was doing VisiCalc Quality Assurance, told me later on that when she saw my first email listing 5 solved bugs, she decided I had to be some kind of a fast-talker and fake. (I can't blame her, here were all these graduates of top technical universities, doing a bug maybe every two-three days, and here I was from a university known for liberal arts, claiming to have solved 5 in a day!) So with the intention to confront me and set me straight, she downloaded my fixes to her PC and checked those out. And what do you know, they were all indeed fixed!

VisiCalc management was happy. Other management was not. They didn't want much attention going to VisiCalc, the "old" program. (This was before anybody had heard of something called "Excel".)

Other programmers at Software Arts were also a problem. Software Arts had attracted a lot of highly talented pedigreed programmers. Software Arts would not normally have even looked at someone of my credentials, had it not been for the fact that none of their highly talented programmers wanted to do any boring work.

Now it turned out, many of these super-programmers had quietly looked at some of the more complex VisiCalc bugs at some time in the past, and had wisely decided not to "check out" the bug. But being super-programmers, they were very annoyed that somebody from an unknown (programming-wise) university would come in and solve those complex bugs without breaking a sweat or without spending one single evening on the premises.

Besides my educational background, at that time Indians weren't particularly considered to be suitable software material. (Amazing how the world turns, eh?)

So mostly, the super-programmers were trying to resolve how I could have solved these bugs, since obviously I couldn't be very intelligent. Well, that is, no way was I intelligent in the same way they were intelligent.

While the super-programmers and the super-managers (I believe Tracy Licklider was the actual management person, Bricklin and Frankston were above the daily management issues) were trying to resolve this dilemma, I was happily and busily solving the bugs.

Within a few months, the bug-list was empty, and VisiCalc management was encouraged to add more features to VisiCalc. So I added Graphics capabilities to VisiCalc, Christine S added sorting features (I can't remember if Joe B had been moved to another "better" project by then, but he probably was, because he was "in-clique".)

So the product was finally ready to be released.

And then things came to a head.

VisiCorp, the marketing organization for VisiCalc, was significantly unhappy with the performance of the product. That's because there was a rival called 1-2-3 from Lotus. It didn't have as many features (for example, it drew crappy line drawings instead of filled-out pie charts) but ran faster and took less memory.

VisiCalc running slower and taking more memory had to do with some inside politics. The in-clique had decided that the program had to be written in Lisp. At that time, there were strong limits on how fast you could run with a language like Lisp, and it was also a memory hog. With segmentation, I had been able to get everything to fit, but just fitting wasn't very good.

To me, the solution was simple -- rewrite the whole thing in something called "assembly language". That's what everybody else was doing on the PC platform in those days. I had already chosen to write the Graphics in assembly language (which is why the Graphics took very little memory and ran fast), and from my segmentation and bug-fixing work, I knew everything about everything else in the VisiCalc program. I could have easily rewritten the whole thing in assembly language in another 4-6 months if really encouraged. Without many bugs.

But turns out, nobody was going to encourage me, or even ask me!

As I mentioned earlier, Tracy Licklider and the super-programmer in-clique were busy trying to resolve the mysterious dilemma of how (a) I could be an Indian and not from a known programming school and (b) I could still fix bugs and add features at this amazing rate.

It looks like they had hit the psych books and all, because they had finally come up with a solution. Obviously, they had concluded, I was an "idiot savant". [An "idiot savant" is an idiot who happens to be mysteriously very gifted in a particular area, e.g. mathematical computations. Their conclusion was that because obviously I couldn't really be "intelligent", my seeming "intelligence" in solving bugs was a result of this "idiot savant" effect.]

Now, while the in-clique of the super-programmers and managers was busy dissing me, the other staff at the company had been noticing all this, and as a result, I had built an incredible support level among the non-programming staff. Non-management and non-programming personnel, such as quality assurance, accounting, sales, even front-desk, frequently sought me out to tell me about the good things they had heard about my work.

So the "idiot savant" declaration got back to me.

I suppose someone with a more combative attitude would have stayed on and fought this thing through, to get the respect he/she deserved.

I am not like that. Specially back then, I was very easygoing. While I could put in tremendous amount of work in something that I believed was worth doing, I just couldn't see the point of working the politics of it.

Being labeleld an "idiot savant" by the management in retaliation for having done some (what I thought to be) amazingly good work, frankly unnerved and annoyed me a lot.

My reaction was, I wanted to get the heck away from those crazies.

I knew many support staff liked me, but I was realistic enough to realize management and programming staff could cause much trouble for me, if they had an attitude like that.

So that was the end of my first brief foray into Personal Computer technology in the early 80s, as I went back into a familiar world of Workstations, Unix, and C programming.


