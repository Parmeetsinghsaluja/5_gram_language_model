This is readme file for question 3

How to run:
1. Install Pythonv3.6.4
2. Run the implementation by entering command on your command line python by command -
   python filename
3.The program asks
a)Enter Path of Training Data :
b)Enter Path of Test Data :
c)Enter Path where you want output files to be stored:
4. The count of 5 grams and 4 grams is stored in fivegrams.txt and fourgrams.txt respectively
5. Highest top 3 perplexity file data will be stored in Perplexity.txt

Note:
For convenience
Perplexity of file 03302.txt is stored in file named 03302.txt it was calculated by just giving it as Test Data
Non english files are detected and their details is stored in List_of_Non_English_Files.txt


Implementation:
Programs takes input all training data and combine together and clear it by removing empty lines, new line characters and empty spaces.
Data in converted to char array.
5 gram and 4 grams are genrated using training data
5 gram Character Language model is generated using Markov Assumption to calculate the probability.
Lambda Smoothing is done by taking lambda 0.1.
Vocabulary size is no of distinct chars in training data.
-1*Log(Probability) is stored in dict.
Test data is collected per file and is cleaned and 5 gram is generated.
Perplexity is calculated using these probabilties per file per character i.e. they are normalized per file.
Perplexities are stored in dictionary and are sorted in decreasing order.

Note:
All of these libraries are imported in program
import glob, os  - used to change directory
import re - used for regex
import collections - used for counting the data
import math - used for mathematical functions
import operator - used for providing operator to sort dictionary

