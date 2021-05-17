
# Create an empty dictionary
d = []
word = ''
words = ''

# Open the file in read mode(txt file should be in the same location as the project file)
with open("sample.txt", encoding='utf-8')as text:
    # Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()

        # Convert the characters in line to
        # lowercase to avoid case mismatch
        line = line.lower()

        # adding all the lines into one string
        word += line + " "

# split the line into words
words = word.split()

#counts the words
d = [words.count(w) for w in words]
# converts into dic with key as name of the word and values as frequency
Word_frequency = dict(zip(words,d))

#every word from the dictionary including the stop words
print(Word_frequency)

rem = ''
with  open("remove.txt",encoding='utf-8') as re:
    for line in re:
        # removes the spaces
        line = line.strip()
        # adding every line to a variable
        rem = rem + line + ","

    # splitting the lines into words
    remo = rem.split(',')

#this loop removes the stop words from the dictionary
for r in remo:
    if r in Word_frequency:
        del Word_frequency[r]
    else:
        continue

#prints the dictionary without the stop words
print(Word_frequency)
