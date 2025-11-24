
"""
tests/stress_tests.py

Very simple "stress style" tests to exercise data structures with larger sizes.
This is not a formal benchmark, but it gives you something to talk about in the report.
Run:
    python tests/stress_tests.py
"""

import time
from src.optimized_hash_table import OptimizedHashTable
from src.optimized_graph import OptimizedGraph
from src.avl_tree import AVLTree


def stress_hash_table(n=100000):
    ht = OptimizedHashTable()
    start = time.time()
    for i in range(n):
        ht.insert(f"product_{i}", i)
    insert_time = time.time() - start

    start = time.time()
    for i in range(n):
        _ = ht.get(f"product_{i}")
    lookup_time = time.time() - start

    print(f"[HashTable] Inserted {n} items in {insert_time:.4f} seconds.")
    print(f"[HashTable] Looked up {n} items in {lookup_time:.4f} seconds.")


def stress_graph(n=5000, edges_per_node=10):
    g = OptimizedGraph(similarity_threshold=0.3)
    start = time.time()
    for i in range(n):
        g.add_product(f"p{i}")
    # add edges
    for i in range(n):
        for j in range(1, edges_per_node + 1):
            neighbor = f"p{(i + j) % n}"
            g.add_similarity(f"p{i}", neighbor, 0.5)
    build_time = time.time() - start

    # sample traversal
    start = time.time()
    for i in range(0, n, max(1, n // 100)):
        _ = g.get_similar_products(f"p{i}", top_k=5)
    traverse_time = time.time() - start

    print(f"[Graph] Built graph with {n} nodes in {build_time:.4f} seconds.")
    print(f"[Graph] Sampled neighbors for ~100 nodes in {traverse_time:.4f} seconds.")


def stress_avl_tree(n=100000):
    tree = AVLTree()
    start = time.time()
    for i in range(n):
        tree.insert(i, i)
    insert_time = time.time() - start

    start = time.time()
    for i in range(n):
        _ = tree.search(i)
    lookup_time = time.time() - start

    print(f"[AVLTree] Inserted {n} keys in {insert_time:.4f} seconds.")
    print(f"[AVLTree] Looked up {n} keys in {lookup_time:.4f} seconds.")


if __name__ == "__main__":
    stress_hash_table(50000)
    print("-" * 40)
    stress_graph(2000, edges_per_node=5)
    print("-" * 40)
    stress_avl_tree(50000)
