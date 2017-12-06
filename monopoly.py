"""
import random
dicecnt=0

monopoly_cnt = []
for x in range(40):
    monopoly_cnt.insert(x, 0)

while(1):
    random.randrange(1,7)
# http://codingdojang.com/scode/550  # answer-filter-area
"""

for x in range(0, 26):
    value=((25-x)**2+100)**0.5+((x**2+100)**0.5)/2
    print("%s %s" %(x, value))


