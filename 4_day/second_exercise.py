import re

def duplicate_sectors():
    with open(r'4_day\input.txt',mode='r') as input_file:
        total = 0
        lines = input_file.readlines()
        for line in lines:
            low_first = int(re.search("^[0-9]+", line).group(0))
            high_first = int(re.search("-[0-9]+,", line).group(0)[1:-1])
            low_second = int(re.search(",[0-9]+-", line).group(0)[1:-1])
            high_second = int(re.search("[0-9]+$", line).group(0))

            if (low_first <= high_second) and (high_first >= low_second):

                total +=1
        print(total)
#699¨, 891 ne
if __name__ == "__main__":
    duplicate_sectors()