# Programming Philosophy & Mindset

Perspectives on the craft of programming, career attitudes, and the joy of coding.

---

## Lehman's Laws of Software Evolution

*Source: https://two-wrongs.com/laws-of-software-evolution - Added: 2026-01-18*

Two fundamental laws from M.M. Lehman (1974) that explain why software requires ongoing maintenance:

**Law 1: Continuing Change**
Software exists to support a real-world task. As the real world changes, the software must change with it or become increasingly less relevant.

**Law 2: Increasing Complexity**
As software is changed, its complexity will increase, raising the cost of further changes—unless effort is spent countering this effect.

### Why This Matters

These laws predate modern corporate software practices (1974), countering the argument that maintenance is purely manufactured demand. Most software interacts with a changing world—adapting to other software and to users who change their attitudes and processes.

### Practical Applications

**The Feedback Loop Problem:**
Teams can get stuck in a reinforcing loop where changes become increasingly difficult. The way out: establish stricter quality controls on changes to reverse the loop.

**Discontinued Product Maintenance:**
When supporting a discontinued product for years, resist the temptation for ugly quick hacks. On long time frames, investing more upfront in proper fixes reduces total cost. Cost savings should come from *fewer fixes* (only critical bugs), not *cheaper fixes*.

### The Nature of Software Change

Unlike manufactured products, code is malleable enough that we think of applying changes on top of existing code to get a new product. Code is more similar to genetic material than other types of design.

**Two approaches to this malleability:**

1. **Redesign processes** - Borrow from other engineering fields to reduce the effects of the second law
2. **Embrace malleability** - Avoid redesign processes entirely, but invest significantly in continuous refactoring to counteract complexity growth

The author favors the second approach, accepting that it accelerates the second law while working toward better software shape through refactoring.

### The Disconnect Between Intent and Reality

Independently of programmer work, users exist with jobs they're trying to perform. They may or may not find it convenient to slot our software into that job. A manager evaluating software quality also exists independently of the user–software–programmer network, with priorities that may not align.

Good intentions don't alter software's actual performance or relationship with users.

---

## The Ontology of Error Messages (Mark J. Nelson)

*Source: https://www.kmjn.org/notes/message_existence.html - Added: 2026-01-18*

A whimsical philosophical analysis of a Microsoft Outlook error message:

> "This message can't be saved because it no longer exists. It can only be discarded. Make sure you copy the contents of the message before you discard if you want to use them later."

**The Paradoxes:**

1. **Indexical problem**: "This message does not exist" - we're referring to something that supposedly doesn't exist
2. **Asymmetric operations**: Saving requires existence, but discarding doesn't. Perhaps discard is a no-op on non-existent objects?
3. **Contents without existence**: The message has copyable contents despite not existing - but only until discarded

**The Troubling Implication:**

