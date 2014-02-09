import urllib.request
import re
from Tools.Scripts.ftpmirror import raw_input

__author__ = 'KOL'


def get_simple_info_about_book_from_amazon(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    matcher = re.compile(r'<span id="btAsinTitle"  >(?:["a-zA-Z0-9-, \(\)]+)[ ]*<span')
    html = str(response.read())

    findall = matcher.findall(html)
    if len(findall) != 0:
        title = findall[0].replace('<span id="btAsinTitle"  >', "").replace("<span", "")
    else:
        title = None

    matcher = re.compile(r'<b class="priceLarge">\$\d+\.?(?:\d+|)</b>|<span class="rentPrice">\$\d+\.?(?:\d+|)</span>')
    findall = matcher.findall(html)
    if len(findall) != 0:
        price = findall[0].replace('<b class="priceLarge">', "").replace('</b>', "").\
            replace('<span class="rentPrice">', "").replace("</span>", "")
    else:
        price = None

    matcher = re.compile(r'<span class="availGreen">[\.a-zA-Z 0-9-_]+</span>')
    findall = matcher.findall(html)
    if len(findall) != 0:
        status = findall[0].replace('<span class="availGreen">', "").replace('.</span>', "")
    else:
        status = None
    return title, price, status

#0132269937
#0672329786
#1449355730
#193518220X
while True:
    isbn = raw_input("Please, input ISBN of book on Amazon.com: ")
    title, price, status = get_simple_info_about_book_from_amazon("http://www.amazon.com/dp/" + isbn)
    print(title, price, status)