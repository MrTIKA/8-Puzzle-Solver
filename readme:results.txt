
Tayfun Turanligil

8 Puzzle Solver: Solves given 8 Puzzles in string representation.
Algorithms used are defined and described detaily in searcher.py


Results based on test_puzzles in this directory



puzzles with 5-move optimal solutions
-------------------------------------
algorithm              num. solved    avg. moves    avg. states tested
----------------------------------------------------------------------
random                     10		5.2		295.6
BFS			   10		5.0		47.6
DFS (depth limit 20)	   10		16.2		19072.7
DFS (depth limit 50)	   10		48.2		49043.0
Greedy Search		   10		5.4		70.3
A*			   10		5.0		6.5





puzzles with 10-move optimal solutions
-------------------------------------
algorithm              num. solved    avg. moves    avg. states tested
----------------------------------------------------------------------
random                     10		14.2		6203.5
BFS			   10		10.0		747.4
DFS (depth limit 20)	   10		18.8		24858.0
DFS (depth limit 50)	   10		49.2		92287.3
Greedy Search		   8		76.0		25.625
A*			   10		10.0		27.3





puzzles with 15-move optimal solutions
-------------------------------------
algorithm              num. solved    avg. moves    avg. states tested
----------------------------------------------------------------------
random                     6		21.33		25357.16
BFS			   10		15.0		12672.0
DFS (depth limit 20)	   10		17.8		68659.0
DFS (depth limit 50)	   10		48.6		111406.0
Greedy Search		   6		90.33		2718.0
A*			   10		15.0		313.8



reflection:
In terms of the average moves value, we have clear winners for all 3 sets of puzzles, BFS and A*. This might seem like having an informed algorithm like A* is pointless, but when we take in to account the avg. states tested, A* does have a clear edge here since it tested far less states to come up to same results as BFS, we can safely say that having an informed algorithm with a  heuristic, saves a lot of computation time. As far as other algorithms concerned, random was pretty expected; close but far from optimal, DFS never failed to find a solution in a reasonable time, but it was definitely slow and tested way too much states.  Finally, Greedy, because it only does not have a solid heuristic, performed worse as the problem got harder.



#############################################################################



heuristic 1
-----------
This heuristic not only finds the number of misplaced tiles, but it also find the distance between the misplaces tiles and adds them up. It does that using nested loops go through each tile and uses a helper function called find() in the board object which finds the location of the given (misplaces) tile in board. 



puzzles with 18-move optimal solutions
--------------------------------------
algorithm              num. solved    avg. moves    avg. states tested
----------------------------------------------------------------------
Greedy (heuristic -1)       7		133.71		4594.0
Greedy (heuristic 1)	    10		76.2		725.7

A* (heuristic -1) 	    10		18.0		1602.0
A* (heuristic 1)	    10		18.0		239.3



puzzles with 21-move optimal solutions
--------------------------------------
algorithm              num. solved    avg. moves    avg. states tested
----------------------------------------------------------------------
Greedy (heuristic -1)       4		109.0		416.5
Greedy (heuristic 1)	    10		75.4		370.7

A* (heuristic -1) 	    10		21.0		6301.7
A* (heuristic 1)	    10		21.0		482.3



puzzles with 24-move optimal solutions
--------------------------------------
algorithm              num. solved    avg. moves    avg. states tested
----------------------------------------------------------------------
Greedy (heuristic -1)       6		123.66		2856.16
Greedy (heuristic 1)	    10		75.2		593.3

A* (heuristic -1) 	    5		24.0		23685.8
A* (heuristic 1)	    10		24.0		1065.5



puzzles with 27-move optimal solutions
--------------------------------------
algorithm              num. solved    avg. moves    avg. states tested
----------------------------------------------------------------------
Greedy (heuristic -1)       4		197.5		4285.5
Greedy (heuristic 1)	    10		90.8		693.9

A* (heuristic -1) 	    0		———		———
A* (heuristic 1)	    10		27.0		5043.0


reflection: Here, the problems are definitely harder to solve. We start to see the importance of a solid heuristic in such large problems. Problems such as Greedy averaging 109.0 moves in 21-move boards to A* not being able to solve any board in 27-move boards at default heuristic. But when we use the better approximation (heuristic) for the which tile to choose, things become so much smoother. A* made a perfect score using: heuristic 1. This signifies that a good heuristic becomes more and more beneficial, or a necessity to solving the problem as the size of the problem increases.









