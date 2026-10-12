# Advent of Code Repository Conventions

This document outlines the naming conventions, code standards, and structure used across all years' solutions in this repository.

## Directory Structure

### Top-level Organization

```
AdventOfCode/
├── AdventOfCode2022/  (25 days)
├── AdventOfCode2023/  (25 days)
├── AdventOfCode2024/  (25 days)
├── AdventOfCode2025/  (12 days)
├── check_answers.py        # hash-based answer-verification harness
├── benchmark.py            # median-of-N timing + hash-verify -> BENCHMARK.md + docs/benchmarks.json
├── hash_answers.py         # regenerate answer_hashes.json from answers_clear.json
├── fetch_answers.py        # fetch accepted answers from adventofcode.com
├── answer_hashes.json      # committed SHA-256 hashes of accepted answers
├── answers_clear.json      # plaintext answers (gitignored)
├── BENCHMARK.md            # generated timing report (answer-free)
├── encrypt_inputs.sh       # age-encrypt every year's input.txt
├── decrypt_inputs.sh       # age-decrypt every year's input.txt.age
├── requirements.txt        # runtime deps (numpy, Pillow, xxhash, sympy, matplotlib)
├── requirements-dev.txt    # lint/type deps (ruff, mypy, radon)
├── pyproject.toml
├── LICENSE
├── .github/
│   ├── workflows/aoc.yml       # benchmark + deploy GitHub Pages
│   ├── workflows/lint.yml      # ruff + mypy + radon quality gate
│   ├── age-public-key.txt      # age recipient (safe to commit)
│   └── scripts/build_site.py   # renders docs/index.html from benchmarks.json
└── CONVENTION.md
```

### Day Directory Naming

**Canonical format**: `day_NN` (underscore + zero-padded two digits) — consistent across all years.

- **2022**: `day_01` through `day_25`
- **2023**: `day_01` through `day_25`
- **2024**: `day_01` through `day_25`
- **2025**: `day_01` through `day_12`

## Solution File Naming

Each day directory contains **solution files** with one of two naming conventions:

### Primary Solution Files (Canonical Names)

Files that implement the actual AoC puzzle solutions and are executed by CI/CD:

**Canonical format**: `part_one.py` (Part 1) + `part_two.py` (Part 2) — consistent across all years.

- **2022**: `part_one.py` + `part_two.py`
- **2023**: `part_one.py` + `part_two.py` (some days have only Part 1)
- **2024**: `part_one.py` + `part_two.py` + `shared.py` (day 25 is Part 1 only)
- **2025**: `part_one.py` + `part_two.py` (+ `run.py` wrapper on some days; day 12, the final day, is Part 1 only)

These files are discovered and executed by `check_answers.py` and `benchmark.py`, which iterate the day/part keys recorded in `answer_hashes.json`.

### Helper/Test/Experiment Files (Prefixed with `_`)

Files that are **not** primary solutions. These include:

- Alternative/optimized implementations: `_second_star_numba.py`, `_second_star_bis.py`
- Debugging scripts: `_debug.py`, `_fs.py`
- Benchmark utilities: `_benchmark.py`
- Test helpers: `_test.py`
- Experimental attempts: `_first_stark.py`, `_first_stard.py`
- Exploratory code: `_control.py`, `_comp.py`
- Stolen/reference solutions: `_not_mine.py`
- Data analysis: `_plot_tiles.py`

**Convention**: Files starting with `_` are excluded from ruff, ruff-format, and mypy, and are not executed by CI/CD. Use this prefix to mark code as secondary/helper.

## Code Quality Standards

### Linting: Ruff

All **primary solution files** (without `_` prefix) must pass ruff checks.

**Configuration** (see `pyproject.toml`):

- Line length: 88
- Target Python: 3.14
- Enabled rules: `E`, `W`, `F`, `I`, `B`, `N`, `S`, `UP`, `RUF`
  (errors, warnings, pyflakes, isort, bugbear, naming, security, pyupgrade, ruff)
