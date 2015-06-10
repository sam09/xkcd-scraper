##Xkcd Scraper

####Description
A program that Scrapes images from xkcd.com

####Usage
`./scraper.py [options] args`

####Installation

* `git clone https://github.com/samrk09/xkcd-scraper.git`

* `cd xkcd-scraper`

* `pip install -r "requirements.txt"`

####Options
	*  i : download image at url http://xkcd.com/i
	* -s 'a' 'b' : download images from index a to b
	* -m 'n' : download the first n images 
	* -h , --help : Help
####Note
All images download are stored in a folder named `Comics` at the current directory
