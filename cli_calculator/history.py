import pandas as pd

class HistoryManager:
    def __init__(self, filename='history.csv'):
        self.filename = filename
        self.df = pd.DataFrame(columns=['operation', 'result'])

    def save_history(self):
        self.df.to_csv(self.filename, index=False)

    def load_history(self):
        self.df = pd.read_csv(self.filename)

    def add_record(self, operation, result):
        new_record = {'operation': operation, 'result': result}
        self.df = self.df.append(new_record, ignore_index=True)