- `N` (naming) and `S` (security) are enforced on the **shared tooling only**;
  puzzle directories are exempted via per-file-ignores, since solutions use
  math-style names and `eval`/`assert` on trusted fixed inputs.
- Excluded rules:
  - `E501`: Line too long (ruff-format handles wrapping)
  - `B007`: Unused loop variable (common in AoC enumerate patterns)
  - `B023`: Function uses loop variable (intentional AoC pattern)
  - `B904`, `B905`, `B912`: `raise from` / `zip`/`map` `strict=` ceremony, unneeded for AoC
  - `UP007`: `X | Y` union rewrite (leave existing annotations)
  - `RUF012`, `RUF015`, `RUF059`: minor micro-style rules

**Helper files** (prefixed with `_`) are excluded from ruff entirely.

### Formatting: Ruff-format

Ruff-format (black-compatible) is the canonical formatter. All **primary
solution files** must pass `ruff format . --check`. (A legacy `[tool.black]`
section remains for compatibility, but ruff-format is authoritative.)

**Configuration** (see `pyproject.toml`):

- Line length: 88
- Target version: Python 3.14
- Quote style: double quotes
- Indent style: space

### Type Checking: mypy

The **shared tooling** (root `*.py` and `.github/scripts/`) is type-checked with
`mypy .`. Puzzle solution directories and `_`-prefixed files are excluded, since
solutions are untyped and reuse module names (`part_one`/`part_two`/`shared`)
across day folders.

### Maintainability: radon

`radon mi .` reports a maintainability-index grade per module (informational).

### Encryption: Puzzle Inputs

All puzzle inputs are stored encrypted using **age**:

- **Plaintext file**: `input.txt` (excluded by `.gitignore`)
- **Encrypted file**: `input.txt.age` (committed to repository)
- **Public key**: Stored in `.github/age-public-key.txt` (safe to commit)
- **Private key**: Stored as GitHub Actions Secret `AGE_SECRET_KEY` (decrypted at runtime)

The public recipient lives in `.github/age-public-key.txt` (committed). The
private key is **never committed** — keep it locally as `age-key.txt`
(gitignored) and mirror it to the GitHub Actions secret `AGE_SECRET_KEY`.

Encrypt every year's inputs (reads the public key above):

```bash
./encrypt_inputs.sh
```

Decrypt every year's inputs locally (requires the private key):

```bash
./decrypt_inputs.sh
```

Rotate to a fresh key pair — regenerates the key, updates
`.github/age-public-key.txt`, re-encrypts all years, and prints the new private
key to store as `AGE_SECRET_KEY`:

```bash
./encrypt_inputs.sh --new-key
```

## Solution File Execution

Solutions are discovered and executed by `check_answers.py` (verification) and
`benchmark.py` (timing), both driven by the keys in `answer_hashes.json`:

1. Iterate the year names recorded in `answer_hashes.json`
   (`AdventOfCode2022` .. `AdventOfCode2025`)
2. For each `day_NN` key, resolve the matching day directory
3. For each `part_one` / `part_two` key, import `part_one.py` / `part_two.py`
   and call `main()` (or `solve_partN()`) — the **returned** value is the answer

Recording an answer in `answer_hashes.json` is all it takes to include a new
day or part; nothing is hard-coded. Each solution runs with `cwd=day_dir`, so
input paths are relative to the day directory (e.g. `"input.txt"`). A 30s
per-solution budget is enforced, and files starting with `_` are never executed.

## Input File Structure

Each day directory contains:

```
AdventOfCodeXXXX/day_NN/
├── part_one.py
├── part_two.py
├── input.txt.age (encrypted)
├── _helper.py (optional, not executed)
└── _test.py (optional, not executed)
```

## CI/CD and GitHub Pages

Python **3.14** is used across both workflows.

