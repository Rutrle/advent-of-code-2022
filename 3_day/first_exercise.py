def duplicate_items_counter():
    with open(r'3_day\input.txt',mode='r') as input_file:
        total = 0
        for line in input_file.readlines():
            line=line.strip()
            first_compartment = set(line[:int(len(line)/2)])
            second_compartment = set(line[int(len(line)/2):])
            same = ''.join(first_compartment.intersection(second_compartment))
            if ord(same) > 94:
                total += ord(same) - 96
            else:
                total += ord(same) - 38

        print(total)

if __name__ == "__main__":
    duplicate_items_counter()