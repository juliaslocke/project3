# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
import requests
from bs4 import BeautifulSoup
import re

base_url = "https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions"
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "lxml")
#results = str(soup)
f = open('bshw3.html', 'w')
results = str(soup)
#f.write(results)
for each in soup.find_all('p'):
	y = results.replace('student', 'AMAZING student')
for each in soup.find_all('iframe'):
	z = y.replace('https://www.youtube.com/embed/mimp_3gquc4?feature=oembed', 'media/me_pic.png')
for each in soup.find_all('img'):
	g = each['src']
	print(g)
	each['src'] = 'media/logo.png'
	b = each['src']
	print(b)
	q = z.replace(g, b)
	# image replaced at the bottom of the webpage but for some reason would not appear at the top

f.write(q)
f.close()

# THE CODE BELOW ARE OTHER METHODS THAT I HAD ATTEMPTED BUT LEFT TO SHOW WORK. NONE OF THE BELOW IS FULL CODE.

#for each in soup.find_all(class_='html not-front not-logged-in two-sidebars page-node page-node- page-node-11581 node-type-general-page section-programs'):
#	for w in each.find_all(class_='body-inside2'):
#		for h in w.find_all(class_='container3'):
#			for x in h.find_all(class_='page'):
#				for y in x.find_all(class_='field-items'):
#					for z in y.find_all(class_='field-item even'):
#						for q in z.find_all('p'):
#							f.write(each.text.replace('student', 'AMAZING student'))
#words = soup.find_all('p')
#for elt in words:
#	element = elt.text
#	paragraph = re.findall('\\bstudent\\b', element)
#	#print (paragraph)
#	f.write(element.replace('student', "AMAZING student"))
#	#print (element)