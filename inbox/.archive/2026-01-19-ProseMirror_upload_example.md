---
type: link
source: notion
url: https://prosemirror.net/examples/upload/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-02-14T15:37:00.000Z
---

# ProseMirror upload example

## AI Summary (from Notion)
- Purpose: The text discusses managing asynchronous operations in text editing, specifically for image uploads in ProseMirror.
- User Experience: Emphasizes the importance of improving user experience by allowing users to insert a placeholder image while the actual image uploads in the background.
- Placeholder Management: Introduces a plugin that manages placeholder decorations, allowing multiple uploads to be handled concurrently.
- Plugin Functionality:
- Initializes a DecorationSet to handle the placeholders.
- Adjusts decoration positions based on document changes.
- Allows adding or removing placeholders through metadata in transactions.
- File Upload Process:
- Describes the event handler for file inputs that triggers the upload process.
- Uses a function to upload the file and resolve to a file URL.
- Error Handling: Provides a mechanism to clean up the placeholder if the upload fails or if the surrounding content is deleted during the upload process.
- Key Takeaway: The integration of asynchronous image uploads can significantly enhance the editing experience by providing immediate visual feedback without interrupting the workflow.

## Content (from Notion)

Some types of editing involve asynchronous operations, but you want to present them to your users as a single action. For example, when inserting an image from the user's local filesystem, you won't have access to the actual image until you've uploaded it and created a URL for it. Yet, you don't want to make the user go through the motion of first uploading the image, then waiting for that to complete, and only then inserting the image into the document.

Ideally, when the image is selected, you start the upload but also immediately insert a placeholder into the document. Then, when the upload finishes, that placeholder is replaced with the final image.

Insert

Type...

⬚

Insert image:

Since the upload might take a moment, and the user might make more changes while waiting for it, the placeholder should move along with its context as the document is edited, and when the final image is inserted, it should be put where the placeholder has ended up by that time.

The easiest way to do this is to make the placeholder a decoration, so that it only exists in the user's interface. Let's start by writing a plugin that manages such decorations.

```plain text
import {Plugin} from "prosemirror-state"
import {Decoration, DecorationSet} from "prosemirror-view"

let placeholderPlugin = new Plugin({
  state: {
    init() { return DecorationSet.empty },
    apply(tr, set) {
      // Adjust decoration positions to changes made by the transaction
      set = set.map(tr.mapping, tr.doc)
      // See if the transaction adds or removes any placeholders
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

This is a thin wrapper around a decoration set—it has to be a set because multiple uploads can be in progress at the same time. The meta property for the plugin can be used to add and remove widget decorations by ID.

The plugin comes with a function that returns the current position of the placeholder with the given ID, if it still exists.

```plain text
function findPlaceholder(state, id) {
  let decos = placeholderPlugin.getState(state)
  let found = decos.find(null, null, spec => spec.id == id)
  return found.length ? found[0].from : null
}

```

When the file input below the editor is used, this event handler checks some conditions, and fires off the upload when possible.

```plain text
document.querySelector("#image-upload").addEventListener("change", e => {
  if (view.state.selection.$from.parent.inlineContent && e.target.files.length)
    startImageUpload(view, e.target.files[0])
  view.focus()
})

```

The core functionality happens in startImageUpload. The utility uploadFile returns a promise that resolves to the uploaded file's URL (in the demo it actually just waits for a bit and then returns a data: URL).

```plain text
function startImageUpload(view, file) {
  // A fresh object to act as the ID for this upload
  let id = {}

  // Replace the selection with a placeholder
  let tr = view.state.tr
  if (!tr.selection.empty) tr.deleteSelection()
  tr.setMeta(placeholderPlugin, {add: {id, pos: tr.selection.from}})
  view.dispatch(tr)

  uploadFile(file).then(url => {
    let pos = findPlaceholder(view.state, id)
    // If the content around the placeholder has been deleted, drop
    // the image
    if (pos == null) return
    // Otherwise, insert it at the placeholder's position, and remove
    // the placeholder
    view.dispatch(view.state.tr
                  .replaceWith(pos, pos, schema.nodes.image.create({src: url}))
                  .setMeta(placeholderPlugin, {remove: {id}}))
  }, () => {
    // On failure, just clean up the placeholder
    view.dispatch(tr.setMeta(placeholderPlugin, {remove: {id}}))
  })
}

```

Because the placeholder plugin maps its decorations through transactions, findPlaceholder will get the accurate position of the image, even if the document was modified during the upload.


