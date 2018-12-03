#!/usr/bin/python
import argparse


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

    return edges


def shortest_path(a, b, p_list):
    '''
    ############################ Function description ############################

    Design a function that returns the length of the shortest path from one to an-
    other. You can use the return value of "adj_list".

    ##############################################################################
    '''
    n = 0
    ##### Please write your code down here #####

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

