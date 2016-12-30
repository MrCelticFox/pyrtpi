from lxml import html
import requests
import sys

if (len(sys.argv) < 2):
    print("Usage: python rtpi.py <stop_number> [<bus_number>]")
    exit(0)

stop_number = sys.argv[1]
bus_number = sys.argv[2] if (len(sys.argv) == 3) else False
link ='http://www.dublinbus.ie/RTPI/Sources-of-Real-Time-Information/?searchtype=view&searchquery='

page = requests.get(link+stop_number)
tree = html.fromstring(page.content)

path = '//tr[@class="odd"]/td[position()<4]/text() | ' + \
        '//tr[@class="even"]/td[position()<4]/text()'
dirty = tree.xpath(path)
times = [s.strip() for s in dirty]

headings = '{:<8}{:<50}{:<8}\n'.format('Route', 'Destination', 'Expected time')
print(headings)

i = 0
while (i<len(times)):
    if (bus_number and (bus_number != times[i])):
        i += 3
        continue
    row = '{:<8}{:<50}{:<8}'.format(times[i],times[i+1],times[i+2])
    print(row)
    i += 3
