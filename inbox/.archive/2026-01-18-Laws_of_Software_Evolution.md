---
type: link
source: notion
url: https://two-wrongs.com/laws-of-software-evolution
notion_type: Software Repo
tags: ['Running']
created: 2024-04-27T05:24:00.000Z
---

# Laws of Software Evolution

## AI Summary (from Notion)
- Software Evolution: The document discusses the concept of software evolution, particularly how software must adapt to changes in the real world and user needs.

- Lehman’s Laws: The author emphasizes two key laws proposed by Lehman:
1. Software must change with the real world or it will become irrelevant.
2. Changes to software increase its complexity, raising the cost of future modifications unless actively managed.

- Continuous Maintenance: Contrasts Andrew Kelly's view of maintenance as a corporate conspiracy with the author's belief that some software naturally requires ongoing maintenance due to its interaction with a changing environment.

- Real-World Examples:
- A team faced a feedback loop that made changes increasingly difficult, resolved by implementing stricter quality controls.
- The author argues against quick fixes for discontinued products, advocating for upfront investment in proper solutions to reduce future maintenance costs.

- Requirements and Change:
- Highlights the disconnect between user needs and software capabilities, stressing that good intentions do not alter the software's actual performance or relationship with users.
- Discusses the misconception that changes can be easily superimposed on existing code without real effort, emphasizing the need for a more intentional redesign process.

- Malleability of Code: The author believes in leveraging the malleability of code to avoid extensive redesign processes, accepting that this approach may accelerate the complexity and maintenance costs associated with software.

- Hot Takes:
- The author challenges simplistic views of software maintenance and development, encouraging a deeper understanding of the underlying dynamics.
- Suggests that the practices of other engineering fields might offer valuable insights for improving software development processes.

- Interesting Facts:
- Lehman's laws were formulated in 1974, indicating that the need for software evolution is not a new concept.
- The author offers a personal perspective on the value of continuous refactoring in software development.

## Content (from Notion)

Andrew Kelly has written a thoughtful article on why we can’t have nice software. He acknowledges that software often gets continuous maintenance, and notes that this is curious, since “bits don’t actually rot” on their own, i.e. software should not get worse just by existing. He searches for another explanation for this maintenance effort, and settles on it being a manufactured demand. Andrew Kelly says continuous maintenance is a corporate conspiracy where in order to make profits companies make changes that are not necessary.

I take issue with this simplification. It’s true that some types of software can be written to a detailed specification and once it is fulfilled to the letter the software is done.

Most software I come in contact with is not of that type.

# Lehman’s Laws of Software Evolution

The software I encounter most is software that interacts with a changing world. It’s software that needs to adapt to other software, but critically, it needs to adapt to its users – to people! People change their attitudes and processes in response to the environment, and the software needs to adapt around that.1

Based on this, Lehman formulated some laws of software evolution.2 This was in 1974, before companies had started with the practises Andrew Kelly discusses, so the idea of software needing continuous maintenance may be older than exploiting finished software for more profit.

Many of the observations Lehman offers in his 1980 article directly contradict observations I’ve made myself, so I don’t propose a blind acceptance of all he says.3 But the first two laws he summarises I carry close to my heart:

1. Software exists to support a real-world task, and as the real world changes, the software must change with it or become increasingly less relevant.
1. As software is changed, its complexity will increase, increasing the cost of further changes – unless effort is spent countering this effect.
I have found these laws to be useful guides through multiple problems I’ve encountered professionally. One example was when a team was stuck in a reinforcing feedback loop of increasing difficulty of change, and the way out was to establish stricter quality controls on changes to turn the loop around.

Another case was when a product was discontinued but bug fixes were supported for existing customers of that product. There was a temptation to make fixes through ugly hacks to spend as little development time as possible on that product. As sensible as that sounds, in this case the customers would not be migrated off that product for several years. When problems are solved with quick hacks, the second law of software evolution is accelerated, and thus maintenance will cost more and more as time goes on. On a long time frame, such as in that case, the better choice is to spend more on fixes up front, to reduce the total cost. The cost savings of discontinuing the product should come from a reduced number of fixes (only fix critical bugs, not long-lived quirks), rather than reduced effort per bug fix.

# Bonus content: requirements and change

Re-reading the Lehman article I want to quote two sections that seem particularly insightful. One concerns the complex network of relationships software forms with its environment.

> 

We often think of software development as a ticket-in-code-out business but this is really only a very small portion of the entire thing. Completely independently of the work done as a programmer, there exists users with different jobs they are trying to perform, and they may or may not find it convenient to slot our software into that job. A manager is not necessarily the right person to evaluate how good a job we are doing because they also exist independently of the user–software–programmer network, and have their own sets of priorities which may or may not align with the rest of the system.

Then we move on to how software change is different from change in many other engineering fields.

> 

Code is malleable enough that we think of applying changes on top of existing code to get a new product, slightly different from the previous one. In this way, code is more similar to genetic material than other types of design. There are two possible takeaways from this:

- Either we can take note on how other industries are doing things and set up redesign processes to reduce the effects of the second law of software evolution; or
- we should embrace the malleability of code and avoid redesign processes at all costs! We do this in full knowledge that it accelerates the second law of software evolution, so we invest significantly in continuous refactoring to work toward a better shape for the software.
I’m in the second camp, but then again, I haven’t work in other engineering fields so what do I know?

# Sidenotes

1

This is ultimately a good thing. Imagine if we didn’t change how we build roads in response to new types of vehicles! Or didn’t change how we handle user data in response to security breaches. In almost any human behaviour change, there is a software system that will struggle to accept it, because software is not good at improvisation.

2

On understanding laws, evolution, and conservation in the large-program life cycle; Lehman; Journal of Systems and Software; 1980.

3

I suggest reading his paper to evaluate the scientific basis more clearly for yourself.


