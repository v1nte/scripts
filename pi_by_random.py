from math import random
import sys
def estimate_pi(n):
    """Estimate pi by using random numbers"""
    num_in_circle = 0
    num_total = 0
    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)

        distance = x*x + y*y
        if distance <= 1:
            num_in_circle += 1
        num_total += 1

    return 4*num_in_circle/num_total

estimate_pi(sys.argv[1])
