class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.map = {}

    def insert(self, val):
        if val not in self.map:
            self.nums.append(val)
            self.map[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val):
        if val not in self.map:
            return False
        else:
            idx_of_val_to_remove = self.map[val]
            last = self.nums[-1]
            self.map[last] = idx_of_val_to_remove
            
            # Swap values at last index and index of value to remove
            self.swap(self.nums, idx_of_val_to_remove, len(self.nums)-1)
            self.nums.pop()
            del self.map[val]
            return True

    def getRandom(self):
        import random
        return self.nums[random.randint(0, len(self.nums)-1)]
    
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
