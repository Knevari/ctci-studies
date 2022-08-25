Testcase = tuple[any, any]


class Tester:
    def __init__(self) -> None:
        self.algorithm = None
        self.algorithm_name = None
        self.testcases = []

    def set_algorithm(self, algorithm) -> None:
        self.algorithm = algorithm

    def set_algorithm_name(self, algorithm_name: str) -> None:
        self.algorithm_name = algorithm_name

    def set_testcases(self, testcases: list[Testcase]) -> None:
        self.testcases = testcases

    def run(self):
        if len(self.testcases) == 0:
            raise Exception("There are no testcases for the given algorithm.")

        for testcase, desired_result in self.testcases:
            # It assumes, in-place algorithms will return the value nonetheless
            algorithm_result = self.algorithm(testcase)

            assert algorithm_result == desired_result, \
                "{}({}) should return {}, instead it returned {}"\
                .format(
                    self.algorithm_name,
                    str(testcase),
                    str(desired_result),
                    str(algorithm_result)
                )
