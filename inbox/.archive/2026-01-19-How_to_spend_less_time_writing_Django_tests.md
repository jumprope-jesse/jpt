---
type: link
source: notion
url: https://blog.kolo.app/tests-no-joy.html?utm_campaign=Django%2BNewsletter&utm_medium=rss&utm_source=Django_Newsletter_222
notion_type: Software Repo
tags: ['Running']
created: 2024-03-08T21:00:00.000Z
---

# How to spend less time writing Django tests

## AI Summary (from Notion)
- Theme of Test Writing: The author dislikes writing tests despite acknowledging their importance for ensuring code reliability.
- Common Sentiment: Many software engineers share the sentiment of not enjoying writing tests, contrasting with the perception that test-driven development is universally loved.
- Value of Tests: Tests provide confidence that code changes do not introduce bugs or unintended consequences.
- Introduction to Kolo: Kolo is a tool designed to simplify the process of generating tests in Django by capturing execution traces.
- Trace Inversion: Kolo allows users to invert traces collected during application execution to automatically generate integration tests.
- Integration Tests vs. Unit Tests: Integration tests validate the entire stack by simulating HTTP requests, while unit tests focus on specific functions.
- Example of Test Generation: The document provides examples of how Kolo can create integration tests from recorded traces using real HTTP requests and SQL queries.
- Customization: Kolo offers customization options for generated tests, allowing developers to tweak and modify them as needed.
- Real-World Application: Kolo has been effectively used in the development of the Simple Poll project, demonstrating its practical benefits in a larger codebase.
- Getting Started with Kolo: Steps for using Kolo include capturing a trace and running a command to generate tests.
- Future Development: There are plans to develop a web version of Kolo, expanding its accessibility beyond VSCode.
- Community Engagement: The author invites feedback and discussions about Kolo and its functionalities.

## Content (from Notion)

### Autogenerating django integration tests using Kolo and trace inversion

Kolo test generation in action

## I don’t enjoy writing tests

I have a confession to make: I don’t enjoy writing tests. I really enjoy writing code, really enjoy bringing a feature to life and getting it out there, but writing tests is probably my least favourite part.

I do appreciate the tests that already exist, the ones that maybe even past me has written. Those tests give me confidence that everything is still working, that I didn’t break anything and that my new code can safely roll out.

I’m grateful for those existing tests, but then whenever I sit down to write tests for a newly built feature, I am filled by dread. I know future me will be thankful, but I wish I didn’t have to do this. The hours I will spend on writing tests, I’d rather spend on building the next feature.

I’ve given a talk version of this blog post at two different conferences and each time asked the audience how they feel about writing tests:

Enjoy tests poll results></p> <p>To be honest, it was a bit of a relief to see that there are other software engineers who feel similarly about writing tests. Sometimes you get the impression that everyone else loves writing tests, loves test driven development, and would in fact love to spend more time writing tests. While that may be an opinion held by some, the majority of us consider it maybe not the most fun part of the job.</p> <h2>Tests give us confidence that everything still works</h2> <p>Before we talk about how to spend less time on writing tests, what’s the value of them in the first place? In a nutshell, tests guarantee that you’re not breaking anything, that there are no unintended consequences to your change. You can move forward with confidence because you know, that everything is still working as it was before. Sure, there can be some other benefits too, but ‘confidence that everything still works’ is the primary value of tests.</p> <h2>Recording traces with Kolo</h2> <p><a href=

Kolo is a tracing, visualisation, and test generation tool for Python and Django. To briefly explain how it works: Kolo collects information about everything that happens in your program. Every function call, every return value, every variable – it’s all captured and saved in a “trace" when Kolo is enabled. Here’s what that looks like for a simple program that multiplies two numbers.

Kolo can then also show you that trace data inline in VSCode:

When you’re using Django you don’t even need to use kolo run – just add the the koloMiddleware to MIDDLEWARE in settings.py. Requests traced by Kolo will then look something like this:

Besides function call data, Kolo also captures served http requests, sql queries (as well as the data retrieved by them) and more! Without us needing to do much, our code actually generates a lot of useful information which we can then use for a number of things, including to generate integration tests. Here’s how that works.

