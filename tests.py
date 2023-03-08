from datetime import datetime as dt
from objects import *


jt_mow = Job_Type("Mow", True, "Mow and trim lawn", ["52 Mower", "Push mower", "Trimmer", "Backpack"])

print("jt_mow",jt_mow.to_dict())

j_job = Job(jt_mow, False, Weekday.Tuesday, dt.now(), Billing_Status.SENT, 7)

print("j_job",str(j_job))

j_kob = Job(jt_mow, True, Weekday.Friday, dt.now(), Billing_Status.NOTSENT, 5)

c_bob = Customer("Bob", [j_job], "bob@bobmail.com", "(904) 675-3122")

c_bob.add_job(j_kob)

ml = MowList([c_bob])

print("Customers",ml.get_customers())
print("Mow List\n",str(ml))