Discarding a non-existent message either:
- Causes the contents to cease existing (so discard isn't a no-op after all)
- Revokes accessibility without affecting existence (the contents persist but become unreachable)

A delightful reminder that error messages encode implicit metaphysics about object lifecycle, existence, and accessibility - usually without much thought given to philosophical consistency.

---

## "i'm just having fun" (jyn)

*Source: https://jyn.dev/i-m-just-having-fun/ - Added: 2026-01-18*

A compiler developer's perspective on learning, specialization, and the joy of programming. Key message: coding should be fun and exploratory, not competitive.

### It's Not a Competition

When people feel "dumb" compared to someone who knows compiler internals:

**You can do hard things:**
- Everything is learned through experimenting, reading, or working through obscure error messages
- There's no magic—it's just hard work sometimes
- Anyone can learn these things

**Everyone has their own area of specialization:**
- Not knowing about computer internals doesn't make you dumb or computer illiterate
- Different specialty ≠ less intelligent
- The author admits: "i don't know jack shit about economics or medicine"

### The STEM Mystique Problem

The author "really hates" that STEM has this mystique in society:

> "To the extent that engineering demonstrates intelligence, it's by repeatedly forcing you to confront the results of your own mistakes, in such a way that errors can't be ignored."

Other domains that deserve equal respect (they also force you to confront mistakes):
- Performance art
- Carpentry
- Running your own business or household

### The Joy of Fucking Around

> "If i can't feminize my compiler, what's the point?"

The author's motivation:
- Learning new things because "fucking around is the point"
- Half the time it's to make people say "jyn NO"
- Half the time it's to make art with code
- **"i really, sincerely, believe that art is one of the most important uses for a computer"**

Not motivated by money:
- Got into the industry before realizing how much programmers make
- Works for a European company without US tech salaries
- Does it "for the love of the game"

### Advice (If You Must Take It)

**#1: Build a tool for yourself**
- A spreadsheet that saves an hour a week
- A little website you play around with
- Something in RPGmaker
- The exact thing doesn't matter
- Important: it's fun AND you have something real at the end
- This motivates you even "when the computer is breaking in three ways you didn't even know were possible"

**#2: Look at things other people have built**
- You won't understand all of it—that's ok
- Pick an interesting part and do a deep dive on how it works

### Key Quotes

On learning:
> "all the things i know i learned by experimenting with them, or by reading books or posts or man pages or really obscure error messages"

On specialization:
> "everyone has their own specialty and mine is compilers and build systems"

On the purpose of coding:
> "the fucking around is the point"

### Why This Matters

- Challenges the competitive, credential-driven culture in tech
- Validates the playfulness that often gets trained out of developers
- Reminds us that art and creativity belong in programming
- Encourages building for the joy of building, not just career advancement

---

## The Appropriate Amount of Effort is Zero

*Source: https://expandingawareness.org/blog/the-appropriate-amount-of-effort-is-zero/ - Added: 2026-01-18*

A mindset principle that applies to both coding and life: the correct amount of **effort** is zero. Here, "effort" means energy expended *beyond* what a task actually requires—like unnecessary tension when typing or gripping a mouse too hard.

### The Core Insight

Over-efforting reduces performance. Evidence from elite athletes:
- **Katie Ledecky** broke world records feeling "so relaxed"
- Top marathon performers appear relaxed while struggling competitors look strained

This connects to the "joy of fucking around" philosophy: when you're not straining against yourself, work flows more naturally.

### Why Programmers Over-Effort

- **Hustle culture** - Tech glorifies grinding, long hours, proving yourself
- **Faulty calibration** - Strain feels like "real work," ease feels like slacking
- **Anxiety-driven coding** - Fear of bugs, deadlines, or looking incompetent adds tension that doesn't help

### Practical Application

- Notice physical tension while coding (shoulders, jaw, grip)
- Experiment with less mental "pushing" when stuck on a problem
- Trust that stepping back often produces better solutions than forcing
- Reduced effort ≠ reduced output (often the opposite)

Aligns with Daoist principle: "Nature does not hurry, yet everything is accomplished."

**Connection to other principles:** This complements "the fucking around is the point" from jyn's philosophy—both reject the idea that valuable work requires visible strain.

---

## Never Rewrite Code From Scratch (Joel Spolsky)

*Source: https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/ - Added: 2026-01-20*

Joel Spolsky's classic 2000 essay argues that rewriting code from scratch is "the single worst strategic mistake that any software company can make."

### The Fundamental Law

> "It's harder to read code than to write it."

This explains:
- Why code reuse is so hard
- Why every team has three functions for splitting strings
- Why programmers always think old code is a mess

### Why Old Code Looks Like a Mess (But Isn't)

That two-page function with weird LoadLibrary calls and mysterious conditionals? Those are **bug fixes**:

- One fixes Nancy's installer problem on machines without IE
- Another handles low memory conditions
- Another handles users yanking floppy disks mid-operation

Each bug took weeks of real-world usage to discover. The fix might be one line, but it represents days of debugging. **When you rewrite, you throw away all that knowledge.**

### The Strategic Disaster

Rewriting gives competitors 2-3 years of free runway while you:
- Ship an old version you can't meaningfully update
- Can't respond to market demands
- Waste money rebuilding what already exists

**Examples:**
- **Netscape**: Rewrote Navigator from scratch, version 5.0 never existed, market share collapsed during the 3-year gap before 6.0
- **Borland**: Rewrote Quattro Pro from scratch, shipped with fewer features than the original
- **Microsoft Word**: Almost made the same mistake with "Pyramid" project—saved only because they kept the old codebase alive

### The Three Kinds of "Mess"

When programmers say code is a mess, they usually mean one of three things:

1. **Architectural problems** - Code not factored correctly. Fix by careful refactoring, moving code, creating better interfaces. One programmer, careful check-ins. No rewrite needed.

2. **Inefficiency** - Slow rendering, etc. Only affects small parts. Optimize or rewrite *that part*. "1% of the work gets you 99% of the bang."

3. **Ugliness** - Mixed naming conventions, weird variable names. "Solve in five minutes with a macro in Emacs."

### The Fallacy of "More Experience"

> "There is absolutely no reason to believe that you are going to do a better job than you did the first time."

- The team that rewrites probably isn't the same team that wrote v1
- You'll make most of the old mistakes again
- You'll introduce new problems that weren't in the original

### The Dangerous Mantra

"Build one to throw away" is fine for experiments and prototypes. **It's dangerous for commercial applications.**

Refactor? Yes. Rewrite a class? Sometimes. Throw away the whole program? Almost never.

### Connection to Other Principles

This complements Lehman's Laws: software evolves through accumulated changes. Rewrites don't reset complexity—they lose the battle-tested knowledge embedded in bug fixes. Also relates to the software project failures documented elsewhere: many failures come from underestimating what the existing system actually accomplishes.

---

## Theory Building Without a Mentor (jyn)

*Source: https://jyn.dev/theory-building-without-a-mentor/ - Added: 2026-01-18*

A practical guide to understanding unfamiliar codebases by creating your own "theory" of the program—based on Peter Naur's 1985 article "Programming as Theory Building."

### The Core Idea

**Naur's claim (challenged):** You can't recover a theory of a program from code and docs alone.

**jyn's counter:** This is exactly what they do for a living—and it's a teachable skill.

### Key Insight: Theory Modification

Programs evolve over time as team members come and go. As ceejbot puts it:

> "programs get rewritten in place with new authors and new goals all the time"

**Implication:** You'll never recover the *same* theory as the original programmers. You're creating a *new* theory that's similar enough to work. Sometimes you'll need to adapt the program to your theory.

### The Process

#### 1. Start with a Specific Goal
- Programs are too large to understand all at once
- Focus on building theory for the parts you care about
- Only understand the rest insofar as it interacts with your parts

#### 2. Finding Relevant Code

**If you can trigger an error:**
- Search for the error message literal
- Get a backtrace to understand the call stack

**If no error is available:**
- Search for literal strings you know exist (command names, UI text)
- Look for substrings that might be part of templates
- Use an LSP to find all callers of a function (better than regex)

**Reverse-engineer the stack:**
- Find callers, narrow down by skimming what they do
- Work your way up until you find the entry point

#### 3. Verify Your Understanding

**Mini experiments:**
- Trigger nearby error conditions to confirm you're in the right place
- Process of elimination: if certain logging/errors didn't happen, rule out code paths
- Simplest experiment: `exit(1)` - easy to notice, doesn't change state

**With a debugger:**
- Break at functions to confirm they execute
- Print local variables
- Hardware watchpoints to see where memory is modified
- Time-travel debuggers (rr) are especially powerful

#### 4. Match Existing Patterns

**When writing new code:**
- Copy small snippets (10-15 lines max) from elsewhere in the codebase
- Modify to your needs
- Goal: make your change as similar to existing code as possible
  - Reduces bug risk
  - Increases maintainer acceptance

**More than 15 lines copied?** → Look for a higher-level API to reuse or create.

#### 5. Test Your Theory

- Find existing tests using the same search techniques
- Read test READMEs (often better documented than code)
- Find how to run individual tests (iteration time matters!)
- Write tests *before* modifying code to verify your theory
- Run existing tests first to identify flaky/environment-dependent ones

### Practical Tips

- Look for `CONTRIBUTING.md` for test documentation
- Check for README files in test directories
- Use `--help` on test commands to find individual test flags
- When `screen:expect()` fails, look for `snapshot_util` helpers

### Key Takeaway

> "reading source code is surprisingly rewarded"

This skill—creating theories from code alone—is valuable for both debugging and adding features. The article focuses on the "micro" level (small portions); macro-level theory building (design decisions) is a separate skill.

---

## Do The Simplest Thing That Could Possibly Work

*Source: https://www.seangoedecke.com/the-simplest-thing-that-could-possibly-work/ - Added: 2026-01-18*

A manifesto for simplicity-first software design. The core principle: when designing software systems, **do the simplest thing that could possibly work**—and take this advice further than you might expect.

### The Anti-Pattern: Designing for "Ideal"

Many engineers design by envisioning the "ideal" system: well-factored, near-infinitely scalable, elegantly distributed. This is entirely the wrong approach.

**Instead:** Spend time understanding the current system deeply, then do the simplest thing that could possibly work.

### Simple Looks Underwhelming

Real mastery often means learning when to do *less*, not more.

> "The fight between an ambitious novice and an old master is a well-worn cliche in martial arts movies: the novice is a blur of motion, flipping and spinning. The master is mostly still."

Great software design looks underwhelming. You know you're seeing it when you think:
- "Oh, I didn't realize the problem was that easy"
- "Oh nice, you don't actually have to do anything difficult"

**Examples of great simple design:**
- **Unicorn** - delivers critical web server guarantees (request isolation, horizontal scaling, crash recovery) by leaning on Unix primitives
- **Rails REST API conventions** - exactly what you need for CRUD in the most boring way possible

### The Rate Limiting Example

Want to add rate limiting to a Golang app?

**First instinct:** Add Redis with a leaky-bucket algorithm.

**Simpler questions to ask first:**
1. Can you keep request counts in-memory? (Lose some data on restart, but does that matter?)
2. Does your edge proxy already support rate limiting? (Just a config file change?)

Only add the infrastructure if simpler approaches genuinely won't work.

### Simplicity is Hard

> "It is not easy to do the simplest thing that could possibly work."

The first few solutions that come to mind are unlikely to be the simplest. Finding the simplest solution requires considering many approaches—it requires doing engineering.

**Hacks are NOT simple.** A hack adds complexity by introducing "another thing you have to always remember." The proper fix is almost always simpler than the hack—just harder to think of because it requires understanding the entire codebase.

### Defining Simplicity

1. **Fewer moving pieces** - fewer things to think about when working with the system
2. **Less internally-connected** - components with clear, straightforward interfaces
3. **Stable** - requires less ongoing work if no requirements change

**Tiebreaker for "which is simpler?":** Simple systems are stable. Compare two states and ask which requires more ongoing maintenance if nothing changes.

Example: In-memory rate limiting vs Redis?
- Redis must be deployed, maintained, monitored, requires separate deployment in new environments
- In-memory just... works
- Therefore in-memory is simpler (if it meets requirements)

### The Scale Obsession

> "The cardinal sin of big tech SaaS engineering is an obsession with scale."

**Why not to over-engineer for scale:**

1. **It doesn't work** - You can't anticipate behavior at 100x traffic because you don't know where bottlenecks will be. At most, prepare for 2-5x and deal with problems as they come.

2. **It makes code inflexible** - Decoupling services for "independent scaling" (often never used) makes features hard to implement because they now require coordination over the wire.

### YAGNI as Ultimate Design Principle

> "Think of it as taking YAGNI as the ultimate design principle: above single-responsibility, above choosing the best tool for the job, and above 'good design'."

You really can build a whole application this way:
- Start with the absolute simplest thing
- Only extend when new requirements force you to

### The Prediction Problem

> "The longer I spend working in tech, the less optimistic I become about our collective ability to predict where a system is going."

**Two ways to develop software:**
1. Predict requirements 6-12 months out, design for that
2. Design for current requirements (the simplest thing that could possibly work)

The main difficulty in good design is getting an accurate big-picture understanding of where the system *currently* is. Most design is done without that understanding.

### Connections

- **Relates to "The Appropriate Amount of Effort is Zero"** - Both reject the idea that visible strain/complexity indicates quality work
- **Relates to "Theory Building"** - Understanding the current system deeply is prerequisite to finding the simplest solution
- **Relates to "joy of fucking around"** - Simple systems leave room for play; over-engineered systems become rigid prisons

---

## How I Build Software Quickly (Evan Hahn)

*Source: https://evanhahn.com/how-i-build-software-quickly/ - Added: 2026-01-18*

Practical lessons on balancing speed and quality in software development. The author focuses on being a developer on a small team maintaining software over multiple years.

### Know Your Quality Target

Early-career instinct: make everything perfect. But there's no single "right way" to build software.

**Context determines quality bar:**
- 24-hour game jam → skip clean code
- Pacemaker device → demands perfection
- Most work → somewhere in the middle

**The author's rule of thumb:** Aim for an 8 out of 10 score, delivered on time. Good code that does its job with minor issues. Adjust based on project needs.

**Key questions:**
- What is my team's idea of "good enough"?
- What bugs are acceptable, if any?
- Where can I do a less-than-perfect job to ship sooner?

### Rough Drafts (Spikes / Walking Skeletons)

Implement a rough draft as quickly as possible, then shape it into the final solution.

**Qualities of a typical spike:**
- Lots of bugs and failed test cases
- Dozens of TODO comments
- Error cases unhandled
- `print()` statements everywhere
- No regard for performance
- Commit messages: "WIP"
- Unused packages still installed
- Lots of repeated code
- Hard-coded data
- Linter is angry

**The one important quality:** It vaguely resembles a good solution.

**Advantages:**
1. **Reveals "unknown unknowns"** - Discover surprises early, before perfecting code that gets discarded
2. **Problems disappear naturally** - Many issues resolve themselves as the draft evolves
3. **Helps focus** - Not fixing unrelated problems or worrying about perfect names
4. **Avoids premature abstractions** - Build what you need, not what you think you might need

**Concrete practices:**
- **Focus on binding decisions** - Language choice, database schema are hard to change later
- **Keep track of hacks** - Add TODO comments, later `git grep TODO` to find everything
- **Build "top to bottom"** - Start with UI/API before business logic; the "dream code" you want to write
- **Extract smaller changes** - Bug fix or dependency upgrade can be separate patches pushed sooner

### Soften the Requirements

Doing less is faster and easier. Questions to ask:
- Could I combine multiple screens into one?
- Is it okay to skip a particularly tricky edge case?
- Instead of supporting 1000 inputs, what if just 10?
- Is a prototype acceptable instead of full version?
- **What if we didn't do this at all?**

### Avoid Wandering Through Code

A dangerous distraction: start one task, end up hours later changing something unrelated. "Lost in the sauce."

**Two concrete fixes:**
1. **Set a timer** - Estimate task duration, get jolted when timer goes off. Also helps practice estimation.
2. **Pair programming** - Another person is less likely to let you waste their time on rabbit holes.

### Make Small Changes

Large patches are terrible advice. Small, focused diffs serve better:

- **Easier to write** - Less to keep in your head
- **Easier to review** - Lighter cognitive load, mistakes easier to spot, merged sooner
- **Easier to revert** - If something goes wrong
- **Fewer bugs** - Changing less at once reduces risk

**Build up:** One patch to fix a bug, one to upgrade a dependency, one to add the screen.

### Skills Worth Developing

- **Reading code** - By far the most important skill. Helps with debugging, understanding dependencies, learning
- **Data modeling** - Worth spending time on. Make invalid states unrepresentable. Schema mistakes cause headaches
- **Scripting** - Quick Bash or Python scripts speed you up. Use Shellcheck for Bash
- **Debuggers** - No substitute for a proper debugger. Much faster than print debugging
- **Knowing when to take a break** - If stuck without progress, step away. Often solve it in 5 minutes after returning
- **Prefer pure functions and immutable data** - Eliminates bugs, reduces mental overhead
- **LLMs** - Despite issues, can accelerate parts of development

### Connections

- **Relates to "Do The Simplest Thing"** - Both emphasize avoiding over-engineering and premature complexity
- **Relates to "The Appropriate Amount of Effort is Zero"** - Rough drafts reject perfectionism as necessary for quality
- **Relates to "Theory Building"** - Understanding existing patterns helps match them in new code
- **Relates to "joy of fucking around"** - Rough drafts preserve the playful exploration that makes coding enjoyable

---

## Peer Programming with LLMs (For Senior+ Engineers)

*Source: https://pmbanugo.me/blog/peer-programming-with-llms - Added: 2026-01-18*

A curated collection of resources on using LLMs effectively as a senior engineer, without the hype.

### The Core Tension

Programming with LLMs is both promising and frustrating. They can help with coding and debugging, but often waste time too. The key is treating them as **peer programmers**, not magic solutions.

### Key Principles for Senior Engineers

1. **LLMs are not as intelligent as they seem** - Maintain a balanced perspective on their capabilities; use them thoughtfully and strategically

2. **Document your prompts** - Keep track of prompts that work well; refine your use of AI tools over time

3. **Use LLMs for brainstorming and co-planning** - Great for generating ideas and exploring approaches before committing to implementation

4. **Balance AI assistance with human input** - LLMs may not replace the nuanced understanding and creativity that human engineers bring to problem-solving

### Seth's Rule

> "When you get stuck, first ask Claude, then ask a human."

This suggests a workflow where AI assistance is a first-line resource for unblocking, reserving human expertise for problems that require deeper context or judgment.

### Connections

- **Relates to "Theory Building"** - LLMs can help explore unfamiliar codebases, but building a real theory still requires human understanding
- **Relates to "Do The Simplest Thing"** - LLMs can suggest over-engineered solutions; apply simplicity filters to their output
- **Relates to "Building Software Quickly"** - LLMs can accelerate rough drafts, but the skill is knowing when their output needs refinement

---

## Reinvent the Wheel (Matthias Endler)

*Source: https://endler.dev/2025/reinvent-the-wheel/ - Added: 2026-01-18*

A defense of "reinventing the wheel" as a learning strategy. The core message: **Reinvent for insight. Reuse for impact.**

### The Harmful Advice

"Don't reinvent the wheel" is typically given by:
1. Those who tried to build a wheel and know how hard it is
2. Those who never tried and blindly follow the advice

Both positions discourage curiosity and exploration. Yet we owe many conveniences of modern life to people who *did* reinvent the wheel—we have much better wheels today than in 4500 BCE.

### Inventing Wheels Is Learning

> "What I cannot create, I do not understand."

To understand something fundamentally, you must implement a toy version first. It doesn't matter if it's any good—you can throw it away later.

In CS, many concepts are assumed beyond mere mortals: protocols, cryptography, web servers. More people should know how these work. People should not be afraid to recreate them.

### Everything Is a Rabbit Hole

Fundamental things are taken for granted. Strings and paths, for example, are super complicated. Great exercise: implement a string or path library yourself.

**What you'll learn:**
- Infinite complexity exists in everyday things
- Building something one person finds useful is humbling
- Humans created these abstractions—they're not perfect; you can make different tradeoffs

**Important caveat:** You only level up if you don't give up before reaching a working version. Jumping between projects teaches nothing.

### Reasons to Reinvent

- Build a better wheel (for some definition of better)
- Learn how wheels are made
- Teach others about wheels
- Learn about the inventors of wheels
- Be able to fix wheels when they break
- Learn the tools needed along the way
- Learn a slice of what building a larger system means
- Help someone needing a special wheel

Your wheel might not work for a car but could be perfect for a skateboard, bike, or something entirely different—a potter's wheel, steering wheel, flywheel.

### Reuse vs Reinvent

Don't reinvent out of distrust or ignorance of others' work. Study their work, reuse where fit. But if you never test your knowledge by building, how would you learn enough to advance your field?

Move quickly by running small experiments. In software, prototypes are cheap. Solve your own problem, start small, keep it simple, iterate.

### Connections

- **Relates to "joy of fucking around"** - Both celebrate curiosity-driven exploration over credential-seeking
- **Relates to "Theory Building"** - Building a toy version is how you construct an accurate mental model
- **Relates to "Learning Hard Things Framework"** - Reinventing the wheel is applying the single-loop to isolate and master one hard aspect at a time
- **Relates to "Do The Simplest Thing"** - Reinventing teaches you *why* the simple solution is simple, and which tradeoffs matter

---

## The Copilot Delusion

*Source: https://deplet.ing/the-copilot-delusion/ - Added: 2026-01-18*

A polemic against AI coding assistants (GitHub Copilot, Claude Code, etc.) arguing that they create an illusion of productivity while degrading programming skills and producing mediocre code.

### The Core Critique

AI coding assistants are like having a terrible pair programmer:
- Types fast but ignores architecture
- Pastes half-understood code from outdated sources
- Introduces bugs and technical debt
- Vanishes when things break
- Gets praised for "productivity"

> "If that programmer—if that thing—walked into your stand-up in human form, typing half-correct garbage into your codebase while ignoring your architecture and disappearing during cleanup, you'd fire them before they could say 'no blockers'. But slap Microsoft's marketing label on it? Now that's innovation."

### Where AI Actually Helps (Grudging Concessions)

The author grants some legitimate use cases:

1. **Syntax memory** - Learning a new language's idioms without absorbing edge cases
2. **Design review** - "What weaknesses does this architecture have?" (filter aggressively, but saves time)
3. **Cognitive offloading** - When you're tired and don't want to juggle LINQ chains in your head
4. **Mathematical scaffolding** - Translating LaTeX-laden whitepapers into starting pseudocode
5. **Codebase orientation** - "What does this inherited mess do?" (won't be poetry, but orients you)

**But:** These are narrow use cases requiring heavy supervision. The tool is "a greasy, high-functioning but practically poor intern" that "will absolutely kill you in production if left alone for 30 seconds."

### The Skills Argument

> "I like to code. Not supervise. Not hover over a synthetic lobotomized chatbot."

The problem isn't just laziness—it's degradation:

- **Outsourcing thinking outsources learning** - You become a "conduit for a mechanical bird regurgitating directly into your baby-bird mouth"
- **Boilerplate is a cop-out** - If you're writing the same code daily, automate it yourself. Write a library. "Reclaim some dignity."
- **AI can't do novel work** - "It can't. It only knows what's been done before. It's autocomplete with a superiority complex."

### The Machine Understanding Gap

This is the technical heart of the critique:

> "The bot has no clue. It can't tell a page fault from a paper cut. It'll hallucinate a memory model."

AI tools cannot:
- Understand memory locality or cache behavior
- Profile or interpret flamegraphs
- Feel the cost of wasted CPU cycles
- Unroll loops or spot false sharing
- Know when inline assembly is warranted

> "It'll copy the advice of a sweaty stranger from an '08 StackOverflow thread who was benchmarking on a Pentium 4 with 512MB of RAM and a dream."

**The real danger:** Most engineers already write bloated, over-abstracted code. AI-generated code makes this worse—it's trained on code that's "already an insult to silicon."

### The Cultural Concern

The author's deepest worry is cultural degradation:

- **Curiosity gets lobotomized** - Kids who would've stayed up debugging OpenGL will be told to "review this AI-generated patchset"
- **Understanding stops being valued** - "Just output. Just tokens per second."
- **Mediocrity gets normalized** - "We'll enshrine this current bloated, sluggish, over-abstracted hellscape as the pinnacle of software"

> "Defer your thinking to the bot, and we all rot."

### The "Real Copilot" Metaphor

A real airline copilot:
- Knows the plane and systems
- Has done simulations and recertification
- Speaks to enhance the pilot, not shotgun random advice

GitHub Copilot:
- "The ghost of a thousand blog posts whispering 'Hey, I saw this once. With my eyes. Which means it's good code. Let's deploy it.'"
- Then vanishes "when the app hits production and the landing gear won't come down"

### Connections

- **Relates to "Reinvent the Wheel"** - Both argue you must build to understand; outsourcing building outsources understanding
- **Relates to "joy of fucking around"** - The author mourns the loss of "kids on IRC with bloodshot eyes" who "wrote code like jazz musicians"
- **Relates to "Theory Building"** - You can't build a theory by having a bot write the code; you need direct engagement
- **Contrasts with "Peer Programming with LLMs"** - Where that piece offers balanced guidance, this is a polemic warning about skill atrophy
- **Relates to "Do The Simplest Thing"** - AI tools suggest over-engineered solutions because they're trained on over-engineered code

---

## The Magic of Software: Vision and Understanding as Bidirectional (Moxie Marlinspike)

*Source: https://moxie.org/2024/09/23/a-good-engineer.html - Added: 2026-01-18*

A meditation on what makes software unique and how the same dynamics that make a good engineer also make a good engineering organization.

### The Unique Nature of Software

Software exists in a strange position: we call ourselves "software engineers" but graduate with degrees in "computer science." Yet:

- **Science** disciplines exist in domains we didn't create and don't fully understand—occupied with discovering how things work
- **Engineering** disciplines combine available resources to manifest a vision

Software seems like straightforward engineering—we built the computer, we understand everything about it, nothing to discover. But this misses the deeper story.

### Vision and Understanding as Bidirectional

The conventional model: Start with a vision → do engineering to manifest it.

The reality: **Deep understanding of tools and technology yields new vision.** The relationship is intertwined and bidirectional.

### The Color Cycling Example

Early computer graphics animations (plasma, waterfalls, the Amiga boing ball) appeared to animate each pixel 30 times per second—which wasn't feasible on hardware at the time.

The actual technique: **color cycling** exploited indexed color systems (a memory optimization). Someone who deeply understood how indexed color worked realized they could create apparent animation by intelligently cycling the 256-color palette.

> "If I had been there at the beginning of it all, I'm not sure I would have predicted that by quickly turning electricity on and off, we could get… all this?"

**Key insight:** Indexed color wasn't created for animation. But engineers who understood it created something unexpectedly great. The understanding informed the vision.

### Abstractions as Shorthand vs. Black Boxes

Two ways to interact with abstraction layers:

1. **As shorthand** - for an understanding of what it's doing on your behalf
2. **As a black box** - no knowledge of internals

> "When we see everything as black boxes, it can be difficult to have any vision at all."

**The platform paradox:** When we create abstraction layers that don't require understanding the layers beneath (platforms, game engines), we expect an explosion of creativity. We do see an explosion of *more stuff*—but it's often more *mediocre* stuff.

Data on games: As it became easier to build games, more were made. But the number of highly-rated games (per Metacritic) has not increased over time.

> "I think we can only truly create when we truly understand what we have to create with."

### When Teams Become Tupperware

The same dynamics apply to engineering organizations.

**Two management philosophies:**
1. **Hierarchical** - Information flows up as reports/summaries, decisions flow down as budgets/priorities
2. **Autonomous teams** - Leadership creates "alignment" across teams pulling toward same vision

Both assume a **unidirectional relationship** between vision and engineering. Neither leaves room for the bidirectional relationship to emerge.

**The microservices architecture of organizations:** Autonomous teams are silos—abstraction layers treated as black boxes. When everyone sees every other part of the organization as a black box, transformative change can't happen.

### The Skype Thought Experiment

Imagine running Skype at the dawn of mobile. Everyone is aligned that mobile is the existential priority. But:

- Existing UX centered on "online/offline" (doesn't exist on mobile)
- Communication protocol depends on desktop-style "background" execution
- Codebase not deployable on mobile OSes

Everything needs to change. But every change depends on every other change. If everyone sees other teams as black boxes, the transformation simply won't happen.

> "While seismic shifts like the mobile revolution may seem rare, I think organizations ill-equipped for radical change are likely underperforming even in stable times."

### The Fruit Loops Fallacy

Aspiring entrepreneurs study current habits of successful entrepreneurs—but whether Jeff Bezos starts with a cold plunge or fruit loops has minimal bearing on his companies' success *now*. To imitate him, look at what he did in 1994.

Same fallacy for engineering organizations: Google's current practices emerged in a company with a money-printing business model. Without selective pressure, practices optimize for decision-makers' benefit, not for creating something great.

> "The most obvious example being the size of the organizations themselves, which I think is much more often the result of the benefits that accrue to the hiring manager for having more 'reports' than to any actual relationship with capacity, ability, or velocity."

### The Opportunity

> "If you're building a company or an engineering team today, I think the real opportunity lies in understanding that you're not bound by the conventions that have been passed down as 'standard.'"

The magic of both software and software organizations comes from those moments where **insight into how something works sparks entirely new ideas about what it could become**.

### Connections

- **Relates to "Theory Building"** - Both emphasize that deep understanding is prerequisite to effective work
- **Relates to "The Copilot Delusion"** - If AI treats codebases as black boxes, it can't have the insights that produce non-obvious results
- **Relates to "Reinvent the Wheel"** - Understanding comes from building, not just using
- **Relates to "Do The Simplest Thing"** - Simple solutions require understanding; black-box thinking produces over-engineering
- **Relates to engineering-leadership-principles.md** - Organizational Legibility section: when orgs become too legible (teams as interchangeable black boxes), they lose ability to innovate

---

## The Philosopher-Engineer Pitfall

*Source: https://www.lesswrong.com/posts/eormZktbERaLEMb2L/the-philosopher-engineer-pitfall - Added: 2026-01-18*

A warning for technically-minded people drawn to philosophical questions (consciousness, ontology, existence) about a specific failure mode: pursuing deep insights that cannot be communicated or externally validated.

### Who This Applies To

People who:
- Love ideas, especially consciousness and ontology/existence
- Are engineer-brained enough to think they can "solve" philosophical problems
- Are sociopathic, autistic, or antisocial but don't realize it yet
- Want to "save the world" for systematic reasons (you live there; other minds probably exist too)
- Have a one-track-mind that seeks The Most Valuable Thing To Do

### The Wrong Path

The failure mode unfolds gradually:

**Phase 1: The Letting Go**
- You drop social connections because they "legitimately don't interest you as much" as The Mission
- It doesn't feel like burnout because you're not forcing anything—you're releasing what doesn't serve you
- "It feels good; you feel lighter and more focused"

**Phase 2: The Trap**

The problem with philosophical insights about consciousness:

> "You do not realize the thing you are trying to investigate, the answers you now seek but do not yet know, have more of the Type Signature of {the feeling of sunlight on your skin} rather than {a proof of something like 1+1=2}."

Even if you achieve genuine insight, all you've done is "solidified an Intuition in your head." It *feels* like you've struck gold, but it cannot be shared in a scalable way.

**Phase 3: The Realization**

> "Trying to share this thing without realizing its full nature is a recipe for literal but thankfully temporary insanity."

The communication problem:
- Mental discovery, learning, building ontologies, building languages, building meaning—all tied together
- It took you years with "perfect communication" happening within your own head
- Perhaps it's all delusion, as no external Mind can check/correct The Full Thing In Your Head

### The Key Insight

> "if you enter into philosophical topics you must do so with open eyes; you can get truly truly lost because the feedback mechanisms suck."

Unlike hard science where you can show someone The Machine/Thing in the external world, philosophical insights about consciousness require literally conveying intuitions through Art—with the tech we have, this doesn't scale.

### The Recommendation

**Pivot to interpretability or hard science.** Choose domains where:
- You can build a Machine/Thing in the external world
- Others can verify your work independently
- Feedback mechanisms exist

> "That path will also lead to these insights, just more indirectly and with more confusion. This is always the tradeoff; there is no definite answer to 'how much thinking, or for how long, is too much before you should test the thinking'."

### The Social Cost

The author emphasizes this isn't just burnout—it's worse:
- You reach a state where even success (genuine insight) can't be utilized
- Your social skills have atrophied
- You've optimized for a local maximum that doesn't connect to the world

### Connections

- **Relates to "Do The Simplest Thing"** - Both emphasize feedback mechanisms and testing against reality
- **Relates to "Theory Building"** - The author's trap is building a theory that can never be validated externally
- **Relates to self-help-philosophy-critique.md** - Baker's warning about spending more time processing despair than addressing its causes echoes here
- **Relates to "Flounder Mode"** - Kevin Kelly's joy-driven approach works partly because his projects have external feedback (readers, viewers, users)
- **Contrasts with "The Copilot Delusion"** - That author mourns the loss of deep understanding; this author warns that some depths have no exit
- **Relates to "joy of fucking around"** - The philosopher-engineer loses the joy by treating thinking as work that must produce The Answer

---

## The Curse of Knowing How (Not A Shelf)

*Source: https://notashelf.dev/posts/curse-of-knowing - Added: 2026-01-18*

A meditation on how technical capability becomes a burden—once you know how to fix things, everything broken becomes your responsibility. The most human skill may be learning when to leave things broken.

### The Threshold

It starts innocently: a Python script to rename files, an alias to save keystrokes. Then you cross a threshold. You look at your tools, your environment, your OS—and suddenly everything is fair game.

> "You could rebuild that (if you wanted to). You could improve that (if you wanted to). Then someone challenges you... and the air changes. It becomes: You should."

From that moment, the world is broken in new and specific ways that only you can see.

### Technical Capability as Moral Weight

Before learning to program, broken software was frustrating but ignorable. Now it's provocative.

> "I notice flaws like a good surgeon notices a limp."

The questions become accusations:
- Why does this site send 10MB of JavaScript for a static page?
- Why is the CLI output not parseable by awk?
- Why is this config hardcoded when it could be declarative?

**The shift:** Every piece of software becomes a TODO list. Every system becomes scaffolding for a better one. Every inconvenience becomes an indictment of inaction.

### Sisyphus Built His Own Boulder

Like Camus' Sisyphus pushing the boulder uphill, programmers are condemned to push the boulder of their own systems. But unlike the myth, **we built the boulder ourselves**. And we keep polishing it on the way up.

The author's graveyard of "I could build this but better" projects:
- A static site generator (existing ones had too many opinions)
- A note-taking tool (didn't like how others structured metadata)
- A CLI task runner (Make is cryptic, Taskfile is YAML hell)
- A personal wiki engine in Rust, then Go, then Nim, then back to Markdown
- A homelab dashboard (webslop)

> "If you ask me, I was solving real, innocent problems. But in hindsight, I was also feeding something else: a compulsion to assert control."

Kafka: "A cage went in search of a bird." These projects can become empty systems we keep building, waiting for purpose.

### Entropy Is Undefeated

Software doesn't stay solved. Every solution starts to rot the moment it exists:
- Libraries deprecate, APIs change
- Performance regressions creep in
- Scripts fail silently when a website changes its HTML

Each failure triggers not just inconvenience but **guilt**: "I built this, and I know better. How could I not have foreseen this?"

> "If you replace every part of the system over time, is it still the same tool? Does it still serve the same purpose? Do you?"

### The Illusion of Finality

We tell ourselves a seductive lie:

> "Once I finish this, it'll be done."

This frames programming as conquest—battles you win, challenges you complete. But the war never ends. **You don't build a castle. You dig trenches. And they flood every time it rains.**

### Technical Work as Emotional Regulation

Marcus Aurelius: "Confine yourself to the present."

But programming lures us into believing we can control outside events. That's where suffering begins.

**The deeper truth:** Sometimes building things is how we self-soothe.
- We write a new tool because we need a small victory
- We refactor not because the code is messy, but because our life is
- We chase the perfect system because it gives us something to hold onto when everything else is spinning

> "I have written entire applications just to avoid thinking about why I was unhappy."

Programming offers instant feedback: run the thing, it works (or you fix it). That agency is addictive, especially when life doesn't offer it.

### The Burnout You Don't See Coming

Burnout doesn't just come from overwork. **It comes from overresponsibility.**

Programming, once internalized deeply enough, makes everything feel like your responsibility. The bloated website. The inefficient script. The clunky onboarding at your job. You *could* fix it. So why aren't you?

> "Nietzsche warned of gazing too long into the abyss. But he didn't warn what happens when the abyss is a Makefile."

### Learning to Let Go

The first step: Not everything broken is yours to fix.

- Not every tool needs replacing
- Not every bad experience is a call to action
- Sometimes it's OK to just use the thing

> "Sometimes the most disciplined thing you can do is walk away from the problem you know how to solve. There's a kind of strength in that. Not apathy, no. Nor laziness. Just… restraint."

### A New Kind of Skill

The real skill isn't technical mastery—it's emotional clarity:

- Knowing which problems are worth your energy
- Knowing which projects are worth maintaining
- Knowing when you're building to help—and when you're building to cope
- Knowing when to stop

> "You learn how to program. You learn how to fix things. But the hardest thing you'll ever learn is when to leave them broken. And maybe that's the most human skill of all."

### Connections

- **Relates to "The Appropriate Amount of Effort is Zero"** - Both reject the idea that strain equals valuable work; restraint can be strength
- **Relates to "joy of fucking around"** - The curse is when "fucking around" becomes compulsion rather than play
- **Contrasts with "The Copilot Delusion"** - That piece mourns lost skills; this warns that deep skills become a burden
- **Relates to "Do The Simplest Thing"** - Knowing when *not* to build is the ultimate simplicity
- **Relates to "The Philosopher-Engineer Pitfall"** - Both warn about pursuing local maxima that disconnect you from the world
- **Relates to self-help-philosophy-critique.md** - Processing despair through building can become avoidance
- **Relates to engineering-leadership-principles.md** - Overresponsibility is a leadership failure mode too

---

## Dad and the Egg Controller (Tom Francis)

*Source: https://www.pentadact.com/2018-12-18-dad-and-the-egg-controller/ - Added: 2026-01-18*

A personal essay by game developer Tom Francis (Gunpoint, Heat Signature) about his inventor father, problem-solving mindset, and successfully using a custom barbecue temperature controller his dad built before dying. A meditation on inheritance, understanding, and the joy of making things work.

### The Inventor Mindset

After his father died, Francis discovered the "Egg Controller"—a device his dad built to automate temperature control for a Big Green Egg barbecue. His father was an electrical engineer, but the better summary: **he was an inventor.**

> "His creations have been impressing people from the garden shed of his childhood home in Woking, to the mayor of Frome, to a chicken farmer in France."

### The Problem That Demanded Solving

The Big Green Egg can maintain stable temperature for hours—in theory. In practice:

> "You open the vents a bit to get the temperature up, then close them a bit, and it keeps going up. So you close them more, and now it's going down."

This bothered Francis because it was exhausting. It bothered his father for a different reason: **it was solvable.** The business of making small adjustments, observing their effect, and reacting accordingly was something computers are perfectly capable of.

### The Inherited Gene

Francis recognizes the same instinct in himself, just applied differently:

> "I can't build gadgets like dad could, so the set of problems I see as solvable is different, but if I feel a solution should exist I will bloody-mindedly create it."

**The business card story:** Francis wanted 200 business cards, each with a unique game code. The card company couldn't combine image + text for him. Proper solutions existed but required learning new tools more complex than needed.

His solution: **He made a game.** In Game Maker (the only language he knew), he created a "game" where the only level displays a giant business card, the menu system writes a code across it, then it takes a screenshot—30 times per second. "You win the game by waiting for 7 seconds." Result: 200 images ready for the printer.

> "This took about three hours to make. How long would it have taken to manually put 200 codes on 200 cards? Look, I'm not on trial here."

### PID Controllers: The Shared Problem

Father and son had the same problem. Francis was trying to get spaceships to slow down just in time to stop at a station—they kept overshooting or falling short. His dad solved this for the Egg Controller.

The solution is called a **Proportional-Integral-Derivative Controller**:

> "It's how cruise control in your car manages to keep a steady speed when the slope of the road changes. I wanted a spaceship to stop exactly at a space station. He wanted a turkey to stop at exactly 72 degrees celsius. The principle is the same."

### The Debugging Story

Francis couldn't figure out how to turn on the Egg Controller. He spent time trying various power sources, feeling like failure would mean "all his hard work on this brilliant device was wasted."

Eventually figured out 9V batteries work—clip onto the weird little cup things. Still didn't work. Then he tried the clips the other way around. **Brilliant green letters appeared.**

But at first use, the temperature kept rising and the fan wouldn't stop. After much frustration, he noticed a red light on a black box component he'd ignored:

> "I flicked a switch on the box. The light went blue. The fan stopped."

The interface worked exactly as he'd first assumed—you just have to flick the mysterious switch first.

> "Dad and I do think alike. Except on the subject of black boxes and what should happen when they're off."

### Understanding as Connection

When Francis couldn't figure out the device, it felt like a loss:

> "Not being able to figure this out made dad feel more distant. I had thought of us as like minds, and it made the loss easier to accept. His brain wasn't entirely gone, I still have a partial version of it in my own head."

When it finally worked perfectly, watching the fan spin up and wind down to maintain exactly 110 degrees:

> "The spaceship has stopped at the station. The car is successfully cruising. The Egg has been Controlled."

### Key Quotes

On the inventor mindset:
> "If I feel a solution should exist I will bloody-mindedly create it."

On solving problems with the wrong tools:
> "I made a game. It's a game where the only level is a giant room that looks like my business card."

On shared understanding:
> "His brain wasn't entirely gone, I still have a partial version of it in my own head."

On success:
> "More than one person said 'Ooh it has a nice smoky flavour!' I think dad would have got a lot of pleasure out of that."

### Connections

- **Relates to "Reinvent the Wheel"** - The business card story is peak "use what you know to solve your actual problem"
- **Relates to "Do The Simplest Thing"** - His Game Maker solution was absurd but perfectly matched his constraints
- **Relates to "The Magic of Software"** - Deep understanding of tools (Game Maker, PID controllers) yields unexpected solutions
- **Relates to "Theory Building"** - Deciphering the Egg Controller required building a theory of how it worked
- **Relates to "joy of fucking around"** - Both father and son built things because solving problems is satisfying

---

## Test-Driven Development with LLMs

*Source: https://blog.yfzhou.fyi/posts/tdd-llm/ - Added: 2026-01-18*

A practical framework for combining TDD with LLM-assisted coding. The key insight: LLMs have fundamentally changed the economics of TDD, making it less cumbersome when you automate the feedback loop.

### The Problem with LLM Coding

LLMs struggle to:
- Look at a clear specification, think deeply, and produce a whole working module
- Handle overwhelming context—stuff in too many tools/libraries and they get distracted
- Give complete solutions; often produce single lines when you want entire functions

What works better:
- Rephrasing project-specific things in general terms
- Introducing context incrementally, only when needed
- Using LLMs as debuggers—pasting raw errors often yields correct diagnoses

**The friction:** Constant copy-paste juggling between IDE, terminal, and chat interface.

### The Automated Event Loop

The solution is automating the TDD cycle:

1. **First prompt:** Give specification + function signature → LLM generates unit test + implementation
2. **Load into sandbox:** Parse output, write to `main.go` + `main_test.go`
3. **Auto-fix and test:** Run `go mod tidy && gofmt -w . && goimports -w .` then `go test . -v`
4. **Iteration prompt:** If tests fail, send code + actual output back to LLM for revision
5. **Repeat until green**

**Key efficiency:** The iteration prompt keeps context constant (just current code + error output), avoiding the cost of sending full debug history.

### Human Intervention Points

The model gets stuck sometimes (failed same test twice in a row). That's when humans provide explicit hints about what's wrong.

**The "who guards the guard" problem:** LLM wrote both tests and implementation—same blindspots appear in both.

**Solution:** Add your own test cases after the LLM generates the structure. If those pass, you can be reasonably confident in the code.

**Advanced idea:** Third prompt for AI-powered mutation testing—ask for a subtle bug that should break tests, verify it does.

### Scaling to Real Codebases

The approach works for leetcode-style problems. For real projects with dependency graphs:

**Structure the project for LLM workflows:**
- Each package (directory) should have independently testable subsets
- Per-subset structure: `shared.go` (typedefs/globals), `x.go` + `x_test.go` (one public function per file)
- Optional `main_test.go` for test environment setup (e.g., testcontainers)

**When invoking LLM for a larger project:**
1. Copy whole project to sandbox for execution
2. But only send the specific subdirectory to the LLM
3. Include gomarkdoc-generated docs for dependency packages
4. Include a same-package example (a tightly-coupled entity's finished implementation)

### The Emergent Benefits

This pattern naturally encourages:
- **Test coverage by default** - every function comes with tests
- **Aggressive decoupling** - adding context to LLM has cost, so you minimize dependencies
- **Small cognitive load per unit** - each chunk is fully understandable in isolation
- **"Deep" modules** - rich functionality, minimal surface area

> "Absent external forces, entropy always grows and logic scatters all over the place."

The LLM workflow creates selective pressure toward good architecture.

### The Bitter Lesson Caveat

> "There is a non-zero chance that we wake up tomorrow to a major shift in AI architecture, eliminating the LLM limitations we talked about, and rendering our efforts meaningless."

Don't refactor your 100k-LOC projects based on this advice just yet.

### Connections

- **Relates to "Peer Programming with LLMs"** - Both treat LLMs as collaborators requiring supervision, not magic solutions
- **Relates to "How I Build Software Quickly"** - The rough draft approach parallels the "spike" concept—get something working first
- **Relates to "Do The Simplest Thing"** - Small, testable modules with minimal dependencies align with simplicity principles
- **Relates to "The Copilot Delusion"** - This framework addresses the critique by keeping humans in the loop for test validation
- **Relates to "Theory Building"** - The iteration loop helps build theory about what the code does through repeated testing

---

## Fogus's Year-End Reflections (2024)

*Source: https://blog.fogus.me/2024/12/23/the-best-things-and-stuff-of-2024/ - Added: 2026-01-18*

Annual "best of" post from Michael Fogus, Clojure core developer and co-author of "Joy of Clojure." A window into how a language designer thinks about learning and exploration.

### The Concatenative Deep Dive

Fogus spent 2024 exploring concatenative languages (Joy, Forth):

> "Joy is a mindfrak of a programming language in the concatenative functional language family. The core of Joy is beautiful and among the foundational programming languages in my opinion."

On Forth:
> "Interestingly the language is incredibly rich in history and conducive to a wide range of techniques and paradigms. I'm unsure if I'll ever find the opportunity to use Forth in anger, but I will say that I should come out of my explorations a stronger programmer and program designer."

**Languages on his radar for 2025:**
- **Joy** - Deep dive into combinatory programming and recursive combinators
- **Mouse** - Another dead concatenative language with lessons to teach
- **POP-11** - 70s/80s AI language, interesting for its application suite
- **Juxt** - His own functional concatenative language experiment on the JVM

### Papers Worth Reading

- **Recursion Theory and Joy** (Manfred von Thun) - How Joy implements recursion via recursive combinators in userspace
- **A Simple Applicative Language: Mini-ML** (Clement et al.) - Beautiful definition of ML and its compilation to an abstract machine

### Code Worth Studying

- **Restrained Datalog in 39loc** (Christophe Grande) - "If Christophe writes a technical article then it behooves me to study it deeply." A rich Datalog implementation showing how far 39 lines of Clojure goes.
- **Post-Apocalyptic Programming** (Serge Zaitsev) - "What technology could/should we create in the absence of modern computing niceties?" Builds a CPU emulator and language.
- **MINT** - Minimal Forth-based language, inspirational for language design trade-offs

### The Tech Radar Approach

Fogus uses a personal tech radar for tracking tools:
- **try**: Boox Go 10.3 tablet
- **adopt**: Blank Spaces app (avoids phone brain-drain)
- **assess**: TypeScript
- **hold**: Zig ("looks like a dead-end for me")
- **stop**: Joy of Clojure 3rd edition ("Another edition is unlikely")

### Why This Matters

This reflects a philosophy of deliberate, curiosity-driven learning:
- Study dead languages for the lessons they teach
- Build toy implementations to understand deeply
- Follow specific authors/programmers whose work rewards close study
- Accept that not every exploration leads to practical use

### Connections

- **Relates to "Reinvent the Wheel"** - Fogus embodies the "reinvent for insight" approach through language exploration
- **Relates to "joy of fucking around"** - His concatenative deep dive is pure curiosity-driven learning
- **Relates to "Theory Building"** - Reading papers and building toy languages are theory-building activities

---

## Software Design is Knowledge Building (olano.dev)

*Source: https://olano.dev/blog/software-design-is-knowledge-building - Added: 2026-01-18*

A case study demonstrating Peter Naur's "Theory Building" thesis in practice. When knowledge walks out the door, even functional 6-month-old systems become haunted forests.

### The Story

A company (ORG) needed to replace expensive middleware SaaS with an in-house system (SVC):

1. A single excellent engineer (X) builds SVC on a tight schedule
2. X finishes on time, follows best practices, good test coverage
3. X moves to other projects, eventually leaves the company
4. A team (TEAM) takes over "just to keep the lights on"
5. Requirements change, business demands modifications
6. **TEAM fails miserably**—taking forever for small changes, constant bugs and outages
7. They restructure to a more senior team (TEAM++)
8. GOTO failure

The whole process takes less than a year.

### The Haunted Forest Problem

> "What fascinates me about this scenario is how a seemingly functional 6-month-old project automatically turns into a haunted forest just by changing hands."

SVC is textbook legacy software because questions about the system consistently get the same answer: **"I don't know."**

TEAM can't build a satisfactory mental model. They work from:
- The client's interpretation of what the system *should* be
- What they can tell from code about what the system *actually* is

These views are disconnected and contradictory. **The code tells the what and the how, but not the why.**

Only X could say what was:
- A functional requirement
- A technical necessity
- A whim
- An accident

The team must resort to reverse engineering, extrapolating, and guessing.

### The Misconception

> "Underlying the decision to move X out of the project once the system was operational, is the common misconception that software development consists of producing code."

The organization believed that once working code exists, programmers are interchangeable operators of varying quality.

### Theory Building (Peter Naur, 1985)

Naur's key insight: **the mental model is the primary product**, not the code.

> "Programming properly should be regarded as an activity by which the programmers form or achieve a certain kind of insight, a theory, of the matters at hand."

The theory allows the programmer to:
- Explain why each part is what it is
- Explain how it corresponds to the real world it handles
- Respond constructively to demands for modifications

When X left, she took the theory with her. The system, while still operational, was **dead** in Naur's terms.

### Parnas on Ignorant Surgery

David Parnas (in "Software Aging") warned against putting software in the hands of developers who don't understand its design. TEAM was bound to make "ignorant surgery"—the system degrading over time.

### Can Dead Systems Be Revived?

Naur suggests program revival from code and documentation alone is **impossible**—the program should be discarded and rebuilt from scratch.

**The author's counter-experience:**

> "Revival is very hard, yes, but I've seen it happen. It may require that the new team ultimately rewrite every line of the original, one at a time. And I've seen fresh starts fail more consistently."

Fresh starts often fail because developers advocate for greenfield rewrites to escape operational annoyances, falling into the same trap: assuming clean code is the hard part.

### Practical Implications

Knowing revival is a plausible future need changes how we work. Mind the people who will one day take the project out of its coma:

- In the style of code and structure of the system
- In the paratexts: comments, docstrings, READMEs, Pull Requests, commit messages, Jira tickets, Confluence pages

### The Proposed Law

> "The ultimate goal of software design should be (organizational) knowledge building."

When you choose a name, structure a project, or ponder whether to write or omit a comment, think: **how much will this decision help or hinder someone's building of a mental model** of the system, of the business, of the world.

### On AI Replacing Programmers

A footnote observes the same misconception is made by those who intend to replace programmers with statistical models—they assume code production is the job, not theory building.

### Connections

- **Directly extends "Theory Building Without a Mentor"** - That piece describes the micro-level skill of building theory from code; this piece describes why organizations should care
- **Relates to "The Magic of Software"** - Both emphasize that understanding (not just using) is prerequisite to good work
- **Relates to "How I Build Software Quickly"** - "Reading code is by far the most important skill" echoes Naur's theory building
- **Relates to "The Copilot Delusion"** - If AI can't build theory, it can only produce code without understanding
- **Relates to "Do The Simplest Thing"** - Simple systems are easier to revive because they're easier to form theories about
- **Contrasts with "Reinvent the Wheel"** - Fresh starts (reinvention) often fail; incremental revival with theory-building works better

---

## A Philosophy of Software Design: Key Ideas (John Ousterhout)

*Source: https://www.16elt.com/2024/09/25/first-book-of-byte-sized-tech/ - Added: 2026-01-18*

Distilled insights from John Ousterhout's influential book. Three core ideas that address how complexity accumulates and how to fight it.

### Idea 1: Zero-Tolerance Toward Complexity

Complexity is not caused by a single error—**it accumulates**. The temptation: "a bit of complexity here won't matter much." But if everyone on the project adopts this mindset, the project becomes complex rapidly.

> "In order to slow the growth of complexity, you must adopt a zero-tolerance philosophy."

**Symptoms of complexity:**
- **Change amplification** - A simple change requires changes in many different places
- **Cognitive load** - The developer needs to learn a lot to complete a task
- **Unknown unknowns** - It's not obvious which pieces of code need to change

**Example:** Duplicated discount logic across `CheckoutService` and `ShippingService`. If the discount criteria change, you must update both places. New developers won't know to check both. The fix: centralize in a `DiscountService` so changes happen in exactly one place.

### Idea 2: Smaller Components Are Not Necessarily Better

The question: "Given two pieces of functionality, should they be implemented together, or should their implementations be separated?"

**Cons of over-splitting:**
- "Some complexity comes just from the number of components"
- "Subdivision can result in additional code to manage the components"
- "Separation makes it harder for developers to see the components at the same time"
- "Subdivision can result in duplication"

**When to merge two pieces of code:**
- They share information
- They are used together **bidirectionally** (using A always requires B and vice versa)
- They overlap conceptually under a simple higher-level category
- It's hard to understand one without looking at the other

**On the "split methods longer than X lines" rule:**

> "Length by itself is rarely a good reason for splitting up a method. Splitting up a method introduces additional interfaces, which add to complexity. You shouldn't break up a method unless it makes the overall system simpler."

**Example:** A `RegisterUser` method split into `ValidateUser`, `SaveUserToDatabase`, `SendWelcomeEmail`—each always called together in strict sequence. The subdivision adds unnecessary interfaces without flexibility. Better to inline them.

### Idea 3: Exception Handling Accounts for a Lot of Complexity

> "Exception handling is one of the worst sources of complexity in software systems."

**The temptation:** Throw an exception and let the caller handle it. But if you're having trouble handling an exception, the caller probably won't know how either.

> "The best way to reduce the complexity damage caused by exception handling is to reduce the number of places where exceptions have to be handled."

**Techniques to reduce exception handlers:**

1. **Define errors out of existence** - Design APIs so there are no exceptions to handle
   - Example: Windows vs Linux file deletion. Windows throws if file is open; Linux marks for deletion and succeeds. The Linux approach eliminates the need for exception handling at call sites.

2. **Mask exceptions** - Handle at a low level so higher levels don't need to know
   - Example: TCP masks packet loss by resending. Application code doesn't handle lost packets—the protocol guarantees delivery.

3. **Exception aggregation** - Handle many exceptions with a single piece of code
   - Instead of separate handlers for `FileNotFoundException`, `AccessDeniedException`, etc., handle all `IOException` in one place.

**The abort problem:** Aborting an operation and passing the exception upward often adds more complexity than handling it locally—you may need to unwind partial state changes.

### Connections

- **Relates to "Do The Simplest Thing"** - Zero-tolerance toward complexity is essentially YAGNI applied to every design decision
- **Relates to "How I Build Software Quickly"** - Both warn against premature abstraction and over-engineering
- **Relates to "The Curse of Knowing How"** - Complexity accumulates because we *can* add features/handlers; restraint is the cure
- **Relates to "Theory Building"** - Simple systems are easier to build theories about; complex systems create unknown unknowns
- **Relates to "Software Design is Knowledge Building"** - Over-split code makes it harder for future developers to form mental models

---

## Throwaway Code Over Design Docs (Doug Turnbull)

*Source: https://softwaredoug.com/blog/2024/12/14/throwaway-prs-not-design-docs - Added: 2026-01-18*

A methodology for using draft PRs as design artifacts instead of traditional design documents. The core insight: we need to hack to find the design—making a giant mess then figuring out how to pick up the pieces may be the most efficient design method.

### The Delusion of Clean Design

We imagine software efforts flow cleanly:
1. Write a design doc
2. Make small incremental changes in PRs
3. Git histories look orderly—a steady march of progress

**Reality:** Once you start coding, you'll eat your design doc's words. You can't take a design doc and go straight to clean gradual rollout.

### The Coding Binge Methodology

Instead of design-first, use "coding binges":

1. **Use a draft PR you don't intend to merge** - Implement your prototype or proof of concept
2. **Get eyes on the PR early** - "What do you think of this approach to giant refactor/feature?" Get alignment before going too deep
3. **Document your approach in the draft PR** - A historical artifact of a design idea
4. **Be prepared to completely discard the draft PR** - As early as possible
5. **Stage PRs out of the draft PR incrementally** - Take a week to stage clean productionizable PRs. Link your draft PR as documentation
6. **Fill in testing and robustness gaps gradually** - As you stage each PR

### The Maturity Requirement

This requires discipline:
- Can you throw away code you've written, or will you be invested in your first solution?
- A major signal for seniority: **feeling comfortable coding something 2-3 different ways**
- Your value isn't lines of code shipped to prod—it's **organizational knowledge gained**

Get alignment early on the important parts so ongoing prototyping isn't a waste. Fail early, gather that organizational knowledge, move to the next idea.

### PRs as Documentation

PRs are one of the best documentation forms for developers:
- **Discoverable** - First place you look when understanding why code is implemented a certain way
- **Honest about temporality** - Don't profess to reflect current state, but state at a point in time
- **Historical artifact** - Preserves context of decisions

**Design docs, by contrast, lie to you.** They're "undead documentation"—unless you're fastidious about updates (most aren't), they reflect an outdated view of reality.

### Show Don't Tell

A prototype can be worth 1000 design docs. If you want to drive change, you don't usually do it in docs—you do it in code.

**The risk:** With an undisciplined organization, your prototype may be seen as the answer, not the question. The org may assume it says "we should do this!" when it really should be "should we do this? Or some other thing?"

### When Design Docs Still Make Sense

- **Multi-stakeholder collaboration** - Organizing feedback from many different stakeholders, managers, outside teams (GitHub won't serve for this)
- **Notional/long-term ideas** - Ideas so abstract you can't easily code them; "North Star" documents
- **Onboarding context** - If you express in writing more efficiently than coding a first draft (not onboarded enough yet)
- **Organizational protection** - If your company lacks discipline to throw away first solutions and instead pushes to ship prototypes to prod immediately
- **Power dynamics** - If junior employees don't feel comfortable pushing back when senior developers build something as an idea

### When Design Docs Are Misused

- To "slow down" the process for less disciplined/skilled developers
- As permanent documentation (they're outdated fast)
- To answer all design questions (you won't discover real problems until you write code)

### Connections

- **Directly relates to "How I Build Software Quickly"** - The "rough draft/spike" approach is the same methodology, applied to individual features rather than design processes
- **Relates to "Do The Simplest Thing"** - Both emphasize that you can't predict requirements; you must discover through implementation
- **Relates to "Theory Building"** - Coding builds organizational knowledge (theory) in ways design docs cannot
- **Relates to "Software Design is Knowledge Building"** - The organizational knowledge gained through prototyping IS the valuable output
- **Contrasts with "Peer Programming with LLMs"** - LLMs might help generate quick prototypes, but the judgment about what to keep requires human theory-building
- **Relates to "The Magic of Software"** - Understanding only comes through hands-on building, not abstract specification

---

## Bill Watterson on Creative Integrity (1987 Interview)

*Source: Honk Magazine Interview, 1987 (via http://timhulsizer.com/cwords/chonk.html) - Added: 2026-01-18*

A remarkable interview with Calvin and Hobbes creator Bill Watterson, conducted just two years after the strip launched. Contains powerful statements on artistic integrity, refusing commercial compromise, and treating creative work as craft rather than job.

### The Path to Calvin and Hobbes

Watterson spent five years getting rejected by syndicates before Calvin and Hobbes was accepted. Key lessons from the struggle:

**On trying to please gatekeepers:**
> "Trying to please the syndicates was pretty much the same as what I had ended up doing at the Cincinnati Post, and I don't think that's the way to draw your best material."

His advice after the journey:
> "You should stick with what you enjoy, what you find funny—that's the humor that will be the strongest, and that will transmit itself. Rather than trying to find out what the latest trend is, you should draw what is personally interesting."

### The Robotman Incident

After one syndicate suggested building Calvin and Hobbes around the stronger side characters (Calvin and Hobbes themselves), they declined to publish the resulting strip. But they offered an alternative: insert their pre-designed character "Robotman" into his strip.

Watterson's response:
> "They told me that if I was to insert Robotman into my strip, they would reconsider it... Not knowing if Calvin and Hobbes would ever go anywhere, it was difficult to turn down another chance at syndication. But I really recoiled at the idea of drawing somebody else's character. It's cartooning by committee, and I have a moral problem with that. It's not art then."

On the broader trend:
> "It's just another way to get the competitive edge. You saturate all the different markets and allow each other to advertise the other, and it's the best of all possible worlds. You can see the financial incentive to work that way. I just think it's to the detriment of integrity in comic strip art."

### Why He Won't Use Assistants or Ghosts

Schulz's quote he lives by:
> "It's like Arnold Palmer having someone to hit his chip shots."

Watterson's philosophy:
> "I spent five years trying to get this stupid job and now that I have it I'm not going to hire it out to somebody else. The whole pleasure for me is having the opportunity to do a comic strip for a living, and now that I've finally got that I'm not going to give it away."

On complete creative control:
> "Any time somebody else has their hand in the ink it's changing the product, and I enjoy the responsibility for this product. I'm willing to take the blame if the strip goes down the drain, and I want the credit if it succeeds. So long as it has my name on it, I want it to be mine."

**The art vs. job distinction:**
> "I guess that's the difference between looking at it as an art and looking at it as a job. I'm not interested in setting up an assembly line to produce this thing more efficiently."

### On Strip Continuation After Death

> "I don't think a strip should ever be continued after the death or retirement of a cartoonist."

(Note: Watterson kept this promise—Calvin and Hobbes ended December 31, 1995, with Watterson declining all licensing deals throughout its run.)

### Striving for Character Depth

On what makes a strip worth reading:
> "I look to strips like Peanuts, where you're really involved with the characters, you feel that you know them. If you have the personalities down, you understand them and identify with them; you can stick them in any situation and have a pretty good idea of how they're going to respond."

**The difference this makes:**
> "That takes a good 75 percent of the work out of it... But if you've got more ambiguous characters or stock stereotypes, the plastic comes through and they don't work as well."

On medium potential:
> "With four panels, the cartoonist has the opportunity to develop characters and storylines. It can be like writing a novel in daily installments. That's where the potential of the medium is."

He names strips that achieve this: Peanuts, Bloom County, Doonesbury, For Better Or For Worse.
> "These strips have heart, and an involvement with the characters, so that they're more than just props to relate a gag. We read about them and sort of go through their life with them."

### On Writing vs. Drawing

> "I find that the writing is the hard part and the drawing is the fun part."

His process: separate writing completely from inking. On writing sessions:
> "I'll sit down and stare into space for an hour and sometimes not come up with a single decent idea... and it's very tempting to go do something else or just draw up a strip, but I find that if I make myself stick to it for another hour I can sometimes come up with several good ideas."

### The Krazy Kat Standard

On why such work seems impossible now:
> "Comic strips are being printed at such a ridiculous size that elimination of dialogue and linework is almost a necessity and you just can't get that kind of depth. I think of Pogo, another strip that had tremendous dialogue and fantastic backgrounds... Those strips were just complete worlds that the reader would be sucked into."

### Connections to Software Craft

The parallels to programming are striking:

- **Refusing Robotman = Refusing feature requests that violate your vision** - Watterson walked away from syndication rather than compromise. How often do we accept "just add this one thing" that undermines system integrity?

- **No ghosts/assistants = Own your code** - "So long as it has my name on it, I want it to be mine." Same principle as not outsourcing the thinking to AI or junior developers you won't supervise.

- **Art vs. job = Craft vs. task completion** - The assembly line mindset produces mediocrity. True craft requires personal investment.

- **Character depth = System coherence** - When you deeply understand your characters (or your codebase), "you can stick them in any situation and have a pretty good idea of how they're going to respond." This is theory building applied to creative work.

- **Complete worlds = Deep systems** - Pogo and Krazy Kat created worlds readers could be "sucked into." The best software does the same—coherent, deep, rewarding exploration.

- **Writing is hard, drawing is fun** - The design/thinking is the hard part; implementation is the reward. But you must do both to own the result.

### Connections

- **Relates to "joy of fucking around"** - Both celebrate intrinsic motivation over external validation
- **Relates to "The Copilot Delusion"** - Watterson's refusal of assistants echoes the warning against outsourcing understanding
- **Relates to "Theory Building"** - Deep character knowledge is Naur's theory building for narrative
- **Relates to "Do The Simplest Thing"** - Watterson's refusal of Robotman is refusing complexity that doesn't serve the work
- **Relates to "The Curse of Knowing How"** - Watterson chose his boulder (the strip) and pushed it himself, finding meaning in the ownership
- **Relates to "Reinvent the Wheel"** - He could have used the syndicate's pre-built character; instead he built his own from scratch

---

## The Opposite of Documentation is Superstition (Hillel Wayne)

*Source: https://buttondown.com/hillelwayne/archive/the-opposite-of-documentation-is-superstition/ - Added: 2026-01-18*

A brief meditation on what happens when features lack documentation: users develop superstitious behaviors through trial and error, unable to distinguish intentional design from coincidence.

### The OneNote Ink-to-Shape Problem

Wayne uses Microsoft OneNote's "ink to shape" feature as a case study:

- The feature converts hand-drawn shapes into clean geometric objects
- **What works:** Drawing a freehand square converts to a square shape
- **What's janky:** The recognizer doesn't always get things right
- **What's missing:** No documentation of what shapes are supported

After years of trying, Wayne accidentally discovered the feature can convert scrawled lines to line segments—but he has no idea *why* what he did worked.

> "Where can I find the list of shapes that OneNote can recognize? Nowhere!"

**The result:** He can't distinguish between:
- Shapes OneNote can't recognize
- Shapes he's consistently failing to draw properly
- Whether his technique is the intended way or just coincidentally close

### The Skinner Pigeon Analogy

BF Skinner's 1948 experiment: feed pigeons at random intervals. By the end, six of eight pigeons developed nonsensical "superstitions"—repeated behaviors they believed triggered food but were actually unrelated to the random feeding.

Wayne's insight:

> "I feel like one of those pigeons right now. I could totally see myself coming up with rules that I thought influenced a completely random process. But you know what would stop me? Knowing it was a random process. Being able to read some documentation that says 'this is a random process'."

### The Documentation-Superstition Axis

The core thesis:

> "Please, for the love of God, write more docs. Don't let me become a crazy person."

Without documentation:
- Users create invented justifications for why identical actions produce different results
- Techniques that work by accident become cargo-culted rituals
- Nobody can learn the "real" way because nobody knows what it is

**The implicit warning for developers:** Every undocumented feature or behavior creates a population of users developing superstitious beliefs about your software.

### Caveats

Wayne notes the pigeon superstition explanation is controversial—some researchers failed to replicate Skinner's results, and behavior scientists debate whether Skinner over-interpreted what he observed. Consider it "a fascinating story" rather than hard evidence.

### Connections

- **Relates to "Theory Building"** - Without documentation, users can't build accurate theories; they build superstitions instead
- **Relates to "Software Design is Knowledge Building"** - This is the user-facing consequence of failing to preserve knowledge in docs
- **Relates to "The Magic of Software"** - When abstractions are black boxes without docs, users can't have insights about how to use them
- **Relates to "A Philosophy of Software Design"** - The "unknown unknowns" symptom of complexity manifests for users as superstition
- **Relates to "The Curse of Knowing How"** - For developers, everything broken is a TODO; for undocumented users, everything broken is a mystery

---

## Codin' Dirty (Carson Gross)

*Source: https://htmx.org/essays/codin-dirty/ - Added: 2026-01-18*

A counterpoint to "Clean Code" orthodoxy from the creator of htmx. The key message: many different approaches to writing software work—this is one of them.

### The Thesis

> "I'm not trying to convince you to code dirty with this essay. Rather, I want to show that it is possible to write reasonably successful software this way and, I hope, offer some balance around software methodology discussions."

Gross has seen projects using all sorts of approaches ship and maintain successful software: strict TDD, end-to-end tests only, OOP lovers and haters, dynamic language enthusiasts and skeptics.

### Big Functions Are Good, Actually

Clean Code says functions should be small—preferably under 5 lines. Gross disagrees.

**His typical function organization:**
- A few large "crux" functions—the real meat of the module (up to 200-300 LOC, sometimes more)
- A fair number of "support" functions (10-20 LOC)
- A fair number of "utility" functions (5-10 LOC)

**Example:** The `issueAjaxRequest()` function in htmx is nearly 400 lines. It has a lot of context to keep around and proceeds in a fairly linear manner. Splitting it would hurt clarity and debuggability without adding reuse.

**The visual argument:**

> "When you split your functions into many equally sized, small implementations you end up smearing the important parts of your implementation around your module."

In "clean" code, everything looks the same: function signature, if statement, maybe a function call, return. In "dirty" code, **important things are big** and unimportant things are small—making it obvious which functions matter.

**Empirical evidence:**

Code Complete (Steve McConnell) cites studies with mixed results—many show better errors-per-line metrics for larger functions. Newer studies show smaller functions have higher "change-proneness" but no significant bug-proneness relationship.

**Real-world examples:**

- **SQLite** - `sqlite3CodeRhsOfIn()` is >200 LOC. Noted for extremely high quality.
- **Chrome** - `ChromeContentRendererClient::RenderFrameCreated()` is >200 LOC.
- **Redis** - `kvstoreScan()` is ~40 LOC, many others are larger.
- **IntelliJ** - `CompilerAction.update()` is ~90 LOC.

> "These are important, complicated, successful & well maintained pieces of software, and yet we can find large functions in all of them."

### Prefer Integration Tests to Unit Tests

Clean Code recommends extensive unit testing with Test-First Development. Gross generally avoids this, especially early in projects.

**The problem with early TDD:**

Early on, you don't know the right abstractions. You need to try different approaches. Test-first creates a bunch of tests that break as you explore the problem space.

Unit tests tie you to a particular implementation. As more tests accumulate, the test suite takes on "its own mass and momentum"—making changes harder through test helpers, mocks, etc.

**The "dirty" testing approach:**

1. Do some unit testing early on, but not a ton
2. Wait until core APIs and concepts crystallize
3. Then test the API exhaustively with integration tests

**Why integration tests are more useful:**

- They remain stable through refactors
- They express higher-level invariants
- They're not tied to current implementation details
- They have longer shelf life for the project

> "Generally, if I can write a higher-level integration test to demonstrate a bug or feature I will try to do so."

**Higher-level TDD:**

Once you have integration tests, you can do TDD at the API level: think about the API you want, write tests for it, implement however you see fit.

### Minimize Classes/Interfaces/Concepts

Clean Code doesn't explicitly say maximize classes, but many recommendations lead there: small classes, polymorphism over if/else, single responsibility principle.

**The "God object" balance:**

Fear of "God objects" can lead to over-decomposed software. Consider Active Record (Ruby on Rails ORM):

- It maps objects to databases (ORM functionality)
- It also provides excellent functionality for building HTML in views
- You pass Active Record instances directly to templates

**Contrast with heavily-factored alternatives:**

- Validation errors as separate "concerns"
- DTO pattern for view layer
- Now you need multiple objects to do what one did

> "Having one class that handles retrieving data from the database, holding domain logic and serves as a vessel for presenting information to the view layer simplifies things tremendously for me."

Will some view-flavored functionality creep into models? Sure. But it reduces layers and concepts.

### Key Takeaway

> "You shouldn't be intimidated if someone calls your code 'dirty': lots of very successful software has been written that way and, if you focus on the core ideas of software engineering, you will likely be successful regardless of how dirty it is."

This is especially for younger developers "who are prone to being intimidated by terms like 'Clean Code'."

### Connections

- **Relates to "Do The Simplest Thing"** - Both reject complexity for complexity's sake; fewer abstractions often means simpler systems
- **Relates to "A Philosophy of Software Design"** - Ousterhout's "smaller is not necessarily better" directly echoes Gross's function size argument
- **Relates to "How I Build Software Quickly"** - Both emphasize rough drafts and delayed commitment to structure
- **Relates to "The Copilot Delusion"** - AI tools trained on "clean code" orthodoxy may push unnecessary decomposition
- **Relates to "Theory Building"** - Keeping related code together makes it easier to form theories about how it works
- **Relates to "Throwaway Code Over Design Docs"** - Integration tests as design artifacts parallel the draft PR methodology
- **Contrasts with Clean Code** - Direct rebuttal, but Gross emphasizes this is "one approach that works," not the only way

---

## Good Software Development Habits (Zarar)

*Source: https://zarar.dev/good-software-development-habits/ - Added: 2026-01-18*

Ten practical habits from a working developer. Not advice—"what's working for me." A compact, actionable complement to the more philosophical pieces in this collection.

### 1. Keep Commits Small

Keep them small enough that you wonder if you're overdoing it. You never know when you'll need to revert a specific change—six days later you'll be grateful to revert just one commit without merge conflict hell.

**Rule of thumb:** Compiling software should be commitable.

### 2. Continuous Refactoring (Kent Beck's Wisdom)

> "For each desired change, make the change easy (warning: this may be hard), then make the easy change."

Aim for at least half of all commits to be refactorings—small improvements you can make in under 10 minutes. This pays off when a bigger requirement comes in and you find yourself making a small change to satisfy it.

**Warning:** Big refactorings are a bad idea.

### 3. Deploy Often

All code is a liability. Undeployed code is the grim reaper of liabilities. You need to know if it works or at least doesn't break anything.

> "Tests give you confidence, production gives you approval."

Working software is the primary measure of progress. **Working** means deployable. **Progress** means contributing to a capability.

### 4. Don't Test the Framework

Know when you're testing the framework's capability—and don't. The framework is already tested by people who know more than you. Trust that `useState()` does what it's supposed to do.

If you keep components small, you reduce the need for tests—the framework does the heavy lifting. Big components introduce complexity that demands more tests.

### 5. Create New Modules Liberally

If a function doesn't fit anywhere, create a new module for it. You'll find a home for it later.

**Better:** An independent construct that doesn't quite fit yet.
**Worse:** Jamming it into an existing module where it doesn't make sense.

Worst case, it lives as an independent module—which isn't too bad anyway.

### 6. Write Tests First for API Design

If you don't know what an API should look like, write tests first. This forces you to think of the "customer" (you). You'll discover cases you wouldn't have thought of if you'd coded first.

**But:** Don't be religious about TDD. Working in larger batches is OK. The amount of code in a red/failing state doesn't always have to be small. Don't let dogma get in the way of productivity.

### 7. Copy-Paste Once, No More

Copy-paste is OK once. The second time you'd create duplication (three copies), don't.

At that point you have enough data to create a good abstraction. The risk of diverging implementations is too high. Better to have wonky parameterization than multiple implementations of nearly the same thing.

**Improving parameters later will be easier than consolidating four implementations.**

### 8. Designs Get Stale

Accept that you'll need to change how things work. You can slow the rate by refactoring, but ultimately change is required.

Don't feel bad about moving away from something you felt proud of. You did the right thing then. You couldn't have "gotten it right enough" to never need changes.

> "Most of the time writing software is changing software. Just accept it and move on. There's no such thing as the perfect design."

**How good you are at changing things is how good you are at software development.**

### 9. Technical Debt Triage

Three types of technical debt:
1. Things preventing you from doing stuff **now**
2. Things that will prevent you from doing stuff **later**
3. Things that **might** prevent you from doing stuff later

Every other classification is a subset of these three.

**Strategy:** Minimize #1. Focus on #2. Ignore #3.

### 10. Testability Correlates with Good Design

Something not being easily testable hints that the design needs to change. Sometimes that design is your test design.

**Example:** If mocking `em.getRepository(User).findOneOrFail({id})` is hard, either:
- Put that call in its own mockable function
- Write a test utility for easier mocking

> "Tests go unwritten when it's hard to test, not because you don't want to test."

### Connections

- **Relates to "Do The Simplest Thing"** - Small commits, liberal module creation, and avoiding premature abstraction all align with simplicity
- **Relates to "How I Build Software Quickly"** - Both emphasize rough drafts, small changes, and delayed commitment
- **Relates to "Codin' Dirty"** - Both reject rigid rules (TDD dogma) while maintaining practical quality standards
- **Relates to "A Philosophy of Software Design"** - Zero-tolerance toward complexity echoes Ousterhout; testability-as-design-signal is shared
- **Relates to "Theory Building"** - "Make the change easy, then make the easy change" requires understanding the system (theory) first
- **Relates to "Software Design is Knowledge Building"** - Acknowledging that designs get stale accepts that software is knowledge that evolves

---

## Removing Stuff is Never Obvious Yet Often Better

*Source: https://www.gkogan.co/removing-stuff/ - Added: 2026-01-18*

A case study from Pinecone demonstrating that removing features often beats fixing them. The pricing calculator was confusing users into wildly overestimating costs (up to 1,000x), so they removed it entirely.

### The Problem

Usage-based pricing calculators seem helpful but can backfire:
- One wrong input → massively overstated estimates
- Users take estimates at face value without verifying
- False confidence prevents them from trying the product
- Attempts to "fix" with disclaimers just add more confusion

> "Any attempt to address one source of confusion inevitably added another."

### The Bold Move

One person asked: "Do we, like, even need a calculator?"

The suggestion was "drowned out and dismissed" initially. But an A/B test proved removing was better:
- **16% more likely to sign up** without the calculator
- **90% more likely to contact the team**
- No increase in pricing-related support tickets

In an internal poll, 7 of 10 employees predicted the calculator version would win.

### Why We Don't Remove Things

1. **We solve through addition, not subtraction** - Research shows people systematically overlook subtractive changes
2. **Incentives favor adding** - You're rarely rewarded for removing
3. **Ego protection** - If you argued for something, admitting it's not working hurts
4. **Social friction** - Removing others' work feels like an attack
5. **Status quo bias** - "It exists, so it must exist for a reason"
6. **Change aversion** - First instinct is to argue against removal before thinking it through

### The Principle

> "Ruthlessly simplifying by cutting out non-essential elements can lead to great results."

Not small cuts—big chunks. If there's big backlash from the team, you're probably on the right path. The hard, counterintuitive, unpopular removals hide the biggest gains.

**The question to ask:** Would anything of value be lost if this chunk was removed?

### Connections

- **Extends "Do The Simplest Thing"** - Goes beyond "don't add unnecessary complexity" to "remove existing unnecessary complexity"
- **Relates to "The Appropriate Amount of Effort is Zero"** - Both challenge the assumption that more = better
- **Relates to YAGNI** - The features you already built that aren't adding value are the realized form of YAGNI violations
- **Applies beyond code** - Works for products, processes, strategies, companies—anything that accumulates cruft

---

## The Best, Worst Codebase: Decoupling Through Chaos

*Source: https://jimmyhmiller.github.io/ugliest-beautiful-codebase - Added: 2026-01-18*

A reflection on working in a legendary legacy codebase that was simultaneously the worst and best the author ever encountered. The chaos inadvertently produced remarkable flexibility and developer autonomy.

### The Legendary Mess

The database horrors:
- **Ran out of columns** - SQL Server's 1024-column limit hit, solved with `Merchants2` (500+ columns)
- **SequenceKey** - A single-row, single-column table for generating IDs across all entities (implicit joins everywhere)
- **The Calendar** - A manually-filled database table that controlled logins. When it runs out, no one can log in. An intern filled it out for 5 more years.
- **Employees table** - Dropped every morning at 7:15am, replaced by ADP CSV upload. Then manually replicated via a guy pushing a button.

The codebase:
- Half VB, half C#
- Every JavaScript framework checked in with custom modifications (knockout, backbone, marionette)
- Session state for everything (same page via different paths = different content)
- A developer named "Gilfoyle" built apps in a weekend, never checked in code, left behind hard drives full of production applications

### The Beautiful Discovery

> "This monolithic app, due to sheer necessity, had grown to be a microcosm of nice, small apps around its edges."

When Justin fixed the dog-slow Merchants Search page, he could make every box its own endpoint and load progressively—taking load time from minutes to sub-second. Why? Because nothing was connected to anything.

**The accidental architecture:**
- No master plan
- No overarching design
- No architectural review board
- No expected format for APIs

**The result:** Developers carved out their own little worlds of sanity. Each improvement orphaned the old code without breaking anything. Code was:
- Written to serve a use
- Designed to touch as little around it as possible
- Easily replaceable

> "Our code was decoupled, because coupling it was simply harder."

### The Missing Ingredient

What made this work wasn't just the chaos—it was the direct user connection:

> "There was no layer between those developers and the users, no translations, no requirements gathering, no cards. Just you standing at the desk of the customer service rep, asking them how you could make their life better."

Fast feedback. No grand plans. Simple problem-to-code connection.

### Key Insights

**On decoupling:**
There are two ways to achieve it:
1. Careful, intentional architecture
2. Making coupling harder than isolation (chaos default)

**On legacy systems:**
- The database becomes the "culture maker" and constraint-setter
- Clever hacks (like SequenceKey) sometimes survive for good reasons
- "Serious" developers abandoning a system can be liberating for the remaining team

**On enterprise patterns:**
> "When faced with yet another 'enterprise design pattern', my mind flashes back to that beautiful, horrible codebase."

The article is a cautionary tale against over-engineering—sometimes the mess produces better outcomes than the master plan.

### Connections

- **Extends "Do The Simplest Thing"** - Shows how enforced simplicity (by chaos) produces flexibility
- **Relates to "Theory Building"** - The author had to build theories about undocumented systems constantly
- **Challenges YAGNI inversely** - Proves that *not* planning for everything can accidentally enable more than planned architectures
- **Supports "Removing Stuff"** - The orphaning of old code was effectively continuous removal

---

## The Software Crisis (wryl)

*Source: https://wryl.tech/log/2024/the-software-crisis.html - Added: 2026-01-18*

A philosophical essay arguing we never resolved the 1968 "software crisis"—we just buried it under abstraction.

### The Original Crisis

The term "software crisis" was coined at the first NATO Software Engineering conference in 1968. Dijkstra identified the cause in his 1972 Turing Award lecture:

> "The major cause of the software crisis is that the machines have become several orders of magnitude more powerful! To put it quite bluntly: as long as there were no machines, programming was no problem at all; when we had a few weak computers, programming became a mild problem, and now we have gigantic computers, programming has become an equally gigantic problem."

### The Illusion of Comfort

We think we've "figured it out"—but this comfort comes from defeat and acceptance, not genuine resolution.

- We form mental models that rarely reflect reality
- It's a "nice coincidence" when our models are correct
- It's **catastrophic** when they're not

### The Pattern: "Abstract It Away"

Every effort to address the software crisis follows the same pattern:
1. Sweep unsavory details into controlled structures
2. Pay performance cost for "independence"
3. Hit roadblock → hardware upgrade
4. Repeat faster than mastery can occur

> "Companies selling equipment don't make money waiting for their users to master their products."

As personal computing grew and hardware cycles accelerated, abstraction became the default mode. Out of sight, out of mind.

### What We Lost

- Nested abstraction layers hide information at multiple levels
- The "death of the individual developer"
- Easy access to fundamental machine features (graphics, sound) is gone
- Nothing comes with a manual
- Users have no control except what authors afford them

> "The water was shallow enough to learn to swim in." (No longer true)

### The Responsibility Problem

> "Don't have good ideas if you aren't willing to be responsible for them." —Alan Perlis

Software builders occupy a blind spot:
- We produce tools whose true potential we won't understand for decades
- We're caught in creative passion or peer pressure
- We're separated from responsibility for what we build
- Stakes felt lowered as commercialization took hold

### The Solution (According to wryl)

Not reversion to constrained platforms, but:

1. **Constrain abstraction layers** - Limit how many we're allowed to apply
2. **Require information preservation** - Between layers
3. **Narrow the semantic gap** - So everyone can scale it
4. **Make things shallow and composable** - Programming models, UIs, hardware

> "We must, as a profession, give agency to the users of the tools we produce."

Monolithic structures "sprayed with endless coats of paint" cannot last—they can't be moved or reconfigured without being torn down.

### Counterculture Movements

Emerging movements raising awareness:
- **Handmade** - Focus on understanding what you build
- **Permacomputing** - Sustainable, long-lasting computing
- Various retro-computing circles

> "Counterculture movements are health signals, and a fever is brewing."

### Connections

- **Relates to "Beautiful Horrible Codebase"** - Both argue that constraints (intentional or accidental) produce better software than infinite flexibility
- **Extends "Do The Simplest Thing"** - Advocates for shallow, composable systems over towering abstractions
- **Complements software-project-failures.md** - That file documents the symptoms; this one diagnoses the disease

---

## VisiCalc and the "Idiot Savant" (1983)

*Source: [My Journey into Personal Computer Software Development in 1983](https://farrs.substack.com/p/my-journey-into-personal-computer) - Added: 2026-01-18*

A first-person account of working at Software Arts (creators of VisiCalc) in 1983, illustrating workplace dynamics, credentialism, and how organizations fail to recognize talent.

### The Setting

The author joined Software Arts to work on VisiCalc for the IBM PC. The program "almost fit" in the 256K memory limit. Bob Frankston (co-creator) had a sound segmentation strategy, but no "pedigreed" programmer wanted the boring work. The author—from a liberal arts university, Indian, without typical credentials—got the job.

### Prolific Bug-Fixing

After completing segmentation in 2-3 months (ahead of schedule), the author tackled a 600-item bug backlog. The established rate was maybe 1 bug per day. The author's rate: **5 bugs per day**.

> "The easy ones were good to perk me up while I finished my morning coffee, another entertaining couple by lunch, and then often I could get one or two more by the end of the day."

Within months, the bug list was empty. The author then added graphics capabilities (written in assembly language for speed).

### The Organizational Response

**QA was thrilled** - Christine P initially assumed the author was "some kind of a fast-talker and fake." After verifying the fixes, she became a supporter.

**Management and "super-programmers" were threatened** - They couldn't reconcile:
- (a) Author was Indian, from an unknown university
- (b) Author was outperforming elite-school graduates

Their solution: label the author an **"idiot savant"**—dismissing clear competence as a mysterious aberration rather than actual skill.

### The Technical Miss

VisiCalc lost to Lotus 1-2-3 partly because the in-clique insisted on Lisp (slow, memory-hungry). The author knew the codebase thoroughly and could have rewritten it in assembly in 4-6 months. But nobody asked—they were too busy explaining away his productivity.

### Lessons

1. **Credentialism blinds organizations** - Credentials became a filter for perceiving competence, causing them to dismiss evidence
2. **Political dynamics trump technical excellence** - The "in-clique" prioritized hierarchy over outcomes
3. **Support staff see clearly** - Non-programming staff (QA, accounting, front-desk) recognized good work when management couldn't
4. **Sometimes leaving is correct** - Fighting workplace politics isn't always worth it; the author returned to Unix/C work

> "Being labeled an 'idiot savant' by the management in retaliation for having done some (what I thought to be) amazingly good work, frankly unnerved and annoyed me a lot."

### Historical Note

This was 1983—before Excel existed, before Indians were seen as "software material." VisiCalc would soon be eclipsed by Lotus 1-2-3. Software Arts' bet on TK!Solver (their "next big thing") never materialized. Sometimes the "legacy" product is the valuable one.

### Connections

- **Relates to "Theory Building"** - The author had built the deepest theory of VisiCalc's code through segmentation and bug-fixing, but management didn't recognize this as valuable
- **Relates to "The Best, Worst Codebase"** - Both stories involve teams ignoring people who understood systems deeply in favor of politics
- **Relates to "joy of fucking around"** - The author found bug-fixing genuinely engaging; complex bugs were preferred, not avoided
- **Relates to engineering-leadership-principles.md** - A case study in recognition failure and the cost of credentialism

---

## Complexity Is Bad (Zvi Mowshowitz)

*Source: https://thezvi.wordpress.com/2017/07/25/complexity-is-bad/ - Added: 2026-01-18*

A framework for thinking about complexity as a resource to be managed, drawing from Mark Rosewater (Magic: The Gathering head designer) and applying broadly to software and life.

### Why Complexity Hurts

**Cognitive limits are real:**
- People can store ~7 things in working memory
- People can actively think about ~3 things simultaneously
- When overwhelmed, people either prioritize wrong, give up entirely, or act randomly

**Complexity compounds problems:**
- It's a barrier to entry—people won't engage
- It papers over mistakes, preventing better solutions
- Complex systems are harder to analyze, more fragile, have more failure points
- Even best-case: complex things require more time and concentration
- Higher complexity → higher standards you're judged by

**People will simplify whether you want them to or not.** They'll distill your argument or system to make it manageable, in ways you can't predict or control.

### The Cost Model

Albert Einstein: "Everything should be made as simple as possible, but no simpler."

Mark Rosewater's framing: **You have complexity points to spend.** Increasing complexity costs points. Spending too many has outsized costs. (This may share a budget with "weirdness points.")

The goal: maximize what you get from your complexity budget.

### Techniques to Manage Complexity

**Resonance** - Map new concepts onto familiar ones. "Flying creatures can't be blocked by non-flying creatures" is instantly understood because... flying.

**Chunking** - Make it easy to combine things into conceptually simple bigger units. A complex system of 10 interacting rules that chunk into 2 concepts is cognitively cheaper than 5 unrelated rules.

**Ramping** - Start simple, introduce complexity gradually. Classic "tutorial" approach. Let people build mental models incrementally.

**Hiding** - Put complexity where new users won't look or care. When they're ready, they'll find it. Hidden features serve power users without burdening beginners.

**Emergent complexity** - Complexity from simple rule interactions rather than explicit rules. Chess has simple rules but emergent complexity; tax code has explicit complexity. One is elegant; one is not.

### Connections

- **Relates to "Do The Simplest Thing"** - Same principle from XP: simplicity reduces cognitive load and failure modes
- **Relates to complex-systems-failure.md** - More complexity → more points of failure (Cook's principles)
- **Relates to "Lehman's Laws"** - Law 2 says complexity increases unless actively countered; these techniques are how you counter it
- **Relates to "A Philosophy of Software Design"** - Ousterhout's "zero-tolerance toward complexity" and symptoms (change amplification, cognitive load, unknown unknowns) map directly to this framework
- **Part of Zvi's "Choices are Bad" series** - Choices impose cognitive costs; simplifying options is simplifying complexity

---

## Deming's Path of Frustration: Bugs vs Systemic Issues

*Source: https://shermanonsoftware.com/2024/04/08/fixing-all-the-bugs-wont-solve-all-the-problems-demings-path-of-frustration/ - Added: 2026-01-19*

A key distinction from quality management: not all software problems are bugs. Some are systemic design issues that no amount of bug-fixing will address.

### Special Cause vs Common Cause

Drawing from W. Edwards Deming's quality management philosophy:

**Special causes (bugs):**
- Individual defects in the code
- Can be fixed by finding and correcting the specific error
- Removing them greatly improves software quality

**Common causes (systemic issues):**
- Problems due to the nature of the system's design and implementation
- Cannot be fixed by bug-hunting
- Require architectural or design changes

### Common Cause Examples

Performance problems that aren't bugs:

- **Geographic latency** - Software "in the cloud" that's really in one US data center, making it slow for European and Asian customers
- **Underprovisioned hardware** - System runs slowly because resources are inadequate, not because code is wrong
- **Unnecessary data transmission** - Large amounts of unneeded data sent to users
- **Inefficient data access patterns** - Poor database query design or architecture

Even with zero bugs, these common cause issues result in low-quality software.

### The Path Off Frustration

> "The way off of Deming's Path Of Frustration is to attack system design and implementation issues with the same fervor used to fight bugs."

Organizations often:
1. Have excellent bug-tracking and fix processes
2. Treat systemic issues as "known limitations" or "future work"
3. Wonder why quality doesn't improve despite high bug-fix velocity

The fix: recognize that systemic issues deserve the same urgency, tracking, and resources as bugs.

### Connections

- **Relates to "A Philosophy of Software Design"** - Ousterhout's complexity symptoms (change amplification, cognitive load) are common causes, not special causes
- **Relates to "Complexity Is Bad"** - Systemic complexity is a common cause that bug-fixing won't address
- **Relates to "Software Design is Knowledge Building"** - Common causes often stem from lost design knowledge—no one remembers *why* the system was designed this way
- **Relates to "The Best, Worst Codebase"** - That legacy system had many common causes (session state, manual replication) that weren't "bugs" per se
- **Relates to "Theory Building"** - Identifying common causes requires understanding the system's theory, not just its symptoms

---

## No Silver Bullet (Fred Brooks, 1987)

*Source: https://www.cgl.ucsf.edu/Outreach/pc204/NoSilverBullet.html - Added: 2026-01-19*

Fred Brooks' seminal essay arguing there is no single breakthrough that will dramatically improve software productivity. Originally appeared in IEEE Computer, 1987.

### The Central Thesis

> "There is no single development, in either technology or in management technique, that by itself promises even one order-of-magnitude improvement in productivity, in reliability, in simplicity."

Software progress is slow not because we're doing something wrong, but because hardware progress is unnaturally fast. No other technology has seen six orders of magnitude in performance/price gain in 30 years.

### Essential vs Accidental Complexity

Following Aristotle, Brooks divides difficulties into:

**Essential difficulties** - Inherent in the nature of software itself:
- **Complexity** - Software entities are more complex for their size than any other human construct. No two parts are alike (or we'd make them a subroutine). The complexity is essential, not accidental.
- **Conformity** - Much complexity comes from arbitrary interfaces designed by different people, not from inherent necessity. The physicist has faith in unifying principles; the software engineer must conform to capricious human systems.
- **Changeability** - Software embodies function, which is the part most subject to pressure for change. Successful software always gets changed—users invent new uses, hardware evolves.
- **Invisibility** - Software has no ready geometric representation. It's multiple overlapping graphs (control flow, data flow, dependencies, time sequence) that aren't even planar.

**Accidental difficulties** - Those that attend production but aren't inherent:
- Machine-level programming (solved by high-level languages)
- Batch processing delays (solved by time-sharing)
- Tool incompatibility (solved by unified environments like Unix)

### Why Past Breakthroughs Worked

Each major advance attacked accidental, not essential difficulties:

1. **High-level languages** - Freed programs from machine representation. "The most a high-level language can do is furnish all the constructs the programmer imagines in the abstract program."

2. **Time-sharing** - Preserved immediacy, enabling mental overview of complexity. But once response time passes the 100ms human threshold, no more gains.

3. **Unified environments** - Unix and Interlisp attacked the accidental difficulties of making programs work together.

### Why Proposed "Silver Bullets" Won't Work

**Ada and language advances:**
> "Ada will not prove to be the silver bullet... It is, after all, just another high-level language, and the biggest payoff came from the first transition—up from the machine."

Brooks predicted Ada's biggest contribution would be occasioning training in modern design techniques, not language features.

**Object-oriented programming:**
Removes "higher-order" accidental difficulty by allowing expression of design without syntactic underbrush. But:
> "An order-of-magnitude gain can be made by object-oriented programming only if the unnecessary type-specification underbrush is itself nine-tenths of the work. I doubt it."

**Artificial intelligence:**
> "The hard thing about building software is deciding what one wants to say, not saying it. No facilitation of expression can give more than marginal gains."

Expert systems may help by putting the best practices at the service of inexperienced programmers, but won't revolutionize productivity.

**Graphical/visual programming:**
> "Nothing even convincing, much less exciting, has yet emerged from such efforts. I am persuaded that nothing will."

Screens are too small, and software is fundamentally unvisualizable—it's multiple superimposed graphs, not a 2D layout like chip design.

**Program verification:**
Can only establish that a program meets its specification. "The hardest part of the software task is arriving at a complete and consistent specification, and much of the essence of building a program is in fact the debugging of the specification."

### What Actually Helps (Attacks on the Essence)

**Buy vs. Build:**
> "The most radical possible solution for constructing software is not to construct it at all."

The mass market spreads development cost across users, effectively multiplying developer productivity by n copies. In the 1960s, users wouldn't use off-the-shelf packages. By the 1980s, they adapted to packages because the cost ratio changed—a $50,000 machine buyer can't afford custom payroll software.

**Requirements Refinement and Rapid Prototyping:**
> "The hardest single part of building software is deciding precisely what to build."

The client doesn't know what they want. It's impossible to specify requirements completely before trying some versions. Prototyping makes the conceptual structure real so clients can test for consistency and usability.

**Incremental Development (Grow, Don't Build):**
The building metaphor has outlived its usefulness. Software should be grown:
1. Make it run (even doing nothing useful)
2. Flesh it out bit by bit
3. Allow easy backtracking
4. Always have a working system at every stage

> "Enthusiasm jumps when there is a running system, even a simple one."

**Great Designers:**
> "The differences between the great and the average approach an order of magnitude."

Great designs come from great designers, not from methodology. Sound methodology can empower the creative mind; it cannot inspire the drudge. Organizations should identify and nurture great designers as carefully as they develop managers.

### The Disease Analogy

> "The first step toward the management of disease was replacement of demon theories and humours theories by the germ theory. That very step, the beginning of hope, in itself dashed all hopes of magical solutions."

Progress will be stepwise, at great effort, requiring persistent care and discipline. There is no royal road, but there is a road.

### Key Quotes

On complexity:
> "The complexity of software is an essential property, not an accidental one. Hence, descriptions of a software entity that abstract away its complexity often abstract away its essence."

On specification:
> "The client does not know what he wants. The client usually does not know what questions must be answered, and he has almost never thought of the problem in the detail necessary for specification."

On great designers:
> "Many fine, useful software systems have been designed by committees and built as part of multipart projects, [but] those software systems that have excited passionate fans are those that are the products of one or a few designing minds."

### Connections

- **Relates to Lehman's Laws** - Brooks' "changeability" maps directly to Lehman's Law of Continuing Change
- **Relates to "Software Design is Knowledge Building"** - Brooks' "grow, don't build" and prototype-based specification are theory-building activities
- **Relates to "Software Project Failures"** - The modern failures documented in that file prove Brooks' thesis still holds: no silver bullet emerged in 40 years
- **Relates to "Cognitive Software Engineering"** - Conjecture's "complexity is the enemy" echoes Brooks' essential complexity
- **Relates to "Do The Simplest Thing"** - Both recognize that complexity cannot be abstracted away when it's essential to the problem

---

## Relationships: Start With Several (Luke Bechtel)

*Source: https://lukebechtel.com/blog/relationships-start-with-several - Added: 2026-01-19*

> "Programmers know three numbers: 0, 1, and N."

A practical heuristic for data modeling: **start with One-To-Many relationships instead of One-To-One**. The initial cost is marginal (maybe 10% more code), but the flexibility saves enormous refactoring pain later.

### Why This Works

Most of the world is polyrelational:
- People have multiple pets
- Employees have multiple managers
- Cars have multiple drivers

The pattern isn't magic—it reflects how the world works and how humans perceive it.

### The Pain of Scaling Up

Going from One-To-One to One-To-Many is painful:
- UI components built around the old system need updating
- Tests were written assuming single relationships
- API calls must change
- Other dependent classes cascade into refactoring
- Each refactor introduces potential bugs
- Shims get put in place to straddle old and new ways

Going from One-To-Many to... still One-To-Many? **Just add another item to the list.**

### Scaling Down Is Easy

Moving from *-to-N to one-to-one is much simpler—just answer "Which of these should we keep?" Getters in OOP and views in databases can often hide the change from customers entirely.

### What About Many-To-Many?

Many-To-Many is possible but introduces a third object—the Relationship itself. This adds complexity. One-To-Many tends to be the best middle ground conceptually.

### Key Insight

> "When it comes to Relationships, at least in Code, prefer starting with several. You'll thank yourself later."

**Connections:**
- **Relates to "Do The Simplest Thing"** - Paradoxically, starting with more flexibility *is* simpler than refactoring later
- **Relates to Brooks' "No Silver Bullet"** - Complexity in relationships is essential, not accidental; designing for it upfront acknowledges reality
