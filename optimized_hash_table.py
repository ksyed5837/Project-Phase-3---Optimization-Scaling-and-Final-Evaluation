
"""
optimized_hash_table.py

Phase 3: Optimized hash table implementation for a dynamic inventory / recommendation system.
Key features:
- Open addressing with quadratic probing
- Automatic resizing based on load factor
- Simple, readable API for beginners
"""

class HashTableEntry:
    __slots__ = ("key", "value", "is_active")

    def __init__(self, key, value):
        self.key = key
        self.value = value
        # is_active helps us handle deletions without breaking probing chains
        self.is_active = True


class OptimizedHashTable:
    def __init__(self, initial_capacity=8, load_factor_threshold=0.7):
        self.capacity = initial_capacity
        self.size = 0
        self.load_factor_threshold = load_factor_threshold
        self.table = [None] * self.capacity

    def _hash(self, key):
        # simple wrapper around Python's built-in hash function
        return hash(key) % self.capacity

    def _probe(self, index, step):
        # quadratic probing: index + step^2
        return (index + step * step) % self.capacity

    def _should_resize(self):
        return self.size / self.capacity >= self.load_factor_threshold

    def _resize(self):
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0  # will be recomputed as we insert

        for entry in old_table:
            if entry is not None and entry.is_active:
                self.insert(entry.key, entry.value)

    def insert(self, key, value):
        if self._should_resize():
            self._resize()

        index = self._hash(key)
        step = 1

        while True:
            entry = self.table[index]
            if entry is None or not entry.is_active:
                # Insert new entry
                self.table[index] = HashTableEntry(key, value)
                self.size += 1
                return
            elif entry.key == key:
                # Update existing
                entry.value = value
                return
            else:
                # Collision: keep probing
                index = self._probe(index, step)
                step += 1

    def get(self, key):
        index = self._hash(key)
        step = 1

        while True:
            entry = self.table[index]
            if entry is None:
                # Not found
                return None
            if entry.is_active and entry.key == key:
                return entry.value

            index = self._probe(index, step)
            step += 1
            if step > self.capacity:
                # safety break to avoid infinite loop
                return None

    def delete(self, key):
        index = self._hash(key)
        step = 1

        while True:
            entry = self.table[index]
            if entry is None:
                return False  # not found
            if entry.is_active and entry.key == key:
                entry.is_active = False
                self.size -= 1
                return True

            index = self._probe(index, step)
            step += 1
            if step > self.capacity:
                return False

    def __len__(self):
        return self.size

    def __contains__(self, key):
        return self.get(key) is not None
