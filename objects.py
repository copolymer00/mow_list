from enum import Enum
import datetime


class Billing_Status(Enum):
    NOTSENT = -1
    SENT = 0
    PAID = 1


class Weekday(Enum):
    Sunday = 1
    Monday = 2
    Tuesday = 3
    Wednesday = 4
    Thursday = 5
    Friday = 6
    Saturday = 7


class Job_Type:
    def __init__(self, name: str, weekly: bool, desc: str, tools: list[str]):
        self.name = name
        self.weekly = weekly
        self.desc = desc
        self.tools = tools

    def to_dict(self):
        return dict(zip(('name', 'desc', 'tools', 'weekly'),
                        (self.name, self.desc, self.tools, self.weekly)))


class Job:
    def __init__(self, j_type: Job_Type, complete: bool, weekday: Weekday,
                 completion_date: datetime.datetime, billing: Billing_Status, hours: int):
        self.j_type = j_type
        self.complete = complete
        self.hours = hours
        self.billing = billing

        if self.j_type.weekly:
            self.weekday = weekday
            if complete:
                self.completion_date = completion_date
        else:
            self.completion_date = completion_date

    def __str__(self):
        return f'{self.j_type.name}\t{"Not Complete" if not self.complete else self.completion_date.strftime("%Y-%m-%d")}\t{self.billing.name}'


class Customer:
    class Info:
        def __init__(self, name: str, email: str, phone: str):
            self.name = name or None
            self.email = email or None
            self.phone = phone or None

    def __init__(self, name: str, jobs: list[Job], email=False, phone=False):
        self.info = self.Info(name, email, phone)
        self.jobs = jobs

    def add_job(self, job):
        self.jobs.append(job)

    def remove_job(self, idx):
        del self.jobs[idx]


class MowList:
    def __init__(self, m_list=list()):
        self.m_list = m_list

    def add_customer(self, cust: Customer):
        if cust not in self.m_list:
            self.m_list += cust

    def remove_customer(self, idx):
        del self.m_list[idx]

    def __str__(self):
        out = "Name\tEmail\t\tPhone\t\tJob\tComplete\tBilling"
        for cust in self.m_list:
            for job in cust.jobs:
                out += "\n" + '\t'.join([cust.info.name, cust.info.email, cust.info.phone, str(job)])
        return out

    def get_customers(self):
        return [cust.info.name for cust in self.m_list]
