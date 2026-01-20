# WebContainers - Browser-Based Node.js Runtime

WebContainers is a browser-based runtime from StackBlitz that runs Node.js directly in the browser using WebAssembly. No remote servers needed.

## Key Capabilities

- **Full Node.js in browser** - Run npm, pnpm, yarn natively (claims 10x faster than local)
- **All major browsers** - Chromium, Firefox, Safari TP
- **Wasm support** - Run WebAssembly applications out of the box
- **Framework agnostic** - Works with any modern framework

## Use Cases

- **Interactive tutorials** - SvelteKit uses it for learn.svelte.dev
- **AI-native IDEs** - re:tune built a copilot that operates in full runtime context
- **Documentation** - Interactive code examples that actually run
- **Low-code editors** - Non-technical contributors can make PRs with live previews
- **Disposable dev environments** - Spin up/down without server costs

## API Example

```javascript
import { WebContainer } from '@webcontainer/api';

const webcontainer = await WebContainer.boot();
await webcontainer.mount(projectFiles);

const install = await webcontainer.spawn('npm', ['i']);
await install.exit;

await webcontainer.spawn('npm', ['run', 'dev']);
```

## Why It Matters

- Eliminates server costs for interactive coding experiences
- Enables fully-branded embedded IDEs without third-party redirects
- Opens possibilities for AI agents that can run code in browser sandboxes

## Links

- Main site: https://webcontainers.io/
- API docs: https://webcontainers.io/guides/quickstart
