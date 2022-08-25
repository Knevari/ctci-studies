# author: Knevari
# 25/02/2022 13:43

from helpers.python.Buzz import Buzz


class Solution:
    def __init__(self, testcases=[]):
        self.testcases = testcases

    def is_unique(self, text: str):
        if text == "":
            return True

        text_characters = {}

        for char in text:
            if char in text_characters:
                return False

            text_characters[char] = True

        return True


def main():
    solution = Solution([("abcdefgg", True), ("fffffff", False), ("", True)])
    buzz = Buzz(solution, solution.is_unique)
    buzz.test()


if __name__ == "__main__":
    main()
