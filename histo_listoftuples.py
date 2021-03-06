# To run in terminal, type: "python3" + "histo_listoftuples.py" + file name
import sys

def histogram():
    f = open(sys.argv[1], "r").read().split()
    tokens = [] #Creates empty list. Tokens (unique words) live here
    word_count = [] #Creates empty list. Quantities of appearance live here
    for word in f:
        if word not in tokens: #If tokens DOESN'T ALREADY contain word....
            tokens.append(word) #...then add word to tokens....
            word_count.append(1) #...and add 1 to word_count.
        else: #If tokens DOES ALREADY contain word....
            word_count[tokens.index(word)] += 1 #...then add +1 to the corresponding index in word_count
    histogram_tuples = [] #Create empty list for tuples
    i = 0 #Initialize counter
    for word in tokens:
        histogram_tuples.append((tokens[i], word_count[i])) #mashes tokens and word_count into a single tuple, then appends this tuple!
        i += 1 #Add +1 to counter to iterating through tokens
    return histogram_tuples

if __name__ == '__main__':
    print(histogram())
