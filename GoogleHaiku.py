#!/usr/bin/env python
# -*- coding: utf-8 -*-

#http://www.google.com/search?q=define+life&ie=utf-8&oe=utf-8&aq=t&rls=org.mozilla:en-US:official&client=firefox-a

from BeautifulSoup import BeautifulSoup 
import re, sys
import urllib2
opener = urllib2.build_opener()

def openURL(query):
	user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
	headers = { 'User-Agent' : user_agent }
	address = urllib2.Request('http://www.google.com/search?q=define+love', None, headers)
	page = urllib2.urlopen(address)
	source = page.read()
	page.close()
	return source

def define(word):
	#soup = BeautifulSoup(openURL(word))
	#deff = soup.find('div', attrs={'class':'dndata'}).contents[0]
	#print deffenition
	deff = 'A word meaning stuff this word is used quite often to define some stuff'
	return deff
	
def remove(word):
	#word.replace(',','').replace(';','').replace('.','').replace('(','').replace(')','')
	return word

def syllable(word):
	#soup = BeautifulSoup(openURL(word))
	#sound = soup.find('h2',attrs={'class':'me'}).contents[0].replace(u'·' , ' ')
	#number = len(sound.split(' '))
	number = 1
	return number
	
if __name__ == '__main__':
	word = raw_input('Write Poem For: ')
	
	print openURL(word)
	
	#print syllable(word)
	
	#deff = define(word).split(' ')
	#deff.pop()
	
	#print deff
	
	#for item in deff:
	#	try:
	#		print syllable(item)
	#	except:
	#		print 'error'
