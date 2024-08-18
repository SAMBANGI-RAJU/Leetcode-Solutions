class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_word = []
        i = 0
        j = 0
        n = len(word1)
        m = len(word2)

        # Iterate over both strings until the end of one is reached
        while i < n and j < m:
            merged_word.append(word1[i])
            merged_word.append(word2[j])
            i += 1
            j += 1

        # Append the remaining characters from word1, if any
        if i < n:
            merged_word.append(word1[i:])

        # Append the remaining characters from word2, if any
        if j < m:
            merged_word.append(word2[j:])

        return ''.join(merged_word)