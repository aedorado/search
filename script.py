from all_imports import *

parser = argparse.ArgumentParser()

parser.add_argument('-b', '--bing', action='store_true', help='Bing Search')
parser.add_argument('-d', '--duck', action='store_true', help='DuckDuckGo Search')
parser.add_argument('-g', '--google', action='store_true', help='Google Search (default)')
parser.add_argument('query', nargs='*')

args = parser.parse_args() 
print args.query

query = ' '.join(args.query)
print query

url = 'https://www.google.com/#q=' + query	# google search by default
if args.bing:
	url = 'http://www.bing.com/search?q=' + query
elif args.duck:
	url = 'https://duckduckgo.com/?q=' + query

webbrowser.open(url)
sys.exit(0)
