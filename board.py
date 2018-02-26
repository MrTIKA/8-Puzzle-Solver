class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9

        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[0] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1


        r = 0
        c = 0
        
        for val in digitstr:
            
            val = int(val)
            self.tiles[r][c] = val

            if val == 0:
                self.blank_r = r
                self.blank_c = c
            
            if c < 2:
                c += 1
                
            else:
                c = 0
                r += 1

            


    def __repr__(self):
        '''returns a string representation of a Board object'''
        s = ''
        for r in range(3):
            for c in range(3):
                
                if self.tiles[r][c] != 0: s += str(self.tiles[r][c])
                else: s += '_'
                
                s += ' '
                
                if c == 2: s += '\n'
        return s

    def move_blank(self, direction):
        '''takes as input a string direction that specifies the direction in which
           the blank should move, and that attempts to modify the contents of the
           called Board object accordingly
        '''
        if direction not in ['up', 'down', 'left', 'right']:
            print("Directions can only be: 'up', 'down', 'left' and 'right'")
            return False

        nr = self.blank_r
        nc = self.blank_c

        if direction == 'up': nr -= 1
        elif direction == 'down': nr += 1
        elif direction == 'left': nc -= 1
        elif direction == 'right': nc += 1

        if nc > 2 or nr > 2 or nc < 0 or nr < 0: return False

        self.tiles[self.blank_r][self.blank_c] = self.tiles[nr][nc]
        self.tiles[nr][nc] = 0
        self.blank_r = nr
        self.blank_c = nc

        return True

    def digit_string(self):
        '''creates and returns a string of digits that corresponds to the current contents
           of the called Board object’s tiles attribute.
        '''
        s = ''
        
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] != '_': s += str(self.tiles[r][c])
                else: s += '0'


        return s
        


    def copy(self):
        ''' returns a newly-constructed Board object that is a deep copy of the called object
        '''
        nb = Board(self.digit_string())

        return nb

    def num_misplaced(self):
        '''counts and returns the number of tiles in the called Board object that are not
           where they should be in the goal state.
        '''

        diff = 0

        real_board = Board("012345678")

        for r in range(3):
            for c in range(3):
                if str(self.tiles[r][c]) in "12345678":
                    if self.tiles[r][c] != real_board.tiles[r][c]:
                        diff += 1



        return diff


    def sum_dis(self):
        '''counts and returns the number of tiles and their distance in the
           called Board object that are not where they should be in the goal state.
        '''
        real_board = Board("012345678")
        
        sum = 0

        for r in range(3):
          for c in range(3):
            if str(self.tiles[r][c]) in "12345678":
                if self.tiles[r][c] != real_board.tiles[r][c]:
                    
                    position = self.find(self.tiles[r][c])
                    target_position = real_board.find(self.tiles[r][c])
                    
                    total = abs(position[0] - target_position[0]) + \
                            abs(position[1] - target_position[1])
                    
                    sum += total
        return sum
                    

    def find(self, val):
        ''' finds and returns the [r,c] of the given int in board'''
        
        for r in range(3):
          for c in range(3):
            if self.tiles[r][c] == val:
                
                return [r,c]

    def find_dis_zero(self,val):
        '''finds and returns the distnce between given tile and zero in the
           called Board object.
        '''

        zero = self.find(0)
        value = self.find(val)
        
        dis = abs(zero[0] - value[0]) + abs(zero[1] - value[1])

        return dis


    def find_misplaced_tiles(self):
       ''' returns a list for the [r,c] of misplaced tiles'''
        
       real_board = Board("012345678")

       list=[]

       for r in range(3):
          for c in range(3):
            if str(self.tiles[r][c]) in "12345678":
                if self.tiles[r][c] != real_board.tiles[r][c]:
                    list += [self.tiles[r][c]]

       return list

    def find_min_dis(self):
        ''' returns the distance of closest misplced tile in board'''

        mp_tiles = self.find_misplaced_tiles()

        if mp_tiles == []: return 0
        
        mint = mp_tiles[0]
        
        for tile in mp_tiles:
            if self.find_dis_zero(mint) > self.find_dis_zero(tile):
                mint = tile
                
        return self.find_dis_zero(mint)
            



    def  __eq__(self, other):
        '''return True if the called object (self) and the argument (other) have the same
           values for the tiles attribute, and False otherwise.
        '''
        return self.tiles == other.tiles
                
        

        

        
