import requests
from xml.etree import ElementTree
import re
url = "https://vanmapp1.vancouver.ca/googleKml/rezoning_applications/?t=1708480550711&_=1708480550447"
response = requests.get(url)

tree = ElementTree.fromstring(response.content)
folder = tree[0][2]
folder = folder[1:]

text_file = open("rezoning-output.txt", "w")
for child in folder:
    #child[0]: address
    #child[1]: status? "Approved", "Rezoning"
    #child[2]: type? "approved_market", "approved_non_market", "approved_strata", "rezoning_market", ...

    text_file.write("\n%s\n" % child[0].text)

    html = child[3].text
    match = re.search(r"(?<=href=').+(?=' )",html)
    if match:
        text_file.write("%s\n" % match[0])

text_file.close()
