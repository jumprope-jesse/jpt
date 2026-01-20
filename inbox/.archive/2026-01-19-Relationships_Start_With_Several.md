---
type: link
source: notion
url: https://lukebechtel.com/blog/relationships-start-with-several
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-02-23T03:43:00.000Z
---

# Relationships: Start With Several

## AI Summary (from Notion)
- Main Idea: Start designing systems with One-To-Many relationships instead of One-To-One relationships to account for future scalability and flexibility.

- Key Takeaway: Many real-world relationships are polyrelational; designing systems to reflect this reality can prevent future refactoring headaches.

- Common Mistake: Novice designers often start with overly simplistic One-To-One relationships, which may lead to complex changes later on.

- Example:
- One-To-One: An owner has exactly one pet.
- One-To-Many: An owner can have multiple pets, which is more representative of reality.

- Complexity: Transitioning from One-To-One to One-To-Many can be cumbersome and error-prone, as it requires significant refactoring of the system.

- Many-To-Many Relationships: While it is possible to start with Many-To-Many relationships, they are often the most complex to maintain due to the introduction of a third object (the relationship itself).

- Efficiency: Scaling down from a One-To-Many relationship to a One-To-One is generally easier than scaling up, as it often involves simply choosing which entity to keep.

- Final Thought: It's better to anticipate needing multiple relationships from the start, as this foresight can save time and effort in the long run.

## Content (from Notion)

> Programmers know three numbers: 0, 1, and N.

This post feels like common sense -- but I've seen it violated (..by me..) so many times that I think it's worth writing down.

When you're designing a system as a novice -- you often start with a single example to represent a relationship -- an Owner has exactly one pet, an Employee has exactly one manager, a Car has exactly one driver. You get the idea.

But as time goes on, the winds of change will continuously push you in the direction of "Relationships should be Many-To-Many". Not always, but very, very often.

This trend isn't magic ✨.

Like most software patterns, it's easily derived from (1) The way the world works, (2) The way humans perceive it.

Most of the world is polyrelational -- either in fact, or in our conception of it. People have more than one pet, most employees have more than one manager, many cars have more than one driver.

(Some people even have multiple romantic relationships, but that's another post ..)

Given this, the following claim:

It's almost always better to start with at least One-To-Many relationships, and it's almost always just as easy to do so.

### Example: One-To-One

Let's imagine you're designing a system to represent a pet owner and their pet.

This is our pet:

```plain text
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 10
        self.happiness = 0

    def feed(self):
        self.hunger -= 1
        self.happiness += 1

    def walk(self):
        self.happiness += 1

```

Let's create two versions of our Owner class -- one for a One-To-One relationship, and one for a One-To-Many relationship.

```plain text
class OwnerOneToOne:
    def __init__(self, pet):
        self.pet = pet

    def feed_pet(self):
        self.pet.feed()

    def walk_pet(self):
        self.pet.walk()

```

```plain text
class OwnerOneToMany:
    def __init__(self, pets):
        self.pets = pets

    def feed_pets(self):
        for pet in self.pets:
            pet.feed()

    def walk_pets(self):
        for pet in self.pets:
            pet.walk()

```

Great! We have a fancy demo of our incredibly complex system.

Let's note that the One-To-Many version is only slightly more complex than the One-To-One version.

It probably took, what, 10% more time to write? Less if you're experienced.

(And if you're using copilot, you probably just wrote the function headers and it did its thing ;))

Regardless -- now our feature is done, and we can finally move on...

### Scaling Up: One-To-Many

> What a crazy couple of months! We did it!

Time has passed, seasons have changed -- our system has been purring away, just like the pets. It's been a hit, and we've been getting rave reviews from our early customers.

We built several other classes, an API, a frontend -- it's all going great.

But we just got word -- owners can have multiple pets.

Unprecedented!

who-could-have-possibly-foreseen-this.jpg?

### One-To-One -> One-To-Many: The path of pain 💀

In the world of One-To-One, this is a huge change.

Our One-To-One system is now obsolete.

We have to refactor it to match the One-to-Many system.

This is a simple example, but experienced programmers know how incredibly frustrating this gets when the system grows large.

In the real world, to make a change like this, and handle its effects elegantly is often a nightmare.

UI components were built around the old system, tests were written around the old system, and other classes were built around the old system, all of which will need updating. API calls will have to be changed.

The list goes on.

Along the way -- each little refactor introduces the potential for more bugs to creep in, as shims ideally shouldn't, but have to, get put in place to straddle both the old way and the new way.

### One-To-Many -> One-To-Many: The Pathless Path ☯️

In the world of One-To-Many, we just... add another pet to the list.

just add it to the list

### Scaling up Further: Many-To-Many

This post isn't about Many-To-Many, so I'll keep it brief.

But some may ask "Why stop there? Why not start with Many-To-Many?"

In practice -- you can do this. And if your design process suggests that a relationship should be Many-to-Many, you should do that.

But in most software systems I've worked with, Many-To-Many relationships are often the most complex, the most difficult to reason about, and the most difficult to maintain, because they introduce a third object -- the Relationship itself.

In my experience, One-To-Many relationships tend to be the best middle-ground conceptually.

And again, if you're thinking One-to-Many, you're already thinking in multiples. Adding multiples the other way can be tricky, but in my experience, not as tricky as going from no multiples at all*.

### Scaling Down

Moving a *-to-N relationship to a one-to-one relationship is usually much, much, much easier than the other way around -- just answer the question "Which of these should we keep?", and you're halfway there.

In many cases, things like getters in OOP & views in a database can make it so that the customer never needs to know there was a change.

### Final Word

Like I said -- this feels like common sense to me. But when I'm in the heat of the moment, I still catch myself thinking "Bah, there won't be more of these."

And I'm usually wrong.

When it comes to Relationships, at least in Code, prefer starting with several.

You'll thank yourself later.


