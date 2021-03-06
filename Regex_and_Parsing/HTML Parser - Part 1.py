from html.parser import HTMLParser


class HtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start : '+tag)
        for attr in attrs:
            print('-> '+attr[0]+' > '+(attr[1] if attr[1] else 'None'))

    def handle_endtag(self, tag):
        print('End   : '+tag)

    def handle_startendtag(self, tag, attrs):
        print('Empty : '+tag)
        for attr in attrs:
            print('-> '+attr[0]+' > '+attr[1] if attr[1] else None)

HtmlParser = HtmlParser()

for line in range(int(input())):
    HtmlParser.feed(input())