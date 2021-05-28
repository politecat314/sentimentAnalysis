NO_OF_CHARS = 256
def badCharHeuristic(string, size):
    '''
    The preprocessing function for
    Boyer Moore's bad character heuristic
    '''

    # Initialize all occurrence as -1
    badChar = [-1] * NO_OF_CHARS

    # Fill the actual value of last occurrence
    for i in range(size):
        badChar[ord(string[i])] = i;

    # retun initialized list
    return badChar

def clear(s,txt,pat):
    if s == 0 and txt[s+len(pat)]==" ":
        return True
    elif s>0 and s+len(pat)==len(txt) and  (txt[s-1] == " " or txt[s-1]=="."):
        return True
    elif s>0 and (txt[s+len(pat)]=="," or txt[s+len(pat)]== '"' or txt[s+len(pat)]==":" or txt[s+len(pat)]==" " or txt[s+len(pat)]==".") and (txt[s-1] == '"' or txt[s-1] == "," or txt[s-1] == " " or txt[s-1]=="."):
        return True
    else:
        return False

def search(txt, pat):
    '''
    A pattern searching function that uses Bad Character
    Heuristic of Boyer Moore Algorithm
    '''
    m = len(pat)
    n = len(txt)
    count = 0
    # create the bad character list by calling
    # the preprocessing function badCharHeuristic()
    # for given pattern
    badChar = badCharHeuristic(pat, m)

    # s is shift of the pattern with respect to text
    s = 0
    while (s <= n - m):
        j = m - 1

        # Keep reducing index j of pattern while
        # characters of pattern and text are matching
        # at this shift s
        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1

        # If the pattern is present at current shift,
        # then index j will become -1 after the above loop
        if j < 0 and clear(s,txt,pat)==True:
            count = count+1


            '''   
                Shift the pattern so that the next character in text
                      aligns with the last occurrence of it in pattern.
                The condition s+m < n is necessary for the case when
                   pattern occurs at the end of text
               '''
            s += (m - badChar[ord(txt[s + m])] if s + m < n else 1)
        else:
            '''
               Shift the pattern so that the bad character in text
               aligns with the last occurrence of it in pattern. The
               max function is used to make sure that we get a positive
               shift. We may get a negative shift if the last occurrence
               of bad character in pattern is on the right side of the
               current character.
            '''
            s += max(1, j - badChar[ord(txt[s + j])])
    return count


def convert(i):
    s1 = "".join(filter(str.isalpha, i))
    return s1




# Driver program to test above function
def main():
    d = []
    word = ''
    words = ''
    with open("sample.txt",encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            line = line.lower()
            word += line + " "


    words = word.split()
    d =  [words.count(w) for w in words]
    Word_frequency = dict(zip(words, d))

    rem = ''
    with  open("stopWordsLong.txt", encoding='utf-8') as re:
        for line in re:
            # removes the spaces
            line = line.strip()
            # adding every line to a variable
            rem = rem + line + ","

        # splitting the lines into words
        remo = rem.split(',')

    # this loop removes the stop words from the dictionary
    for r in remo:
        if r in Word_frequency:
            del Word_frequency[r]
        else:
            continue

    t = ''
    for i in words:
        t = t + convert(i) + " "

    du_WF = list(t.split(" "))
    ser =  [du_WF.count(w) for w in du_WF]
    dummy_WF = dict(zip(du_WF,ser))
    with open('positiveWords.txt',encoding='utf-8') as f:
        s = f.readlines()[0].split(",  ")
    pwords = dict()
    for i in s:
        count = search(t, i)
        if count >= 1:
            pwords.update({i: count})


    with open("negativeWords.txt", encoding='ISO-8859-1') as f:
        tr = f.readlines()[0].split(",    ")
    nwords = dict()
    for i in tr:
        count = search(t, i)
        if count >= 1:
            nwords.update({i: count})

    for i in nwords:
        if i in dummy_WF:
            del dummy_WF[i]

    for i in pwords:
        if i in dummy_WF:
            del dummy_WF[i]

    #positive words
    print(pwords)
    #Negative Words
    print(nwords)
    #Neutral Words
    print(dummy_WF)

    Psum = 0
    Nsum = 0
    NE_sum = 0

    for i in pwords:
        Psum = Psum+pwords[i]
    for i in nwords:
        Nsum = Nsum + nwords[i]
    for i in dummy_WF:
        NE_sum = NE_sum + dummy_WF[i]

    if(Psum > Nsum):
        print("Positive Sentiment")
    elif(Nsum > Psum):
        print("Negative Sentiment")
    else:
        print("Neutral Sentiment")



# if __name__ == '__main__':
    # main()