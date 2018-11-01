import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--A', default='bca', type=str)
    parser.add_argument('--B', default='baaa', type=str)
    args = parser.parse_args()

    return args


def LCS(a, b):
    '''
    ############################ Function description ############################

    Design a function that returns the length of the LCS (Longest Common Subsequen
    ce) between two strings.

    ##############################################################################
    '''
    L = 0
    ##### Please write your code down here #####

    pivot_b = 0
    len_a = len(a)
    len_b = len(b)

    for i in range(0, len_a) :
        for j in range(pivot_b, len_b) :
            if a[i] == b[j] :
                L += 1

                pivot_b = j + 1
                break 
        
    return L


def increase_LCS_by_one(a, b):
    '''
    ############################ Function description ############################

    Design a function that returns the number of total ways to insert a character
    in string A to increase the length of the LCS (Longest Common Subsequence) bet
    ween two strings by one.(i,e L -> L + 1)

    ##############################################################################
    '''
    n = 0
    ##### Please write your code down here #####
    L = LCS(a, b) 
    b_char_list = list()
    for c in b :
        if c not in b_char_list : 
            b_char_list.append(c)

    for c in b_char_list :
        for i in range(0, len(a) + 1) :
            if LCS(a[0:i] + c + a[i:], b) == L + 1 :
                n += 1

    return n


if __name__ == '__main__':

    # The input will be randomly changed by TAs when grading
    # The default strings are set as the example in the homework pdf.
    # If you execute <python3 hw2.py>, the strings will be set by the default.
    # You can also use your own strings by executing command  <python3 hw2.py --A aaa --B ccc>

    args = parse_args()
    A = args.A
    B = args.B
    print('Input string A : {:s}'.format(A))
    print('Input string B : {:s}'.format(B))
    L = LCS(A, B)
    print('The length of the LCS between A and B is : {:d}'.format(L))

    n = increase_LCS_by_one(A, B)
    print('The total number of ways to increase the length of the LCS is : {:d}'.format(n))


