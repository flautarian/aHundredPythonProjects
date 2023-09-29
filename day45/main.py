import os
from bs4 import BeautifulSoup
import requests

html_request = requests.get("https://news.ycombinator.com/news")

script_dir = os.path.dirname(__file__)

def sortUpvotes(dict):
  return dict['upvotes']

#with open(script_dir + "/website.html", encoding='utf8') as file:
#     contents = file.read()

ycombinator_text = html_request.text

soup = BeautifulSoup(ycombinator_text, "html.parser")

# print(soup.prettify())
# print(soup.title.string)

all_tr = soup.findAll(name="tr")

all_links = []

max_pop = 0

for i in range(0, len(all_tr)):
    if not all_tr[i].get("class") == None and "athing" in all_tr[i].get("class") and i + 1 < len(all_tr):
        anchor_points = next((x for x in all_tr[i+1].findAll("span") if "score" in x.get("class")), None)
        if not anchor_points == None :
            anchor_points = int(anchor_points.contents[0].split(" ")[0])
            link_span = next((x for x in all_tr[i].findAll("span") if "titleline" in x.get("class")), None)
            link = link_span.find("a")
            all_links.append({
                "upvotes": anchor_points,
                "link": link.get("href"),
                "title": link.contents[0]
            })

all_links.sort(key=sortUpvotes, reverse=True)

for i in range(0, min(len(all_links), 10)):
    print(f"{all_links[i]['link']} - {all_links[i]['upvotes']}")
    
# heading = soup.find(name="h1", id="name")
# print(heading)
    
