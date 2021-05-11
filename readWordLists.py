

# read wordlists
with open("./wordlists/positiveWords.txt", encoding='utf-8') as f:
    positiveWordList = f.readlines()[0].split(",")
    
with open("./wordlists/negativeWords.txt", encoding='ISO-8859-1') as f:
    negativeWordList = f.readlines()[0].split(",")
    
with open("./wordlists/stopWordsLong.txt", encoding='utf-8') as f:
    stopWordsLong = f.readlines()[0].split(",")