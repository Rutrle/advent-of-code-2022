import csv
import numpy as np
from copy import copy

def tail_postitions_counter()-> int:
    vertical=0
    horizontal=0
    tail_positions=set()
    #head_position=np.array([0,0])
    knot_positions = np.array([0,0]*9)
    tail_position=np.array([0,0])
    tail_positions.add(tuple(tail_position))
    
    move_vectors={
        'R':np.array([0,1]),
        'L':np.array([0,-1]),
        'U':np.array([1,0]),
        'D':np.array([-1,0])
    }
    with open('9_day/input.txt', mode='r') as input_file:
        head_moves = csv.reader(input_file, delimiter=' ')
        for row in head_moves:

            for _ in range(int(row[1])):
                previous_head_position = copy(knot_positions[0])
                knot_positions[0] += move_vectors[row[0]]
                

                for i, knot in enumerate(knot_positions[1:]):
                    if abs(distance_vector[0])>1 or abs(distance_vector[1])>1:
                        distance_vector = knot_positions[i-1] - knot_positions[i]
                        knot_positions[i] = copy(knot_positions[i-1])
                        

                distance_vector = knot_positions[8] - tail_position

                

                if abs(distance_vector[0])>1 or abs(distance_vector[1])>1:
                    tail_position = copy(previous_head_position)
                    tail_positions.add(tuple(tail_position))

                print(head_position, previous_head_position)



    return len(tail_positions)

if __name__ == '__main__':
    position_number = tail_postitions_counter()
    print(position_number)