import csv
from konlpy.tag import Okt
import pandas as pd
from pandas import DataFrame as df

okt = Okt()
path = '/Users/angeonhui/Desktop/2020학년도 2학기/1. 수업/02. 졸업프로젝트 20-2/paper crawling/crawled_csv/스마트폰 사용자의 해석수준에 따른 스마트폰 자기통제에 관한 연구.csv'
new_path = '/Users/angeonhui/Desktop/2020학년도 2학기/1. 수업/02. 졸업프로젝트 20-2/paper crawling/crawled_csv/스마트폰 사용자의 해석수준에 따른 스마트폰 자기통제에 관한 연구_revised.csv'

def spacing_okt(wrongSentence):
    tagged = okt.pos(wrongSentence)
    corrected = ""
    for i in tagged:
        if i[1] in ('Josa', 'PreEomi', 'Eomi', 'Suffix', 'Punctuation'):
            corrected += i[0]
        else:
            corrected += " "+i[0]
    print(corrected)
    if not corrected:
        return corrected+'.'
    if corrected[0] == " ":
        corrected = corrected[1:]
    return corrected

def spacing_join(text):
    text = text.split('.')
    res = []

    for sentence in text:
        sentence = spacing_okt(sentence)
        res.append(' ' + sentence)

    return ''.join(res)

f = open(path, 'r', encoding='utf-8')
rdr = csv.reader(f)
text = pd.read_csv(path)
text_abs = ''
text_body = ''
for line in rdr:
    text_abs = line[2]
    text_body = line[5]

print(text_abs)
print(text_body)

new_abs = spacing_join(text_abs)
new_body = spacing_join(text_body)

text['abstract'] = new_abs
text['body'] = new_body

text.to_csv(new_path)

f.close()
