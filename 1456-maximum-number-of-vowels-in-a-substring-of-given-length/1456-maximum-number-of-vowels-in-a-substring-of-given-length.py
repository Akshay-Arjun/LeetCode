class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def count_vowels(substring):
            vowels = set("aeiou")
            return sum(1 for char in substring if char in vowels)

        max_vowels = current_vowels = count_vowels(s[:k])

        for i in range(k, len(s)):
            if s[i - k] in "aeiou":
                current_vowels -= 1
            if s[i] in "aeiou":
                current_vowels += 1
            max_vowels = max(max_vowels, current_vowels)

        return max_vowels