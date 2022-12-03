def count_calories():
    with open('1_day\input.txt','r') as inputfile:
        lines = inputfile.readlines()
        elf_calories_max = 0
        current_elf_calories = 0
        for line in lines:
            if line == "\n":
                if current_elf_calories > elf_calories_max:
                    elf_calories_max = current_elf_calories
                current_elf_calories = 0
            else:
                current_elf_calories += int(line)
        
        print(elf_calories_max)




if __name__ == "__main__":
    count_calories()