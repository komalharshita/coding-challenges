import math
import os
import random
import re
import sys

def weightedMean(X, W):
        weighted_sum = 0
        weight = 0
        
        for i in range (len(X)):
                weighted_sum += X[i] * W[i]
                weight += W[i]
                        
        mean = weighted_sum / weight
        print(f"{mean:.1f}")

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
