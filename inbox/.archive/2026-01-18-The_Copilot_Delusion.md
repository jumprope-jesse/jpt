---
type: link
source: notion
url: https://deplet.ing/the-copilot-delusion/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-05-23T03:43:00.000Z
---

# The Copilot Delusion

## Overview (from Notion)
- Impact of AI on Software Development: The text critiques the reliance on AI tools like GitHub Copilot, emphasizing that while they can assist with syntax and basic tasks, they often lack depth and understanding, potentially leading to poor code quality and technical debt.

- The Human Element: It underscores the importance of genuine programming skills and critical thinking, suggesting that relying too heavily on AI may lead to a loss of essential coding craftsmanship and a disconnect from the underlying technology.

- Cultural Commentary: The piece reflects a concern about the evolving tech culture, warning against mediocrity and the rise of developers who rely on shortcuts rather than mastering their craft.

- Personal Development: It advocates for hands-on learning and deep engagement with programming, which resonates with the idea of setting a strong example for your children, showcasing the value of hard work and dedication in any field.

- Entrepreneurial Perspective: As a founder, consider how the critique of AI tools could influence your approach to product development and team dynamics, ensuring that creativity and innovation are prioritized over mere efficiency.

- Potential for Frustration: Acknowledge the frustration that may arise from navigating the balance between leveraging AI assistance and maintaining a high standard of quality in your work.

- Alternate Views: Some may argue that AI tools enhance productivity and democratize programming, making it more accessible, but the text prompts a critical examination of whether this truly benefits the industry in the long run.

## AI Summary (from Notion)
Critique of AI coding assistants like GitHub Copilot highlights the illusion of productivity they create, arguing that reliance on such tools degrades programming skills and understanding, ultimately leading to mediocrity in software development. True programming requires deep engagement and knowledge of the machine, which AI cannot replace.

## Content (from Notion)

### Chapter 1: My Coworker, The Programmer

A shell of a man—more of a parrot than a person. My boss, a true believer in the sacred rite of Pair Programming, chained myself and this "programmer"-colleague together like conjoined twins from different planets. We shared a keyboard, but not a brain. Lord, not even close.

"Hold up. I’ve got an idea. Gimme the keyboard real quick."

An idea. Yes. The same way a toddler has “an idea” to stick a fork in a wall socket. I was halfway through constructing something beautiful—a lean, elegant piece of logic that sliced through complexity like a blade through butter—and here he comes, pounding the keyboard like it owes him money, pasting in code he Frankensteined from a stack overflow comment written by an Uncle Bob disciple in 2014.

Did he know what our system did? No.

Did he read the ticket? Absolutely fucking not.

Did he feel confident mutating global state with reckless abandon? He absolutely fucking did.

I’m doing some refactoring. Tightening the bolts, cleaning up component trees, re-aligning the chakras of the system.

Suddenly:

"Hey, I added a useEffect that refetches everything when anything changes. Cool, right?"

"Why?" I ask, blinking like a hostage on a tape sent home from a military operation gone wrong.

"It fixed the thing," he says. "Where the thing wasn’t working. It's a working thing now."

A chaos monkey disguised as a teammate. No tests. No profiling. No understanding of side effects or performance impact. Just blind clicking and tapping and typing. The programming equivalent of punching your TV to make the static stop.

And he did this with everyone. A one-man bug factory. Whispering half-formed solutions into the ears of juniors like a sick, twisted full-stack Rasputin. Apparently, friendly fire will be tolerated.

The system explodes. Nothing deploys. The UI is frozen like the vegetables in my freezer I was supposed to defrost 8 years ago. And where is my dear co-pilot?

Nowhere.

He’s vanished—probably reading about a shiny new JS framework he’ll try to shove down my throat next week. Meanwhile, I’m left spelunking through callback hell with a flashlight made of regret.

My boss corners me.

"Why aren’t you pairing more with him? He types twice as fast as you."

Of course he does. So does a cat having a seizure on a mechanical keyboard. But that doesn’t mean it should be writing production code.

I kept pushing myself—learning infrastructure, refining my mental models, sweating over trade-offs. And him? He googled. He skimmed. He pasted. Occasionally he’d show off a clever trick—half-correct, contextless—and the team would ooh and aah like cavemen discovering fire.

