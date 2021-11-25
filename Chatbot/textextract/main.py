from textextract.linkextract import Try
import os
import re
from googletrans import Translator
import time


obj = Try()
obj.html_collect()
f = open("htmls.txt", "w+")
for element in obj.reformat():
    f.write(element+'\n')
f.close()

obj = Try()
obj.linkextract()

with open("../textextract/unreformat.txt", "r+", encoding='utf-8') as data:
    contents = data.readlines()
    new_code = '[' + ',\n'.join(contents) + ']'
    f = open("../textextract/Output.txt", "w", encoding='utf-8')
    f.write(new_code)
f.close()

with open("../textextract/Output.txt", "r+", encoding='utf-8') as line:
    collect = line.readlines()






    count = 0
    for line in collect:
        if line[0] == ',' or line[0] == '[' or line[0] == '\n' or line[0] == ']':
            print("")
        else:


            with open("../textextract/copy.txt", "a", encoding='utf-8') as f:
                f.write(line)
                f.close

if os.path.exists("halfcompleted.txt"):
    open('halfcompleted.txt', 'w').close()

with open("../textextract/copy.txt", "r+", encoding='utf-8') as data:
    contents = data.readlines()
    n = len(contents)
    text = []
    print(n)
    count = 0
    for line in contents:
        if count < n - 1:
            myString = contents[count].replace("\u00A0", " ")
            f = open("halfcompleted.txt", "a", encoding='utf-8')
            print(re.sub(r"^\s+", "", contents[count + 1]), sep='', file=f)

            f.close()
            count += 1



        else:
            continue
print(text)

data.close()

if os.path.exists("../textextract/ok.txt"):
    open('../textextract/ok.txt', 'w').close()
with open("halfcompleted.txt", "r+", encoding='utf-8') as data:
    contents = data.readlines()
    for line in contents:
        f = open("../textextract/ok.txt", "a", encoding='utf-8')
        if line == '\n':
            continue
        print(line.rstrip("\n"), file=f)
data.close

if os.path.exists('../textextract/english.txt'):
    open('../textextract/english.txt', 'w').close()

translator = Translator()
f = open("../textextract/ok.txt", "r", encoding='utf-8')
sample = f.readlines()
count = 0
i = 100
translated = []

for line in sample:
    with open("../textextract/english.txt", "a", encoding='utf-8') as english:
        try:
            if count == i:
                time.sleep(1.1)
                translated = translator.translate(sample[count], dest="en")
                print(translated)
                english.write(translated.text + '\n')
                english.close()
                i += i
                count += 1
            else:
                translated = translator.translate(sample[count], dest="en")
                time.sleep(0.15)
                print(translated)
                english.write(translated.text + '\n')
                english.close()
                count += 1

        except Exception as e:
            print(e)
            count += 1


f.close()
