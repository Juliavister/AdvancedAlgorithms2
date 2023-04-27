# AdvancedAlgorithms2
Group project 2 from the course Advanced Algorithms.

* Part One 

	A) "Me spell rite"

	The Evil Lord Wladimir has cast the Spellus Incorrectus magical spell on your fellow students. Your task is to
	implement a simple spell checker that decides whether each individual word in a text file is spelled correctly.
	You might use the english word list available in this directory.
	Try: a naive (linear list) approach, string BBST, trie and a hash map. You may use library solutions for BBST, e.g. std::ordered_set or alike.
	Compare running times for dictionary building and spell checking on a large piece of text.
	Your report should contain description of algorithms, comparison findings including graphs showing the relation of RT against the text length.

	B) "Triwizard Tournament"
	One competition in the TT is to get out of a labyrinth as quickly as possible. Your task as the tournament supervisor is:
	given the labyrinth map, initial positions of the three competing wizzards and their speeds (in corridors per minute)
	predict which of them will reach the exit first. Assume that the magical wands used in the play
	are capable of guiding the wizards to the exit along a shortest possible path. The BFS should be used exactly once.


** Part Two 

	"Aunt's Namesday"

	Your beloved aunt Petunia is throwing her namesday party, to which as usual, she invites all her friends and family.
	There are however some animosities among the invited guests. Aunt's idea is to have two separate tables, so that no two disliking one another people would have to sit at the same table.
	Given the list of the invited guests and the corresponding list of your aunt's suggestions on "who doesn't like whom",
	your task, as your aunt's dear little pumpkin sausage computer genius, is to use a recursive DFS algorithm to set up a "sitting scheme".

*** Part three 

	"Full house"

	Implement a Hash Table with separate chaining and two HTs with open addressing, say linear probing and double hashing.
	Compare the relations between the search/insert times (y-axis) and the load factor (x-axis) for each implementation.
