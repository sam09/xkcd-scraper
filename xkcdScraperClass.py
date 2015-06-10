from bs4 import BeautifulSoup as soup
import requests, os


class xkcdScraper():

	def __init__(self):
		self.url = "http://xkcd.com/"
		self.metaData = None
	def get_HTML(self, i):
		r = requests.get(self.url+str(i))
		HTML  = soup(r.text)
		return HTML

	def parse_HTML(self, HTML):
		img = str(HTML.find_all("img")[2])
		img = img.split("\"")
		src = "http:" + img[3]
		text = img[5]
		title = HTML.title.text
		start = title.find("xkcd: ") + len("xkcd: ")
		title = title[start:]
		ext = src.split(".")
		filename = ext[len(ext) -2]
		filename = filename.split("/")
		filename = filename[len(filename) - 1]
		ext = ext[len(ext) - 1]
		filename = filename + "." + ext
		metaData = { 'src' : src, 'filename' :filename, 'title': title , 'text' : text}

		self.metaData = metaData

	def download(self, i):
		HTML = self.get_HTML(i)
		self.parse_HTML(HTML)
		src = self.metaData['src']
		path = "Comics"
		if not os.path.exists(path):
			os.makedirs(path)
			print path + " created"
		path = "Comics/" + self.metaData['filename']
		
		r = requests.get(src)
		if r.status_code == 200:
			with open(path, 'wb') as f:
				for chunk in r.iter_content():
					f.write(chunk)
		
		print self.metaData['filename'] + " downloaded to " + path