
"""
tests/unit_tests.py

Basic unit tests for the optimized data structures.
Run:
    python -m tests.unit_tests
"""

import unittest

from src.optimized_hash_table import OptimizedHashTable
from src.optimized_graph import OptimizedGraph
from src.avl_tree import AVLTree


class TestOptimizedHashTable(unittest.TestCase):
    def test_insert_and_get(self):
        ht = OptimizedHashTable()
        ht.insert("apple", 10)
        ht.insert("banana", 20)
        self.assertEqual(ht.get("apple"), 10)
        self.assertEqual(ht.get("banana"), 20)
        self.assertIsNone(ht.get("missing"))

    def test_update_value(self):
        ht = OptimizedHashTable()
        ht.insert("apple", 10)
        ht.insert("apple", 99)
        self.assertEqual(ht.get("apple"), 99)

    def test_delete(self):
        ht = OptimizedHashTable()
        ht.insert("apple", 10)
        self.assertTrue(ht.delete("apple"))
        self.assertIsNone(ht.get("apple"))
        self.assertFalse(ht.delete("apple"))


class TestOptimizedGraph(unittest.TestCase):
    def test_add_and_get_similar(self):
        g = OptimizedGraph(similarity_threshold=0.3)
        g.add_similarity("p1", "p2", 0.5)
        g.add_similarity("p1", "p3", 0.2)  # pruned
        similar = g.get_similar_products("p1")
        self.assertEqual(len(similar), 1)
        self.assertEqual(similar[0][0], "p2")


class TestAVLTree(unittest.TestCase):
    def test_insert_and_search(self):
        tree = AVLTree()
        keys = [10, 20, 5, 4, 15]
        for k in keys:
            tree.insert(k, str(k))
        self.assertEqual(tree.search(10), "10")
        self.assertEqual(tree.search(15), "15")
        self.assertIsNone(tree.search(100))

    def test_delete(self):
        tree = AVLTree()
        keys = [10, 20, 5, 4, 15]
        for k in keys:
            tree.insert(k, str(k))
        tree.delete(10)
        self.assertIsNone(tree.search(10))
        self.assertIsNotNone(tree.search(20))


if __name__ == "__main__":
    unittest.main()
