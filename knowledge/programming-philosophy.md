# Programming Philosophy & Mindset

Perspectives on the craft of programming, career attitudes, and the joy of coding.

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

> "reading source code is surprisingly rewarding"

This skill—creating theories from code alone—is valuable for both debugging and adding features. The article focuses on the "micro" level (small portions); macro-level theory building (design decisions) is a separate skill.
