---
type: link
source: notion
url: https://trunk.io/blog/reasons-developers-hate-linters
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-03-21T03:21:00.000Z
---

# Why Developers Don't Use Linters

## AI Summary (from Notion)
- Purpose of the Blog: Address concerns about automated code linters and formatters, especially among developers who may fear they introduce more issues than they solve.

- Benefits of Linters:
- Detect potential errors and enforce code consistency.
- Facilitate easier onboarding for new team members.
- Automate style checks, saving time in code reviews.

- Challenges in Adoption:
- Fear of overwhelming backlogs of issues from enabling linters.
- The risk of losing insight into codebase quality if errors are ignored.
- Code history modification issues caused by tools that auto-fix errors.

- Incremental Rollout Strategies:
- Running linters on a part of the codebase or only on changed files to avoid being overwhelmed.
- Temporarily downgrading error checks to warnings to ease the transition.
- The impracticality of halting development to fix all issues at once.

- Hold the Line Concept:
- Only apply linters to new changes, allowing gradual improvement without overwhelming existing code.

- Managing Code History:
- Tools that format code can disrupt git blame history.
- Use of .git-blame-ignore-revs file to filter out commits that alter formatting, preserving the history of human contributions.

- Conclusion: Emphasizes the importance of adopting automated tools to improve code quality while managing the challenges that come with integrating them into existing workflows.

## Content (from Notion)

Automated code linters and formatters can be almost magical. They find potential errors, enforce consistency across your codebase, and speed up development at the same time. Consistency makes it easier to see what code does and where it goes wrong. Consistency makes it easier for new people to join the team. And having a tool to determine rules means your team doesn’t have to waste time bikeshedding the rules, or waste valuable code review time checking for style violations; the tools have already done it. This is the magic of automation, and the value increases when you use these tools across multiple repos. It’s a rare win / win in software development. So why did we write this blog?

As a company that specializes in dev tool automation, you’d expect us to have the opinion that automated tools are good 😉. Yet, some of our customer interactions reveal that not everyone is convinced, fearing an increase in errors and disruptions to their project histories. We aim to address these concerns by offering strategies for a smoother integration of automation into your workflows.

## The challenges

When a team (whether commercial or open source) considers adding tool automation, they often worry that turning on the tools will find too many problems. They worry that the team will be swamped with a backlog of issues and, the older the codebase is, not be able to make forward progress. To fight it some developers will just disable the checks for every found error, resulting in code that is not any better. Worse, they have now lost insight into the state of their codebase; making it even harder to go back and address those issues once they become invisible.

Another challenge is modifying codebase history. Some tools, like code beautifiers, can not only find errors but fix them as well. This is great because you can upgrade the entire codebase at once, but that introduces a new problem: applying tools to the whole codebase will mess up git-blame. As a developer, I want to see which human last modified this line, but now the tool is listed instead.

These challenges hinder the adoption of automated tools, but there is hope: incremental rollout.

## Eating the elephant one bite at a time

When a team first turns on linters and formatters, they often are overwhelmed by the number of errors and warnings found. If everything is a problem then where do you focus? Which are the most important ones to fix? If the warnings are reported as errors then everything will block development. Many tools usually encourage you to treat the output as errors that prevent the code from being committed, or the branch from being merged. Once the process is smooth this actually is a good policy, but when you first start with an existing codebase, this policy will slow things down. There are a couple of ways to address this:

1. You can run the linters only on a portion of the code base. Maybe you pick just the UI and not the server, or only the database code. Or you could only run linters on changed files. The downside is that when you change only one line in a file, you are now responsible for fixing all of the issues in that file which is especially daunting if it’s a big one. (This used to happen to me all the time at my last company!).
1. Another option is to downgrade the error checking. Many linters can be configured to treat errors as warnings or to reduce the number of types of issues found. This is helpful initially but make sure your remember to revert to stricter settings eventually.
1. Finally you could just stop development for a month and fix all of the errors. Unsurprisingly, few teams want to do this due to the high cost in time and progress.
The problem with all of the above solutions is that they are still manual. The whole point of automation is to avoid manual errors. A better solution is what we call “Hold the Line”, which focuses on improving code quality without exacerbating existing issues, allowing for gradual improvement over time.

## Hold the Line

Hold the line is a concept which means tools will only run on new changes, not on old code. This means you can adopt the tool without running it on your entire codebase, only the new changes. Over time you can go back and fix the older code at your leisure.

At a previous company I had a lot of coffeescript to turn into typescript. Our policy was to only port code when already modifying that file for other reasons (bug fixes or new features). This ensured we made progress on our technical debt but not be overwhelmed by it. In some other cases we would make these changes on a line by line basis rather than file by file (such as adding extra property types to older React JS code). The point is Hold The Line lets you keep working without eating the elephant all at once.

If your tool supports Hold the Line, then absolutely turn it on. If your tool doesn’t, then use Trunk Check to run them. Trunk Check implements Hold The Line across all of the tools we have wrapped, at the level of single code lines, giving you one consistent place to manage their settings. Either way, you can now introduce checking to a new project and get immediate value on only your new code. You don’t have to go back and fix everything since the beginning. Once you get some breathing room you can slowly go back and fix issues in older code.

## Never Change History

Tools which can not only detect but fix issues for you don’t have the problems above. You can upgrade the entire codebase at once and be done with it. Code formatters like Prettier (my personal favorite) work like this. The problem is that even if they work perfectly, they have created a giant break in the history of the codebase.

If searching through code is like archeology, then reformatting your codebase creates a KT Boundary that obscures the real things you are looking for. We dig through old code using git blame to find when a particular line was last modified and by whom. Running a beautifier on your entire codebase will essentially reset history. Most IDEs even bundle git blame into their text editor gutters, so resetting history affects a development aide used every day. Not good! But there is a solution.

Git will show the last modifier of a particular line when using gitblame, and if the last modifier was a tool that’s what you are going to get. However, Git supports a way to filter the output using the little known --ignore-revs-file option pointing to a special file known as the .git-blame-ignore-revs file. This file contains the hashes of revisions to ignore when running git blame. GitHub respects the contents of this file, so when it renders diffs and code history it will skip those refs.

You can also configure your local git so it always ignores the revs in that file even without using the --ignore-revs-file option:

```plain text
1git config blame.ignoreRevsFile .git-blame-ignore-revs
```

Since this is so useful, Trunk Check will automatically add it to your config.

With ignore-revs in hand you can run a full codebase reformat and hide it from the git blame history. Here’s an example.

```plain text
1# check the current git blame2git blame somefile.txt34# reformat the codebase5trunk fmt --all6git commit -m 'reformat code'78# get the commit hash 9git log 1011# put into the ignore revs file12echo "26125bcc894c7e3988985ba459967c0fb21f9194" | cat > .git-blame-ignore-revs13git add .git-blame-ignore-revs 14git commit -m 'add git blame ignore file'15git push1617# turn it on by default18git config blame.ignoreRevsFile .git-blame-ignore-revs1920# git blame the same file to see that it works21git blame somefile.txt22
```

In the above example, the 26125bcc894c7e3988985ba459967c0fb21f9194 part is the hash of the specific commit that includes the reformat changes. Putting it into the .git-blame-ignore-revs file makes git blame (and GitHub) ignore it.

## Conclusion

Tool automation is magical. It’s one of the rare win/wins in software development. For a large codebase adopting these tools wholesale can still bring disruption. Hopefully the tips above will help your team adopt automated linters and formatters. And if you want an easy way to manage them, try out Trunk Check.


