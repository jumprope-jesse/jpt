# Angular Signals & Modern Component API

Angular's "renaissance" - major framework modernization with standalone components and Signals as the new reactive primitive.

## Signals Overview

Signals (popularized by SolidJS) provide reactive state management. Angular has built new APIs on top of this primitive.

### Basic Signal

```typescript
import { Component, signal } from '@angular/core';

@Component({
  template: `<p>Count: {{count()}}</p>`,
  standalone: true,
})
export class AppComponent {
  count = signal(0);

  increment() {
    this.count.update((val) => ++val);
  }
  reset() {
    this.count.set(0);
  }
}
```

- `signal(initialValue)` - creates a signal
- `signal()` - invoke to read current value
- `signal.set(value)` - set new value directly
- `signal.update(fn)` - update based on current value

### Computed Signals

Derived values that auto-update when dependencies change:

```typescript
count = signal(0);
doubled = computed(() => this.count() * 2);
```

### Effects

Run side effects when signals change:

```typescript
constructor() {
  effect(() => {
    console.log(`Count changed: ${this.count()}`);
  });
}
```

Effects only run when accessed signals change.

## Signal-Based Component APIs

### Input Signals (replaces @Input)

Old way with setters:
```typescript
@Input()
set passedData(val) {
  this._data = val;
  this.doSomething();
}
```

New way:
```typescript
passedData = input('default');
// or required:
passedData = input.required<string>();

constructor() {
  effect(() => {
    console.log(`Input changed: ${this.passedData()}`);
  });
}
```

### ViewChild Signals

```typescript
divEl = viewChild.required<ElementRef<HTMLDivElement>>('el');

constructor() {
  effect(() => {
    new Maps({ el: this.divEl().nativeElement });
  });
}
```

### Two-Way Binding with model()

Signal-based ngModel replacement:

```typescript
// Child component
@Component({
  template: `
    <p>Checked: {{ checked() }}</p>
    <button (click)="toggle()">Toggle</button>
  `,
})
export class SomeCheckbox {
  checked = model(false);
  toggle() {
    this.checked.update(c => !c);
  }
}

// Parent
@Component({
  template: `<some-checkbox [(checked)]="isAdmin" />`,
})
export class SomePage {
  isAdmin = signal(false);
}
```

## Migration Path

All these APIs are optional - existing @Input/@Output decorators still work. Signals provide:
- Cleaner reactive patterns (no setter boilerplate)
- Consistent API across inputs, outputs, queries
- Better integration with computed values and effects

Source: Ionic Blog - Mike Hartington (2024)
