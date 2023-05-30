import time


class HashTable:
    # Create empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)] # create a list of empty lists with a length of size

    def hash_function(self, key):
        #if isinstance(key, str):
            h = 0
            for char in key:
                h = (h * 31 + ord(char)) % self.size
            return h
        # else:
            # return key % self.size

    # Insert values into hash map
    def set_val(self, key, val):
        # Get the index from the key
        # using hash function
        hashed_key = self.hash_function(key) % self.size # so it is in valid range of bucket indexes
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            # check if the bucket has same key as the key to be inserted
            if record_key == key:
                found_key = True
                break
            # If the bucket has same key as the key to be inserted,
            # Update the key value
            # Otherwise append the new key-value pair to the bucket
        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))

    # Return searched value with specific key
    def get_val(self, key):
        # Get the index from the key using
        # hash function
        hashed_key = self.hash_function(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if the bucket has same key as
            # the key being searched
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
            if found_key:
                return record_val
            else:
                return "No record found"





