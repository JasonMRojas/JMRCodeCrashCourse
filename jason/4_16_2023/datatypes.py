"""
How do programs work?

They "look" at the file they are running on currently.
They go line by line and follow the logical path they are instructed to follow.
There is a "stack" which manages the current location that the interpreter is currently at


What is a datatype?

A data type, in programming, is a classification that specifies which type of value a variable has and what type of mathematical, relational or logical operations can be applied to it without causing an error.


A data type is a classification of information within a computer that lets you do specific types of work.

int -- 3, 0, 22, 33, -10
    - Can represent an amount of someting!
    - You can do math on them! -- (iteration on an integer is possible)
        - 3 + 5 = 8
        - 10 / 2 = 5
        - 2 * 8 = 16
        - -2 - 4 = -6
        - % modulo operator -- Which returns the remained of some equation
        - = assignment operator which lets you set a value in a variable.
        - == Compares two values to see if they are equal
        - != 2 values are not the same
        - >, <, <=, >= inequality operators which can do the same stuff they do in math
    - Math still follows pemdas
float -- 3.0, 3.1. 22.2223232323, -213.2232
Boolean -- True, False 
    -- These are used to handle boolean logic in a programs flow
    -- Booleans have their special math operators
        - or -- Resolves two distinct boolean statements as True if either of the options is True or Both are True
            - (True or True) == True
            - (True or False) == True
            - (False or True) == True
            - (False or False) == False
        - and -- Resolves two distinct boolean statements as True only if both statements are True otherwise they total is considered false
            - (True and True) == True
            - (True and False) == False
            - (False and True) == False
            - (False and False) == False
        - xor -- Resolves to True if either of the statements is True but not both
            - (True xor True) == False
            - (True xor False) == True
            - (False xor True) == True
            - (False xor False) == False
        - not -- Not Operator evalues to the opposite of the evaluated boolean statement
String -- "Word", "Hello World I am a string", "H3ll0"
dictionaries -- Key Value paired datastructures
lists (arrays) -- An ordered series of "items"
char -- 'a'
NoneType (Also called NULL in certain langauges) -- Literally means Nothing is assigned but is defined.


We use 'operators' to do work on datatypes -- Mathematical, Relational or Logical operations that can be performmed on a datatype without error.



If statements facilitate programatic flow using boolean logic
"""
print("Hello World")