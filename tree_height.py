# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    nodes = int(n)
    parents_arr = numpy.fromiter(parents.split(), dtype = int)
    root = 0
    h = 1

    node_list = []
    for i in range(nodes):
        node_list.append([])

    for leaf in range(nodes):
        branch = parents_arr[leaf]
        if branch == -1:
            root = leaf
        else:
            node_list[branch].append(leaf)
    
    def biggest_height(node_list, i, h):
        max_height = 0

        if not node_list[i]:
            return h
        
        for j in node_list[i]:
            max_height = max(max_height, biggest_height(node_list, j, h + 1))

        return max_height
    
    # Your code here
    return biggest_height(node_list, root, h)


def main():
    # implement input form keyboard and from files
    input_method = input()
    n = ""
    parents = ""
    if input_method.startswith("I"):
        n = input()
        parents = input()
    elif input_method.startswith("F"):
        print("File path: ")
        file_name = input()
        file_path = "./test/"
        if "a" not in file_name:
            with open(file_path + file_name, mode = "r") as file:
                n = file.readline()
                parents = file.readline()
        else:
            exit()
    else:
        exit()
    height = compute_height(n, parents)
    print(height)
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()