---
type: link
source: notion
url: https://saashammer.com/blog/lightweight-javascript-framework-review-for-django-developers/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-01-25T06:09:00.000Z
---

# Lightweight Javascript Framework Review (For Django Developers)

## AI Summary (from Notion)
- The document is a review of lightweight JavaScript frameworks for Django developers.
- It addresses the confusion developers face when selecting a lightweight framework for Django projects due to the abundance of options.
- The author presents a comparison of various frameworks, including those from other communities like Phoenix, Rails, and Laravel.
- Key frameworks discussed:
- Phoenix LiveView: A library for real-time user experiences with server-rendered HTML, emphasizing the importance of WebSockets.
- Django Reactor and Django Unicorn: Inspired by Phoenix LiveView, with Unicorn using AJAX instead of WebSockets, making it simpler.
- Laravel Livewire: A full-stack framework for Laravel, working well with Alpine.js for front-end interactions.
- HTMX and Alpine.js: Solutions that enhance HTML with AJAX capabilities and minimal JavaScript.
- Turbo (part of Hotwire): Offers features like Turbo Drive, Frames, and Streams for a smooth user experience.
- The document highlights the importance of understanding user needs and the trade-offs between using WebSockets and traditional HTTP requests.
- Major themes:
- The balance between simplicity and functionality in lightweight frameworks.
- The growing popularity of frameworks like HTMX and Alpine.js among Django developers.
- The advantages of Hotwire as a solid solution, backed by extensive community support and resources.
- Takeaways:
- For quick prototyping without extensive JavaScript knowledge, Alpine.js + HTMX is recommended.
- For a more robust solution with solid architecture, Hotwire (Turbo + Stimulus) is favored despite a steeper learning curve.
- Interesting facts:
- The author notes that frameworks like HTMX and Alpine.js are gaining traction in the Django community due to their versatility.
- Many successful applications utilize Hotwire, showcasing its reliability as projects scale.

## Content (from Notion)

## Introduction

Many developers are confused when they try to find a Lightweight Javascript Framework for the Django project because there are so many options.

In this post, I will talk and compare lightweight javascript frameworks, and help you decide which one is the best for your Django project.

If you want to:

1. Render HTML in Django, and use Javascript to enhance the server-rendred HTML.
1. Say no to the heavy frontend solutions such as React, Vue, Svelte, Angular
1. Say no to the Decoupled Architecture
Then this post can help you!

## Why this Post is Unique

Unlike other posts which only compare existing solutions in the Django community, I will also talk about solutions in other communities (Phoenix, Rails, Laravel) and how they influenced each other.

Below is a list of frameworks that I will talk about in this post

1. Phoenix LiveView
1. Laravel Livewire
1. Hotwire (Turbo, Stimulus)
1. StimulusReflex
1. Catalyst
1. HTMX
1. Unpoly
1. Alpine.js
1. Django Reactor
1. Django Unicorn
1. django-sockpuppet
1. Tetra
I hope that can help you get a better understanding.

## Phoenix LiveView

At first, I'd like to talk about Phoenix LiveView, because it is so important and inspired so many javascript frameworks.

> 

Phoenix LiveView is library which enables rich, real-time user experiences with server-rendered HTML.

The LiveView applications are stateful due to the bidirectional communication with WebSockets.

Events in LiveView are regular messages which may cause changes to its state. Once the state changes, LiveView will re-render the relevant parts of its HTML template and push it back to the browser, which updates itself in the most efficient manner.

A LiveView begins as a regular HTTP request and HTML response, and then upgrades to a stateful view on client connect (Websocket). Any time a stateful view changes or updates its socket assigns, it is automatically re-rendered and the updates are pushed to the client.

For example, to react to a click on a button:

```plain text
<button phx-click="inc_temperature">+</button>

```

On the server

```plain text
def handle_event("inc_temperature", _value, socket) do
  {:ok, new_temp} = Thermostat.inc_temperature(socket.assigns.id)
  {:noreply, assign(socket, :temperature, new_temp)}
end

```

After receiving the message, the server re-rendered the HTML, push it back to the client via Websocket, the page UI can be updated and user feel it is real-time.

Phoenix LiveView

With LiveView, in many cases, developers do not need to write a single line of JavaScript to build feature.

But you should also know, in some cases, developers still need to sprinkle JavaScript behavior directly into the HTML. For example, tabs, dropdowns, popovers and modals.

### Websocket

As we already know, WebSocket is very important in Phoenix LiveView, since it makes bidirectional communication between the client and the server possible.

> 

You should also know, other programming languages such as PHP, Ruby, Python can not do the same as Elixir in the Concurrency area.