## Inverting a trace to build an integration test

When I say "build an integration test", I mean using the django test client to make an http request and that request passing through the full django http stack and through our code. After the request is finished, we then make assertions on the http response (status code, content, etc.) or on state changes in the database.

This is different to a unit test where we might import a specific function and test it against specific inputs and outputs or an end to end browser test where we’d fire up Chrome to programmatically click on UI elements.

I like and mostly write integration tests. They excel at giving us confidence that everything still works. For more on why integration tests give you the most bang for your buck, check out this excellent post: “Write tests. Not too many. Mostly integration”

### Arrange – the hardest part of making an integration test

The most annoying thing about integration tests is just that they can be a little tricky to arrange and scaffold out – especially when you’re doing it for the first time. But that’s exactly what Kolo is here to help us with!

Generating an integration test with Kolo always starts with an already recorded trace that you’d like to use as the starting point for your test. Imagine you’re working on a todo app and all todos are displayed when you visit /. You’ve had Kolo enabled while doing this and now have a trace recorded.

The trace contains a number of individual events (or frames), which Kolo can use to generate an equivalent line of code in our integration test.

In this case, the http request was a GET to / so to have this same identical request happen in our integration test Kolo writes a line to make a GET request to / using the django test client:

response = self.client.get("/")

Similarly, if the associated http response was recorded as status code 200 Kolo will put the appropriate assertion in the generated test:

self.assertEqual(response.status_code, 200)

At its core, this is a very basic idea. For every event that is in the trace, there’s a corresponding bit of code we can put in our integration test. This gets particularly interesting and useful for SQL queries.

### SQL Queries

Now imagine our traced request when visiting / also included the above SELECT SQL query. Kolo captured the details of the two rows that were loaded from the database and can add the exact same data to our test database before we make the request to /.

So the full auto-generated integration would look like this:

```plain text
from django.test import TestCase

class MyTestCase(TestCase):
    def test_my_view(self):
        todo, _created = Todo.objects.get_or_create(
            title="Give a talk at Django Day Copenhagen",
            defaults={"id": 50}
        )

        todo_2, _created = Todo.objects.get_or_create(
            title="Take over the world with kindness",
            defaults={"id": 51}
        )

        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

```

We can run that test (as you can see in the GIF at the very top) and it passes 😎! That’s a fully working integration test, using real data, hitting the same code that we did when we browsed to /. And just like that we've added some code coverage to our codebase.

### Kolo’s aim is to provide a great starting point for your test

You might have noticed that the seed data set up above is slightly unusual in that it specifies our todos be created with specific ids (50 and 51). Kolo does this to play it safe. It's currently not smart enough to know if our code loaded these two todos because the incoming request specified them.

That’s actually not the case here (our code lists todos, it doesn’t fetch them by id), but let me show you another example where specifying todos by id in the request itself would be the case: We might have this view to complete a specific todo.

```plain text
def complete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.is_completed = True
    todo.save()

    return HttpResponseRedirect("/")

```

A trace recorded from completing a todo will look something like this:

```plain text
{
    "frames": [
        {
            "method": "POST",
            "path_info": "/complete/50/",
            "type": "django_request",
        },
        {
            "qualname": "core.views.complete_todo",
            "event": "call",
            "locals": {"request": <WSGIRequest: POST '/complete/50/'>, "todo_id": 50},
            "type": "frame",
        },
        {
            "query": "SELECT \"core_todo\".\"id\", \"core_todo\".\"title\", \"core_todo\".\"is_completed\" FROM \"core_todo\" WHERE \"core_todo\".\"id\" = 50 LIMIT 21",
            "query_data": [[(50,"Give a talk at Django Day Copenhagen",False)]],
            "type": "end_sql_query"
        },
        {
            "query": "UPDATE \"core_todo\" SET \"title\" = 'Give a talk at Django Day Copenhagen', \"is_completed\" = true WHERE \"core_todo\".\"id\" = 50",
            "type": "end_sql_query"
        },
        {
            "qualname": "core.views.complete_todo",
            "event": "return",
            "locals": {"request": <WSGIRequest: POST '/complete/50/'>,"todo_id": 50,"todo": <Todo: Todo object (50)>},
            "type": "frame",
        },
        {
            "status_code": 302,
            "type": "django_response",
        }
    ],
}

```

