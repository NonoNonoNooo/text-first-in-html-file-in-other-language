from googletrans import Translator
from bs4 import BeautifulSoup
import some_name

# create a translator object
translator = Translator()

# Open HTML file
with open('index.html', 'r', encoding='utf-8') as file:
    file_contents = file.read()

# the HTML code to be translated
# the text_editor function removes transfers in the file
# between tags otherwise we would have an error
html = some_name.text_editor(file_contents)

# parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# find all the text nodes and translate them
for node in soup.find_all(text=True):
    # ignore script and style tags
    if node.parent.name in ['script', 'style']:
        continue
    # translate the text and replace it in the HTML
    try:
        node.replace_with(translator.translate(node, dest='en').text)
    except:
        continue


result = soup.prettify()

# result file I created for example and comparison
# you can overwrite your source file
with open('result.html', 'w', encoding='utf-8') as file:
    file.write(result)

file.close()