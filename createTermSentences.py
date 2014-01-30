import nltk.data

"""
Use the following function to get all sentences containing a certain term from a source file.

Requires a STRING for desiredTerm and a FILE LOCATION for path
"""

def createTermSentences(desiredTerm, text):
	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	sentences = tokenizer.tokenize(text)
	termSentences = [sentence for sentence in sentences if desiredTerm in sentence]
        return termSentences

if __name__ == '__main__':
    pass