And then the generated test would be:

```plain text
class MyTestCase(TestCase):
    def test_my_view(self):
        todo, _created = Todo.objects.get_or_create(
            title="Give a talk at Django Day Copenhagen", defaults={"id": 50}
        )
        response = self.client.post("/complete/50/")

        self.assertEqual(response.status_code, 302)

        todo.refresh_from_db()
        self.assertEqual(todo.title, "Give a talk at Django Day Copenhagen")
        self.assertEqual(todo.is_completed, True)

```

In this generated test, it’s crucial that Kolo specifies the todo with id 50 since 50 is referenced in the request itself – without that the test wouldn’t pass.

But really the point I want to make here is that Kolo’s aim is to give you a great starting point: The aim is to give you a fully arranged, working, passing integration test that uses real data and covers your code. It’s always a lot easier to tweak and modify something that already exists (and works), rather than building a whole new test from scratch.

You might see the test Kolo generates and decide you don’t need or want certain parts of it. That’s totally fine – deleting code is easy! In this specific case, we might want to make the todo id dynamic:

```plain text
class MyTestCase(TestCase):
    def test_my_view(self):
        todo = Todo.objects.create(title="Give a talk at Django Day Copenhagen")
        response = self.client.post(f"/complete/{todo.id}/")

        self.assertEqual(response.status_code, 302)

        todo.refresh_from_db()
        self.assertEqual(todo.title, "Give a talk at Django Day Copenhagen")
        self.assertEqual(todo.is_completed, True)

```

And since there was an UPDATE in the trace we generated the test from, Kolo actually also added two asserts at the bottom for us. One of them is exactly what we want here (asserting the todo is in fact now completed) – but we don’t really need the other one that asserts on the title, so we could delete it. Kolo helps us get to a good starting point, and then we can take it from there, modifying our test(s) as we see fit.

## A real example

This todo app is a cute demo, but does all this actually work in a real codebase? Yes, it actually does! And we've been making extensive use of Kolo in building Simple Poll – which is the other product made by the six of us in the company behind Kolo.

(We actually started building Kolo to improve our own developer experience building Simple Poll, but that’s a story for another time. Kolo is completely free right now, so the revenue from Simple Poll is also how we’ve been funding the development of Kolo for the past several years)

Simple Poll makes it very simple to create all kinds of polls and surveys in Slack. It’s been around for over eight years and at around 80k lines of app and 100k lines of test code is a decently sized Django codebase.

One of the busiest codepaths that we have in Simple Poll is casting a vote on a poll. This is what a trace of the “vote” request looks like in the visualisation Kolo provides:

Kolo trace of a vote request

Every white node represents a function call, every purple node is a SQL query, the blue node is an outbound http request, and green nodes are background tasks.

With the Kolo CLI we can get the trace id of our most recent trace:

```plain text
➜  simplepoll git:(main) ✗ kolo trace list --count 1
trc_01HQBJJEWHNRPFJE8Z53E47E1F at 2024-02-23 18:10:20.670 (444.4 KB)

```

And then use that trace id to generate a test:

kolo generate-test trc_01HQBJJEWHNRPFJE8Z53E47E1F > test_vote.py

And despite the size of this view (305 frames including 31 SQL queries), Kolo manages to generate a working integration test (imports omitted for brevity):

