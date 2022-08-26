class Solution:
    def one_away(self, s1: str, s2: str) -> bool:
        if abs(len(s1) - len(s2)) > 1:
            return False

        found_difference = False
        i, j = 0, 0

        while i < len(s1) or j < len(s2):
            if s1[i] == s2[j]:
                i += 1
                j += 1
            else:
                if found_difference:
                    return False

                found_difference = True

                if s1[i + 1] == s2[j]:
                    i += 1
                elif s2[j + 1] == s1[i]:
                    j += 1
                elif s1[i + 1] == s2[j + 1]:
                    i += 1
                    j += 1
                else:
                    return False

        return found_difference


def main():
    solution = Solution()

    assert solution.one_away("pale", "pal") == True, \
        "one_away('pale', 'pal') should return True"

    print("All tests passed!")

if __name__ == "__main__":
  main()
