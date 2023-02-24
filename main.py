from ui import Input,Output
from objects import MowList

def main():
    output = Output()
    input_c = Input()
    mow_list = MowList(input_c)
    output.display(mow_list)
main()

