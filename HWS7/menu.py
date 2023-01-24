from os import system

class Menu:
    
    def __init__(self, elements=[]):
        self.elements = elements

    def print(self):
        for (mark, text, _) in self.elements:
            print(f'{mark} - {text}')

    def run(self, prompt='Select the command: '):
        def clrScr(): return system('cls')
        while (True):
            clrScr()
            self.print()
            user_choice = input(prompt)
            for (mark, _, run_method) in self.elements:
                if user_choice == mark:
                    if run_method == -1:
                        return True
                    clrScr()
                    run_method()
                    break
