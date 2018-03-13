import os 
import csv
import re

ParagraphData = os.path.join('data','paragraph_2.txt')
outputTXT= os.path.join("data", "paragraph_2_solution.txt")

with open(ParagraphData, 'r', newline="") as textfile:
    paratext = textfile.read()
    #print(paratext)
    print()

    def wordCount(mystring):  
        tempcount = 0  
        count = 1  

        try:  
            for character in mystring:  
                if character == " ":  
                    tempcount +=1  
                    if tempcount ==1:  
                        count +=1  

                    else:  
                        tempcount +=1   
                else:
                    tempcount=0
            return count 

        except Exception:  
            error = "Not a string"  
            return error  


    def mean(numbers):
        return float(sum(numbers)) / max(len(numbers), 1)
    linecount = paratext.count('.')

    s = paratext
    SentList = re.split(r'[?!.]', s)
    Countword = len(re.findall(r'\w+', str(SentList)))
    avgword = (Countword)/(linecount)
   
    print("Approximate word count:",str(wordCount(paratext)))
    print("Approximate sentence count:",str(paratext.count('.')))
    print("Approximate letter count (per word):",str(mean(list(map(len,paratext.split())))))

    print("Average sentence length (in words):", str(avgword))
    

    #print(wordCount(paratext))
    #print(paratext.count('.'))
    #print(len(paratext)/wordCount(paratext))    
    #print(char_frequency(paratext))

with open(outputTXT, 'w',) as textFile:
    textFile.write("Pragraph stats")
    textFile.write("\n----------------------------------------")
    textFile.write("\napprox word count = "+ str(wordCount(paratext)))
    textFile.write("\napprox sentence count = " + str(paratext.count('.')))
    textFile.write("\napprox letter count (per word) =" + str(mean(list(map(len,paratext.split())))))
    textFile.write("\naverage sentence length = " + str(avgword))
       