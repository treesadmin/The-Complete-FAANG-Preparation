
# Contributed by Paraj Shah
# https://github.com/parajshah

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    count = sum(i <= 0 for i in a)
    if count < k:
        return "YES"
    return "NO"
if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        t = int(input())

        for _ in range(t):
            nk = input().split()

            n = int(nk[0])

            k = int(nk[1])

            a = list(map(int, input().rstrip().split()))

            result = angryProfessor(k, a)

            fptr.write(result + '\n')
