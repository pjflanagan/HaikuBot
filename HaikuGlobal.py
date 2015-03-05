#!/usr/bin/env python
# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import re, sys
import urllib2

###	 OPEN URL
def openURL(query,place):
	if place == 'dict':
		address = 'http://dictionary.reference.com/browse/' +str(query)
	elif place == 'thres':
		address = 'http://thesaurus.com/browse/' +str(query)
	page = urllib2.urlopen(address)
	source = BeautifulSoup(page.read())
	page.close()
	return source

### DEFINE WORD
def define(word):
	soup = openURL(word,'dict')
	deff = clean(soup.find('div', attrs={'class':'dndata'}).contents[0])
	print deff
	return deff

### CLEAN UP PHRASE
def clean(phrase):
	print phrase
	phrase = phrase.replace(',','').replace(';','').replace('.','').replace('(','').replace(')','').replace(':','')
	return phrase

### GET SYLLABLES
def syllable(word):
	soup = openURL(word,'dict')
	try:
		sound = soup.find('h2',attrs={'class':'me'}).contents[0].replace(u'·' , ' ')
		number = len(sound.split(' '))
		return number
	except:
		print word

### GET SYNONYMS
def synonym(word,len):
	soup = openURL(word,'thres')
	cell = soup.find('table',attrs={'class':'the_content'})
	list = []
	for a in cell.findAll('a'):
		try:
			list.append(a.contents[0])
		except: 
			pass
	print list
	list.pop(0)
	list.pop(0)
	list.pop(0)
	print list
	synonym = '!Failure!'
	for word in list:
		number = syllable(word)
		if number == len:
			synonym = word
			return synonym
	return synonym

### WRITE LINE 1
def write1():
	global deff
	cword = 0 #current word
	line = 0 #sylables of line
	line1 = '' #text of line one
	for word in deff:
		csyll = syllable(word)
		line += csyll
		if line == 5:
			line1 = write(cword)
			return line1
		elif line > 5:
			overflow = line - 5
			len = csyll - overflow #length needed to fit
			syn = synonym(word,len)
			deff.pop(cword)
			deff.insert(cword,syn)
			return line1
		cword+=1 #Move to next word
			
### WRITE LINE 2
def write2():
	global deff
	cword = 0
	line = 0
	line2 = ''
	for word in deff:
		csyll = syllable(word)
		line += csyll
		if line == 7:
			line2 = write(cword)
			return line2
		elif line > 7:
			#Find synonym
			overflow = line - 7
			len = csyll - overflow #length needed to fit
			syn = synonym(word,len)
			deff.pop(cword)
			deff.insert(cword,syn)
			#write
			line2 = write(cword)
			return line2
		cword+=1 #Move to next word 

### WRITE LINE 3
def write3():
	global deff
	cword = 0 #current word
	line = 0 #sylables of line
	line3 = '' #text of line one
	for word in deff:
		csyll = syllable(word)
		line += csyll
		if line == 5:
			line3 = write(cword)
			return line3
		elif line > 5:
			overflow = line - 5
			len = csyll - overflow #length needed to fit
			syn = synonym(word,len)
			deff.pop(cword)
			deff.insert(cword,syn)
			line3 = write(cword)
			return line3
		cword+=1 #Move to next word

### WRITE LINE
def write(cword):
	global deff
	verse = ''
	while cword >= 0:
		verse = deff[cword] + ' ' +verse
		deff.pop(cword)
		cword -= 1
	return verse
	
### WRITE HAIKU
if __name__ == '__main__':
	#### TESTING ZONE ####
	poem = raw_input('Write Poem For: ')
	#print syllable(poem)
	#sys.exit()

	#len = input('How many: ')
	#print synonym(poem,len)
	#sys.exit()
	#### TESTING ZONE ####
	
	global deff
	deff = define(poem).split(' ')
	deff.pop()
	
	
	line1 = write1()
	print line1
	#print deff
	line2 = write2()
	print line2
	#print deff
	line3 = write3()
	print line3
	
	print ''
	print line1 +'\n' +line2 +'\n' +line3
	
	
#the condition that
#distinguishes animals
#from inorganic


