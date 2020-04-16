import retinasdk
liteClient = retinasdk.LiteClient("")


def get_topic(titles):
    paragraph = ""
    for title in titles:
        paragraph += title
    keywords = liteClient.getKeywords(paragraph.encode('utf-8'))
    for index, title in enumerate(titles):
        if keywords[0] in title.lower():
            return index
