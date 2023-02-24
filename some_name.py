from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = ""
        self.inside_tag = False
        self.inside_style = False

    def handle_data(self, data):
        if self.inside_tag or self.inside_style:
            self.result += data.strip()
        else:
            self.result += data.strip().replace("\n", " ")

    def handle_starttag(self, tag, attrs):
        self.inside_tag = True
        self.result += f"<{tag}"
        if tag == "style":
            self.inside_style = True
        for attr in attrs:
            self.result += f' {attr[0]}="{attr[1]}"'
        self.result += ">"

    def handle_endtag(self, tag):
        self.inside_tag = False
        if tag == "style":
            self.inside_style = False
        self.result += f"</{tag}>"

    def handle_startendtag(self, tag, attrs):
        self.result += f"<{tag}"
        for attr in attrs:
            self.result += f' {attr[0]}="{attr[1]}"'
        self.result += "/>"

parser = MyHTMLParser()

def text_editor(text):
    global parser
    parser.feed(text)
    return parser.result