### Workflow: `.github/workflows/aoc.yml` (benchmark + deploy)

1. Installs runtime deps via `pip install -r requirements.txt`
2. Installs `age` from the Ubuntu repos (`apt-get install -y age`)
3. Decrypts all `input.txt.age` files using the `AGE_SECRET_KEY` secret
4. Benchmarks every solution (median of 5 runs, `BENCH_RUNS: "5"`) and writes
   `docs/benchmarks.json` — timings and hash-verification status only, **no answers**
5. Builds the static site (`build_site.py`) from that JSON and deploys `docs/`
   to GitHub Pages

### Workflow: `.github/workflows/lint.yml` (quality gate)

Runs on pushes to `main` and on pull requests. Installs `requirements-dev.txt`,
then runs the full gate: `radon mi . && ruff check . && ruff format . --check && mypy .`.

### Build Scripts

- **`benchmark.py`**: Benchmarks solutions (median of N runs) and emits
  `BENCHMARK.md` + `docs/benchmarks.json` (timings and status, never answers)
- **`.github/scripts/build_site.py`**: Renders `docs/index.html` — an AoC-themed,
  times-only page — from `docs/benchmarks.json`

## Linting & Formatting Workflow

### Local Development

All commands run from the repo root against the whole tree (the venv provides
`ruff`, `mypy`, and `radon`):

```bash
# Auto-fix lint + format
ruff check . --fix
ruff format .

# Verify the full gate (what lint.yml runs)
radon mi . && ruff check . && ruff format . --check && mypy .
```

### Answer Verification

```bash
# Hash-verify every recorded solution (30s budget per solution)
python3 check_answers.py           # or: python3 check_answers.py 2024

# Regenerate answer_hashes.json after editing answers_clear.json
python3 hash_answers.py
```

### Benchmarking

```bash
# Time every solution (median of 5 runs) -> BENCHMARK.md + docs/benchmarks.json
python3 benchmark.py               # or: python3 benchmark.py 2024
BENCH_RUNS=3 python3 benchmark.py  # override runs per part
```

Answers are hash-verified while benchmarking but **never** written to the report
or the JSON — only timings and pass/fail status are published.

### CI/CD

All checks are verified in GitHub Actions (`lint.yml`):

- `radon mi .` — maintainability index (informational)
- `ruff check .` — linting
- `ruff format . --check` — formatting
- `mypy .` — type-checking of shared tooling

## Normalization Rules

### File Naming

1. **Primary solutions**: `part_one.py` and `part_two.py` only (+ `run.py` wrapper if needed)
2. **Helpers/Tests/Experiments**: Prefix with `_` and use descriptive names
3. **No mixed patterns**: Don't use `_` in primary solution filenames or omit it for helpers

### Code Standards

1. **Linting**: All primary files must pass `ruff check .`
2. **Formatting**: All primary files must pass `ruff format . --check`
3. **Imports**: Organized by isort (enabled via ruff `I` rule)
4. **Dead code**: Remove unused variables; use `# noqa: RULE` only for intentional patterns

### Directory Conventions

1. Keep each day's files together in a single directory
2. Place only solution and input files at the top level; move helpers/tests to subdirectories or prefix with `_`
3. Maintain consistent zero-padding in day numbering within a year

## Future Enhancements

- [x] Standardize directory naming across all years to `day_NN`
- [x] Standardize solution file naming to `part_one.py` / `part_two.py`
- [x] Add timing benchmarks (`benchmark.py` -> `BENCHMARK.md` + `docs/benchmarks.json`, median of 5)
- [x] Add answer verification + quality gate (`check_answers.py`, `lint.yml`)
- [ ] Create a helper library for common AoC utilities (parsing, grid traversal, etc.)
- [ ] Generate leaderboard/progress tracker in GitHub Pages

---

**Last Updated**: 2026-10-12  
**Maintainer**: Automated Code Quality System
