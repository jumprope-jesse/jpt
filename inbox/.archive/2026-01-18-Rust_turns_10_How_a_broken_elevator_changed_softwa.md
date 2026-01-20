---
type: link
source: notion
url: https://www.zdnet.com/article/rust-turns-10-how-a-broken-elevator-changed-software-forever/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-05-21T03:54:00.000Z
---

# Rust turns 10: How a broken elevator changed software forever | ZDNET

## Overview (from Notion)
- Rust’s emphasis on memory safety and concurrency can enhance your software projects, reducing bugs and improving reliability—beneficial for your role as a founder.
- The community-driven development of Rust mirrors the collaborative spirit often required in startups, promoting shared ownership and innovation.
- The story of Rust’s creation, sparked by a frustrating experience with a faulty elevator, could inspire you to identify and solve everyday problems through technology.
- As a NYC resident, consider how Rust's growing adoption by major tech companies can impact local job opportunities and the tech ecosystem.
- The ability to create reliable infrastructure with Rust aligns with the increasing demand for robust software solutions in a tech-dependent world.
- Explore the learning curve of Rust as a personal challenge; mastering it could set your projects apart and attract top talent to your company.
- Alternate views might emphasize the steep learning curve and potential over-engineering of solutions in Rust, suggesting simpler languages could be more efficient for specific projects.

## AI Summary (from Notion)
Rust, created by Graydon Hoare in response to frustrations with unreliable software, emphasizes memory safety and concurrency, transforming software development over the past decade. Its community-driven growth has led to significant adoption by major tech companies, making systems programming safer and more enjoyable.

## Content (from Notion)

Elyse Betters Picaro / ZDNET

Eric S. Raymond, one of open-source's founders, famously said, "Every good work of software starts by scratching a developer's personal itch." That was certainly the case with Graydon Hoare, a Mozilla software developer, when he started work on the Rust programming language.

In 2006, Hoare was annoyed with his apartment building's elevator that kept breaking down. As he later said, "It's ridiculous that we computer people couldn't even make an elevator that works without crashing!" He suspected it kept breaking down because of memory errors in its control software, which was likely written in C or C++. Both are popular systems languages that are difficult to code in -- in no small part because it's too easy to write semi-functional code with memory errors.

Also: The most popular programming languages in 2025 (and what that even means)

So Hoare, sick of dragging himself up 21 flights of stairs every day, began designing a new computer language. He wanted to create a small, fast programming language without the potential for memory bugs. He called it Rust, after a family of tough fungi he described as "over-engineered for survival."

## A turning point

His goal was to create a safe and concurrent language. Unlike C and C++, Rust enforces memory safety through its unique ownership system. It prevents common errors like null pointer dereferencing and buffer overflows by ensuring that each piece of data has a single owner and is automatically freed when it goes out of scope. This approach eliminates entire categories of memory bugs at compile time. Rust's concurrency model further enhances safety by catching data races before the code runs, making it easier for developers to write programs that are both safe and efficiently concurrent.

This wasn't easy. While it began as a home project, Mozilla saw the potential and started officially sponsoring Rust in 2009. The language was publicly announced in 2010, and after years of iteration, Rust 1.0 shipped on May 15, 2015.

That 10 years ago.

Also: ChatGPT writes my routine in 12 top programming languages. Here's what the results tell me

The first stable release of the Rust programming language quietly marked a turning point in the world of software development. Today, Rust is not just a technical achievement but a testament to the power of community-driven innovation, transforming from a Mozilla-backed experiment into a mainstream tool embraced by tech giants and open-source communities alike.

## Just the beginning

Rust's first stable release was just the beginning. In the decade since, the language has grown by leaps and bounds. Rust's package registry alone, crates.io, has ballooned from about 2,000 packages ("crates") at 1.0 to over 180,000 today. The standard library tripled in size, and the toolchain matured with features like rust-analyzer for IDE support and a robust package manager, Cargo.

