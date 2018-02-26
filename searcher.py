
import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    def __init__(self, init_state, depth_limit):
        '''constructs a new Searcher object'''
        self.states = [init_state]
        self.num_tested = 0
        self.depth_limit = depth_limit

    def should_add(self, state):
        '''takes a State object called state and returns True if the called
           Searcher should add state to its list of untested states, and False
           otherwise.
        '''

        if (self.depth_limit != -1 and state.num_moves > self.depth_limit):
            return False
        if state.creates_cycle():
            return False
        
        return True

    
    def add_state(self, new_state):
        '''adds takes a single State object called new_state and adds it to the
           Searcher‘s list of untested states
        '''
        self.states.append(new_state)
        
    def add_states(self, new_states):
        '''takes a list State objects called new_states, and that processes
           the elements of new_states one at a time
        '''

        for s in new_states:
            if self.should_add(s):
                self.add_state(s)

    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    def find_solution(self):
        '''performs a full random state-space search, stopping when the
           goal state is found or when the Searcher runs out of untested
           states.
        '''

        while self.states != []:
            s = self.next_state()
            self.num_tested += 1
            
            if s.is_goal():
                return s
            else:
                self.add_states(s.generate_successors())
        return None
        

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s




########   Searchers    ######


class BFSearcher(Searcher):
    '''a subclass of the Searcher, BFS performs breadth-first
       search instead of random search
    '''

    def next_state(self):
        '''overrides the next_state method that is inherited from Searcher.
           this version of next_state follows FIFO ordering,
           choosing the state that has been in the list the longest.
        '''
        s = self.states[0]
        self.states.remove(s)
        return s


    
    
class DFSearcher(Searcher):
    '''a subclass of the Searcher, DFS performs depth-first
       search instead of random search
    '''

    def next_state(self):
        '''overrides the next_state method that is inherited from Searcher.
           this version of next_state follows LIFO ordering,
           choosing the state that has been in the list the shortest.
        '''
        s = self.states[-1]
        self.states.remove(s)
        return s


    

class GreedySearcher(Searcher):
    '''a subclass of the Searcher, GreedySearcher performs greedy
       search instead of random search using a heuristic
    '''
    def priority(self, state):
        '''takes a State object called state, and that computes and
           returns the priority of that state
        '''

        if self.heuristic == 1:
            
            pri = -1 * (state.board.sum_dis())
            
        elif self.heuristic == 2:
            pri = -1 * (state.board.sum_dis() + state.board.find_min_dis())

        else:
            pri = -1 * state.board.num_misplaced()
            
        return pri

    
    def __init__(self, init_state, heuristic, depth_limit):
        """ constructor for a GreedySearcher object
            inputs:
             * init_state - a State object for the initial state
             * heuristic - an integer specifying which heuristic
       function should be used when computing the priority
       of a state
             * depth_limit - the depth limit of the searcher
        """
        self.heuristic = heuristic
        self.states = [[self.priority(init_state), init_state]]
        self.num_tested = 0
        self.depth_limit = depth_limit
        

    def add_state(self, state):
        '''overrides the add_state method that is inherited from Searcher.
           adds a sublist that is a [priority, state] pair
        '''
        self.states.append([self.priority(state), state])

    def next_state(self):
        '''overrides the next_state method that is inherited from Searcher.
           this chooses one of the states with the highest priority.
        '''
        s = max(self.states)
        self.states.remove(s)
        s = s[1]
        return s

class AStarSearcher(GreedySearcher):
    '''a subclass of the GreedySearcher, AStarSearcher performs
       search instead of random search using a heuristic
    '''

    def priority(self, state):
        '''overrides priority method in GreedySearcher ,takes a State
           object called state, and that computes and
           returns the priority of that state
        '''

        if self.heuristic == 1:
            pri = -1 * (state.board.sum_dis() + state.num_moves)

        elif self.heuristic == 2:
            pri = -1 * (state.board.sum_dis() + state.num_moves + state.board.find_min_dis())
        else:
            pri = -1 * (state.board.num_misplaced() + state.num_moves)


        return pri

        















    
