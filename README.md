# Instagram story generator

`pip install -r requirements.txt`

`python app.py`

## Pre-requisite

1. get [cutt.ly api key](https://cutt.ly/cuttly-api)

    - The API is available only to registered users. API key can be generate in account edit page

2. paste the api key in the api_key.txt directly, save it.

## How it works

1. Get rss tech news feed from [http://feeds.feedburner.com/TechCrunch/](http://feeds.feedburner.com/TechCrunch/)

2. For each news, do keywords extractions from the title

3. The highest weight of the title wins

4. generate the instagram story based on the news into folder output/