At the same time, Rust's commitment to non-breaking releases and regular six-week cycles has enabled rapid innovation without sacrificing reliability. Over 246,000 changes have been merged since 1.0, with 6,700 contributors and nearly 600,000 public crates tested for each release.

Also: How to use ChatGPT to write code - and my favorite trick to debug what it generates

Hoare recently acknowledged this, saying, "Rust is a story about a large community of stakeholders coming together to design, build, maintain, and expand shared technical infrastructure. It's a story with many actors." The actors include developers, language designers, authors, and educators, and the institutions that support Rust. What has brought them together, said Hoare, was "a common interest in infrastructure."

By infrastructure, Hoare means "a tool for building other infrastructure: network protocols, web servers, load balancers, telemetry systems, databases, codecs, cryptography, file systems, operating systems, virtual machines, interpreters, etc., etc."

Hoare added, "The world needs robust and reliable infrastructure, and the infrastructure we had was not up to the task. Put simply: it failed too often, in spectacular and expensive ways. Crashes and downtime are, in the best cases, and security vulnerabilities are, in the worst. Efficient 'infrastructure-building' languages existed, but they were very hard to use, and nearly impossible to use safely, especially when writing concurrent code." Rust was Hoare's answer.

I'd call this systems programming.

## Underlying plumbing

Unlike other popular languages, such as Python, JavaScript, or Java, Rust isn't meant for writing high-level programs that end users work with; instead, it's used to create the underlying plumbing that all software needs to work.

This is not the kind of programming that everyone does. However, for those who do work with the software, pipes, and fittings, Rust is very popular. So it is that, according to the Stack Overflow developer survey, for the eighth year in a row, "Rust is the most admired language; more than 80% of developers who use it want to use it again next year."

I confess I'm one of them. While I haven't been a serious developer for years, when I do code these days, Rust is my first choice. It just works, and I don't need to sweat the memory details as I once did with C.

I'm far from alone. Rust's adopters read like a who's who of modern computing. For example, Mozilla uses it in Firefox; Google in Android, Chrome OS, and Fuchsia; and Microsoft in its Windows core libraries and Azure Confidential Compute.

Also: Linus Torvalds talks AI, Rust adoption, and why the Linux kernel is 'the only thing that matters'

Nearest and dearest to my heart, the Linux kernel is now incorporating Rust. It hasn't been a smooth journey. As Linus Torvalds recently said, "I was expecting [Rust] updates to be faster, but part of the problem is that old-time kernel developers are used to C and don't know Rust. They're not exactly excited about having to learn a new language that is, in some respects, very different. So there's been some pushback on Rust." Still, Torvalds remains a stalwart Rust-in-Linux supporter.

## Learning Rust

That said, using and learning Rust is not without its hurdles. Its learning curve, especially around the borrow checker and lifetimes, remains steep for newcomers. Personally, I didn't find it that hard. If you want to learn Rust yourself, I recommend starting with The Rust Programming Language (aka The Book), followed by Rust for Rustaceans. The websites Rust by Example and Google's Welcome to Comprehensive Rust are also helpful, and they're free to boot.

So it is that, a decade after 1.0 was released, Rust has achieved what once seemed impossible: making systems programming both safe and enjoyable.

Also: The best AI for coding in 2025 (and what not to use - including DeepSeek R1)

As Hoare reflected on Rust's 10th anniversary, "Rust is a story about a large community of stakeholders coming together to design, build, maintain, and expand shared technical infrastructure." In a world increasingly reliant on secure, reliable, and high-performance software, Rust's next decade looks brighter than ever.

Get the morning's top stories in your inbox each day with our Tech Today newsletter.

### Featured

How to move your codebase into GitHub for analysis by ChatGPT Deep Research - and why you should

Your car's USB port is seriously underrated: 5 features you're not using enough

I test dozens of Android phones every year: Here's how the best models stack up

My favorite Garmin safety feature is coming to Forerunner models - and I can't recommend it enough


