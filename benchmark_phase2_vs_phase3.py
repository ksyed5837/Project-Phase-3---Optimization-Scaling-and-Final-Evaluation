
"""
benchmarks/benchmark_phase2_vs_phase3.py

This file fakes a simple "Phase 2" implementation using Python dicts and lists,
and compares it to the optimized data structures from Phase 3.

Run:
    python benchmarks/benchmark_phase2_vs_phase3.py
"""

import time
from src.optimized_hash_table import OptimizedHashTable
from src.avl_tree import AVLTree


def benchmark_hash_table(n=50000):
    # Phase 2 style: plain dictionary
    start = time.time()
    d = {}
    for i in range(n):
        d[f"product_{i}"] = i
    dict_insert = time.time() - start

    start = time.time()
    for i in range(n):
        _ = d.get(f"product_{i}")
    dict_lookup = time.time() - start

    # Phase 3: optimized hash table
    ht = OptimizedHashTable()
    start = time.time()
    for i in range(n):
        ht.insert(f"product_{i}", i)
    ht_insert = time.time() - start

    start = time.time()
    for i in range(n):
        _ = ht.get(f"product_{i}")
    ht_lookup = time.time() - start

    print(f"Phase 2 (dict) insert: {dict_insert:.4f}s, lookup: {dict_lookup:.4f}s")
    print(f"Phase 3 (OptimizedHashTable) insert: {ht_insert:.4f}s, lookup: {ht_lookup:.4f}s")


def benchmark_avl_vs_list(n=50000):
    # Phase 2 style: sorted list + linear search
    arr = []
    start = time.time()
    for i in range(n):
        arr.append(i)
    list_build = time.time() - start

    start = time.time()
    for i in range(n):
        _ = (i in arr)
    list_lookup = time.time() - start

    # Phase 3: AVL
    tree = AVLTree()
    start = time.time()
    for i in range(n):
        tree.insert(i, i)
    avl_build = time.time() - start

    start = time.time()
    for i in range(n):
        _ = tree.search(i)
    avl_lookup = time.time() - start

    print(f"Phase 2 (list) build: {list_build:.4f}s, lookup: {list_lookup:.4f}s")
    print(f"Phase 3 (AVLTree) build: {avl_build:.4f}s, lookup: {avl_lookup:.4f}s")


if __name__ == "__main__":
    print("=== Benchmark Hash Table ===")
    benchmark_hash_table()
    print("\n=== Benchmark AVL vs List ===")
    benchmark_avl_vs_list()
