#!/usr/bin/env python
from xkcdScraper import xkcdScraper, is_int

import sys 

def print_help():
	help_str = """
	*  i : download image at url http://xkcd.com/i
	* -s 'a' 'b' : download images from index a to b
	* -m 'n' : download the first n images 
	* -h , --help : Help
	"""
	print help_str
def main():
	try:
		choice = sys.argv[1]
		dl  = xkcdScraper()
		if is_int(choice):
			dl.download(choice)
		elif choice == "-m":
			try:
				count = sys.argv[2]
				if is_int(count):
					i = 1
					count = int(count)
					while i<= count:
						dl.download(i)
						i += 1
				else:
					print "The argument must be an integer"
			except:
				print_help()
		elif choice == "-s":
			try:
				start = sys.argv[2]
				try:
					end = sys.argv[3]
					if is_int(start):
						start = int(start)
						if is_int(end):
							end = int(end)
							i = start
							while i <= end:
								dl.download(i)
								i+=1
						else:
							print "Invalid option. The second argument must be an integer"
					else:
						print "Invalid option. The first argument must be an integer"
				except:
					print_help()
			except:
				print_help()
		elif choice == "-h" or choice == "--help":
			print_help()
		else:
			print "Invalid option. Try -h to get a list of all possible options"
	except:
		print_help()
if __name__== "__main__":
    main()
