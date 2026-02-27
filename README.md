# trex

Rust-powered pytest collection. Run your tests the same way you always do — just faster.

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