And I got lazy. Of course I did. When the system forces you to code with a hallucinating clown, eventually you stop resisting. You let him type. You let him be "productive." You check out. You surrender your brain to the noise and just float.

Captain Obvious is here to Save the Day.

I wasn’t talking about a programmer. I was describing GitHub Copilot. Or Claude Codex. Or OpenAI lmnop6.5 ultra watermelon.

This isn’t about tools or productivity or acceleration. It’s about the illusion of progress. Because if that programmer—if that thing, that CREATURE—walked into your stand-up in human form, typing half-correct garbage into your codebase while ignoring your architecture and disappearing during cleanup, you’d fire them before they could say "no blockers".

But slap Microsoft's marketing label on it and plug it into the IDE of every developer in the org? Now that’s innovation. Science. Progress. Profit.

A real copilot, on a commercial airline? They know the plane. The systems. They’ve done the simulations. They go through recertification. When they speak, it’s to enhance the pilot—not to shotgun random advice into the cockpit and eject themselves mid-flight.

Copilot isn’t that. It’s just the ghost of a thousand blog posts and cocky stack-overflow posts whispering, "Hey, I saw this once. With my eyes. Which means it's good code. Let’s deploy it." Then vanishing when the app hits production and the landing gear won’t come down.

If you let that ghost fly the plane, you deserve the ball of flames you go up in.

### Chapter 2: The Props

Let’s get one thing straight before I resume torching this synthoid hellspawn with the fury of the sun: it ain’t all bad.

Even the grifter at the poker table with a booze lobotomy occasionally hits a flush. And Copilot? Well, sometimes it knows a thing or two.

You’re young. You’ve never touched C++. You’re staring at the syntax like it’s some Martian cave painting. You ask the oracle for help and boom—there it is. Templates, smart pointers, range-based for-loops—syntactically pristine, like it slithered straight out of Bjarne’s brain and onto your screen.

Of course, it doesn’t know the edge cases. It won’t whisper, "Hey—shared_ptr might leak if you get clever and toss raw pointers into the mix like a maniac." It doesn’t point you to the holy scrolls where veterans debate exception guarantees like theologians dissecting scripture. But if you already know what you want and just need the incantation, it’s a better, quicker scribe than most human interns—and it doesn’t complain when you ask it to write template metaprogramming code at 3 a.m.

Now let’s say you’re doing real programming work—system design. Big-boy decisions. Infrastructure. The kind of thing that requires a spine and an encyclopedic knowledge of the ByteByteGo YouTube channel. You lay out your plan like a general before a war: here’s the ingress, here’s the queue, here’s the cache invalidation policy that might just kill us all.

Then you ask Copilot, "Hey, what’s going to break?"

Suddenly, it’s rattling off weaknesses like a security auditor. Maybe half of them are dumb. Maybe some are duplicated. But it dumped the brainstorm faster than your junior ever could, and now you’ve got the ammo to write a spec that makes you look like you crank your hog with Martin Kleppmann himself.

Sometimes you’re just tired. Not mentally dead, but running low—your brain’s in "turning-object-into-a-string" mode. You don’t need help. You just don’t want to rotate the matrix in your skull like you’re solving a Rubik’s Cube made of jelly.

So you say, "Hey, I’ve got this C# object and I want a LINQ query that groups it by field X, sums Y, and filters Z."

Copilot answers like a weird little gremlin slave creature with a clipboard: "Done, boss."

You don’t trust it. You check it line by line. But still—you didn’t have to juggle twenty method chains in your head, and that buys you time to think about actual problems.

Maybe you’re reading some dense mathematical whitepaper, the kind written by deranged mathematicians with PhDs and no regard for human sanity. You don’t have the energy to transmute this LaTeX-laden elder scroll into code. Copilot takes a swing and gives you a half-baked pseudocode scaffold. Garbage? Maybe. But garbage you can build on. You handle the performance tuning, the SIMD, the low-level grit. It just gave you the scaffolding to stack explosives on.

Maybe you inherited someone else’s codebase. A minefield of nested closures, half-commented hacks, and variable names like d and foo. A mess of complex OOPisms, where you have to traverse 18 files just to follow a single behaviour. You don’t have all day. You need a flyover—an aerial view of the warzone before you land and start disarming traps.

