import re

def clock_circuit():
    signal_register=[1]
    overhead=0

    with open('10_day/input.txt', mode='r') as readfile:
        for line in readfile.readlines():
            if line.strip() == 'noop':
                signal_register.append(signal_register[-1]+overhead)
                overhead = 0
            else:
                add_number = int(line.split(sep=' ')[1])
                signal_register.append(signal_register[-1]+overhead)
                signal_register.append(signal_register[-1])
                overhead = add_number
    print(len(signal_register))
    display=[]
    signal_cycles=(40,80,120,160,200,240)
    for i in signal_cycles:
        display.append([])
        display_position=0
        for i in range(i-39,i+1):

            if signal_register[i] == display_position or signal_register[i] == display_position-1 or signal_register[i] == display_position+1:
                display[-1].append('#')
            else:
                display[-1].append('.')
            print(display_position,i, signal_register[i], ''.join(display[-1]))
            display_position +=1

    for row in display:
        print(''.join(row))


if __name__ == "__main__":
    clock_circuit()