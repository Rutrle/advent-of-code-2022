def find_first_unique():
    with open('6_day\input.txt','r') as inputfile:
        lines = inputfile.readlines()
        line=lines[0]
        for i in range(len(line)):
            test_set=set()
            flag=True
            for n in range(14):
                if line[i+n] in test_set:
                    flag=False
                    break
            
                elif line[i+n] not in test_set:
                    test_set.add(line[i+n])
            if flag:
                print(i+14)
                break

        




if __name__ == "__main__":
    find_first_unique()