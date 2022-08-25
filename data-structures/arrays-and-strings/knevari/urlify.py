# author: Knevari
# 25/02/2022 18:43

class Solution:
    def urlify(self, text: list[str], true_length: int):
        # Count number of spaces
        n_spaces = 0

        for i in range(true_length):
            char = text[i]
            if char == " ":
                n_spaces += 1

        index = true_length - 1
        offset_index = true_length + n_spaces * 2 - 1

        while index > 0 and n_spaces > 0:
            if text[index] == " ":
                text[offset_index] = "0"
                text[offset_index-1] = "2"
                text[offset_index-2] = "%"
                n_spaces -= 1
                offset_index -= 3
            else:
                text[offset_index] = text[index]
                offset_index -= 1

            index -= 1

        return text


def main():
    solution = Solution()

    assert solution.urlify(list("Mr John Smith    "), 13) == list("Mr%20John%20Smith"), \
        "urlify('Mr John Smith    ', 13) should return 'Mr%20John%20Smith'"

    print("All tests passed!")


if __name__ == "__main__":
    main()
