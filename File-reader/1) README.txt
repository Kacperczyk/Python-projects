main.py
Its the program which allow user to choose file (csv file) and read this file with limited columns.
----------------------------------------------------------------------------------------------------
DONE 1) Upon launching it shows list of columns of selected file.
DONE 2) The user is able to choose the columns of interest.
DONE 3) After selecting one column, they must decide whether to choose another.
DONE 3) a) If yes, then the chosen column is removed from the pool of available columns.
      The selected column is added to an unseen list, which stores the user's choices.
      This will enable later loading of the file with only the chosen columns.
DONE 3) b) If the user type "stop" the loop is interrupted, and we proceed to step 4).
DONE 4) We choose what to do next.
DONE 4) a) Reading a file with the selected columns.
DONE 4) b) Saving as a new file with the selected columns.
        REMARKS: currently stores whole file(New_persons.txt) as a list, which consumes a lot of memory, a generator should be used
DONE 4) c) Reading a file with the selected columns as a table
DONE 4) d) Saving as a new file with the selected columns as a table
     REMARKS: the same code is repeated in many places - fix it
IN PROGRESS 5) Reorganizing the code and writing it into functions
IN PROGRESS 6) Reorganizing all the code and saving it in classes
IN PROGRESS 7) Using Pandas and numpy to optimize the code
IN PROGRESS 8) Adding user interface
IN PROGRESS BONUS) Adding comments

main.py2
This simple program allow user to create new csv file with a certain amount of randomly generated persons.
The number of columns is strictly limited.
This program was created solely for the purpose of main.py
--------------------------------------------------------------------------------------------------
