from lxml import html
import requests
import sys

if (len(sys.argv) < 2):
    print("Usage: python rtpi.py <stop_number>")
    exit(0)

stop_number = sys.argv[1]
link ='http://www.dublinbus.ie/RTPI/Sources-of-Real-Time-Information/?searchtype=view&searchquery='

page = requests.get(link+stop_number)
tree = html.fromstring(page.content)

path = '//tr[@class="odd"]/td[position()<4]/text() | ' + \
        '//tr[@class="even"]/td[position()<4]/text()'
dirty = tree.xpath(path)
times = [s.strip() for s in dirty]

headings = '{:<8}{:<40}{:<8}\n'.format('Route', 'Destination', 'Expected time')
print(headings)

i = 0
while(i<len(times)):
    row = '{:<8}{:<40}{:<8}'.format(times[i],times[i+1],times[i+2])
    print(row)
    i += 3
