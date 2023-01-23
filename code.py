from itertools import combinations #if the input iterable is sorted, the combination tuples will be produced in sorted order

N = int(input())
L = input().split()
K = int(input())

C = list(combinations(L, K))
F = filter(lambda c: 'a' in c, C) #takes fun and list 
print("{0:.3}".format(len(list(F))/len(C)))


'''
input consists of three lines. The first line contains the integer, denoting the length of the list. The next line consists of space-separated lowercase English letters,
 denoting the elements of the list.
The third and the last line of input contains the integer, denoting the number of indices to be selected.

Output Format
Output a single line consisting of the probability that at least one of the indices selected contains the letter:''.

Note: The answer must be correct up to 3 decimal places.
'''
