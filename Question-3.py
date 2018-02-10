import glob, os
import re
import collections
import math
import operator

def ngrams(data, n):
  #Creating a list to store n grams
  lst=list()

  #Ordered List
  ordered_list= []

  #Making ngrams
  for i in range(len(data)-n+1):

     #Apending data in ordered_list
     ordered_list = ''.join(data[i:i+n])

     #Apending data in normal list
     lst.append(ordered_list)

  #Returning the list
  return lst

#creating 5gram character model
def fivegrammodel(fourgrams,fivegrams,V):

	#declaring default dict
    model = collections.defaultdict(lambda: -math.log(1/V))
    #first assigning the counts
    for key in fivegrams.keys():
        try:
            model[key] = fivegrams[key]
        except KeyError:
            model[key] = 1/V
            continue
    #assigning probabilities and smoothing them
    for word in model:
        model[word] = -math.log((model[word]+0.1)/(fourgrams[word[0:4]]+ 0.1*V))
    return model

#Calulating perplexity
def perplexity(testset, model, N):
    perplexity = 0

    #Adding perplexties
    for word in testset:
        perplexity = perplexity + model[word]

    #Normalizing Perplexity
    perplexity = perplexity/N
    return math.exp(perplexity)

#Taking input of all path
training_data_path= input("Enter Path of Training Data :")
test_data_path= input("Enter Path of Test Data :")
path= input("Enter Path where you want output files to be stored:")

#Changing directory to given path
os.chdir(training_data_path)
text=""
#getting all .txt files
for file in glob.glob("*.txt"):

	#opening .txt files one by one
	with open(file,"r",encoding="ISO-8859-1") as f:

		#reading files one by one
		lines=f.readlines()
		for line in lines:

			#checking if there is no empty line
			if not len(line.strip()) == 0:
				text= text+line


#Replacing all new line character with spaces
text = text.replace('\n','')

#Removing extra spaces from the data
final=re.sub(' +',' ',text)

#Converting data to characters
chrs =[c for c in final]

#Calulating Vocabulary size
vocabgram_counter=collections.Counter()
vocabgram_counter.update(chrs)


fivegram_counter=collections.Counter()
#generating 5gram
fivegram_counter.update(ngrams(chrs,5))
#Converting counter object to dictionary object
fivegram_dict  =dict(fivegram_counter)

#Printing the count in a file so changing directory to desired path
os.chdir(path)

#Opening the file to write the data
file = open('fivegrams.txt' , 'w+')
file.write("Number of fivegrams generated in training data are:" +str(sum(fivegram_dict.values())))

#Closing the file
file.close()

fourgram_counter=collections.Counter()
#generating 4gram
fourgram_counter.update(ngrams(chrs,4))
#Converting counter object to dictionary object
fourgram_dict  =dict(fourgram_counter)

#Printing the count in a file so changing directory to desired path
os.chdir(path)

#Opening the file to write the data
file = open('fourgrams.txt' , 'w+')
file.write("Number of fourgrams generated in training data are:" +str(sum(fourgram_dict.values())))

#Closing the file
file.close()

#Creating  5 gram Character Language Model
model = fivegrammodel(fourgram_dict,fivegram_dict,len(vocabgram_counter.keys()))


#Changing directory to given path
os.chdir(test_data_path)

#Creating dictionary for perplexity
perplexity_dict =dict()

#getting all .txt files
for file in glob.glob("*.txt"):

	#opening .txt files one by one
	with open(test_data_path+"\\"+file,"r",encoding="ISO-8859-1") as f:

		#reading files one by one
		testtext=""
		lines=f.readlines()
		for line in lines:

			#checking if there is no empty line
			if not len(line.strip()) == 0:
				testtext= testtext+line

		#Replacing all new line character with spaces
		testtext = testtext.replace('\n','')

		#Removing extra spaces from the data
		finaltesttext=re.sub(' +',' ',testtext)

		#Converting testdata to characters
		testchrs =[c for c in finaltesttext]

        #generating 5gram of test data
		testdata = ngrams(testchrs,5)

		#calculating perplexity file
		perplexity_dict[file] = perplexity(testdata,model,len(testchrs))


#Sorting the files in decreasing order of perplexity
sorted_dict = sorted(perplexity_dict.items(), key=operator.itemgetter(1),reverse =True)

count =0
os.chdir(path)

#Writing the data into a text file
file = open('Perplexity.txt' , 'w+')

for key,value in sorted_dict:
	if count<3:
		file.write(key+","+str(value)+"\n")
		count=count+1
	else:
		break
		
#Closing the file
file.close()
