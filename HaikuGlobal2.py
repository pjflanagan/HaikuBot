#!/usr/bin/env python
# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import re, sys
import urllib2

one = ['a','the','of','from','to','is','and','in','that','was','it','for','as','or','I']
#in > into 2


def strip(untrusted_html):
	"""
	Strips out all tags from untrusted_html, leaving only text.
	Converts XML entities to Unicode characters.  This is desirable because it 
	reduces the likelihood that a filter further down the text processing chain 
	will double-encode the XML entities.
	"""
	soup = BeautifulSoup(untrusted_html, convertEntities=BeautifulSoup.ALL_ENTITIES)
	safe_html = ''.join(soup.findAll(text=True))
	return safe_html
	
### CLEAN UP PHRASE
def clean(phrase):
	phrase = filter(lambda x: x in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ \n', phrase)
	return phrase

### OPEN URL
def openURL(query,place):
	if place == 'dict':
		address = 'http://dictionary.reference.com/browse/' +str(query)
	elif place == 'thres':
		address = 'http://thesaurus.com/browse/' +str(query)
	try:
		page = urllib2.urlopen(address)
		source = BeautifulSoup(page.read())#,'html.parser')
		page.close()
	except:
		return '!Failure!'
	return source

### DEFINE WORD
def define(word):
	soup = openURL(word,'dict')
	#define = clean(strip(
	define = soup.findAll('div', {'class':'def-content'})#))
	print define
	define = clean(strip(str(define)))
	return define


### GET SYLLABLES
def syllable(word): ###(word,purpose)
	global deff, cword
	if word in one:
		return 1
	else:
		soup = openURL(word,'dict')
		sound = strip(str(soup.find('h2',attrs={'class':'me'}))).replace(u'·','+')
		number = len(sound.split('+'))
		deff.pop(cword)
		deff.insert(cword,sound.replace('+','')) 
		return number
	"""
	if purpose = 'word':
		sound = sound.replace
		return number
	elif purpose = 'numb':
		number = len(sound.split(' '))
		return number
	"""





### GET SYNONYMS
def synonym(word,len):
	#global deff
	soup = openURL(word,'thres')
	try:
		cell = clean(strip(str(soup.find('table',attrs={'class':'the_content'})))).replace('\n',' ').split(' ')
		cell = filter(lambda a: a != '', cell)
		start = cell.index('Synonyms')+1
		
		try:
			end = cell.index('Antonyms')
			cell = cell[start:end]
		except:
			cell = cell[start:]
	except:
		return '!Failure!'
		
	for word in cell:
		number = syllable(word)
		if number == len:
			return word
			
	return '!Failure!'
	### SPLIT EVERY LINE TO ONLY GET ONE WORD RESPONSES (NO PHRASES like "bad feeling")




### CHECK HAIKU LINES
def checkLine(len):
	global deff, cword
	cword = 0 #current word
	line = 0 #sylables of line
	verse = '' #text of line 
	
	for word in deff:
		csyll = syllable(word)
		line += csyll
		
		if line == len:
			verse = write(cword)
			return verse
			
		#if line is more than length
		elif line > len:
			
			overflow = line - len
			length = csyll - overflow #length needed to fit
			syn = synonym(word,length)
			
			if syn != '!Failure!':
			
				deff.pop(cword) #THIS STEP COULD
				deff.insert(cword,syn) #BE MOVED
				verse = write(cword) #TO SYNONYM()
				return verse
			
			elif syn == '!Failure!':
			
				length = len - line
			
				while syn == '!Failure!':
		
					cword -= 1
					if cword >= 0:
						
						syn = synonym(deff[cword],length)
			
					elif cword < 0:
						pass
						print('Sorry Bud')
						sys.exit()
						#Here is where we would add
						#The possibility that the synonym did not work:
						#move word down one line and find longer synonyms for other words
		cword+=1 #Move to next word





### WRITE LINE
def write(cword):
	global deff
	verse = ''
	while cword >= 0:
		verse = str(deff[cword]) + ' ' +str(verse)
		deff.pop(cword)
		cword -= 1
	return verse




### MAIN LOOP
### WRITE HAIKU
if __name__ == '__main__':
	
	global deff
	poem = raw_input('Write Poem For: ')
	print('\n\t' +poem.title())
	
	deff = define(poem).split(' ')
	deff.pop()

	
	line1 = checkLine(5)
	print(line1)
	line2 = checkLine(7)
	print(line2)
	line3 = checkLine(5)
	print(line3)
	
	tweet = str(poem) +': ' +str(line1) +' / ' +str(line2) +' / ' +str(line3)	
	print(len(tweet))
	
	#print ''
	#print str(line1) +'\n' +str(line2) +'\n' +str(line3)


#HAIKU WRITEN:

#LOVE
#a profound tender 
#passionate affection for 
#another person

#IMAGINE
#the faculty of 
#imagine or of form deep 
#image or concept 

#INTELLIGENCE
#capacity for 
#learning reasoning forbearing 
#and similar form 
	
#LIFE
#the condition that
#distinguishes organisms from
#inorganic bulk

#SMART
#to be a source 
#of sharp local and mainly 
#superficial pain 

#MEANING
#what is intended 
#to be or actually 
#is expressed or marked

#PASSION
#any powerful 
#or compelling emotion 
#or feeling as love 

#better syllable check from sound out area: len(str('[op-tuh-muh m]').split('-'))
#use defenition 2 if 1 is not long enough