And you can check this post Phoenix Channels vs Rails Action Cable

So developers in other community usually solve the problem in this way:

1. User trigger some event (click the button)
1. Use HTTP to transfer event from the client to the server. (not Websocket)
1. Server re-render the component HTML, and return HTML back in HTTP response.
1. Extract HTML from the HTTP response and update page UI.
Next, let's take a look at some other javascript frameworks.

### Django Community

- Django Reactor is a port of Phoenix LiveView, it depends on Django channels, a package which provides Websocket support.
- Django Unicorn is inspired by Phoenix LiveView, but it does not depend on Websocket. When event fired on the browser, it sends AJAX request to the backend, and then use the response to update the page UI.
For example, to react to a click on a button in Django Unicorn

```plain text
<button unicorn:click="increment">+</button>

```

The server component

```plain text
from django_unicorn.components import UnicornView


class ClicksView(UnicornView):
    count = 0

    def increment(self):
        self.count += 1

```

From Github stats, more people like Django Unicorn than Reactor, I guess that is because:

1. Django Unicorn does not depend on Websocket, which makes the infrastructure simpler.
1. The attributes (for example unicorn:click) is cleaner than using Django templatetag.
### Laravel Community

Laravel is the most popular web framework in the PHP community.

Laravel Livewire is a full-stack framework for Laravel, which is also inspired by Phoenix LiveView

Let's take a look at the counter example.

```plain text
<button wire:click="increment">+</button>

```

The server side:

```plain text
class Counter extends Component
{
    public $count = 0;

    public function increment()
    {
        $this->count++;
    }

    public function render()
    {
        return view('livewire.counter');
    }
}

```

Livewire also use HTTP to transfer data, but it can also work with websocket to provide real-time functionality.

Actually Livewire and Alpine.js are created by ONE developer, Caleb Porzio, they can work together very well and people in Laravel community usually choose this combination.

Below is a component, which use both Livewire and Alpine.js:

```plain text
<div x-data="{ open: false }">
    <button @click="open = true">Show More...</button>

    <ul x-show="open" @click.outside="open = false">
        <li><button wire:click="archive">Archive</button></li>
        <li><button wire:click="delete">Delete</button></li>
    </ul>
</div>

```

1. The Alpine.js can do the pure frontend work.
1. The Livewire is used to communicate with the backend server.
This project also inspired Django developers and there is a project https://www.tetraframework.com/, you can check if if you are interested.

Now we have seen some solutions which are inspired by Phoenix LiveView, next, let's take a look at another way to solve the Javascript issue.

## Stimulus

Stimulus is part of the Rails official frontend solution Hotwire.

> 

These JavaScript objects are called controllers, and Stimulus continuously monitors the page waiting for HTML data-controller attributes to appear. For each attribute, Stimulus looks at the attribute’s value to find a corresponding controller class, creates a new instance of that class, and connects it to the element.

For example, we have HTML:

```plain text
<div data-controller="hello">
  <input data-hello-target="name" type="text">
  <button data-action="click->hello#greet">Greet</button>
</div>

```

And we have hello_controller.js

```plain text
import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
  static targets = [ "name" ]

  greet() {
    const element = this.nameTarget
    const name = element.value
    console.log(`Hello, ${name}!`)
  }
}

```

Notes:

1. When Stimulus detect data-controller="hello", it will create a new controller instance from hello_controller.js and attach it to the HTML.
1. data-action="click->hello#greet" means, if user click the button, great method in hello controller will be executed to handle the JS event.
Stimulus is a pure frontend framework, and can be used with ANY backend framework.

1. I highly recommend you to read Stimulus 1.0: A modest JavaScript framework for the HTML you already have, published in 2018, by DHH, the creator of Ruby on Rails.
1. You can also check Stimulus official doc to learn more.
### StimulusReflex

StimulusReflex extends capabilities of both Rails and Stimulus by intercepting user interactions and passing them to Rails over real-time websockets.

StimulusReflex can make Rails app work like Phoenix LiveView (it is also inspired by LiveView), by using the Rails ActionCable, which integrates WebSockets with Rails.

For example:

```plain text
<a href="#"
  data-reflex="click->Counter#increment"
  data-step="1"
  data-count="<%= @count.to_i %>"
>Increment <%= @count.to_i %></a>

```

The data-reflex attribute allows us to map an action on the client to code that will be executed on the server.

```plain text
class CounterReflex < ApplicationReflex
  def increment
    @count = element.dataset[:count].to_i + element.dataset[:step].to_i
  end
end

```

