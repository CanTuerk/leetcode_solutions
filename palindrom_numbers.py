# https://leetcode.com/problems/palindrome-number/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        x_length = len(str_x)
        if x < 0:
            return False
        if x_length == 1:
            return True
        middle_index = x_length // 2
        left_half = str_x[:middle_index]
        right_half = str_x[middle_index + int(not (x_length % 2 == 0)) :][::-1]
        return left_half == right_half

    def anotherIsPalindrome(self, x: int) -> bool:
        x = str(x)
        return x[::-1] == x


if __name__ == "__main__":
    s = Solution()
    res = s.anotherIsPalindrome(12321)
    print(res)
