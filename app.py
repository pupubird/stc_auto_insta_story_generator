import feedparser
import textwrap
from datetime import date
from bs4 import BeautifulSoup
from generate_story import output_cert
from keywords_extract import get_topic
from generate_short_link import generate_short_link

INVOLED_DAY = 0


def generate(index):
    entry = NewsFeed.entries[index]
    soup = BeautifulSoup(
        entry.summary_detail['value'].encode('utf-8'), 'html.parser')
    title = textwrap.wrap(entry.title, width=35)
    link = textwrap.wrap(entry.link, width=35)

    output_title, output_link, output_text = "", "", ""
    for i in title:
        output_title += i+"\n"
    for i in link:
        output_link += i + "\n"

    key = ""
    with open("api_key.txt", 'r')as f:
        key = f.read().replace(" ", "").replace("\n", "")

    res = generate_short_link(
        entry.link, key, 'stc-insta-'+str(date.today().month)+"-"+str(date.today().day))
    output_link = res['url'].get('shortLink', output_link)

    output_link = "Read more on: \n"+output_link

    paragraphs = soup.get_text().split(". ")
    text_len = 0
    for paragraph in paragraphs:
        text = textwrap.wrap(paragraph, width=35)
        text_len += len(text)
        for i in text:
            output_text += i + "\n"
        output_text += "\n"

    output_cert('title', output_title, len(title))
    output_cert('link', output_link, len(link))
    output_cert('summary', output_text, text_len)


NewsFeed = feedparser.parse(
    "http://feeds.feedburner.com/TechCrunch/")

titles = []
amount = 0
try:
    for entry in NewsFeed.entries:
        arr = entry.published.split(" ")
        if int(arr[1]) >= date.today().day - INVOLED_DAY:
            amount += 1
    for i in range(amount):
        titles.append(NewsFeed.entries[i].title)
    index = get_topic(titles)
    generate(index)
except TypeError:
    print("No news for now, try to adjust INVOLED_DAY more than or equal to 1 to include yesterday news (2 days ago if adjusted to 2)")