```plain text
class MyTestCase(CustomTestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.timestamp = str(int(time.time()))

    @httpretty.activate(allow_net_connect=False)
    def test_my_view(self):
        with time_machine.travel("2024-02-26T10:55:10"):
            team, _created = Team.objects.get_or_create(
                team_name="Wilhelm Klopp",
                team_domain="wilhelmklopp",
                has_app_installed=True,
                defaults={"team_id": "T0GQP31BJ"},
            )
            user = UserFactory.create(
                user_id="U0GQNK50S",
                name="wilhelm",
                email="wilhelm@simplepoll.rocks",
                team=team,
                access_token="xoxp-redacted",
            )
            bot, _created = Bot.objects.get_or_create(
                team=team,
                scope="commands,im:read,im:write,chat:write,channels:join,app_mentions:read,team:read,users:read,channels:read,groups:read,mpim:read,workflow.steps:execute",
                bot_user_id="UP61WQZ3Q",
                last_installed_by_user_id="U0GQNK50S",
                defaults={"id": 8},
            )
            poll = PollFactory.create(
                question="Tabs or Spaces?",
                creator=user,
                timestamp="1708944744.188289",
                channel_id="C0GQNEU7R",
                posted_with="post_message",
                unique_uuid="5fe17e21-8354-4bac-8a22-8d0d4d2f3509",
            )
            option, _created = Option.objects.get_or_create(
                poll=poll,
                attachment_id=1,
                text="Spaces",
                creator=user,
                defaults={"id": 10780986},
            )
            option_2, _created = Option.objects.get_or_create(
                poll=poll,
                attachment_id=1,
                text="Tabs",
                creator=user,
                defaults={"id": 10780985},
            )
            httpretty.register_uri(
                httpretty.POST,
                "https://hooks.slack.com/actions/T0GQP31BJ/6723364718336/vjQ25RiwsJSMgmhr3eH7fjmh",
                status=200,
                body=json.dumps({"ok": True}),
                content_type="application/json; charset=utf-8",
            )

            response = self.client.post(
                "/buttons/poll_action/block_actions/poll-5fe17e21-8354-4bac-8a22-8d0d4d2f3509-vote-10780986/vote-10780986/",
                urlencode(
                    {
                        "payload": '{"type":"block_actions","user":{"id":"U0GQNK50S","username":"wilhelm","name":"wilhelm","team_id":"T0GQP31BJ"},"api_app_id":"A0U898NL8","token":"redacted","container":{"type":"message","message_ts":"1708944744.188289","channel_id":"C0GQNEU7R","is_ephemeral":false},"trigger_id":"6693937574470.16839103392.0dece04abfb0dc7c1d475b1482fecc1e","team":{"id":"T0GQP31BJ","domain":"wilhelmklopp"},"enterprise":null,"is_enterprise_install":false,"channel":{"id":"C0GQNEU7R","name":"general"},"message":{"bot_id":"BNR2AFPPC","type":"message","text":"Tabs or Spaces?","user":"UP61WQZ3Q","ts":"1708944744.188289","app_id":"A0U898NL8","blocks":[{"type":"section","block_id":"poll-5fe17e21-8354-4bac-8a22-8d0d4d2f3509-title-and-menu","text":{"type":"mrkdwn","text":"*Tabs or Spaces?*","verbatim":false},"accessory":{"type":"overflow","action_id":"title-and-menu","options":[{"text":{"type":"plain_text","text":":information_source: Edit Poll","emoji":true},"value":"view_info"},{"text":{"type":"plain_text","text":":lock: Close Poll","emoji":true},"value":"close_poll"},{"text":{"type":"plain_text","text":":recycle: Recreate this Poll","emoji":true},"value":"create_poll_from_recent_poll"},{"text":{"type":"plain_text","text":":x: Delete Poll","emoji":true},"value":"delete_poll"},{"text":{"type":"plain_text","text":":arrow_heading_down: Promote Poll","emoji":true},"value":"promote_poll"}]}},{"type":"section","block_id":"poll-5fe17e21-8354-4bac-8a22-8d0d4d2f3509-vote-10780985","text":{"type":"mrkdwn","text":":one: Tabs\\n","verbatim":false},"accessory":{"type":"button","action_id":"vote-10780985","text":{"type":"plain_text","text":":one:","emoji":true}}},{"type":"section","block_id":"poll-5fe17e21-8354-4bac-8a22-8d0d4d2f3509-vote-10780986","text":{"type":"mrkdwn","text":":two: Spaces\\n","verbatim":false},"accessory":{"type":"button","action_id":"vote-10780986","text":{"type":"plain_text","text":":two:","emoji":true}}},{"type":"context","block_id":"+CwAa","elements":[{"type":"mrkdwn","text":"Created by <@U0GQNK50S> with \\/poll","verbatim":false}]}],"team":"T0GQP31BJ","edited":{"user":"BNR2AFPPC","ts":"1708944894.000000"}},"state":{"values":{}},"response_url":"https:\\/\\/hooks.slack.com\\/actions\\/T0GQP31BJ\\/6723364718336\\/vjQ25RiwsJSMgmhr3eH7fjmh","actions":[{"action_id":"vote-10780986","block_id":"poll-5fe17e21-8354-4bac-8a22-8d0d4d2f3509-vote-10780986","text":{"type":"plain_text","text":":two:","emoji":true},"type":"button","action_ts":"1708944910.297843"}]}'
                    }
                ),
                HTTP_X_SLACK_REQUEST_TIMESTAMP="1708944910",
                HTTP_X_SLACK_SIGNATURE="v0=4f66698cd3d88c2dde84f3b815da229fe24d6780e02b37cb48630f5c7995b4b0",
                content_type="application/x-www-form-urlencoded",
            )

            self.assertEqual(response.status_code, 200)

            option_vote = OptionVote.objects.get(option=option, user=user)

            event = Event.objects.get(team=team, user=user)
            self.assertEqual(event.name, "Vote")
            self.assertEqual(event.slack_user_id, "U0GQNK50S")

```

