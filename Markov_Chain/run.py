from fetch_data import fetch_poem
from markov_python.cc_markov import MarkovChain

def intialize_model():
	'''Feed the data to a markov chain and return the object of it'''
	poems = fetch_poem()

	mc = MarkovChain()

	for poem in poems:
		mc.add_string(poems[poem])

	return mc

def generate_poem(mc, para = 3):
	'''Prints the paragraphs for the poem generated via Markov Chain generated text

	   Input : 
	    mc : object for the markov model 
	   	para : No. of paragraphs to print (Default is 3)'''
	
	for p in range(para): 
		words = mc.generate_text(48)
		line = ''

		for idx, word in enumerate(words):
			if idx % 8 == 0:
				print(line)
				line = ''
			line += word + ' '
		print()

if __name__ == '__main__':
	print ("This program generates poem similiar to Wiliam Shakespeare's poems")
	mc = intialize_model()
	n = int(input("Number of Paragraphs you want to generate : "))
	generate_poem(mc, n)
	input()