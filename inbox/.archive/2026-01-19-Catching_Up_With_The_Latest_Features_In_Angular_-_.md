---
type: link
source: notion
url: https://ionic.io/blog/catching-up-with-the-latest-features-in-angular
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-02-20T20:22:00.000Z
---

# Catching Up With The Latest Features In Angular - Ionic Blog

## AI Summary (from Notion)
- Angular Renaissance: Angular is undergoing significant updates with a focus on standalone components and new features.
- Introduction of Signals:
- Signals provide a new way to manage component state, enabling reactive programming.
- Signals allow for state management and automatic updates in templates.
- Core Features:
- Raw Signals: Basic state management through a signal function that manages values.
- Computed Signals: Allows creation of derived values based on other signals.
- Effects: Functions that trigger when a signal's value changes, improving reactivity.
- New Input API:
- Signals can now replace traditional @Input decorators, enhancing data passing into components.
- Signals can be marked as required to ensure developers provide necessary data.
- Enhanced Component API: Other decorators like @ViewChild and @Output are transitioning to signal-based implementations.
- Reactive ngModel: A new reactive version of ngModel is introduced for better form data binding using signals.
- Future of Angular: Signals are central to upcoming changes in Angular, with ongoing discussions about their implementation.
- Conclusion: The Angular framework is evolving rapidly, with Signals playing a crucial role in improving developer experience and enhancing component functionality.

## Content (from Notion)

Angular is having a bit of a renaissance lately. With the move to standalone components, the Angular team has been on a roll shipping new features and improvements to the framework at such speed, it’s hard to believe this is the same Angular we’ve come to know. With all these changes, you might be confused about what you need to update to or what’s been removed. Let’s look at a new modern Angular structure and start to adopt these new features.

## A New Primitive

With recent releases of Angular, the core team has introduced a new way to manage component state, Signals. Signals, having been popularized in SolidJS, provide an API for managing state, and reacting to changes in that state. Angular has adapted Signals into the framework and have started to build a set of new features that utilize Signals as their cornerstone.

The first feature is just a raw signal:

```plain text
import { Component, signal } from '@angular/core';

@Component({
  template: `
    <p>The current count is {{count()}}</p>
  `,
  standalone: true,
  imports: [],
})
export class AppComponent {
  count = signal(0);
}
```

A signal is a function that takes an initial value and when invoked, returns the current value of the signal. In our component, we create a signal called count with an initial value of 0. Then to access that signal, we invoke it via {{count()}}. When rendered, this will display “0”. To change the value of the signal, we can use set or update:

```plain text
import { Component, signal } from '@angular/core';

@Component({
  template: `
    <p>The current count is {{count()}}</p>
    <button (click)="increment()">Increment</button>
    <button (click)="decrement()">Decrement</button>
    <button (click)="reset()">Reset</button>
  `,
  standalone: true,
  imports: [],
})
export class AppComponent {
  count = signal(0);

  increment(){
    this.count.update((currentValue) => ++currentValue);
  }
  decrement(){
    this.count.update((currentValue) => --currentValue);
  }
  reset(){
    this.count.set(0);
  }
}
```

Using update allows us to access the current value of the signal, and set allows us to set a new value without caring about the current value.

In addition to just raw Signals, we also can utilize computed to create derived values. computed allows us to create a signal that is based on another signal:

```plain text
import { Component, computed, signal } from '@angular/core';

@Component({
  template: `
    <p>The current count is {{count()}}</p>
    <p>The current count doubled is {{doubled()}}</p>
    <button (click)="increment()">Increment</button>
    <button (click)="decrement()">Decrement</button>
    <button (click)="reset()">Reset</button>
  `,
  standalone: true,
  imports: [],
})
export class AppComponent {
  count = signal(0);
  doubled = computed(() => this.count() * 2);
  increment(){
    this.count.update((currentValue) => ++currentValue);
  }
  decrement(){
    this.count.update((currentValue) => --currentValue);
  }
  reset(){
    this.count.set(0);
  }
}
```

Here, doubled is going to render double whatever count’s value is. What’s helpful here is that because Signals are reactive, when count changes, double will automatically update to reflect the new value.

Finally, the last concept of Signals that we need to know about are effects. effects are functions that get invoked when the value of a signal is changed.