Ask Copilot: "What’s this code doing?"

It won’t be poetry. It won’t necessarily provide a full picture. But it’ll be close enough to orient yourself before diving into the guts.

So—props where props are due. Copilot is like a greasy, high-functioning but practically poor intern:

- Great with syntax memory.
- Surprisingly quick at listing out your blind spots.
- Good at building scaffolding if you feed it the exact right words.
- Horrible at nuance.
- Useless without supervision.
- Will absolutely kill you in production if left alone for 30 seconds.
Now, let’s go back to setting it on fire.

### Chapter 3: You as a Programmer

First things first: I like to code. Not supervise. Not hover over a synthetic lobotomized chatbot like some drooling silicon intern trying to remember what std::move actually does. I don’t want to be the meatbag middle-manager reviewing some neural net’s fever dream of a switch statement. I want to build shit. Real shit. Weird shit. Systems that are *on fire* type shit.

"But I just use AI for boilerplate!" you whimper, clutching your Co-Pilot subscription. Listen to yourself. If you’re writing the same boilerplate every day like some industrial-age cog monkey, automate it yourself. Write a library. Invent a macro. Reclaim some dignity. If AI’s doing your "boring parts", what exactly is left for you to do? Fidget with sliders? Paint by numbers while the inference works it's magic?

And let’s not ignore the FOMO goblins. I see you. Pounding Monster energy at 2 A.M., telling yourself you’re "building the future" while you slap together some Frankenstein CRUD app with a bot spoon-feeding you syntax it scraped from 2016 GitHub. It's buggy. It's ugly. You didn't even give it a once over before you posted that video to Twitter. "I’m just moving fast!" you say. Yeah—straight off a cliff, like a lemming. AI isn’t helping you build something novel. It can’t. It only knows what’s been done before. It’s autocomplete with a superiority complex.

You want real connection to code? You earn that. You dig in. You wrestle with segfaults at 3 in the morning. You pace your apartment muttering about pointer arithmetic. You burn through Handmade Hero until you get it. You write your own damn notes instead of snapping lecture slides and pretending it counts. When you outsource the thinking, you outsource the learning. You become a conduit for a mechanical bird regurgitating it's hunt directly into your baby-bird mouth. You don’t know your code. You’re babysitting it.

Let’s talk about the quality of your code, too—because it ain’t getting better. Most engineers already write bloated, abstracted, glacial code that burns CPU cycles like a California wildfire. Clean code? Ha! You’re writing for other programmers’ academic circlejerk, not the hardware. You’ve forgotten that the machine matters. AI has no concept of memory locality. No intuition for cache misses. It won’t unroll a loop or spot the false sharing in your atomic struct. It’s trained on code that’s already an insult to silicon.

The problem isn’t just laziness. It’s degradation. Engineers stop exploring. Stop improving. Stop caring. One more layer of abstraction. One more lazy fetch call inside a render loop. Eventually, you’re living in a cathedral of technical debt, and every user pays—milliseconds at a time, each click a tax on your apathy.

And the "copilot" branding. A real copilot? That’s a peer. That’s a certified operator who can fly the bird if you pass out from bad taco bell. They train. They practice. They review checklists with you. GitHub Copilot is more like some guy who played Arma 3 for 200 hours and thinks he can land a 747. He read the manual once. In Mandarin. Backwards. And now he’s shouting over your shoulder, "Let me code that bit real quick, I saw it in a Slashdot comment!"

At that point, you’re not working with a copilot. You’re playing Russian roulette with a loaded dependency graph.

You want to be a real programmer? Use your head. Respect the machine. Or get out of the cockpit.

### Chapter 4: The Computer as a Machine

Listen. You’re human. Soft flesh, rotting teeth, synapses pissing electrical signals at each other motivated by caffeine and spite. But you—at your most frazzled, sleep-deprived, raccoon-eyed best—you can try. You can squint at the layers of abstraction and see through them. Peel back the nice ergonomic type-safe, pure, lazy, immutable syntactic sugar and imagine the mess of assembly the compiler pukes up. You can feel the cache lines like a sixth sense. You know where the data wants to be. And where the silicon gets angry when you screw that up.

