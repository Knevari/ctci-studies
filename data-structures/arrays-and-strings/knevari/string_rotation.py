# function given by problem
def is_substring(s1, s2):
    return s1 in s2


class Solution:
    def string_rotation(self, s1, s2):
        return is_substring(s1, s2 + s2)


def main():
    solution = Solution()

    assert solution.string_rotation(
        "waterbottle", "erbottlewat"), "string_rotation('waterbottle', 'erbottlewat') should return True"

    print("All tests passed!")


if __name__ == "__main__":
    main()