Running the test confirms that it’s working as expected 🎉

```plain text
➜  simplepoll git:(main) ✗ python manage.py test -k test_vote
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.209s

OK
Destroying test database for alias 'default'...

```

There’s a few additional things happening in this test generated from a real view in a real codebase. Here’s a quick overview:

- httpretty (an http mocking library) is activated, ensuring our test won’t make any real http requests to the internet
- we use time-machine to set the same time to when the original trace was captured, ensuring no timing related bugs
- the next 50 lines of code are all arranging our seed data: creating a team, user, poll, etc. Note how Kolo is able to make use of our factoryboy factories
- we then mock the specific http request we expect to make in our code (httpretty.register_uri)
- now that all the set up is done, we act by making our incoming http request with the django test client, using the exact same data we captured via the trace
- finally we assert that what we expected to happen did in fact happen: that the request returned a 200 and that the vote we cast now exists in the database
While testing Kolo’s test generation abilities on the Simple Poll codebase, we learned early on that it’s quite useful to customise the generated test a bit, which is why you can pretty much customise all parts of Kolo’s test generation: factoryboy factories, custom trace processors (which turn trace data into context available in the test template), and fully custom templates. More on customising the generated tests in our docs.

## Using Kolo test generation in your project

So how can you spend less time writing tests? Consider auto generating (parts of) your integration tests! There’s really just two steps to it:

1. Capture a trace with Kolo enabled (by having the Kolo middleware installed and then making a request to your locally running django app)
1. Run kolo generate-test {trace_id} > test_example.py
We have documentation and guides for each step:

1. Getting started with Kolo and traces
1. Generate tests with Kolo (note: VSCode is not required to generate tests with Kolo)
We’ve also set up the todo demo app from earlier on replit, where you can play around with Kolo all in the browser

1. Go to our demo repl and click “Fork & Run”
1. Make some requests (you may need to click “New tab” and add/complete todos in the new tab rather than replit’s built in browser)
1. In the replit shell run this command to generate a test from the latest Kolo trace: kolo generate-test $(kolo trace list --count 1 | awk '{print $1}') > core/tests.py
1. View the generated test in core/tests.py and run it using python manage.py test 🎉
Have got thoughts / ideas / questions about Kolo or this whole concept of inverting traces to generate tests? We’d love to know and talk! Drop us an email at w@kolo.app 🫶

## Assorted links

- Talk version of this blog post
- Kolo Newsletter
- Kolo Issue Tracker
- Kolo VSCode extension
- “Write tests. Not too many. Mostly integration”
🤫 Psst – we’re in the process of building out a web version of Kolo (early sneak peek screenshot below). Much of Kolo’s best functionality currently lives in the VSCode extension and the most frequent feedback we get is “Kolo looks great, but when will you build an extension for Pycharm/Sublime/Vim?” – so we’re excited to finally bring Kolo to everyone via the web. We’re looking for a handful of beta testers who’re willing to endure some rough edges and provide feedback. If that’s you, please send an email with subject line “Kolo Web Beta” to w@kolo.app ✌️


