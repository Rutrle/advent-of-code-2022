def best_tree()-> int:
    with open('8_day/input.txt', mode='r') as input_file:
        forrest = input_file.readlines()
        trees = [[int(t) for t in forrest_line.strip()] for forrest_line in forrest]

        print(trees)
        bestest_tree = 0

        for i, line in  enumerate(trees):
            for j, evaluated_tree in enumerate(line):
                right = 0
                left = 0
                up = 0
                down = 0


                up_direction = i
                while up_direction>0:
                    up_direction -=1
                    up+=1
                    if trees[up_direction][j]<evaluated_tree:
                        pass
                    else:
                        break

                down_direction = i
                while down_direction<len(trees)-1:
                    down_direction +=1
                    down+=1
                    if trees[down_direction][j]<evaluated_tree:
                        pass
                    else:
                        break

                left_direction = j
                while left_direction>0:
                    left_direction -=1
                    left+=1
                    if trees[i][left_direction]<evaluated_tree:
                        pass
                    else:
                        break

                right_direction = j
                while right_direction<len(trees[0])-1:
                    right_direction +=1
                    right+=1
                    if trees[i][right_direction]<evaluated_tree:
                        pass
                    else:
                        break
                
                current_tree_score = up*down*left*right

                

                if current_tree_score> bestest_tree:
                    bestest_tree = current_tree_score
                    print((i,j), current_tree_score,up, down, left, right)


        return bestest_tree

if __name__ == '__main__':
    solution = best_tree()
    print(solution)