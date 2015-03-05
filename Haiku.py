#!/usr/bin/env python
# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import re, sys
import urllib2

###	 OPEN URL
def openURL(query,place):
	if place == 'dict':
		address = 'http://dictionary.reference.com/browse/' +query
	elif place == 'thres':
		address = 'http://thesaurus.com/browse/' +query
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
	phrase = phrase.replace(',','').replace(';','').replace('.','').replace('(','').replace(')','')
	return phrase

### GET SYLLABLES
def syllable(word):
	soup = openURL(word,'dict')
	sound = soup.find('h2',attrs={'class':'me'}).contents[0].replace(u'·' , ' ')
	number = len(sound.split(' '))
	return number

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
	list.pop(0)
	list.pop(0)
	list.pop(0)
	for word in list:
		number = syllable(word)
		if number == len:
			return word

### WRITE HAIKU
if __name__ == '__main__':
	poem = raw_input('Write Poem For: ')
	
	deff = define(poem).split(' ')
	deff.pop()
	
	#SETUP
	csyll = 0
	cword = 0 #current word
	lword = 0 #last word
	line = 0 #sylables of line
	stanz = 1 #current line
	line1 = '' #text of line one
	line2 = '' #two
	line3 = '' # and three
	end = False
	
	while end == False:
		for word in deff:
			try:
				csyll = syllable(word)
				line += csyll
				
				#CHECK LINE ONE
				if stanz == 1:
					if line == 5:
						while cword >= lword:
							line1 = deff[cword] +' ' +line1
							cword -= 1
						stanz += 1
						line = 0
						lword = cword
					elif line > 5:
						overflow = line - 5
						len = csyll - overflow #length needed to fit
						synonym(word,len)
				#CHECK LINE TWO
				elif stanz == 2:
					if line == 7:
						while cword >= lword:
							line1 = deff[cword] +' ' +line1
							cword -= 1
						stanz += 1
						line = 0
						lword = cword
					elif line > 7:
						overflow = line - 7
						len = csyll - overflow #length needed to fit
						#replace word in defenition
						syn = synonym(word,len)
						if syn == '!Failure!':
							pass
							#Here we have two options
							#check other words in the list
							#if that doesnt work we can move the word down a line
							#and then check for a sylable even longer
						else:
							deff.pop(cword)
							deff.insert(cword,syn)
							while cword >= lword:
								line2 = deff[cword] +' ' +line2
								cword -= 1
							stanz +=1
							line = 0
							lword = cword
				#CHECK LINE 3
				"""
				elif stanz == 3:
					if line == 5:
						while cword >= lword:
							line3 = deff[cword] +' ' +line3
							cword -= 1
						stanz += 1
						line = 0
						lword = cword
					print line3
					end = True
				"""
				cword += 1
			except:
				print 'Error'
			
	print line1 +'\n' +line2 +'\n' +line2
	
#the condition that
#distinguishes animals
#from inorganic


