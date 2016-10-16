from lxml import html
import requests
import sys

if (len(sys.argv) < 2) :
    print("Usage: python rtpi.py <stop_number>")
    exit(0)

stop_number = sys.argv[1]
link ='http://www.dublinbus.ie/RTPI/Sources-of-Real-Time-Information/?searchtype=view&searchquery='

page = requests.get(link+stop_number)
tree = html.fromstring(page.content)

dirty = tree.xpath('//table[@id="rtpi-results"]/child::*/child::*/child::text()')
times = [s.strip() for s in dirty]

# times no looks something like this: ['Route', 'Destination', 'Expected Time',
#'Notes', '15b', 'Benson Street via Rathmines', '20:57', '', '', '', '', '15b',
#'Benson Street via Rathmines', '21:28', '', '', '', '']
# this next part cleans it so we just have bus number, destination and time
# TODO: use a better xpath query to avoid most of this
info = []
i = 4
while(1):
    if (i >= len(times)):
        break
    info.append(times[i])
    info.append(times[i+1])
    info.append(times[i+2])
    i += 7

print(info)
# <table id="rtpi-results" cellspacing="0">
#                                 <tbody><tr class="yellow">
#                                     <th width="10%">
#                                         Route
#                                     </th>
#                                     <th width="40%">
#                                         Destination
#                                     </th>
#                                     <th width="20%">
#                                         Expected Time
#                                     </th>
#                                     <th width="30%">
#                                         Notes
#                                     </th>
#                                 </tr>
#
#                             <tr class="even">
#                                 <td>
#                                     15b
#                                 </td>
#                                 <td>
#                                     Benson Street via Rathmines
#                                 </td>
#                                 <td>
#                                     17:58
#                                 </td>
#                                 <td>
#                                     <img src="/Templates/Public/Styles/Images/icon-small-accessible.gif" alt="Accessible" class="">
#
#                                     <img src="/Templates/Public/Styles/Images/icon-small-R-pred.gif" alt="R Prediction" class="display_none">
#                                     <img src="/Templates/Public/Styles/Images/icon-small-E-pred.gif" alt="E Prediction" class="display_none">
#                                 </td>
#                             </tr>
#
#                             <tr class="odd">
#                                 <td>
#                                     15b
#                                 </td>
#                                 <td>
#                                     Benson Street via Rathmines
#                                 </td>
#                                 <td>
#                                     18:28
#                                 </td>
#                                 <td>
#                                     <img src="/Templates/Public/Styles/Images/icon-small-accessible.gif" alt="Accessible" class="">
#
#                                     <img src="/Templates/Public/Styles/Images/icon-small-R-pred.gif" alt="R Prediction" class="display_none">
#                                     <img src="/Templates/Public/Styles/Images/icon-small-E-pred.gif" alt="E Prediction" class="display_none">
#                                 </td>
#                             </tr>
#
#                             </tbody></table>
