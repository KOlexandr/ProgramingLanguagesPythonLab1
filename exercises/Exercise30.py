__author__ = 'KOL'

html = open("links.html", 'w')
links = open("links.csv", 'r')

html.write("<!DOCTYPE html>\n<html>\n<head>\n")
html.write("<title>Links</title>\n")
html.write("</head>\n<body>\n")

lines = links.readlines()
links.close()

for i in lines:
    tmp = str(i).replace("\n", "")
    href = tmp.split(",")[0]
    description = tmp.split(",")[1]
    html.write("<a href=\"" + href + "\" target=\"_blank\">" + description + "</a>\n")

html.write("</body>\n</html>\n")
html.close()