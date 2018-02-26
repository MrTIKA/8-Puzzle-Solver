
from searcher import *
from timer import *

def eight_puzzle(init_boardstr, algorithm, extra=-1):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * extra - an optional extra parameter that can be used to
            specify either a depth limit or the number of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')

    if algorithm == 'random':
        searcher = Searcher(init_state, extra)
    elif algorithm == 'BFS':
        searcher = BFSearcher(init_state, extra)
    elif algorithm == 'DFS':
        searcher = DFSearcher(init_state, extra)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(init_state, extra, -1)
    elif algorithm == 'A*':
        searcher = AStarSearcher(init_state, extra, -1)
    else:  
        print('unknown algorithm:', algorithm)
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution()
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states tested')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()

            

def process_file(filename, algorithm, extra=-1):
        '''opens the file with the specified filename:
             1)obtains the digit string on that line
             2)takes the steps needed to solve the eight puzzle for that digit string
             3)reports the number of moves in the solution
        '''

        file = open(filename, 'r')

        num_puzzles = 0
        total_moves = 0
        total_states = 0

        for line in file:

            init_boardstr = line[0:9]
            
            init_board = Board(init_boardstr)
            init_state = State(init_board, None, 'init')
            
            
            if algorithm == 'random':
                searcher = Searcher(init_state, extra)
            elif algorithm == 'BFS':
                searcher = BFSearcher(init_state, extra)
            elif algorithm == 'DFS':
                searcher = DFSearcher(init_state, extra)
            elif algorithm == 'Greedy':
                searcher = GreedySearcher(init_state, extra, -1)
            elif algorithm == 'A*':
                searcher = AStarSearcher(init_state, extra, -1)
            else:  
                print('unknown algorithm:', algorithm)
                return


            soln = None
            try:
                soln = searcher.find_solution()
            except KeyboardInterrupt:
                print(init_boardstr + ": " , end='')
                print('search terminated, ', end='')
                print('no solotion')
                continue

            if soln == None:
                print(init_boardstr + ": " , end='')
                print('no solotion')

                
            else:
                print(init_boardstr + ": " , end='')
                print(soln.num_moves , " moves, ", end='')
                print(searcher.num_tested , " states tested")
                
                total_moves += soln.num_moves
                total_states += searcher.num_tested 
                num_puzzles += 1

            

        print()
        print("solved " + str(num_puzzles) + " puzzles")

        if num_puzzles != 0:
            print("averages: "+str(total_moves/num_puzzles)+" moves, " \
                  +str(total_states/num_puzzles) +" states tested")

        file.close()
        









        
             
