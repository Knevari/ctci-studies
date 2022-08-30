class Solution:
    def string_compression(self, s):
        compressed_str = ""
        char_count = 0

        for index in range(len(s)):
            char_count += 1
            if index + 1 < len(s) and s[index] != s[index + 1]:
                compressed_str += s[index] + str(char_count)
                char_count = 0

        compressed_str += s[index] + str(char_count)

        return min(s, compressed_str)


def main():
    solution = Solution()

    assert solution.string_compression("aabcccccaaa") == "a2b1c5a3",\
        "string_compression('aabcccccaaa') should return a2b1c5a3"

    print("All tests passed!")


if __name__ == "__main__":
    main()
