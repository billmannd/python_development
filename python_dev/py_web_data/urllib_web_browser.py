import urllib
fhand = urllib.urlopen('http://www.uc.edu')

counts = dict()
for line in fhand:
	words = line.split()
	for word in words:
		counts[word] = counts.get(words, 0) + 1
print(counts)

