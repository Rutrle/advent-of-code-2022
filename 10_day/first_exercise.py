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
    signal_strength_important=(20,60,100,140,180,220)
    signal_strength_sum=0
    for signal in signal_strength_important:
        print(signal)
        signal_strength = signal*signal_register[signal]
        signal_strength_sum += signal_strength

    print(signal_strength_sum)


if __name__ == "__main__":
    clock_circuit()