```plain text
import { Component, computed, effect, signal } from '@angular/core';

export class AppComponent {
  count = signal(0);
  doubled = computed(() => this.count() * 2);

  constructor(){
    effect(() => {
      console.log(`The value of count has changed: ${this.count()}`)
    })
    effect(() => {
      console.log(`The value of double has changed: ${this.doubled()}`)
    })
  }
}
```

What’s important to know here is that an effect will only run when the accessed signal is invoked. Meaning, if we only access doubled, the effect will only run when doubled changes.

And with all of this, you now know all about Signals! Congrats, but there is so much more now that we know what Signals are. With this, the Angular team has been revisiting the component API that has been with us since Angular v2.0. These optional changes provide an improved developer experience and are based all on Signals!

## Signals for all the things

If you’ve ever wanted to pass data into a component with Angular, you’ve used the @Input decorator. When developers set data on the component itself, the data is then accessible to the template.

```plain text
import { Component, Input } from '@angular/core';

@Component({
  template: ``,
  standalone: true,
  imports: [],
})
export class ChildComponent {
  @Input()
  passedData = 'foo';
}
```

Now this works fine for data that we just need to display, it can become pretty limiting if we need to perform any other actions. This leads to an approach where setters/getters are used in combination with the @Input in order to achieve this:

```plain text
export class ChildComponent {
  private _internalData = 'foo';

  @Input()
  get passedData() {
    return this._internalData;
  }

  set passedData(val) {
    this._internalData = val;
    this.someOtherAction();
  }
  someOtherAction() {
    console.log(`passedData has changed: ${this.passedData}`);
  }
}
```

This works, but it can be better. The setter for passedData acts the same way as an effect does in our previous example on Signals, so why not just use Signals instead? The Angular team agrees and has provided a new input API.

Similar to @Input, the signal based approach lets users pass data into a component using the signal primitive. Meaning, not only can we access it in our template like a normal signal, we can also use an effect when that input has changed.

```plain text
export class ChildComponent {
  passedData = input('foo');

  constructor() {
    effect(() => {
      console.log(`passedData has changed: ${this.passedData()}`);
    });
  }
}
```

We can also mark our input as required so that developers know they must set that data.

```plain text
export class ChildComponent {
  passedData = input.required('foo');

  constructor() {
    effect(() => {
      console.log(`passedData has changed: ${this.passedData()}`);
    });
  }
}
```

Now it doesn’t stop there, we also have a few more decorators that we use inside our components. Things like @ViewChild and @Output are also on their way to becoming signal-based.

Just released, an implementation of queries provide a more consistent way of working with the DOM elements. Outputs have always been merged, but are still marked as private to the framework.

```plain text
import { Component, ElementRef, effect } from '@angular/core';

@Component({
  standalone: true,
  template: `<div #el></div>`,
})
export class AppComponent {
  divEl = viewChild.required<ElementRef<HTMLDivElement>>('el');

  constructor(){
    effect(() => {
      // some mapping library
      new Maps({
        el: this.divEl.nativeElement
      })
    })
  }
}
```

## Two Way Signals

Everything we’ve seen here has been the building block for what we have next, a reactive version of ngModel. ngModel has been with us all the way back in the Angular v1.0 days, and for good reason. It’s traditionally been used for handling form data binding, where text inputs can have their value bound to a variable, and on input, update that variable’s value.

Now with Signals, we can recreate ngModel using the same primitive that make up the rest of our API, Signals.

```plain text
@Component({
  standalone: true,
  selector: 'some-checkbox',
  template: `
    <p>Checked: {{ checked() }}</p>
    <button (click)="toggle()">Toggle</button>
  `,
})
export class SomeCheckbox {
  checked = model(false);

  toggle() {
    checked.update(c => !c);
  }
}

@Component({
  Signals: true,
  selector: 'some-page',
  template: `
    <some-checkbox [(checked)]="isAdmin" />
  `,
})
export class SomePage {
  isAdmin = signal(false);
}
```

## Parting Thoughts

So, we got Signals for almost every new part of Angular, input, output, viewChild, and model! There’s a lot of momentum around Angular at the moment, with Signals in the middle of it. To get more detail and understand the future of Signals in Angular components, be sure to check out the current RFC on the subject.

### Mike Hartington

Director of Developer Relation...

## Join our newsletter. No spam-only the good stuff.

Sign up to receive the latest updates from our Blog.


