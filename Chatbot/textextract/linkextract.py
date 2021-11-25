import bs4
from bs4 import BeautifulSoup

import urllib
import urllib.request


class Try:
    def html_collect(self):
        r = urllib.request.urlopen('https://www.iit.uni-miskolc.hu/').read()
        soup = BeautifulSoup(r, "lxml")
        type(soup)
        bs4.BeautifulSoup

        links = []
        for link in soup.find_all('a'):
            # print(link.get('href'))
            links.append(link.get('href'))
            link.get('href')

        return links

    def reformat(self):
        links = self.html_collect()
        n = len(links)
        reformatted = []
        for i in range(0, n - 1):
            if links[i] != '#top' and links[i] is not None and links[i] != '/':

                reformatted.append(links[i])
            else:
                i += 1
        new_n = len(reformatted)
        last_reformatted = []
        for i in range(0, new_n - 1):
            if reformatted[i][0] == '/':
                str1 = reformatted[i]
                list1 = list(str1)
                list1[0] = "https://www.iit.uni-miskolc.hu/"
                str1 = ''.join(list1)
                last_reformatted.append(str1)
            else:
                last_reformatted.append(reformatted[i])
                i += 1

        return last_reformatted



    def linkextract(self):
            with open("../textextract/htmls.txt", "r+") as data:

                contents = data.readlines()
                print(contents)
                print(len(contents))
                print(contents[0])

            try:
                for x in contents:
                    with urllib.request.urlopen(x) as response:
                        html = response.read()
                        soup = BeautifulSoup(html, "lxml")
                        type(soup)
                        text_only = soup.get_text()
                        with open("../textextract/unreformat.txt", "a", encoding='utf-8') as f:
                            f.write(text_only)
                            f.close
            except Exception as e:
                print(e)




obj = Try()
f = open("htmls.txt", "w+")
for element in obj.reformat():
    f.write(element+'\n')
f.close()




