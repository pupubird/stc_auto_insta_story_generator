import feedparser
import textwrap
from bs4 import BeautifulSoup
from generate_story import output_cert
from keywords_extract import get_topic


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
for entry in NewsFeed.entries:
    titles.append(entry.title)
index = get_topic(titles)
generate(index)
