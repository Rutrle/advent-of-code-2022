def rock_paper_scissor():
    points_dict = {
        'A': 1,
        'B': 2,
        'C': 3
    }

    win_dict = {
        'B': 'C',
        'C': 'A',
        'A': 'B'
    }

    draws_dict = {
        'A': 'A',
        'B': 'B',
        'C': 'C'
    }

    loose_dict = {
        'B': 'A',
        'C': 'B',
        'A': 'C'
    }

    with open(r'2_day\input.txt',mode='r') as input_file:
        total_score=0

        for line in input_file.readlines():
            elf_play = line[0]
            play_result = line[2]

            if play_result == 'X':
                my_play = loose_dict[elf_play]
                total_score += points_dict[my_play]

            elif play_result == 'Y':
                my_play = draws_dict[elf_play]
                total_score += points_dict[my_play] + 3

            elif play_result == 'Z':
                my_play = win_dict[elf_play]
                total_score += points_dict[my_play] + 6


    print(total_score)    

if __name__ == "__main__":
    rock_paper_scissor()