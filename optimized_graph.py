
"""
optimized_graph.py

Phase 3: Optimized product similarity graph.
Key ideas:
- Adjacency list representation
- Edge pruning based on similarity threshold to reduce memory
"""

class OptimizedGraph:
    def __init__(self, similarity_threshold=0.3):
        # adjacency list: product_id -> list of (neighbor_id, weight)
        self.adj_list = {}
        self.similarity_threshold = similarity_threshold

    def add_product(self, product_id):
        if product_id not in self.adj_list:
            self.adj_list[product_id] = []

    def add_similarity(self, product_a, product_b, weight):
        # prune low-similarity edges
        if weight < self.similarity_threshold:
            return

        self.add_product(product_a)
        self.add_product(product_b)

        self.adj_list[product_a].append((product_b, weight))
        self.adj_list[product_b].append((product_a, weight))

    def get_similar_products(self, product_id, top_k=5):
        """
        Returns up to top_k most similar products by weight.
        """
        neighbors = self.adj_list.get(product_id, [])
        # sort by weight descending
        neighbors_sorted = sorted(neighbors, key=lambda x: x[1], reverse=True)
        return neighbors_sorted[:top_k]

    def degree(self, product_id):
        return len(self.adj_list.get(product_id, []))

    def number_of_products(self):
        return len(self.adj_list)
