from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        merged_string = "".join("".join(chars) for chars in zip(*strs))
        list_length = len(strs)
        same_indices_count = 0
        for i in range(0, len(merged_string), list_length):
            check_str = merged_string[i : i + list_length]
            is_all_same = check_str.count(check_str[0]) == len(check_str)
            if is_all_same:
                same_indices_count += 1
            else:
                break
        return strs[0][:same_indices_count]

    def anotherLongestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res


if __name__ == "__main__":
    s = Solution()
    strs = ["flower", "flow", "flowigu"]
    # res = s.longestCommonPrefix(strs)
    another_res = s.anotherLongestCommonPrefix(strs)
    print(another_res)
