import urllib.request
url = "http://www.gutenberg.org/files/10/10-0.txt"
file = urllib.request.urlopen(url)

for line in file:
	decoded_line = line.decode("utf-8")
	print(decoded_line)