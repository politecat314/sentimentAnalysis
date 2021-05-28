

def positive():
    with open("./wordlists/positiveWords.txt", encoding='utf-8') as f:
        positiveWordList = f.readlines()[0].split(",")
    return positiveWordList

def negative():
    with open("./wordlists/negativeWords.txt", encoding='ISO-8859-1') as f:
        negativeWordList = f.readlines()[0].split(",")
    return negativeWordList

def stop():
    with open("./wordlists/stopWordsLong.txt", encoding='utf-8') as f:
        stopWordsLong = f.readlines()[0].split(",")
    return stopWordsLong