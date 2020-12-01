from dataloader.base import BaseLoader
from rouge_score import rouge_scorer
from collections import namedtuple

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
        parser.add_argument('--data_input_path', type=str, default='output',
                            help='Base path of the input original texts.')
        parser.add_argument('--data_kr_input_path', type=str, default='input',
                            help='Base path of the input abstracted by krwordrank texts.')
        parser.add_argument('--data_txt_input_path', type=str, default='output',
                            help='Base path of the input abstracted by textrank texts.')
        parser.add_argument('--data_save_path', type=str, default='output',
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
        # print(self.text_name_list[text_index])
        if (text is None):
            text_path = os.path.join(self.args.data_input_path, ('%s.txt' % (self.text_name_list[text_index])))
            text = self._load_text(text_path)

        return text

    def _get_input_text_kr(self, text_index):
        text = None
        # print(self.text_name_list[text_index])
        if (text is None):
            text_path = os.path.join(self.args.data_kr_input_path, ('%s.txt' % (self.text_name_list[text_index])))
            text = self._load_text(text_path)

        return text

    def _get_input_text_txt(self, text_index):
        text = None
        # print(self.text_name_list[text_index])
        if (text is None):
            text_path = os.path.join(self.args.data_txt_input_path, ('%s.txt' % (self.text_name_list[text_index])))
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

basic_loader = BasicLoader()
basic_loader.parse_args()
basic_loader.prepare()
text_list = list(range(basic_loader.get_num_texts()))
idx = 0

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
    krwordrank_abs = basic_loader._get_input_text_kr(idx)
    txt_abs = basic_loader._get_input_text_txt(idx)
    original = basic_loader._get_input_text(idx)


    scorer = rouge_scorer.RougeScorer(['rouge1'], use_stemmer=True)
    scores_kr = scorer.score(krwordrank_abs, krwordrank_abs)
    scores_txt = scorer.score(original, txt_abs)

    print('kr:', scores_kr)
    print('txt: ', scores_txt)
