import datetime
from ui import UI
from objects import MowList

def main():
    mow_list = MowList(UI().new())
    print(mow_list.get_list())
    print(mow_list.get_list()[0].get_jobs())
    print(mow_list.get_list()[0].get_jobs()[0].name)
main()

