# itertools.permutations() generates permutations 
# for an iterable. Time to brute-force those passwords ;-)

import itertools
for p in itertools.permutations('ABCD'):
   print(p)
