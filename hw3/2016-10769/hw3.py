#!/usr/bin/python
import argparse
import copy


def parse_args(p_list):
    parser = argparse.ArgumentParser()
    parser.add_argument('--A', default='6329', type=int)
    parser.add_argument('--B', default='8537', type=int)
    args = parser.parse_args()
    if args.A not in p_list or args.B not in p_list:
        parser.error("At least one of the input is not a prime number with 4 digits")

    return args


def load_primes(txt_path):
    f = open(txt_path, "r")
    lines = f.readlines()
    all = "".join(lines) # join lines
    all = all.split()
    all = map(int, all)
    f.close()

    # only want the 4-digit primes
    p_list = [p for p in all if 1000 <= p and p <= 9999]
    return p_list

def get_diff_count(str1, str2) :
    count = 0
    for idx in range(len(str1)) :
        if str1[idx] != str2[idx] :
            count += 1

    return count

def adj_list(p_list):
    '''
    ############################ Function description ############################

    Design a function that returns an adjacency list representation of the graph
    of primes in the form of dictionary. The edges of the graph connect the prime
    numbers which have only a single different digit, such as 6329 - 6529.

    ##############################################################################
    '''
    edges = {}
    ##### Please write your code down here #####

    for p in p_list :
        edges[p] = list()
        for q in p_list :
            if get_diff_count(str(p), str(q)) == 1 :
                edges[p].append(q)
    
    return edges


def shortest_path(a, b, p_list):
    '''
    ############################ Function description ############################

    Design a function that returns the length of the shortest path from one to an-
    other. You can use the return value of "adj_list".

    ##############################################################################
    '''
    n = 0
    graph = adj_list(p_list)
    queue = list() 
    path = dict()
    
    queue.append(a) 
    # init first node's path
    path[a] = list()
    
    while len(queue) != 0 :
        # pop the first element of queue
        cur_node = queue.pop(0)
        for adj in graph[cur_node] :
            # If path already exists, then visited node.
            if adj not in path.keys() :
                path[adj] = copy.deepcopy(path[cur_node])
                # Append itself and record path
                path[adj].append(adj)
                # We find it!
                if adj == b :
                    n = len(path[adj])
                    return n

                # appen self and go on.
                queue.append(adj)

    return n


if __name__ == '__main__':
    '''
    # The input will be randomly changed by TAs when grading.
    # The default strings are set as the example in the homework pdf.
    # If you execute <python3 hw3.py>, the two prime numbers will be set by the default.
    # You can also use your own strings by executing command  <python3 hw3.py --A 1033 --B 8179>
    # You can freely define a new function or import modules if you need.
    # You should "not" modify the "main" function
    # You are "not" allowed to use the modules that directly calculate the shortest path, such as "Dijkstar" or "NetworkX".
    '''
    prime_txt = 'prime.txt'
    prime_list = load_primes(prime_txt)
    args = parse_args(prime_list)
    A = args.A
    B = args.B
    print('Input number A : {:d}'.format(A))
    print('Input number B : {:d}'.format(B))

    N = shortest_path(A, B, prime_list)
    print('The length of the desired shortest path from A to B is : {:d}'.format(N))

