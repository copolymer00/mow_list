import datetime
class MowList:
    _list = list()

    def __init__(self, ui):
        self.populate_list(ui)
    def populate_list(self, ui):
        self._list += ui.load_customers()
    def add_customer(self, cust):
        if cust not in self._list:
            self._list += cust
    def remove_customer(self, name: str):
        for cust in self._list:
            if cust.get_name() == name:
                self._list.pop(cust)
    #--------------------------------------#
    def get_list(self):
        return self._list

class Customer:
    _name = str()
    _jobs = list()
    def __init__(self, name, ui):
        self._name = name
        self.populate_jobs(ui)
    def add_job(self, job):
        self._jobs.append(job)
    def remove_job(self, name):
        for job in _jobs:
            if job.get_name() == name:
                self._jobs.pop(job)
    def populate_jobs(self, ui):
        self._jobs += ui.load_jobs(self._name)
    #--------------------------------#
    def get_name(self):
        return self._name
    def get_jobs(self):
        return self._jobs



class Job:
    name = str()
    weekly = bool()
    complete = bool()
    weekday = int()
    completion_date = datetime.date
    hours = float()

    def __init__(self, ui, name, weekly=True, complete=False, weekday=0):
        self.name = name
        self.weekly = weekly
        if self.weekly:
            self.weekday = weekday
            if complete:
                self.completion_date = ui.get_completion_date()
                self.hours = ui.get_job_hours()
                self.complete = complete ()
        else:
            self.complete = complete

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

def main():
    mow_list = MowList(UI().new())
    print(mow_list.get_list())
    print(mow_list.get_list()[0].get_jobs())
    print(mow_list.get_list()[0].get_jobs()[0].name)
main()

