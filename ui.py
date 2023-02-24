import datetime
from objects import Customer, Job

class Output:
    def __init__(self):
        pass
    def display(self, data):
        print(str(data));


class Input:
    # Config
    def load_customers(self):
        return [Customer("Joe Bonner", self)]
    def load_jobs(self, name):
        return [Job(self, "Mow", weekly=True, complete=False, weekday=3),
                Job(self, "Patio", weekly=False, complete=True, weekday=1)]
    # StdIn
    def get_completion_date(self):
        return datetime.date(1970,1,1)
    def get_job_hours(self):
        return 1.0
