import Tester


class Buzz:
    """
                         Mano, tu é gay?
        ⠀  ⠀⠀⣀⣤⣶⠶⠾⠿⠛⠛⠿⠷⠶⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣠⣴⠟⠋⠁  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣦⣄⠀⠀⠀⠀⠀
    ⠀⠀⠀⣠⣾⠟⠁⠀⠀⠀⣠⣤⣶⣾⣿⣿⣷⣶⣤⣄⠀ ⠀⠀⠈⠻⣷⣄⠀⠀⠀
    ⠀⠀⣴⠟⠁⠀⠀⠀⠀⣼⣿⣉⣀⠀⠀⢀⣠⣴⣿⣿⣧⠀  ⠀⠀⠀⠈⠻⣦⠀⠀
    ⠀⣼⠏⠀⠀⠀⠀⠀⢠⣿⠏⣩⣿⣇⠀⠈⣩⣥⣄⠈⣿⡀⠀⠀ ⠀⠀⠀⠹⣧⠀
    ⢸⡟⠀⠀⠀⠀⠀⠀⢸⣿⠀⠋⣹⠟⠁⠈⠁⣽⠟⠀⣿⡇⠀⠀⠀ ⠀⠀⠀⢻⡇
    ⣾⡇⠀⠀⠀⠀⠀⠀⣾⠇⠀⠀⠀⢠⣴⣦⡄⠀⠀⠀⠸⣷⠀⠀⠀⠀  ⠀⠀⢸⣷
    ⣿⠀⠀⠀⢀⣠⡆⢠⣿⠀⢀⣤⣀⣈⣀⣀⣁⣤⣶⣄⠀⣿⡄⢰⣄⡀⠀⠀⠀⣿
    ⣿⠀⢀⣶⣿⣿⡇⢸⣿⠀⠉⠙⢿⣏⣉⣉⣽⡿⠁⠀⠀⣿⡇⢸⣿⣿⣶⡀⠀⣿
    ⣿⠀⢸⣿⣿⣿⣇⠀⣿⡀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⢀⣿⠀⣸⣿⣿⣿⡇⠀⣿
    ⣿⠀⢸⣿⡿⠟⠋⡀⠹⣧⡀⠀⠀⠀⠿⢿⠀⠀⠀⢀⣼⠏⢀⠙⠻⢿⣿⡇⠀⣿
    ⣿⡆⠘⠟⠀⣴⡿⠗⠀⢹⣿⣦⣄⣀⣀⣀⣀⣠⣴⣿⡏⠀⠺⢿⣦⠀⠻⠃⢰⣿
    ⢿⣿⣦⣄⡀⠉⠀⠶⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠶⠀⠉⢀⣠⣴⣿⡿
    ⠈⠛⢿⣿⣿⣿⣶⣦⣤⣤⣄⣀⣈⣉⣉⣉⣉⣁⣀⣠⣤⣤⣤⣶⣿⣿⣿⡿⠛⠁
    ⠀⠀⠀⠈⠉⠙⠛⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠛⠋⠉⠁⠀⠀⠀

    Descrição:
        Buzz consegue testar a solução que você passar como parâmetro
        e avaliar a partir dos casos de teste se está correta ou não.
    """

    def __init__(self, solution, solution_algorithm) -> None:
        self.tester = Tester()
        self.tester.set_algorithm(solution_algorithm)
        self.tester.set_algorithm_name(solution_algorithm.__name__)
        self.tester.set_testcases(solution.testcases)

    def speak(self, msg):
        print("Buzz:", msg)

    def test(self):
        try:
            self.speak("Vou testar ele aqui mano")
            self.tester.run()
        except Exception as e:
            self.speak("Ele não é gay não mano\n\t {}".format(
                str(e)))
        else:
            self.speak("Testei ele umas {} vezes mano"
                       .format(len(self.tester.testcases)))
            self.speak("Acho que ele é gay")