On the server, we use element.dataset[:count] to access the data-count, increment the value by 1 and set @count. The Reflex will then push the DOM back to client via Websocket. At last, client will update the page UI.

Please check https://docs.stimulusreflex.com/ to know more about StimulusReflex

This project also inspired Django developers and there is a project django-sockpuppet, which is port of the StimulusReflex.

### Turbo

Turbo derived from Rails Turbolinks package, now it is also part of Rails official frontend solution (Hotwire).

> 

One interesting feature brought by Turbo is Turbo Stream

A Turbo Streams message is a fragment of HTML consisting of <turbo-stream> elements. The stream message below demonstrates the seven possible stream actions

```plain text
<turbo-stream action="append" target="messages">
  <template>
    <div id="message_1">
      This div will be appended to the element with the DOM ID "messages".
    </div>
  </template>
</turbo-stream>

```

With Turbo Stream, we can return HTML from the server to manipunate page DOM without using Javascript, this can let us build many powerful features such as chat room, auto complete search box, and etc.

Another feature of Turbo is Turbo Frame

> 

Turbo Frame provide an opportunity to decompose pages into self-contained fragments.

Both Turbo Stream and Turbo Frame are inspired by Phoenix LiveView

I highly recommend you to check this youtube video What is Hotwire?

### Catalyst

> 

Stimulus inspired Catalyst Catalyst, GitHub’s web component set of patterns.

Github is the web component lover, Stimulus inspired them to build Catalyst, which help developers to build web components using Stimulus like syntax.

The backend Component can have one-to-one relationship with frontend web component, allowing developers to work on a single abstraction for both front-end and backend.

```plain text
<hello-world>
  <input data-target="hello-world.name" type="text">

  <button data-action="click:hello-world#greet">
    Greet
  </button>

  <span data-target="hello-world.output">
  </span>
</hello-world>

```

```plain text
import { controller, target } from "@github/catalyst"

@controller
class HelloWorldElement extends HTMLElement {
  @target name: HTMLElement
  @target output: HTMLElement

  greet() {
    this.output.textContent = `Hello, ${this.name.value}!`
  }
}

```

Catalyst is a very interesting tech, and you can check links below to learn more.

- Catalyst doc
- How we use Web Components at GitHub
## HTMX

> 

```plain text
<button hx-post="/clicked" hx-swap="outerHTML">
  Click Me
</button>

```

1. The attributes have hx prefix
1. The above HTML code means: when a user clicks on this button, issue an AJAX request to /clicked, and replace the entire button with the response
With HTMX, the workflow is very simple, client trigger event and send request, the server return HTML, and then the client update the page according to the response.

HTMX focus more on the communication between the server using Ajax, it seems like Django Unicorn, but the backend does not need to implement stateful component, just render HTML with Django view and get things done.

You can check https://htmx.org/examples/ to know more about HTMX.

There is a project Unpoly which do similar work as HTMX, you can check if you are interested.

## Alpine.js

> 

Let's check an example counter built by Alpine.js

```plain text
<div x-data="{ count: 0 }">
    <button x-on:click="count++">Increment</button>
    <span x-text="count"></span>
</div>

```

1. With x-data, we declared a counter component, which has count=0
1. x-on:click means if user click the button, the count++ will run.
1. x-text="count" means the DOM element will display the count value of the component.
As you can see, it is easy to use Alpine.js to sprinkle JavaScript behavior directly into the HTML.

Alpine.js directives syntax is very similar with Vue.js, because Vue.js is very popular in the PHP community.

Alpine.js is a good option to deal with pure frontend stuff, for example: tabs, modals.

Please check https://alpinejs.dev/ if you want to know more about Alpine.js

## Rough Comparison

Now, we already know many lightweight javascript frameworks, next, we will compare some of them and find out some promising solutions.

### Django Reactor

As we know, this package needs you to install Django channels, a package which provides Websocket support.

Compared with HTTP, Websocket needs more resources on the server (for example: redis connections), and make things more complicated when you need to scale your web application.

That is why I do not recommend any frontend framework which require Websocket (Django Reactor, django-sockpuppet)

Actually, if you take a look at Laravel Livewire, and Hotwire (official frontend framework in Rails community), they use HTTP to transfer data by default, and Websocket is optional.

### Django Unicorn

Django Unicorn use HTTP to transfer data, and the attributes are clean.

It can help the client do communication between the server using Ajax without writing Javascript.

If you want to sprinkle JavaScript behavior directly into the HTML (tabs, dropdowns, popovers and modals), you might still need vanilla javascript or other framework such as Alpine.js

django-unicorn + Alpine.js can be a promising solution.

### HTMX

