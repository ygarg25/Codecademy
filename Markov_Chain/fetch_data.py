import urllib.request
from bs4 import BeautifulSoup as BS

def fetch_poem():
	'''Fetch Shakespeare poems from MIT site (http://shakespeare.mit.edu/) 
	and writes them into a file poem_name.txt for example The Sonnets.txt
	Also return a dictionary with poem name as key and the poem as value'''

	poems = { "A Lover's Complaint" : 'LoversComplaint',
			 'The Rape of Lucrece' : 'RapeOfLucrece',
			 'Venus and Adonis' : 'VenusAndAdonis'}			 
	poem_dicts = {}
	url = "http://shakespeare.mit.edu/Poetry/"

	for poem in poems:
		poem_url = url + poems[poem] + '.html'
		response = urllib.request.urlopen(poem_url)
		html_doc = response.read().decode('utf-8')
		html_string = BS(html_doc, 'html.parser')
		poem_lines = ''
		for block in html_string.find_all('blockquote'):
			for line in block.strings:
				poem_lines += line

		# with open(poem+'.txt', 'w') as f:
		# 	f.write(poem_lines)

		poem_dicts[poem] = poem_lines

	return poem_dicts 