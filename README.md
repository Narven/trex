# trex

Rust-powered pytest collection. Run your tests the same way you always do — just faster.

**Beta / work in progress** — trex is still in early stages. It works for typical pytest layouts, but expect rough edges and changes as it evolves.

### What trex does

Pytest’s normal lifecycle is: **discover** which files might be tests, **collect** them (import modules, find test functions and classes), then **run** the tests. The discovery and collection steps are done in Python and can be slow on large trees.

Trex is a small Rust binary that does discovery and test-name extraction very quickly. The `conftest.py` that `trex init` creates plugs into pytest’s hooks: it runs trex once at the start, then **hijacks** which paths pytest collects (`pytest_ignore_collect`) and which items are kept and in what order (`pytest_collection_modifyitems`). Pytest still imports and runs your tests — it just no longer decides *which* files to look at or *in what order*; trex does. Same tests, same commands, faster collection.

---

## How to use (that’s it)

1. Have `trex` on your `PATH`, or set `TREX_BIN` to the path of the `trex` binary.
2. In your Python project directory, run:
   ```bash
   trex init
   ```
   When prompted, answer **y** to generate `conftest.py`.
3. Run pytest exactly as you already do:
   ```bash
   pytest
   # or
   uv run pytest
   # or
   pytest -v
   pytest tests/
   # etc.
   ```

No other workflow changes. No extra flags. You just get faster collection.

---

## Installation

Build the binary and make it available to your projects:

```bash
git clone https://github.com/narven/trex.git
cd trex
cargo build --release
```

Then either:

- Put `target/release/trex` on your `PATH`, or  
- Set `TREX_BIN` to the full path to `trex` when running pytest (e.g. in your shell or env).

---

## For more information

**`trex init`** — Run in a project directory. If there’s no `conftest.py`, it asks whether to create one. That conftest wires pytest to trex so collection is driven by the Rust binary.

**`trex collect`** — For special cases only (e.g. scripting or debugging). Discovers test files under a directory and prints a JSON manifest of test node IDs. You don’t need to run this yourself when using trex with pytest; the conftest does it for you.

```bash
trex collect .                              # current dir, default pattern test_*.py
trex collect /path/to/project --pattern "test_*.py"
```

> If the `trex` binary isn’t found or fails, pytest falls back to normal collection — your runs still work, just without the speedup.

---

## License

MIT. See [LICENSE](LICENSE).
