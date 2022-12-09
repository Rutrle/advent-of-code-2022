import csv
import numpy as np

def tail_postitions_counter_universal()-> int:
    tail_positions=set()
    knot_positions = np.zeros((9,2))
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
                knot_positions[0] += move_vectors[row[0]]
                
                for i in range(1,len(knot_positions)):
                    distance_vector = ((knot_positions[i-1]) - (knot_positions[i])).astype('int32')
                    if abs(distance_vector[0])>1 or abs(distance_vector[1])>1:
                        increment = np.floor_divide(distance_vector,np.absolute(distance_vector),dtype='int32',out=np.zeros_like(distance_vector), where=distance_vector!=0)
                        knot_positions[i] += increment


                distance_vector = (knot_positions[8] - tail_position).astype('int32')
                
                
                if abs(distance_vector[0])>1 or abs(distance_vector[1])>1:
                    increment = np.floor_divide(distance_vector,np.absolute(distance_vector),dtype='int32',out=np.zeros_like(distance_vector), where=distance_vector!=0)
                    tail_position += increment
                    tail_positions.add(tuple(tail_position))




    return len(tail_positions)

if __name__ == '__main__':
    position_number = tail_postitions_counter_universal()
    print(position_number)