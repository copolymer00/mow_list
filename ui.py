from objects import *

class UI:
    def __init__(self):
        pass
    def new(self):
        return self

    def load_customers(self):
        return [Customer("Joe Bonner", self)]
    def load_jobs(self, name):
        return [Job(self, "Mow", weekly=True, complete=False, weekday=3)]

    def get_completion_date(self):
        return datetime.date(1970,1,1)
    def get_job_hours(self):
        return 1.0
