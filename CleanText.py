from __future__ import print_function
from dataloader.base import BaseLoader
from konlpy.tag import Okt
import importlib
import argparse
import parser
import importlib
import json
import os
import copy
from konlpy.tag import Mecab
import re
from lexrankr import LexRank


class BasicLoader(BaseLoader):
    def __init__(self):
        super().__init__()

    def parse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--data_input_path', type=str, default='/Users/angeonhui/Desktop/data/crawled_txt/body', help='Base path of the input texts.')

        self.args, remaining_args = parser.parse_known_args()
        return copy.deepcopy(self.args), remaining_args

    def prepare(self):
        # retrieve text name list
        print(self.args.data_input_path)
        input_path = os.path.join(self.args.data_input_path)
        self.text_name_list = [os.path.splitext(f)[0] for f in os.listdir(input_path) if f.lower().endswith('.txt') and f != '.txt']
        print(self.text_name_list)
        print('data: %d texts are prepared' % (len(self.text_name_list)))

    def get_num_texts(self):
        return len(self.text_name_list)

    def _get_input_text(self, text_index):
        text = None

        if (text is None):
            text_path = os.path.join(self.args.data_input_path, ('%s.txt' % (self.text_name_list[text_index])))
            text = self._load_text(text_path)

        return text

    def _load_text(self, path):
        f = open(path, 'r')
        text = f.read()
        f.close()
        return text

    def _save_text(self, text, text_index):
        path = self.args.data_input_path
        save_path = os.path.join(path, ('%s.txt' % (self.text_name_list[text_index])))
        with open(save_path, 'w') as f:
            f.write(text)


mecab = Mecab()

def spacing_mecab(wrongSentence):
    tagged = mecab.pos(wrongSentence)
    corrected = ""
    for i in tagged:
        # print(i[0], i[1])

        if i[1] in ('JKS', 'JKC', 'JKG', 'JKO', 'JKB' ,'JKV', 'JKQ', 'JX', 'JC', 'EP', 'EC', 'ETN', 'ETM', 'XPN', 'XSN', 'XSV', 'SA', 'SF'):
            corrected += i[0]
        else:
            corrected += " "+i[0]

    if not corrected:
        return corrected+'.'
    if corrected[0] == " ":
        corrected = corrected[1:]
    return corrected

def clean_sentense(txt):
    pattern = '(\d\d\d-\d\d\d\d-\d\d\d\d)'  # 전화번호 제거 (000-0000-0000),\d: 숫자 1개
    txt = re.sub(pattern=pattern, repl='', string=txt)
    pattern = '([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'  # E-mail제거, a-z 사이의 문자,
    txt = re.sub(pattern=pattern, repl='', string=txt)
    pattern = '(http|ftp|https)://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'  # URL제거
    txt = re.sub(pattern=pattern, repl='', string=txt)
    pattern = '([ㄱ-ㅎㅏ-ㅣ]+)'  # 한글 자음, 모음 제거
    txt = re.sub(pattern=pattern, repl='', string=txt)
    pattern = '<[^>]*>'  # HTML 태그 제거
    txt = re.sub(pattern=pattern, repl='', string=txt)
    pattern = '[^\w\s.]'  # 특수기호제거
    txt = re.sub(pattern=pattern, repl='', string=txt)
    pattern = 'ˇˇ+'  # removing info and tab
    txt = re.sub(pattern=pattern, repl='', string=txt)
    pattern = 'bsc'  # removing info and tab
    txt = re.sub(pattern=pattern, repl='', string=txt)
    pattern = 'body'  # removing info and tab
    txt = re.sub(pattern=pattern, repl='', string=txt)
    pattern = '  +'  # removing info and tab
    txt = re.sub(pattern=pattern, repl='', string=txt)

    return txt


basic_loader = BasicLoader()
basic_loader.parse_args()
basic_loader.prepare()
text_list = list(range(basic_loader.get_num_texts()))
idx = 0

while idx in text_list:
    text = basic_loader._get_input_text(idx)
    text = clean_sentense(text)
    text = spacing_mecab(text)

    print(text)
    basic_loader._save_text(text, idx)
    idx += 1