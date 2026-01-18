---
type: link
source: notion
url: https://linusakesson.net/programming/kernighans-lever/index.php
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-12-22T12:08:00.000Z
---

# Kernighan's lever

## Overview (from Notion)
- Embrace the concept of Kernighan's lever: Use short-term challenges to drive long-term growth in your coding skills.
- Recognize that clever coding can lead to complex debugging, which is an opportunity for learning and skill enhancement.
- Reflect on how debugging experiences can parallel parenting challenges—both require patience, problem-solving, and the realization that mistakes lead to growth.
- In the fast-paced environment of NYC, leverage your experiences in software to create innovative solutions that simplify life for others, particularly in family-oriented tech.
- Consider alternate viewpoints: Some argue that debugging methods can be systematic, suggesting that cleverness isn’t always necessary. This can lead to more straightforward coding practices.
- Use your role as a company founder to foster a culture of learning and experimentation, encouraging your team to embrace complexity as a path to improvement.
- Balance clever coding with clarity and simplicity, ensuring that others can understand and maintain the code you write.

## AI Summary (from Notion)
Kernighan's lever highlights the challenge of debugging, emphasizing that clever coding can lead to difficulties in problem-solving. It suggests that skill in programming is developed through practice and motivation, which can be driven by the desire to overcome challenges. Avoiding clever techniques may hinder personal growth, while engaging with complex problems can enhance one's abilities. The concept of flow illustrates the balance between skill level and challenge, advocating for tackling problems to gain experience and improve as a programmer.

## Content (from Notion)

Brian Kernighan famously wrote:

Everyone knows that debugging is twice as hard as writing a program in the first place. So if you're as clever as you can be when you write it, how will you ever debug it?

— The Elements of Programming Style, 2nd edition, chapter 2

The following version also circulates on the net:

Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it.

This second quote may or may not be by Kernighan — the questionable use of "by definition" makes me uncertain — but it is useful as a provocative sound bite conveying the same essential idea.

It is tempting to interpret Kernighan's aphorism as a warning: Stay away from clever techniques, it seems to say, because if you write clever code, you will never be able to get it to work. But this interpretation is unfortunate, and rests on the false assumption that cleverness is static.

While it is possible that Kernighan intended us to interpret the message in a specific way, he wisely restricted himself to merely presenting an observation, allowing us to draw our own conclusions from it.

Pay close attention to what is actually being said: Having written code as cleverly as you can, you will suddenly face a problem that you are not clever enough to solve. Certainly, "clever" in this context does not refer to some innate talent, because nobody is born with the ability to write clever code in the first place. The "cleverness" required to write and understand intricate code is an acquired mental skill.

Cat at keyboard

If you are a programmer, you will be familiar with a sense of wonder, gradually transforming into utter stupor, as you stare at some perfectly reasonable code that couldn't possibly fail, and yet somehow it does. And since you are confident that you understand how the code works, having written it yourself, you feel that you must be able to figure out what is going on. Not only the desire to deliver working software on time, but other powerful forces such as pride, stubbornness and curiosity contribute to the motivation that pushes you onwards through the arduous task of tracking down the root cause of the error. Suddenly you see it, and you're blinded by a bright light as all the pieces fall into place. The inexperienced programmer may fall into the trap of self-degradation: "Oh, look at how stupid I was!" But that same sentiment is proof that your programming-related cleverness, or skill, has increased: "Oh, look at how clever I've become!" (Although I wouldn't recommend saying that out loud.)

Skill is the result of practice, that is, of systematically trying to work slightly beyond one's ability. Quite understandably, most of us don't spend that kind of effort unless we have good reason to. Hence, without motivation we do not practise, but simply cruise along at our current level and never improve any further.

The mind is very good at rationalising, and will convince us that our current skills are sufficient, that we are all "good enough"; certainly better than the average programmer anyway. The human brain will do this trick regardless of our actual level of skill. So while we all tend to consider ourselves sufficiently skilled right now, we never regret improving.

You effortlessly wield clever programming techniques today that would've baffled your younger self. (If not, then I'm afraid you stopped evolving as a programmer long ago.) But this improvement is the result of practice, and something must have motivated you to put in all those hours of work. Kernighan's witty remarks provide a clue: In programming, as soon as you work at your current level, you will automatically end up in a situation where you have to work beyond your current level. By means of this very fortunate mechanism, you will leverage several basic human drives (honour, pride, stubbornness, curiosity) into providing the motivation necessary for improvement.

