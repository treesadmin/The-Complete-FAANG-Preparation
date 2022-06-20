
# Contributed by Paraj Shah
# https://github.com/parajshah

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marcsCakewalk' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY calorie as parameter.
#

def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    return sum(2**i * calorie[i] for i in range(len(calorie)))
    

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        n = int(input().strip())

        calorie = list(map(int, input().rstrip().split()))

        result = marcsCakewalk(calorie)

        fptr.write(str(result) + '\n')
