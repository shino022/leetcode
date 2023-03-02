"""
The algorithm aims to find the number of distinct subsequences of string s that match string t. It uses a dynamic programming approach to solve the problem.

The algorithm iterates through s and t using two indices i and j, respectively. At each iteration, there are two cases to consider:

  1. If s[i] is equal to t[j], there are two sub-cases:
    a. We can include s[i] in the subsequence and move to the next character in both s and t.
    b. We can exclude s[i] from the subsequence and only move to the next character in s. However, we also need to check if there is a potential match between s[i+1:] and t[j:] by deleting s[i].
    We cache the sum of the returned values from both sub-cases.

  2. If s[i] is not equal to t[j], we can only exclude s[i] from the subsequence and move to the next character in s. We cache the returned value

The base cases are:

1. If t[j] is empty, it is always possible to make the subsequence out of s. Therefore, the function returns 1 since we found a subsequence.
2. If t[j] is not empty and s[i] is empty, we cannot form a subsequence by deleting characters from an empty string. Therefore, the function returns 0.
3. If (i, j) has already been computed, we return the cached value to avoid redundant computation.

The function dfs is a recursive function that takes two indices i and j as input and returns the number of distinct subsequences of s[i:] that match t[j:]. The function numDistinct is the entry point of the algorithm and returns the result of calling dfs with i=0 and j=0. The memoization table dp is used to cache the results of the subproblems to avoid redundant computation.
"""