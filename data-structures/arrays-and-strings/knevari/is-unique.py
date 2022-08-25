# author: Knevari
# 25/02/2022 13:43

class Solution:
    def is_unique(self, text: str):
        if text == "":
            return True

        character_count = {}

        for char in text:
            if char in character_count:
                return False

            character_count[char] = True

        return True


def main():
    solution = Solution()

    assert solution.is_unique("abcdefg") == True,\
        "is_unique('abcdefg') should be True"

    assert solution.is_unique("fffffff") == False,\
        "is_unique('fffffff') should be False"

    assert solution.is_unique("") == True,\
        "is_unique('') should be True"

    print("All tests passed!")


if __name__ == "__main__":
    main()
