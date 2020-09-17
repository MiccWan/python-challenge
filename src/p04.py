import urllib.request
import re

base_link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing_id = "12345"
while nothing_id:
    html = urllib.request.urlopen(base_link + nothing_id).read().decode()
    print(nothing_id, html)
    nothing_id = re.findall('nothing is ([0-9]*)', html)[0]
print(html)

# 16044
# 8022
# peak.html