The machine is real. The silicon is real. The DRAM, the L1, the false sharing, the branch predictor flipping a coin—it’s all real. And if you care, you can work with it. You can make your programs slither through memory like a steel serpent with little to no overhead. You can tee up prefetches with finesse. You can hand-roll an allocation strategy that makes malloc look like child's play. You can know—actually know—when it’s time to crack your knuckles and write a few lines of filthy, yet beautiful inline assembly to directly inject steroids into your program's shiny cheeks.

But the bot? The bot? The bot has no clue.

The bot has zero understanding. It can’t tell a page fault from a paper cut. It’ll hallucinate a memory model like I hallucinate after 2 days of no sleep. It can’t profile. It can’t understand a flamegraph. It can’t feel the cold burn of wasted CPU cycles on a hot loop. It’ll copy the advice of a sweaty stranger from an ‘08 StackOverflow thread who was benchmarking on a Pentium 4 with 512MB of RAM and a dream. It will say, "This is optimal", like it knows anything. Like it’s seen a cache miss. It hasn’t. You have.

The thing will feed you trash. It’ll feed you fake wisdom from fake people and beg you to trust it. But if you want to make a fast, beautiful system—if you want to sculpt the kind of software that gets embedded in pacemakers and missile guidance systems and M1 tanks—you better throw that bot out the airlock and learn.

You build taste by doing. By hurting. By shaving nanoseconds with surgical tools. By writing a routine on Monday, rewriting it Tuesday, and realizing Wednesday it still sucks. You don’t build taste by asking the MS Clippy of 2025 how to do your job.

We are, in the long arc of computing history, still covered in dirt, yanking our bits around with ploughs. We ride horses. But some of us—the ones with blown-out eyeballs and scorched keyboards—some of us know how to build the next thing. Trains. Speedboats. Hypersonic jets of pure code.

And the ones who keep using AI like it’s a divine oracle? They’ll be out there trying to duct-tape horses to an engine block, wondering why it doesn’t fly. Saying, "Hey. It's still not flying. ... ... ... Still not flying. ... ... ... Still doesn't fly fix it please.".

### Chapter 5: Conclusion

The thing I hate the most about AI and it's ease of access; the slow, painful death of the hacker soul—brought not by war or scarcity, but by convenience. By buttons. By bots.

The real horror isn’t that AI will take our jobs—it’s that it will let people in who never wanted the job to begin with. Vampires with SaaS dreams and Web3 in their LinkedIn bio. Empty husks who see the terminal not as a frontier, but as a shovel for digging up VC money. They’ll drool over their GitHub Copilot like it’s the holy spirit of productivity, pumping out React CRUD like it’s oxygen. They'll fork VS Code yet again, just to sell the same dream to a similarly deluded kid.

There was once magic here. There was once madness.

Kids would stay up all night on IRC with bloodshot eyes, trying to render a cube in OpenGL without segfaulting their future. They cared. They would install Gentoo on a toaster just to see if it’d boot. They knew the smell of burnt voltage regulators and the exact line of assembly where Doom hit 10 FPS on their calculator. These were *artists*. They wrote code like jazz musicians—full of rage, precision, and divine chaos.

Now? We’re building a world where that curiosity gets lobotomized at the door. Some poor bastard—born to be great—is going to get told to "review this AI-generated patchset" for eight hours a day, until all that wonder calcifies into apathy. The terminal will become a spreadsheet. The debugger a coffin.

Because you don’t know what you don’t know. That’s the cruel joke. We’ll fill this industry with people who think they’re good, because their bot passed CI. They'll float through, confident, while the real ones—the hungry ones—get chewed up by a system that doesn’t value understanding anymore. Just output. Just tokens per second.

And what’s worse, we’ll normalize this mediocrity. Cement it in tooling. Turn it into a best practice. We'll enshrine this current bloated, sluggish, over-abstracted hellscape as the pinnacle of software—and the idea of squeezing every last drop of performance out of a system, or building something lean and wild and precise, will sound like folklore.

If that happens? If the last real programmers are drowned in a sea of button-clicking career-chasers—then I pity the smart outsider kids to come after me.

Defer your thinking to the bot, and we all rot.


