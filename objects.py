import datetime

class MowList:
    _list = list()

    def __init__(self, inpt):
        self.populate_list(inpt)
    def populate_list(self, inpt):
        self._list += inpt.load_customers()
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
    def __str__(self):
        out = '{\n'
        out += '\tCust. Name:\tJob\tCompletion\n' + '-'*40 + '\n'
        for cust in self._list:
            out += '\t' + cust.get_name() + ':\t'
            for job in cust.get_jobs():
                out += job.name + '\t' + ('X' if job.complete else 'O') + '\n\t\t\t'
        out += '\n}'
        return out

class Customer:
    _name = str()
    _jobs = list()
    def __init__(self, name, inpt):
        self._name = name
        self.populate_jobs(inpt)
    def add_job(self, job):
        self._jobs.append(job)
    def remove_job(self, name):
        for job in _jobs:
            if job.get_name() == name:
                self._jobs.pop(job)
    def populate_jobs(self, inpt):
        self._jobs += inpt.load_jobs(self._name)
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

    def __init__(self, inpt, name, weekly=True, complete=False, weekday=0):
        self.name = name
        self.weekly = weekly
        if self.weekly:
            self.weekday = weekday
            if complete:
                self.completion_date = inpt.get_completion_date()
                self.hours = inpt.get_job_hours()
                self.complete = complete ()
        else:
            self.complete = complete
