import cmd

class Calculator(cmd.Cmd):
    prompt = '(calculator) '
    
    def do_add(self, arg):
        """Add numbers."""
        numbers = list(map(int, arg.split()))
        print(f'Sum: {sum(numbers)}')
    
    def do_exit(self, arg):
        """Exit the REPL."""
        return True

if __name__ == '__main__':
    Calculator().cmdloop()
