Here I will explain how I solved the problem and the approaches I took. 

I saw the problem on the Internet and I was already familiar with the algorithm which solves the sudoku. I liked the idea and decided to give it a try. After some googling I found out that most of the people are using pygame, a module I am not familiar with. For this reason I decided to use tkinter, something already familiar to me. 

I started by writing a simple algorithm which solves the sudoku. Nothing special, it even removed all the correct numbers it had previously placed going back through the stack (backtracking). And the solution is lost

I knew the backtracking bug would be a problem, but I decided that I will tackle this last. I creates the labels, used IntVar to give me the ability to change the values of the labels, named the IntVar-s. But I had one problem, I didn't know when I should change the values. I tried at the very beginning of each recursive call, which didn't work of course. 
So I simplified the problem. 

I created another file where I experimented until I was able to solve one line and display in the GUI. Then I scaled up everything to change the variables of the sudoku. But one problem remained, I backtracked when I was not supposed to. 

I had to change the solve_sudoku so it uses some logic to know when it should backtrack. Turned out to be easier than I thought, changed the recursive calls into if statements, added return True where needed and return False at the end of the definition. Now every time False is returned we backtracked. 

One thing remains, to make it look like a real sudoku. Tkinter borders and lines should do the trick.
P.S. Interestingly enough, trying to use the grid system to add lines is a bad idea. Used separators because this is the only line-like object, which can be added to the grid system. Turns out I am unable to make the separator thicker so it is just a thin line, or at least I can't find the argument to do it. But still looks like a sudoku, it is not too bad. The more important part for me was the algorithm, so I will leave it at this


Open for a discussion about how I approached the problem and if there is anything better I could do. 