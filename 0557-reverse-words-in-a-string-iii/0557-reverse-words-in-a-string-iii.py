class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse_word(word):
            return word[::-1]

        words = s.split(' ')
        reversed_words = [reverse_word(word) for word in words]
        result = ' '.join(reversed_words)
        return result

# Example usage:
solution_instance = Solution()
input_str = "Let's take LeetCode contest"
output_str = solution_instance.reverseWords(input_str)
print(output_str)
