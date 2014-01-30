import nltk.data

"""
Use the following function to get all sentences containing a certain term from a source file.

Requires a STRING for desiredTerm and a FILE LOCATION for path
"""

def createTermSentences(desiredTerm, path):

	"""opens text output file"""
	f = open(path,"r")

	"""creates string with text from file"""
	text = f.read()

	"""creates NLTK's tokenizer"""
	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

	"""Uses tokenizer to separate text into sentences"""
	sentences = tokenizer.tokenize(text)

	"""Desired term in sentences"""
	keyTerm = desiredTerm

	"""Creates array of sentences containing keyTerm"""
	termSentences = [sentence for sentence in sentences if keyTerm in sentence]

	print termSentences