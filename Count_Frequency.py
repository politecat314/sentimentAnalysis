


# Open the file in read mode(txt file should be in the same location as the project file)
text = open("sample.txt", encoding='utf-8')

# Create an empty dictionary
d = []
word = ''
words = ''
# Loop through each line of the file
for line in text:
    # Remove the leading spaces and newline character
    line = line.strip()

    # Convert the characters in line to
    # lowercase to avoid case mismatch
    line = line.lower()

    # adding all the lines into one string
    word += line+" "

# split the line into words
words = word.split()

#counts the words
d = [words.count(w) for w in words]
# converts into dic with key as name of the word and values as frequency
Word_frequency = dict(zip(words,d))

print(Word_frequency)

