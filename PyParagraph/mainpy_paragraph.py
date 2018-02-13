#import modules 
import os
import csv
#initialize counter variables
word_count=0
letter_count=0
sentence_count=0
lines=0
#open file
with open('Resources/passage.txt',) as textfile:
    csv_reader=csv.reader(textfile)
    #stores passage into a list
    for row in csv_reader:
        print(row)
        #loops through each index
        for line in row:
            #separates words
            each_row=line.split()
            #increments count of words
            word_count+=len(each_row)
            #increment to move to the next line of the passage
            lines+=1
            #another loop for going through each word
            for words in each_row:
            #remove punctuation marks and other special characters to count the letters    
                words.strip(".")
                words.strip(" ")
                words.strip("?")
                words.strip("!")
                words.strip("-")
                words.strip("*")
                words.strip("$")
                words.strip("@")
                words.strip("%")
                words.strip(",")
                words.strip("&")
                words.strip("^")
                words.strip("(")
                words.strip(")")
                words.strip("+")
                words.strip("=")
            #counts the letters
                letter_count+=len(words)
            #loop to count the sentences by identifying punctuation marks    
            for letter in line:
                if letter=="." or letter=="?" or letter=="!":
                    sentence_count+=1
    print("Paragraph Analysis")
    print("--------------------")        
    print("Approximate Word Count:" +str(word_count))
    print("Approximate Letter Count:" +str(letter_count))
    print("Approximate Sentence Count:"+str(sentence_count))