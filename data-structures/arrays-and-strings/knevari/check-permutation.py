# author: Knevari
# 25/02/2022 18:26

class Solution:
    def check_permutation(self, s1: str, s2: str) -> bool:
        # Check if both strings have the same length
        if len(s1) != len(s2):
            return False

        s1_character_count = {}

        for char in s1:
            if not char in s1_character_count:
                s1_character_count[char] = 0
            s1_character_count[char] += 1

        for char in s2:
            if not char in s1_character_count:
                return False

            s1_character_count[char] -= 1

            if s1_character_count[char] < 0:
                return False

        return True


def main():
    solution = Solution()

    assert solution.check_permutation("abc", "bca") == True, \
        "check_permutation('abc', 'bca') should return True"

    print("All tests passed!")


if __name__ == "__main__":
    main()
