import pandas as pd
import csv
import os

path = '/Users/angeonhui/Downloads/dataset' # 바꿀 csv 파일이 저장되어있는 경로
path_save_info = '/Users/angeonhui/Desktop/data/cralwed_txt/info' # information 항목을 저장할 경로
path_save_abstract = '/Users/angeonhui/Desktop/data/cralwed_txt/abstract' # abstract 항목을 저장할 경로
text_name_list = [os.path.splitext(f)[0] for f in os.listdir(path) if f.lower().endswith('.csv')] # 파일 이름을 따로 저장한다.
n = len(text_name_list)

for i in range(n):
    path_save_info = '/Users/angeonhui/Desktop/data/crawled_txt/info' # 경로 초기화. 하지 않으면 이전에 만든 경로 뒤에 계속 파일 이름이 붙는다.
    path_save_abstract = '/Users/angeonhui/Desktop/data/crawled_txt/abstract'  # 경로 초기화. 하지 않으면 이전에 만든 경로 뒤에 계속 파일 이름이 붙는다.
    path_save_body = '/Users/angeonhui/Desktop/data/crawled_txt/body' # 경로 초기화. 하지 않으면 이전에 만든 경로 뒤에 계속 파일 이름이 붙는다.

    path_open = os.path.join(path, ('%s.csv' % (text_name_list[i]))) # i번째 파일의 경로
    path_save_info = os.path.join(path_save_info,('%s.txt' % (text_name_list[i]))) # i번째 파일의 info를 저장할 경로. txt를 바꾸면 파일 형식을 바꿀 수 있다.
    path_save_abstract = os.path.join(path_save_abstract,
                                  ('%s.txt' % (text_name_list[i])))  # i번째 파일의 info를 저장할 경로. txt를 바꾸면 파일 형식을 바꿀 수 있다.
    path_save_body = os.path.join(path_save_body,('%s.txt' % (text_name_list[i]))) # i번째 파일의 abstract를 저장할 경로. txt를 바꾸면 파일 형식을 바꿀 수 있다.
    print(text_name_list[i])

    text = pd.read_csv(path_open, encoding='utf-8') # csv 파일 읽어오기

    sliceData = text.loc[:, 'information']  # information 열만 자름
    sliceData.to_csv(path_save_info, index=False)  # txt 저장

    sliceData = text.loc[:, 'abstract']  # abstract 열만 자름
    sliceData.to_csv(path_save_abstract, index=False)  # txt 저장

    sliceData = text.loc[:, 'body']  # body 열만 자름
    sliceData.to_csv(path_save_body, index=False)  # txt 저장

    # f_info = open(path_save_info, 'w', encoding='utf-8')
    # f_abstract = open(path_save_abstract, 'w', encoding='utf-8')

    # with open(path_save_info, "w") as file:
    #     file.write(info)
    # with open(path_save_abstract, 'w') as file:
    #     file.write(abstract)



