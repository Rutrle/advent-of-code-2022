def rock_paper_scissor():
    points_dict = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    win_dict = {
        'X': 'C',
        'Y': 'A',
        'Z': 'B'
    }

    draws_dict = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C'
    }

    with open(r'2_day\input.txt',mode='r') as input_file:
        total_score=0

        for line in input_file.readlines():
            my_play = line[2]
            total_score += points_dict[my_play]
            
            if win_dict[my_play] == line[0]:
                total_score+=6
            elif draws_dict[my_play] == line[0]:
                total_score+=3

    print(total_score)    

if __name__ == "__main__":
    rock_paper_scissor()