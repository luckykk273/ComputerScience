from random import randint


# Create randomized, unsorted arrays
def create_array(size=10, max_=100):
    return [randint(0, max_) for _ in range(size)]
