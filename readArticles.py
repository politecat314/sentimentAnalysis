import re

def read():
    """
    returns a dictionary of the form
    key: "company name"
    value: [article1, article2, article3]
    """

    companyNames = ["CLE", "DHL", "GDEX", "J&T", "PL"]

    articles = {}

    for name in companyNames:
        articles[name] = []
        for i in range(1, 4):
            with open(f"./articles/{name} Article {i}.txt", encoding='utf-8') as f:
                articleText = f.read()
                
                # convert everything to lower case
                articleText = articleText.lower()
                
                # replace full stops with space
                articleText = articleText.replace("."," ")
                
                # remove special characters from article
                articleText = re.sub('[^A-Za-z ]+', '', articleText)
                
                # add processed article to dictionary
                articles[name].append(articleText)

    return articles