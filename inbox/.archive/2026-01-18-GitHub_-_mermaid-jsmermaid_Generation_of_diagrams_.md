---
type: link
source: notion
url: https://github.com/mermaid-js/mermaid
notion_type: Software Repo
tags: ['Running']
created: 2025-05-24T12:31:00.000Z
---

# GitHub - mermaid-js/mermaid: Generation of diagrams like flowcharts or sequence diagrams from text in a similar manner as markdown

## Overview (from Notion)
- Visualization in Documentation: Embracing tools like Mermaid can streamline complex concepts in your software projects, making it easier to communicate ideas to your team or clients.
- Efficiency Boost: Using diagramming tools reduces the time spent on documentation, allowing for more focus on development and innovation.
- Collaboration Enhancement: Visual aids foster better collaboration among team members, especially in a diverse workforce, by ensuring everyone understands the same concepts.
- User-Centric Design: Understanding user journeys and feedback through diagrams can lead to better product development, enhancing user experience.
- Educational Tool: Mermaid can be a great teaching aid when mentoring junior developers or conducting workshops, simplifying complex programming concepts.
- Community Engagement: Contributing to open-source projects like Mermaid can expand your network and establish you as a thought leader in your field.
- Security Awareness: The caution around user-generated content in diagrams highlights the importance of security in software development, relevant in today’s threat landscape.
- Flexibility in Work Environment: The ability to create dynamic diagrams supports remote work setups, allowing clarity in virtual meetings or asynchronous communication.
- Personalization: Adapting Mermaid for personal projects can reflect your unique approach to problem-solving and creativity in software solutions.
- Alternative Tools: While Mermaid is powerful, exploring other diagramming tools might provide different features that could better suit specific project needs.

## AI Summary (from Notion)
Mermaid is a JavaScript tool for generating diagrams from markdown-like text, enabling easy creation and modification of complex diagrams for documentation. It includes a live editor, various diagram types, and emphasizes community contributions and security measures for safe diagram rendering.

## Content (from Notion)

# Mermaid

Generate diagrams from markdown-like text.

Live Editor!

📖 Documentation | 🚀 Getting Started | 🌐 CDN | 🙌 Join Us

简体中文

Try Live Editor previews of future releases: Develop | Next

🏆 Mermaid was nominated and won the JS Open Source Awards (2019) in the category "The most exciting use of technology"!!!

Thanks to all involved, people committing pull requests, people answering questions! 🙏

## Table of content

## About

Mermaid is a JavaScript-based diagramming and charting tool that uses Markdown-inspired text definitions and a renderer to create and modify complex diagrams. The main purpose of Mermaid is to help documentation catch up with development.

> 

Diagramming and documentation costs precious developer time and gets outdated quickly. But not having diagrams or docs ruins productivity and hurts organizational learning.

Mermaid addresses this problem by enabling users to create easily modifiable diagrams. It can also be made part of production scripts (and other pieces of code).

Mermaid allows even non-programmers to easily create detailed diagrams through the Mermaid Live Editor.

For video tutorials, visit our Tutorials page. Use Mermaid with your favorite applications, check out the list of Integrations and Usages of Mermaid.

You can also use Mermaid within GitHub as well many of your other favorite applications—check out the list of Integrations and Usages of Mermaid.

For a more detailed introduction to Mermaid and some of its more basic uses, look to the Beginner's Guide, Usage and Tutorials.

Our PR Visual Regression Testing is powered by Argos with their generous Open Source plan. It makes the process of reviewing PRs with visual changes a breeze.

In our release process we rely heavily on visual regression tests using applitools. Applitools is a great service which has been easy to use and integrate with our tests.

## Mermaid AI Bot

Mermaid Bot will help you understand this repository better. You can ask for code examples, installation guide, debugging help and much more.

## Examples

The following are some examples of the diagrams, charts and graphs that can be made using Mermaid. Click here to jump into the text syntax.

### Flowchart [docs - live editor]

```plain text
flowchart LR

A[Hard] -->|Text| B(Round)
B --> C{Decision}
C -->|One| D[Result 1]
C -->|Two| E[Result 2]

```

Loading

```plain text
flowchart LR

A[Hard] -->|Text| B(Round)
B --> C{Decision}
C -->|One| D[Result 1]
C -->|Two| E[Result 2]

```

### Sequence diagram [docs - live editor]

```plain text
sequenceDiagram
Alice->>John: Hello John, how are you?
loop HealthCheck
    John->>John: Fight against hypochondria
end
Note right of John: Rational thoughts!
John-->>Alice: Great!
John->>Bob: How about you?
Bob-->>John: Jolly good!

```

