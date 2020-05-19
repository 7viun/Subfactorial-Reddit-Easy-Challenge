
import sys
from math import *
import itertools



def derangement(n):
	if n == 0:
		return 1
	if n == 1:
		return 0
	return (n-1) * (derangement(n - 1) + derangement(n - 2))
result=[]
def main(n):
	for i in range(n):
		a=derangement(i)
		result.append(a)

b=int(input("enter something here:\n"))

main(b)
c=len(result)
print(c)