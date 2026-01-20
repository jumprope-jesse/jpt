# ProseMirror: Async Upload Pattern with Placeholder Decorations

*Source: [ProseMirror upload example](https://prosemirror.net/examples/upload/) - Added: 2026-01-19*

## The Problem

When implementing image uploads in a rich text editor, you face a UX challenge:
- Upload takes time (asynchronous operation)
- User shouldn't wait for upload to complete before continuing to edit
- Placeholder needs to move with surrounding text as document is edited
- Final image should replace placeholder wherever it ends up

Traditional approach: Make user wait → upload → insert. This breaks flow.

## The Solution: Decoration-Based Placeholders

Use **decorations** (ephemeral UI-only additions) instead of real document nodes:

1. Insert a placeholder decoration immediately when file is selected
2. Start upload in background
3. Decoration moves automatically as document is edited
4. When upload completes, replace decoration with actual image node
5. If upload fails or content deleted, remove decoration cleanly

## Implementation

### 1. Placeholder Plugin

Manages a `DecorationSet` that tracks all active upload placeholders:

```javascript
import {Plugin} from "prosemirror-state"
import {Decoration, DecorationSet} from "prosemirror-view"

let placeholderPlugin = new Plugin({
  state: {
    init() { return DecorationSet.empty },
    apply(tr, set) {
      // Automatically adjust decoration positions as doc changes
      set = set.map(tr.mapping, tr.doc)

      // Check transaction metadata for add/remove commands
      let action = tr.getMeta(this)
      if (action && action.add) {
        let widget = document.createElement("placeholder")
        let deco = Decoration.widget(action.add.pos, widget, {id: action.add.id})
        set = set.add(tr.doc, [deco])
      } else if (action && action.remove) {
        set = set.remove(set.find(null, null,
                                  spec => spec.id == action.remove.id))
      }
      return set
    }
  },
  props: {
    decorations(state) { return this.getState(state) }
  }
})
```

**Key insight:** `set.map(tr.mapping, tr.doc)` automatically updates all decoration positions as the document changes. This is the magic that makes placeholders "stick" to their context.

### 2. Finding Placeholders

Helper to get current position of a placeholder by ID:

```javascript
function findPlaceholder(state, id) {
  let decos = placeholderPlugin.getState(state)
  let found = decos.find(null, null, spec => spec.id == id)
  return found.length ? found[0].from : null
}
```

Returns `null` if placeholder was deleted (surrounding content removed).

### 3. Upload Flow

```javascript
function startImageUpload(view, file) {
  // Fresh object as unique ID for this upload
  let id = {}

  // Insert placeholder at selection
  let tr = view.state.tr
  if (!tr.selection.empty) tr.deleteSelection()
  tr.setMeta(placeholderPlugin, {add: {id, pos: tr.selection.from}})
  view.dispatch(tr)

  // Start async upload
  uploadFile(file).then(url => {
    let pos = findPlaceholder(view.state, id)

    // Content deleted during upload? Just bail
    if (pos == null) return

    // Otherwise insert image at placeholder's current position
    view.dispatch(view.state.tr
                  .replaceWith(pos, pos, schema.nodes.image.create({src: url}))
                  .setMeta(placeholderPlugin, {remove: {id}}))
  }, () => {
    // Upload failed - clean up placeholder
    view.dispatch(tr.setMeta(placeholderPlugin, {remove: {id}}))
  })
}
```

### 4. File Input Handler

```javascript
document.querySelector("#image-upload").addEventListener("change", e => {
  if (view.state.selection.$from.parent.inlineContent && e.target.files.length)
    startImageUpload(view, e.target.files[0])
  view.focus()
})
```

## Why This Pattern Works

### Decorations vs Document Nodes

| Aspect | Decorations | Document Nodes |
|--------|-------------|----------------|
| Persistence | UI-only, ephemeral | Part of document state |
| Position tracking | Auto-updates with `map()` | Manual tracking needed |
| Undo/redo | Not affected | Requires special handling |
| Collaborative editing | No conflicts | Can cause sync issues |

**Using decorations for placeholders means:**
- Upload state doesn't pollute document state
- No special undo/redo logic needed
- Works seamlessly in collaborative contexts
- Cleanup is trivial (just remove decoration)

### Multiple Concurrent Uploads

The `DecorationSet` naturally handles multiple simultaneous uploads:
- Each gets unique ID (fresh object: `let id = {}`)
- All positions update independently as doc changes
- No coordination needed between uploads

### Graceful Failure Handling

Three failure modes all handled cleanly:

1. **Upload fails** → Remove decoration via error handler
2. **User deletes surrounding content** → `findPlaceholder()` returns null, bail out
3. **User undoes past placeholder insertion** → Decoration disappears, position lookup returns null

## Key Takeaways

1. **Decorations are perfect for transient UI** - Don't pollute document state with temporary upload state
2. **Transaction metadata is clean coordination** - Plugin communicates via `tr.setMeta()` rather than global state
3. **Position mapping is automatic** - ProseMirror's `Mapping` system keeps decorations synced as doc changes
4. **Unique object IDs are elegant** - No need for UUID library, `{}` creates unique identity
5. **Null checks handle edge cases** - Simple `if (pos == null) return` covers deletion scenarios

## When to Use This Pattern

- **Image/file uploads** - Main use case
- **Async API calls** - Fetching embed data, link previews
- **Background processing** - OCR, image optimization, video transcoding
- **Collaborative cursors** - Track other users' positions (similar concept)

## Limitations

- Decorations don't survive page reload (need to track upload state separately for persistence)
- Can't easily show upload progress (decoration is static widget)
- If many simultaneous uploads, may want debounced UI updates

## Related Patterns

- **Collaborative editing with CRDTs** - Similar position-tracking challenges
- **OverType transparent textarea** - Different approach to WYSIWYG (see `overtype-transparent-textarea-editor.md`)
- **ContentEditable alternatives** - ProseMirror avoids many ContentEditable quirks
- **Optimistic UI updates** - Similar pattern in React/Redux for async operations

## See Also

- ProseMirror Guide: https://prosemirror.net/docs/guide/
- Decorations reference: https://prosemirror.net/docs/ref/#view.Decoration
- Transaction metadata: https://prosemirror.net/docs/ref/#state.Transaction.setMeta
