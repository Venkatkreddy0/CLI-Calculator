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
    
import logging
from dotenv import load_dotenv
import os

load_dotenv()
log_level = os.getenv('LOG_LEVEL', 'INFO')
log_output = os.getenv('LOG_OUTPUT', 'console')

if log_output == 'console':
    logging.basicConfig(level=log_level)
else:
    logging.basicConfig(filename='app.log', level=log_level)

logger = logging.getLogger(__name__)

logger.info("Calculator started")