HTMX also focuses more on the communication between the server using Ajax. Unlike Django Unicorn, it is a generalized framework, and developers can user it with any backend framework.

When using HTMX with Django, developers can still use Django views to return HTML, no need to touch component, which is straightforward.

If you want to sprinkle JavaScript behavior directly into the HTML (tabs, dropdowns, popovers and modals), you have below options:

1. Vanilla javascript
1. Alpine.js
1. hyperscript is a sister project of HTMX
From the community, many people like HTMX + Alpine.js solution, for example: https://django-htmx-alpine.nicholasmoen.com/

HTMX + Alpine.js can be a promising solution.

### Hotwire (Turbo + Stimulus)

As we know, Hotwire is the official frontend solution in the Rails community, which includes Turbo and Stimulus.

The Turbo package contains:

1. Turbo Drive accelerates links and form submissions by negating the need for full page reloads. Which bring SPA experience to our app.
1. Turbo Frames decompose pages into independent contexts, which scope navigation and can be lazily loaded.
1. Turbo Streams deliver page changes over WebSocket, SSE or in response to form submissions using just HTML and a set of CRUD-like actions.
1. Turbo Native help build hybrid apps for iOS and Android
The Stimulus is designed to enhance static or server-rendered HTML, by connecting JavaScript objects to elements on the page using simple annotations

1. We can see Turbo as a competitor of HTMX, they communicate with the backend server.
1. Stimulus can be seen as a competitor of Alpine.js, they do pure frontend work.
Hotwire can be used with ANY backend framework, and it is also very popular in the PHP community (Symfony).

So Turbo + Stimulus can be a promising solution.

## Which Solution Should I Choose

Now we got below promising solutions:

1. django-unicorn + Alpine.js
1. HTMX + Alpine.js
1. Turbo + Stimulus (Hotwire)
In the Django community, it seems HTMX + Alpine.js is more popular than django-unicorn + Alpine.js, since they are similar, I will only talk about HTMX + Alpine.js in the next sections. If you prefer django-unicorn, please feel free to switch.

Next, I will compare HTMX + Alpine.js with Turbo + Stimulus.

### Ecosystem

Let's first take a look at Hotwire.

Hotwire is the official frontend framework in Rails, it is build by people at Basecamp, and powers the Basecamp, HEY email service. (and other Rails web applications)

Both Basecamp and HEY are large web applications, which means Hotwire is solid and works good as your codebase grow bigger and bigger.

And there are many high quality tutorials, open source projects about Hotwire. Since Hotwire is pure frontend framework, we can easily make them work with any backend web frameworks. (Symfony, Django, Flask...)

1. Awesome StimulusJS
1. Turbo Showcase
1. https://thoughtbot.com/blog/tags/hotwire
Backed by Rails community and some successful business companies, Hotwire has healthy ecosystem.

In most cases, if you meet problem, you can easily find answer at StackOverflow, someone's blog, or Github.

Next, let's take a look at Alpine.js and HTMX

Alpine.js is very popular, and there are many resources about it.

From what I see, most of the blogs, videos, open sources projects about HTMX, come from Python developers (Django, Flask), I guess that is because Laravel and Rails already have default frontend solution, so most developers would not try HTMX.

I tried to find what business companies that are using Alpine.js + HTMX to build what products, but I can not find that info.

So the ecosystem of Hotwire seems better than Alpine.js + HTMX, and the large web applications give developers confidence that they can stick with it as the project grow.

### Difficulty of Installation

HTMX + Alpine.js is easy to install, we can import via CDN link, no need transpile or bundle solution.

```plain text
<script src="https://unpkg.com/htmx.org@1.7.0"></script>
<script src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>

```

And then you can write code to enhance the HTML, which is cool!

To install Turbo + Stimulus in your Django project, now you need a bundle solution.

Some Django developers complain they do not like to touch tedious Webpack config or frontend config stuff. Fortunately, the project python-webpack-boilerplate can help you create frontend project which bundled by Webpack within minutes, even you have no idea how to config Webpack.

python-webpack-boilerplate also has detailed doc and pre-defined config to help you keep Javascript and CSS/SCSS in good style.

From Rails 7, it introduced a new tech importmap to use JavaScript libraries made for ES modules (ESM) without the need for transpiling or bundling.

In the future, Django developers can switch to importmap and drop the Webpack, and some people already did attempt. django-importmap

So HTMX + Alpine.js is easy to install than Turbo + Stimulus, but many people overestimate the difficulty.

Because I am pretty sure a beginner Django developer can use python-webpack-boilerplate to install Turbo + Stimulus within ONE hour.

### Directives or Vanilla Javascript

