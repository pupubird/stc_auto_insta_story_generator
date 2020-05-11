import feedparser
import textwrap
from datetime import date
from bs4 import BeautifulSoup
from generate_story import output_cert
from keywords_extract import get_topic
from generate_short_link import generate_short_link

INVOLED_DAY = 2


def generate(index):
    entry = NewsFeed.entries[index]
    soup = BeautifulSoup(
        entry.summary_detail['value'].encode('utf-8'), 'html.parser')
    title = textwrap.wrap(entry.title, width=40)
    link = textwrap.wrap(entry.link, width=40)

    output_title, output_link, output_text = "", "", ""
    for i in title:
        output_title += i+"\n"
    for i in link:
        output_link += i + "\n"

    key = ""
    with open("api_key.txt", 'r')as f:
        key = f.read().replace(" ", "").replace("\n", "")

    res = generate_short_link(
        link, key)
    output_link = res['shortenedLink'] or link

    output_link = "Read more on: \n"+output_link + \
        "\n"+"(or you may dm us to get the link!)"

    paragraphs = soup.get_text().split(". ")
    text_len = 0
    for paragraph in paragraphs:
        text = textwrap.wrap(paragraph, width=40)
        text_len += len(text)
        for i in text:
            output_text += i + "\n"
        output_text += "\n"

    output_cert('title', output_title, len(title))
    output_cert('link', output_link, len(link))
    output_cert('summary', output_text, text_len)


NewsFeed = feedparser.parse("https://www.techrepublic.com/rssfeeds/articles/")

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
