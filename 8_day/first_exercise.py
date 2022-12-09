def visible_trees()-> int:
    with open('8_day/input.txt', mode='r') as input_file:
        forrest = input_file.readlines()
        trees = [[int(t) for t in forrest_line.strip()] for forrest_line in forrest]

        print(trees)
        visible_trees = set()

        for i, line in  enumerate(trees):
            current_max = -1
            for j, tree in enumerate(line):
                if tree > current_max:
                    current_max = tree
                    visible_trees.add((i,j))
  
        for i, line in  enumerate(trees):
            current_max = -1
            for j, tree in enumerate(line[::-1]):

                if tree > current_max:
                    print(tree, (i, len(line)-1-j) )
                    current_max = tree
                    visible_trees.add((i,len(line)-1-j))

        for j in  range(len(trees[0])):
            current_max = -1
            for i in range(len(trees)):
                if trees[i][j] > current_max:
                    current_max = trees[i][j]
                    visible_trees.add((i,j))

        for j in  range(len(trees[0])):
            current_max = -1
            for i in range(len(trees)-1,-1,-1):
                if trees[i][j] > current_max:
                    current_max = trees[i][j]
                    visible_trees.add((i,j))

        print(visible_trees)

        return len(visible_trees)

if __name__ == '__main__':
    solution = visible_trees()
    print(solution)