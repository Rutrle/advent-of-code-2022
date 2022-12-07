import re
from copy import copy

def duplicate_sectors():
    with open(r'5_day\input.txt',mode='r') as input_file:
        lines = input_file.readlines()

        piles_num = 9
        big_ugly_list=[[] for i in range(piles_num)]

        for line in lines[:8]:
            current_chars = list(line[1::4])
            print(current_chars)
            for i, char in enumerate(current_chars):
                if char != ' ':
                    big_ugly_list[i].insert(0,char)

        for line in lines[10:]:
            move =int(re.search("move ([0-9]+)", line).group(1))
            from_column =int(re.search("from ([0-9]+)", line).group(1))
            to_column = int(re.search("to ([0-9]+)", line).group(1))

            for _ in range(move):
                big_ugly_list[to_column-1].append(big_ugly_list[from_column-1].pop())



        print(big_ugly_list)
        for smaler_list in big_ugly_list:
            print(smaler_list[-1])

if __name__ == "__main__":
    duplicate_sectors()