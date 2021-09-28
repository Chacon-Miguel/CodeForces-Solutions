"""
TIME LIMIT PER TEST:    3 seconds
MEMORY LIMIT PER TEST:  256 megabytes
INPUT:                  standard input
OUTPUT:                 standard output
"Contestant who earns a score equal to or greater than the k-th place finisher's score will advance to the next 
round, as long as the contestant earns a positive score..." — an excerpt from contest rules.
A total of n participants took part in the contest (n ≥ k), and you already know their scores. 
Calculate how many participants will advance to the next round.
INPUT
    The first line of the input contains two integers n and k (1 ≤ k ≤ n ≤ 50) separated by a single space.
    The second line contains n space-separated integers a1, a2, ..., an (0 ≤ ai ≤ 100), where ai is the score 
    earned by the participant who got the i-th place. The given sequence is non-increasing (that is, for all i 
    from 1 to n - 1 the following condition is fulfilled: ai ≥ ai + 1).
OUTPUT
    Output the number of participants who advance to the next round.
"""

n, k = [int(a) for a in input().split()]
scores = [int(a) for a in input().split()]
accum = 0
for score in scores[:n]:
    if score >= scores[k-1] and score > 0:
        accum += 1
print(accum)