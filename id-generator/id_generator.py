import random
import string
import csv

pool_sizes = [500, 500, 500, 500, 500, 30000]
number_pools = []

for i in range(len(pool_sizes)):
	number_pools.append( random.sample(range(10000, 99999), pool_sizes[i]) )



seed_pools = []
initials = ['a', 'b', 'c', 'm', 's']

for i in range(len(initials)):
	pool = []

	for y in range( len(number_pools[i]) ):
		element = initials[i]
		element += ''.join(random.choices(string.ascii_lowercase, k=2))
		element += '_'
		element += str(number_pools[i][y])

		pool.append(element)

	seed_pools.append(pool)



augmented_pool = []
unwanted_chars = 'abcms'

for i in range(len(number_pools[5])):
	element = random.choice([s for s in string.ascii_lowercase if s not in unwanted_chars])
	element += ''.join(random.choices(string.ascii_lowercase, k=2))
	element += '_'
	element += str(number_pools[5][i])

	augmented_pool.append(element)



pools = seed_pools
pools.append(augmented_pool)

with open("ids.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(pools)
