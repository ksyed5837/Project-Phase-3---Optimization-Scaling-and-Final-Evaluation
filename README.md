
# Project Phase 3 - Optimization, Scaling, and Final Evaluation

This folder contains the **code deliverables** for Phase 3 of the project.

## Structure

- `src/optimized_hash_table.py`  
  Optimized hash table using:
  - Open addressing with quadratic probing
  - Dynamic resizing based on load factor
  - Simple `insert`, `get`, and `delete` methods

- `src/optimized_graph.py`  
  Optimized similarity graph:
  - Adjacency list representation
  - Pruning of low-similarity edges

- `src/avl_tree.py`  
  Balanced AVL tree for fast `insert`, `search`, `delete` operations.

- `tests/unit_tests.py`  
  Basic unit tests for the data structures.

- `tests/stress_tests.py`  
  Simple stress tests to simulate larger datasets and show performance.

- `benchmarks/benchmark_phase2_vs_phase3.py`  
  Small benchmark comparing a naive Phase 2-style approach to the optimized Phase 3 structures.

## How to Run

From the folder that contains this project:

```bash
# Run unit tests
python -m tests.unit_tests

# Run stress tests
python tests/stress_tests.py

# Run simple benchmarks
python benchmarks/benchmark_phase2_vs_phase3.py
```


