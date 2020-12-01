from __future__ import print_function
from dataloader.base import BaseLoader
from krwordrank.sentence import summarize_with_sentences
from collections import namedtuple
from konlpy.tag import Komoran

import os
import argparse
import copy

class BasicLoader(BaseLoader):
    def __init__(self):
        super().__init__()

    # /Users/angeonhui/Desktop/data/crawled_txt/abstract
    # /Users/angeonhui/Desktop/data/abstracted_abs
    def parse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--data_input_path', type=str, default='input', help='Base path of the input texts.')
        parser.add_argument('--data_save_path', type=str, default='output',
                            help='Base path of the saving texts.')
        parser.add_argument('--keyword_save_path', type=str, default='output',
                            help='Base path of the saving texts.')

        self.args, remaining_args = parser.parse_known_args()
        return copy.deepcopy(self.args), remaining_args

    def prepare(self):
        # retrieve text name list
        input_path = os.path.join(self.args.data_input_path)
        # print(self.args.data_input_path)
        self.text_name_list = [os.path.splitext(f)[0] for f in os.listdir(input_path) if f.lower().endswith('.txt') and f != '.txt']
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
        save_path = os.path.join(self.args.data_save_path, ('%s.txt' % (self.text_name_list[text_index])))
        with open(save_path, 'w') as f:
            f.write(text)

    def _save_keyword(self, text, text_index):
        save_path = os.path.join(self.args.keyword_save_path, ('%s.txt' % (self.text_name_list[text_index])))
        with open(save_path, 'w') as f:
            f.write(text)

basic_loader = BasicLoader()
basic_loader.parse_args()
basic_loader.prepare()
text_list = list(range(basic_loader.get_num_texts()))
idx = 0

# lexrank = LexRank()  # can init with various settings
#
from konlpy.tag import Mecab
from textrank import KeysentenceSummarizer
mecab = Mecab()

def mecab_tokenizer(sent):
    words = mecab.pos(sent)
    words = [w for w in words if w[1] in ('NNG' or 'NNP' or 'VA' or 'VV' or 'XR')]
    return words

Performance = namedtuple('Performance', 'n_keywords n_keysents rouge1'.split())

def rouge1(keywords, keysents, tokenize, n_keywords=None, n_keysents=None):
    if n_keywords is None:
        n_keywords = [10, 20, 30, 50, 100]
    if n_keysents is None:
        n_keysents = [3, 5, 10, 20, 30]

    keysents = [tokenize(sent) for sent in keysents]
    performance = []
    for n_keyword in n_keywords:
        keywords_ = {w for w, _ in sorted(keywords.items(), key=lambda x: -x[1])[:n_keyword]}
        for n_keysent in n_keysents:
            sents = keysents[:n_keysent]
            word_set = {w for sent in sents for w in sent}
            word_set = {w for w in word_set if w in keywords_}
            recall = len(word_set) / n_keyword
            performance.append(Performance(n_keyword, n_keysent, recall))
    return performance

while idx in text_list:
    text = basic_loader._get_input_text(idx)
    num_keysents = 1

    text = text.split('.')
    if ' ' in text:
        text = list(filter(lambda a: a != ' ', text))
    if '' in text:
        text = list(filter(lambda a: a != '', text))

    print(len(text), text)
    keysents = ''
    if len(text)<=num_keysents:
        keysents = text[0]
        keysents = '. '.join(keysents)
    else:
        keywords, keysents = summarize_with_sentences(
            text,
            diversity=0.7,
            num_keysents=1,
            scaling=lambda x: 1,
            verbose=False,
        )

        keysents = '. '.join(keysents)
        # print(keysents)

    basic_loader._save_text(keysents, idx)

    # score = rouge1(keywords, keysents, mecab_tokenizer)

    # print(idx, score)

    idx += 1
#     lexrank.summarize(text)
#     summaries = lexrank.probe(1)
#     idx += 1
#     for text in summaries:
#         print(text)