I call this mechanism Kernighan's lever. By putting in a small amount of motivation towards the short-term goal of implementing some functionality, you suddenly end up with a much larger amount of motivation towards a long term investment in your own personal growth as a programmer.

If we deliberately stay away from clever techniques when writing code, in order to avoid the need for skill when debugging, we dodge the lever and miss out on the improvement. We would then need other sources of motivation in order to grow as programmers, and if no such motivation appears, our abilities stagnate (or even deteriorate).

The psychological concept of flow, somewhat simplified, can be used to visualise the process. Flow is when you are "fully immersed in a feeling of energised focus, full involvement, and enjoyment in the process of the activity" (wikipedia), and it only occurs when the challenge that you are tackling matches your current level of skill.

Flow chart

Implement below your ability, and you get to debug in the "flow" area.

Flow chart

Implement at your ability, and the debugging will be frustrating, but you gain skill.

You will find yourself situated at a particular x-coordinate, corresponding to your current level of skill. If writing code is a point on this graph, then (according to Kernighan's assumption) debugging the same code would be a point a fair bit directly above it.

It is certainly possible to deliberately pick a low starting point just to avoid ending up in the frustration area. But this will put you squarely in the boredom area, and boredom is frankly no better than frustration. However, should you pick a starting point in the enjoyable flow area, Kernighan's lever will screech into action and push you sideways through the graph, increasing your skill until it matches the challenge posed by the bugs in your code.

Naturally, the real world is more complex than this, and you will sometimes have compelling reasons to go for the boring option, and artificially reduce your cleverness in order to dumb down the debugging phase. But it may harm your long-term personal development if you go down that road every single time you write a program.

In conclusion, the answer to Kernighan's rhetorical question — "how will you ever debug it?" — is straight-forward: By tackling the problem, thereby gaining valuable experience and becoming more clever in the process. And the second version of the quote can be adorned with a single word at the end: Yet.

### Discuss this page

Disclaimer: I am not responsible for what people (other than myself) write in the forums. Please report any abuse, such as insults, slander, spam and illegal material, and I will take appropriate actions. Don't feed the trolls.

Jag tar inget ansvar för det som skrivs i forumet, förutom mina egna inlägg. Vänligen rapportera alla inlägg som bryter mot reglerna, så ska jag se vad jag kan göra. Som regelbrott räknas till exempel förolämpningar, förtal, spam och olagligt material. Mata inte trålarna.

Anonymous

Sat 22-Dec-2012 00:10

If this is all true, a perfect solution would be to debug the program 10 years after you've wrote it...

However, you will be tempted to rewrite it because after those years the code will be rated down into the boring area, so you'll need another 10 years to wait to debug it.

Anonymous

Wed 21-Dec-2022 20:41

Mark Fitzsimmons

Engineer, woodworker, philosopher, fan

My response is, both of the original statements are false, because the skills required for programming and debugging are subtly different, and not inherently easier or harder. The debugging task has methods that can be systematic and stepwise (making the task "easier"), and sometimes requiring additional code writing to interrogate what were, in your original inspired creation phase, leaps of intuition or complex design you imagined were simpler than you thought (making the task "harder"). Debugging is in part a process of learning how complex your design intent really is, when translated into a language of a complex machine. They are not really separate things, programming and debugging.

Anonymous

Tue 15-Aug-2023 07:17

This matches with my experience as well. Thanks for sharing.

Talmid

Anonymous

Sun 11-Feb-2024 22:21

My interpretation of "clever" as Kernighan uses it is based on writings by him and Thompson in the Unix heyday. Thompson wrote the kernel using simple mechanisms that could be optimzied later if required, and only optimized after profiling. So "clever" could be interpreted as overdesigned. Of course the points you make about improvement are valid, and if we interpret "clever" as meaning as good an algorithm and data structure as possible, then yes, by all means, so long as the pattern can be discerned by others later. Like good writing, one must write elegantly and clearly.

Anonymous

Tue 8-Oct-2024 20:21

Two authors, Brian Kernighan and Bill Plauger, wrote "The Elements of Programming Style" while working at Bell Labs in the 70's. Bill also authored several books. Bill probably wrote the first commercial C compiler and a UNIX clone called Idris. Brian and Bill were brilliant programmers who were convinced to write the elements of programming style because of the dreadful Fortran code published in numerical analysis texts. They collaborated on two further books focused on software tools, one in Ratfor and the other in Pascal.