HTMX has about 30 custom attributes (also called directives).

Alpine.js has about 18 custom attributes (also called directives).

For some people, directives is the killer feature, which can let them get things done directly in the template.

However, the directives adds a new layer of complexity, even people who already learned Javascript, still need to learn the syntax (for example, what does hx-trigger="keyup changed delay:1s" mean?).

The Stimulus in Hotwire only use attributes to pass value from the server-rendered HTML to the Stimulus Controller, and the Stimulus Controller is written with normal Javascript syntax, which is more friendly to Javascript people.

### Encapsulation

About 10 years ago, when we build web application, we are told we better decouple HTML, CSS, and JavaScript

At that time, we write Javascript code in a separate JS file with the help of framework such as jQuery.

1. If we want to change content, we edit HTML
1. If we want to change style, we edit CSS
1. If we want to change frontend behavior, we change Javascript.
Let's take a look at the Alpine.js official Dropdown component

```plain text
<div class="flex justify-center">
    <div
        x-data="{
            open: false,
            toggle() {
                if (this.open) {
                    return this.close()
                }

                this.$refs.button.focus()

                this.open = true
            },
            close(focusAfter) {
                if (! this.open) return

                this.open = false

                focusAfter && focusAfter.focus()
            }
        }"
        x-on:keydown.escape.prevent.stop="close($refs.button)"
        x-on:focusin.window="! $refs.panel.contains($event.target) && close()"
        x-id="['dropdown-button']"
        class="relative"
    >
        <!-- Button -->
        <button
            x-ref="button"
            x-on:click="toggle()"
            :aria-expanded="open"
            :aria-controls="$id('dropdown-button')"
            type="button"
            class="bg-white px-5 py-2.5 rounded-md shadow"
        >
            <span>Actions</span>
            <span aria-hidden="true">&darr;</span>
        </button>

    </div>
</div>

```

Notes:

1. This is part of the full code.
1. Do you really believe writing Javascript in your template file is a good idea?
1. If you check the code after 1 month, could you quickly understand what the Alpine.js component do?
1. If you need to update some logic, you might need to change multiple templates?
Even Alpine.js provides a way to register component (Alpine.data), so developers can reuse the code. From what I see, very few Django developers do that.

Stimulus encourage developers to write Javascript in .js, and one controller is for one one type of work. (For example: dropdown_controller.js), this helps the frontend code better organized.

After you write some Stimulus components, you can reuse them in convenient way.

You can check Stimulus Components, which can help you understand and follow the DRY (Don't Repeat Yourself) principle with Stimulus.

### Code Quality, Code Linting

> 

Both Stimulus and Turbo are written with TypeScript,

And you can also write Stimulus controller with TypeScript

https://github.com/stimulus-use/stimulus-use is an interesting project, it learned from React Hook and bring the use syntax to Stimulus. So we can just write callback method in the Stimulus controller.

As a 3-party package which will be used by other people, it is written in TypeScript, to improve the code quality.

Since the Stimulus Controller is a Javascript file, developers can also use mature code linting tool such as Eslint and Prettier to keep the Javascript code in good style.

Let's take a look at Alpine.js + HTMX

1. Both Alpine.js and HTMX are written with regular Javascript.
1. Some people also shared TypeScript solution in Alpine.js, but very few people use it.
1. The code linting tool can not help you detect Javascript very well in the template.
### Learning Curve

Alpine.js + HTMX is easy to install and get started, but things might become a little complicated as your project grow.

Turbo + Stimulus is a little hard to install and get started, but once you understand the concepts, the rest is to build feature with Vanilla javascript. You do not need to remember custom directives such as (hx-trigger, hx-get, hx-post), or the argument syntax such as keyup changed delay:1s.

## Conclusion

If you want to start quickly (prototyping) and do not like to learn Javascript, you can choose Alpine.js + HTMX (or Alpine.js + django-unicorn).

If you do not mind learning some Javascript, and want a solid solution, please try Hotwire. You might feel slow at first, but after you learn it, you will like it and you do not need to switch to another solution until your product exceed the size of https://basecamp.com/, or https://www.hey.com/

## FAQ

### Are there good learning resources about Hotwire and Django?

I released a book to help people to learn Hotwire with Django in a systematic way, please check The Definitive Guide to Hotwire and Django

### Should I use Turbo and Stimulus together?

They are built to solve different problems, and you can use one of them in your project.

For example, you can use Stimulus as a replacement of jQuery.

If possible, you better use them together for better user experience.

Launch Products Faster with Django

SaaS Hammer helps you launch products in faster way. It contains all the foundations you need so you can focus on your product.

Learn More


