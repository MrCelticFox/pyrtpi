from lxml import html
import requests
import sys
from getopt import getopt

def printHelp():
    print("Usage: python rtpi.py <stop_number> [OPTIONS]\n")
    print("-n <num>\tnumber of results to print")
    print("-b <bnum>\tspecify a bus number to limit results to a specific route")
    print("-h\tprint this help message and exit")
    exit(0)

if (len(sys.argv) < 2):
    printHelp()
    exit(0)

stop_number = sys.argv[1]
bus_number = ''
n_results = 0

# handle options
options = getopt(sys.argv[2:], "n:b:h")[0]
for option in options:
    if option[0] == '-n':
        n_results = int(option[1])
    elif option[0] == '-b':
        bus_number = option[1]
    elif option[0] == '-h':
        printHelp()

# retrieve information from Dublin bus website
link ='http://www.dublinbus.ie/RTPI/Sources-of-Real-Time-Information/?searchtype=view&searchquery='
page = requests.get(link+stop_number)
tree = html.fromstring(page.content)
path = '//tr[@class="odd"]/td[position()<4]/text() | ' + \
        '//tr[@class="even"]/td[position()<4]/text()'
dirty = tree.xpath(path)
times = [s.strip() for s in dirty]

if (n_results == 0): # if no limit set then show all results
    n_results = len(times)/3

headings = '{:<8}{:<50}{:<8}\n'.format('Route', 'Destination', 'Expected time')
print(headings)

i = 0
while (i<len(times)):
    # if set, show only results for the specified route
    if (bus_number != '' and bus_number != times[i]):
        i += 3
        continue

    if (n_results == 0):
        break

    row = '{:<8}{:<50}{:<8}'.format(times[i],times[i+1],times[i+2])
    print(row)
    n_results -= 1
    i += 3