Loading

```plain text
sequenceDiagram
Alice->>John: Hello John, how are you?
loop HealthCheck
    John->>John: Fight against hypochondria
end
Note right of John: Rational thoughts!
John-->>Alice: Great!
John->>Bob: How about you?
Bob-->>John: Jolly good!

```

### Gantt chart [docs - live editor]

```plain text
gantt
    section Section
    Completed :done,    des1, 2014-01-06,2014-01-08
    Active        :active,  des2, 2014-01-07, 3d
    Parallel 1   :         des3, after des1, 1d
    Parallel 2   :         des4, after des1, 1d
    Parallel 3   :         des5, after des3, 1d
    Parallel 4   :         des6, after des4, 1d

```

Loading

```plain text
gantt
    section Section
    Completed :done,    des1, 2014-01-06,2014-01-08
    Active        :active,  des2, 2014-01-07, 3d
    Parallel 1   :         des3, after des1, 1d
    Parallel 2   :         des4, after des1, 1d
    Parallel 3   :         des5, after des3, 1d
    Parallel 4   :         des6, after des4, 1d

```

### Class diagram [docs - live editor]

```plain text
classDiagram
Class01 <|-- AveryLongClass : Cool
<<Interface>> Class01
Class09 --> C2 : Where am I?
Class09 --* C3
Class09 --|> Class07
Class07 : equals()
Class07 : Object[] elementData
Class01 : size()
Class01 : int chimp
Class01 : int gorilla
class Class10 {
  <<service>>
  int id
  size()
}


```

Loading

```plain text
classDiagram
Class01 <|-- AveryLongClass : Cool
<<Interface>> Class01
Class09 --> C2 : Where am I?
Class09 --* C3
Class09 --|> Class07
Class07 : equals()
Class07 : Object[] elementData
Class01 : size()
Class01 : int chimp
Class01 : int gorilla
class Class10 {
  <<service>>
  int id
  size()
}


```

### State diagram [docs - live editor]

```plain text
stateDiagram-v2
[*] --> Still
Still --> [*]
Still --> Moving
Moving --> Still
Moving --> Crash
Crash --> [*]

```

Loading

```plain text
stateDiagram-v2
[*] --> Still
Still --> [*]
Still --> Moving
Moving --> Still
Moving --> Crash
Crash --> [*]

```

### Pie chart [docs - live editor]

```plain text
pie
"Dogs" : 386
"Cats" : 85.9
"Rats" : 15

```

Loading

```plain text
pie
"Dogs" : 386
"Cats" : 85.9
"Rats" : 15

```

### Git graph [experimental - live editor]

```plain text
gitGraph
  commit
  commit
  branch develop
  checkout develop
  commit
  commit
  checkout main
  merge develop
  commit
  commit

```

Loading

```plain text
gitGraph
  commit
  commit
  branch develop
  checkout develop
  commit
  commit
  checkout main
  merge develop
  commit
  commit

```

### Bar chart (using gantt chart) [docs - live editor]

```plain text
gantt
    title Git Issues - days since last update
    dateFormat  X
    axisFormat %s

    section Issue19062
    71   : 0, 71
    section Issue19401
    36   : 0, 36
    section Issue193
    34   : 0, 34
    section Issue7441
    9    : 0, 9
    section Issue1300
    5    : 0, 5

```

Loading

```plain text
gantt
    title Git Issues - days since last update
    dateFormat  X
    axisFormat %s

    section Issue19062
    71   : 0, 71
    section Issue19401
    36   : 0, 36
    section Issue193
    34   : 0, 34
    section Issue7441
    9    : 0, 9
    section Issue1300
    5    : 0, 5

```

### User Journey diagram [docs - live editor]

```plain text
  journey
    title My working day
    section Go to work
      Make tea: 5: Me
      Go upstairs: 3: Me
      Do work: 1: Me, Cat
    section Go home
      Go downstairs: 5: Me
      Sit down: 3: Me

```

Loading

```plain text
  journey
    title My working day
    section Go to work
      Make tea: 5: Me
      Go upstairs: 3: Me
      Do work: 1: Me, Cat
    section Go home
      Go downstairs: 5: Me
      Sit down: 3: Me

```

### C4 diagram [docs]

