# AI Practical Solutions

Foundation of Artificial Intelligence and Machine Learning

Course:
CS-321-VSC-P

University:
Savitribai Phule Pune University (T.Y.B.Sc. Computer Science SEM-V)

Language:
Python

## Repository Purpose

This repository contains complete, verified, standalone Python solutions for the university practical examination question bank across all 14 examination slips.

All solutions are organized by **PROGRAM TOPIC / QUESTION CONCEPT** rather than slip number. This design allows instantaneous lookup during a practical examination even when an exam slip contains no slip number.

## Project Structure

```
AI/
├── bfs-monkey-banana/
│   ├── solution.py
│   └── question.txt
├── astar-shortest-path/
│   ├── solution.py
│   └── question.txt
├── map-coloring-csp/
│   ├── solution.py
│   └── question.txt
├── bfs-water-jug/
│   ├── solution.py
│   └── question.txt
├── backtracking-csp/
│   ├── solution.py
│   └── question.txt
├── game-tree/
│   ├── solution.py
│   └── question.txt
├── bfs-graph/
│   ├── solution.py
│   └── question.txt
├── alpha-beta-pruning/
│   ├── solution.py
│   └── question.txt
├── propositional-logic/
│   ├── solution.py
│   └── question.txt
├── state-space-bfs/
│   ├── solution.py
│   └── question.txt
├── predicate-logic/
│   ├── solution.py
│   └── question.txt
├── gaussian-naive-bayes/
│   ├── solution.py
│   └── question.txt
├── tic-tac-toe-minimax/
│   ├── solution.py
│   └── question.txt
├── four-puzzle-astar/
│   ├── solution.py
│   └── question.txt
├── minimax-alpha-beta-comparison/
│   ├── solution.py
│   └── question.txt
├── rule-based-expert-system/
│   ├── solution.py
│   └── question.txt
├── hill-climbing/
│   ├── solution.py
│   └── question.txt
├── forward-chaining/
│   ├── solution.py
│   └── question.txt
├── decision-tree-classifier/
│   ├── solution.py
│   └── question.txt
├── backward-chaining/
│   ├── solution.py
│   └── question.txt
├── random-forest-classifier/
│   ├── solution.py
│   └── question.txt
├── dfs-state-space/
│   ├── solution.py
│   └── question.txt
├── clustering-objective-functions/
│   ├── solution.py
│   └── question.txt
├── knowledge-base/
│   ├── solution.py
│   └── question.txt
├── depth-limited-search/
│   ├── solution.py
│   └── question.txt
├── kmeans-clustering/
│   ├── solution.py
│   └── question.txt
├── best-first-search/
│   ├── solution.py
│   └── question.txt
├── euclidean-distance/
│   ├── solution.py
│   └── question.txt
├── tower-of-hanoi/
│   ├── solution.py
│   └── question.txt
├── n-queens/
│   ├── solution.py
│   └── question.txt
├── supervised-vs-unsupervised/
│   ├── solution.py
│   └── question.txt
├── ao-star/
│   ├── solution.py
│   └── question.txt
├── minimax/
│   ├── solution.py
│   └── question.txt
├── search.py
├── verify_all.py
├── upload_repository.py
├── QUESTION_INDEX.md
└── README.md
```

## How Questions Are Organized

- Every unique problem from the examination slips has its own descriptive folder.
- Substantially different problems have separate folders (e.g., `astar-shortest-path` vs `four-puzzle-astar`).
- Identical questions occurring across multiple slips share a single canonical folder, with all slip occurrences listed in `question.txt`.
- OR questions are given separate unique folders as distinct solutions.

## How Duplicate Questions Are Handled

When the exact same question appears on multiple slips, only one solution folder is created to prevent unnecessary code duplication. The `question.txt` preserves all occurrences across the examination paper.

Example:
- `map-coloring-csp` appears in Slip 1, Slip 5, and Slip 13.
- `minimax-alpha-beta-comparison` appears in Slip 6 and Slip 8.
- `rule-based-expert-system` appears in Slip 6 and Slip 12.
- `forward-chaining` appears in Slip 7 and Slip 14.
- `backward-chaining` appears in Slip 8 and Slip 10.
- `hill-climbing` appears in Slip 7 and Slip 13.

## Zero Comments Rule

In strict accordance with examination requirements, all Python source files (`solution.py`, `search.py`, `verify_all.py`, `upload_repository.py`) contain **zero comments** (`#`).

## Searching for Questions

### Using Python Search Script

```bash
python search.py "Map Coloring"
python search.py "A* Search"
python search.py "Water Jug"
python search.py "N-Queens"
python search.py "Minimax"
python search.py "Alpha-Beta"
python search.py "Gaussian"
```

### Using Linux find

```bash
find . -iname "*astar*"
find . -iname "*water*jug*"
find . -iname "*nqueens*"
find . -iname "*minimax*"
```

### Using grep

```bash
grep -Rni "Map Coloring" .
grep -Rni "Constraint Satisfaction" .
grep -Rni "Alpha-Beta" .
grep -Rni "Gaussian" .
grep -Rni "Tower of Hanoi" .
```

## Verification

Run the verification test suite to validate all 33 programs:

```bash
python verify_all.py
```

Expected output:
```
========================================
AI PRACTICAL VERIFICATION
========================================
Total program folders checked: 33
Total source files checked: 33
Total question files checked: 33

Syntax validation: PASS
Comment validation: PASS
Empty-file validation: PASS
Question mapping: PASS
Duplicate handling: PASS

ALL FILES PASSED VERIFICATION!
```

## GitHub Automation

To upload this repository to GitHub:

```bash
python upload_repository.py YOUR_GITHUB_TOKEN
```

Or set the environment variable:
```bash
export GITHUB_TOKEN="your_token"
python upload_repository.py
```

## How to Clone

```bash
git clone https://github.com/YOUR_USERNAME/AI.git
cd AI
python search.py "A* Search"
```
