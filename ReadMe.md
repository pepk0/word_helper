# Word Helper

Simple project, used to help with generating valid Bulgarian words  
from a specified sequence of letters and length.
I made this program to help me with solving word puzzles from a popular Bulgarian mobile app.

### The App:
> The mobile app has some random letters and the goal is to create a valid word.  
> Problem is often you get stuck on a word and to get a hint, you need to spend money.  
> To counter this I made a word finder program.

![app](https://i.imgur.com/6vNWu8F.jpg)  

----

### Quick Demo:
![word_helper](https://i.imgur.com/YCFnT6z.gif)

----

### Usage:

 1. In the dropdown menu choose the desired length of the output words.
 2. Enter the letter sequence in the text input bar.
 3. Click the Generate button.

| **Program output** | **Crossword** |
| --- | --- |
| ![program with 3 letters](https://i.imgur.com/mUDbM0z.jpg) | ![crossword](https://i.imgur.com/GkPUtC2.jpg) |
| ![program with 4 letters](https://i.imgur.com/0be41fJ.jpg) | ![crossword](https://i.imgur.com/2muhuM2.jpg) |
| ![program with 5 letter](https://i.imgur.com/jl0cpTs.jpg) | ![crossword](https://i.imgur.com/1cRONjM.jpg) |

---- 

### Additional functionality:
* __Cache functionality__
    > The cache functionality uses a Python dictionary to cache previous queries, future quires that are stored in the dictionary are instantly returned.
* __Validation__
    > This functionality validates the inputs and sets the correct parameters if any are wrong.
* __File not found error handling__
    > A message is displayed if the file is missing or the path is incorrect, instead of the program crashing.
----

### How it works:   
This program uses a txt file of bulgarian words, when a query is made with a sequence of elements and a specific length, a permutation function is called and all permutations with the given length are created and stored in a list, a validate word function is called and a loop runs through the list of validated words, and checks if any of them match the permutations.

----
### Constraints:
While the program uses a list of 230k+ validated Bulgarian words, some of the mobile app's words may not appear in the words list.

----