```plain text
C4Context
title System Context diagram for Internet Banking System

Person(customerA, "Banking Customer A", "A customer of the bank, with personal bank accounts.")
Person(customerB, "Banking Customer B")
Person_Ext(customerC, "Banking Customer C")
System(SystemAA, "Internet Banking System", "Allows customers to view information about their bank accounts, and make payments.")

Person(customerD, "Banking Customer D", "A customer of the bank, <br/> with personal bank accounts.")

Enterprise_Boundary(b1, "BankBoundary") {

  SystemDb_Ext(SystemE, "Mainframe Banking System", "Stores all of the core banking information about customers, accounts, transactions, etc.")

  System_Boundary(b2, "BankBoundary2") {
    System(SystemA, "Banking System A")
    System(SystemB, "Banking System B", "A system of the bank, with personal bank accounts.")
  }

  System_Ext(SystemC, "E-mail system", "The internal Microsoft Exchange e-mail system.")
  SystemDb(SystemD, "Banking System D Database", "A system of the bank, with personal bank accounts.")

  Boundary(b3, "BankBoundary3", "boundary") {
    SystemQueue(SystemF, "Banking System F Queue", "A system of the bank, with personal bank accounts.")
    SystemQueue_Ext(SystemG, "Banking System G Queue", "A system of the bank, with personal bank accounts.")
  }
}

BiRel(customerA, SystemAA, "Uses")
BiRel(SystemAA, SystemE, "Uses")
Rel(SystemAA, SystemC, "Sends e-mails", "SMTP")
Rel(SystemC, customerA, "Sends e-mails to")

```

Loading

```plain text
C4Context
title System Context diagram for Internet Banking System

Person(customerA, "Banking Customer A", "A customer of the bank, with personal bank accounts.")
Person(customerB, "Banking Customer B")
Person_Ext(customerC, "Banking Customer C")
System(SystemAA, "Internet Banking System", "Allows customers to view information about their bank accounts, and make payments.")

Person(customerD, "Banking Customer D", "A customer of the bank, <br/> with personal bank accounts.")

Enterprise_Boundary(b1, "BankBoundary") {

  SystemDb_Ext(SystemE, "Mainframe Banking System", "Stores all of the core banking information about customers, accounts, transactions, etc.")

  System_Boundary(b2, "BankBoundary2") {
    System(SystemA, "Banking System A")
    System(SystemB, "Banking System B", "A system of the bank, with personal bank accounts.")
  }

  System_Ext(SystemC, "E-mail system", "The internal Microsoft Exchange e-mail system.")
  SystemDb(SystemD, "Banking System D Database", "A system of the bank, with personal bank accounts.")

  Boundary(b3, "BankBoundary3", "boundary") {
    SystemQueue(SystemF, "Banking System F Queue", "A system of the bank, with personal bank accounts.")
    SystemQueue_Ext(SystemG, "Banking System G Queue", "A system of the bank, with personal bank accounts.")
  }
}

BiRel(customerA, SystemAA, "Uses")
BiRel(SystemAA, SystemE, "Uses")
Rel(SystemAA, SystemC, "Sends e-mails", "SMTP")
Rel(SystemC, customerA, "Sends e-mails to")

```

## Release

For those who have the permission to do so:

Update version number in package.json.

```plain text
npm publish
```

The above command generates files into the dist folder and publishes them to https://www.npmjs.com.

## Related projects

- Command Line Interface
- Live Editor
- HTTP Server
## Contributors  

Mermaid is a growing community and is always accepting new contributors. There's a lot of different ways to help out and we're always looking for extra hands! Look at this issue if you want to know where to start helping out.

Detailed information about how to contribute can be found in the contribution guide

## Security and safe diagrams

For public sites, it can be precarious to retrieve text from users on the internet, storing that content for presentation in a browser at a later stage. The reason is that the user content can contain embedded malicious scripts that will run when the data is presented. For Mermaid this is a risk, specially as mermaid diagrams contain many characters that are used in html which makes the standard sanitation unusable as it also breaks the diagrams. We still make an effort to sanitize the incoming code and keep refining the process but it is hard to guarantee that there are no loop holes.

As an extra level of security for sites with external users we are happy to introduce a new security level in which the diagram is rendered in a sandboxed iframe preventing javascript in the code from being executed. This is a great step forward for better security.

Unfortunately you cannot have a cake and eat it at the same time which in this case means that some of the interactive functionality gets blocked along with the possible malicious code.

## Reporting vulnerabilities

To report a vulnerability, please e-mail security@mermaid.live with a description of the issue, the steps you took to create the issue, affected versions, and if known, mitigations for the issue.

## Appreciation

A quick note from Knut Sveidqvist:

> 

Mermaid was created by Knut Sveidqvist for easier documentation.


