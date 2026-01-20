# PyPy as a CPython Replacement

PyPy is an alternative Python interpreter that aims to be a drop-in CPython replacement while being faster.

## Key Takeaways

- PyPy has matured to the point where it "just works" for most packages
- When using pipx with PyPy as the default interpreter, even complex packages (like cloud provider CLIs) run without issues
- Significant packages are now routinely tested under PyPy and handle differences like deferred garbage collection

## Potential Gotchas

- Deferred garbage collection can affect code that relies on immediate cleanup (e.g., files not being closed immediately)
- Using `with` statements avoids this by explicitly closing resources
- Some code may still have issues, but it's increasingly rare

## Use Case

Works well as a pipx backend for installing Python CLI tools - provides potential performance benefits without compatibility headaches.

## Source

- https://utcc.utoronto.ca/~cks/space/blog/python/PyPyQuietlyWorking (May 2024)
