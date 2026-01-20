---
type: link
source: notion
url: https://cq2.co/blog/the-best-way-to-have-complex-discussions
notion_type: Software Repo
tags: ['Running']
created: 2024-05-06T21:52:00.000Z
---

# The best way to have complex discussions — CQ2

## AI Summary (from Notion)
- Complex Discussions: The document emphasizes the importance of structured discussions for complex topics to avoid impulsive responses and unorganized comments.

- Current Tools Limitations:
- In-person discussions are prone to impulsive responses.
- Platforms like Discourse and Slack lack the necessary structure for deep discussions, leading to confusion (e.g., "quote hell").

- CQ2 Introduction:
- CQ2 is a free and open-source tool designed specifically for complex discussions.
- It aims to enhance discussion organization and productivity.

- Key Features of CQ2:
- Threading: Allows creation of threads within threads to keep discussions organized and focused.
- Replying Mechanism: Users can reply to specific quotes, avoiding the clutter of unrelated comments.
- Navigation: Offers a tree structure for easy navigation between threads and visibility of unread comments.
- Concluding Discussions: Users can mark threads and discussions as concluded for clearer communication.

- Future Plans: CQ2 has plans for additional features such as rich text support, custom titles, and an AI assistant.

- Mission: The ultimate goal of CQ2 is to facilitate better discussions, leading to a deeper understanding, better decision-making, and arriving at truth.

## Content (from Notion)

CQ2 demo screenshot

We love complex, deep discussions.

We've seen or been part of many discussions — strategic discussions at work, discussions on AI alignment, technical design documents, public policy, etc. For us, the most frustrating issues with discussions are: impulsive responses and lack of structure.

The default way of discussions — in-person ones — are highly susceptible to impulsive responses and are extremely hard to provide a good structure for, making them the worst for complex topics.

The first issue of impulsive responses is a hard nut to crack. Practising and advocating for active listening is the ideal solution but it's not guaranteed to work every time and in every team. That's why we prefer written, async discussions over in-person ones for complex topics — they help prevent impulsive responses to an extent (and even more with features like slow mode) and promote thoughtful responses. But the second issue still remains — written, async discussions lack structure too. If you've used chat/forum platforms like Slack and Discourse for complex discussions, you know how hard it is to follow comments there.

DiscourseIn Discourse, discussions are a stream of unorganised comments. This way of discussion — where people talk over one another and topics get mixed up — doesn't work for deep dives into complex and lengthy topics. For such topics, the discussion needs to be carefully written and organised.

There's no concept of “where” you are in Discourse discussions. There's only “when” you are, since the comments are ordered only by time. Discourse does provide some organisation to see the replies to a comment at one place. However if you need to see the replies to a particular reply inside a comment, you need to scroll down through other comments, find that particular reply (repeated as a comment!) and then check its replies:

CQ2 demo screenshot

SlackSlack is not really built for written, async discussions, but since it's widely used, let's talk about it. Discussions there are a stream of unorganised comments too, but at least Slack has threads to discuss a particular comment in detail in a separate pane. However, if you want to discuss a comment inside a thread in detail (i.e., create a new thread from a thread), you can't — Slack allows only one level of threads. Moreover, Slack feels too chatty — it feels impossible to have a long-running async discussion there. Its UI encourages sending bursts of fast, short comments instead of well-formed thoughts, and the typing indicator keeps everyone else distracted while one person tries to form their idea.

Quote hellNow behold the common annoyance in all chat/forum platforms — the quote hell. What's that? Let's say Ava puts a comment about something. Then Caleb puts a comment with his replies to some quotes from Ava's comment. Now Ava puts a comment with her replies to Caleb's replies in quotes. What's happening? Replies to a topic are spread across different comments and you're forced to mentally manage all those quotes and their replies! On top of that, there are unrelated comments between that break your flow. These problems might not seem big for a discussion between two people, but a complex and lengthy discussion with 5+ participants quickly turns into a huge mess. Here's what a quote hell looks like:

After being frustrated with Slack, Discourse, etc., we started searching for a tool specifically built for complex discussions. We found none, began exploring how such a tool would work and look like, and started building:

CQ2It's a free and open source tool for complex discussions. It's in its early stages, but it's the start of something that we think will both make discussions immensely enjoyable and radically increase productivity. We simulated a small discussion from LessWrong on CQ2. Check it out on the live demo, here! It turned out to be much better organised and easier to follow.

In CQ2, there's no mess of unorganised comments — create threads inside threads so that each thread stays on topic and organised. Forget quote hell — create threads around specific quotes and find all replies related to a topic at one place. Never lose context of where you are — see all parent threads of the current thread in the same view. Focus on what matters — see which threads have unread comments, which are concluded and quickly go to a particular thread using CQ2's tree. Conclude threads — add conclusions to resolved threads and to the whole discussion once it's resolved.

The CQ2 way of having complex discussions:

StartingCreate a discussion by providing a title and a description. The description could be short or long, and is used to set the context, provide necessary information and/or your thoughts before starting the discussion. Then share the link with the participants.

CQ2 demo screenshot

Commenting and creating threadsGeneral comments about the discussion go in the main (first and leftmost) thread. To reply to a particular text from the main description or from any comment, select the text, click on the popped-up “Reply in new thread” button to create a new thread around that specific quote, and reply there. You can reply to the whole comment as well, instead of a particular text inside it, by using the reply button on the top-right of the comment.

CQ2 demo screenshot

Opening threadsIf someone has already created a thread for a particular quote, the quote would appear highlighted. You can click on it to open its corresponding thread and continue the discussion there. If someone has already created a thread for a whole comment, there would be a highlighted comments button on the top-right of the comment which you can click on to open the corresponding thread.

CQ2 demo screenshot

NavigatingTo move between different threads, you can scroll using a trackpad or using your mouse's scroll wheel with the shift key. You can also use the tree from the navigation bar to quickly go to a particular thread. The tree also shows the number of comments in a thread, the number of unread comments and whether the thread has been concluded.

CQ2 demo screenshot

ConcludingYou can conclude a thread by using the “Conclude thread” button on top of the thread. Concluded threads have a green badge on top and the conclusion comment in green. To conclude the whole discussion, use the “Conclude discussion” button in the navigation bar.

CQ2 demo screenshot

Try creating some threads and adding some comments in the demo, here!

We have many more interesting and useful features planned, including rich text, workspaces, custom titles for threads, mentions, slow mode, useful reactions (and not just emojis) and even an AI assistant to help you find overlooked parts of the discussion.

With CQ2, we want to help people have better discussions, and ultimately, systematically arrive at truth, better understand others and make better decisions. If you resonate with CQ2's mission, we would love for you to try it out, provide your feedback here and share this post with your friends!

Get early access, here.


