# graduationProject_nlp

1. 파일 및 폴더 설명
dataloader: 입력한 경로의 데이터를 한꺼번에 부르기 위한 datalodader class의 기본 모듈
summary-reward-no-reference: KR-WordRank를 사용하기 위한 라이브러리
textrank: TextRank를 사용하기 위한 라이브러리

AbstractToTitle_krwordrank.py: KR-WordRank를 이용하여 초록에서 제목을 생성함
AbstractToTitle_textrank.py: TextRank를 이용하여 초록에서 제목을 생성함
CleanText.py: 한국어 텍스트 전처리 파일 (with Mecab)
CsvToTxt.py: Csv 파일의 제목, 초록을 txt 파일로 변환하여 저장함
DataPreProcessing_okt.py: 한국어 텍스트 전처리 파일 (with Okt)
pdf_crawler.py: pdf를 csv 파일로 변환하여 저장함


2. 실행 코드

python AbstractToTitle_krwordrank.py --data_input_path=your_input_path --data_save_path=your_save_path
python AbstractToTitle_textrank.py --data_input_path=your_input_path --data_save_path=your_save_path
python CleanText_mecab.py --data_input_path=your_input_path --data_save_path=your_save_path
