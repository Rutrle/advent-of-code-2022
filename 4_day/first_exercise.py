import re

def duplicate_sectors():
    with open(r'4_day\input.txt',mode='r') as input_file:
        total = 0
        lines = input_file.readlines()
        for line in lines:
            first_num = int(re.search("^[0-9]+", line).group(0))
            second_num = int(re.search("-[0-9]+,", line).group(0)[1:-1])
            third_num = int(re.search(",[0-9]+-", line).group(0)[1:-1])
            fourth_num = int(re.search("[0-9]+$", line).group(0))

            if (first_num <= third_num and second_num >= fourth_num) or (first_num >= third_num and second_num <= fourth_num):
                print(first_num, second_num, third_num, fourth_num)
                total +=1




        print(total)

if __name__ == "__main__":
    duplicate_sectors()