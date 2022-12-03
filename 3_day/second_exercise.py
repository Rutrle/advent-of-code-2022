def duplicate_items_counter():
    with open(r'3_day\input.txt',mode='r') as input_file:
        total = 0
        lines = input_file.readlines()
        for i in range(0,len(lines),3):
            first_elf =set(lines[i].strip())
            second_elf =set(lines[i+1].strip())
            third_elf =set(lines[i+2].strip())

            same = ''.join(first_elf.intersection(second_elf,third_elf))

            if ord(same) > 94:
                total += ord(same) - 96
            else:
                total += ord(same) - 38

        print(total)

if __name__ == "__main__":
    duplicate_items_counter()