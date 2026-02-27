# trex

Rust-powered [pytest](https://pytest.org/) collection: drive test discovery and ordering from a fast native binary.

## Features

- **`trex collect`** — Recursively discovers Python test files, parses them with regex (no Python runtime), and outputs a JSON manifest of test node IDs.
- **`trex init`** — In a directory without `conftest.py`, prompts to generate one so you can use trex with pytest immediately.
- **Pytest integration** — Drop a `conftest.py` into your project; it calls `trex collect` and uses the result to:
  - Restrict which files pytest collects (`pytest_ignore_collect`).
  - Filter and reorder test items (`pytest_collection_modifyitems`).
- **Single subprocess per run** — Trex is invoked once in `pytest_configure`; the manifest is cached and reused.
- **Graceful fallback** — If the `trex` binary is missing or fails, pytest runs with default collection.

## Installation

### Build from source

```bash
git clone https://github.com/narven/trex.git
cd trex
cargo build --release
```

The binary is at `target/release/trex`.

### Use with pytest (UV project)

1. Copy or symlink `trex` to a path on your `PATH`, or set `TREX_BIN` to the full path.
2. Add a `conftest.py` in your project root — run `trex init` in the project dir and answer `y` when prompted, or copy from [examples/example1/conftest.py](examples/example1/conftest.py).
3. Ensure your test root is passed as the first argument when the plugin runs `trex collect <rootdir>`.

## Usage

### CLI

```bash
# Generate conftest.py in the current dir (prompts if not present)
trex init

# Generate in a specific directory
trex init /path/to/project

# Discover tests under the current directory (default pattern: test_*.py)
trex collect .

# Custom glob pattern
trex collect /path/to/project --pattern "test_*.py"
```

Output is a JSON array to stdout, one entry per test file:

```json
[
  {
    "file": "tests/test_foo.py",
    "tests": ["TestBar::test_baz", "test_quux"]
  }
]
```

### Pytest

From your project root (e.g. `examples/example1`):

```bash
uv run pytest -v
```

With trex available, collection is driven by the manifest; without it, pytest falls back to normal collection.

Set `TREX_BIN` to the path of the `trex` binary if it is not at the default relative path (`../../target/release/trex` from the conftest directory).

## Requirements

- Rust 1.70+ (to build trex).
- Python 3.x and pytest (for the plugin).
- Test files following usual pytest conventions: `test_*.py` / `*_test.py`, `Test*` classes, `test_*` functions.

## Development

```bash
cargo build
cargo test
```

Run the example pytest suite:

```bash
cd examples/example1
cargo build --release   # from repo root if needed
uv run pytest -v
```

## License

MIT. See [LICENSE](LICENSE).
