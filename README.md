# graduationProject_nlp

1. 파일 및 폴더 설명<br>
dataloader: 입력한 경로의 데이터를 한꺼번에 부르기 위한 datalodader class의 기본 모듈 <br>
summary-reward-no-reference: KR-WordRank를 사용하기 위한 라이브러리<br>
textrank: TextRank를 사용하기 위한 라이브러리<br>

AbstractToTitle_krwordrank.py: KR-WordRank를 이용하여 초록에서 제목을 생성함<br>
AbstractToTitle_textrank.py: TextRank를 이용하여 초록에서 제목을 생성함<br>
CleanText.py: 한국어 텍스트 전처리 파일 (with Mecab)<br>
CsvToTxt.py: Csv 파일의 제목, 초록을 txt 파일로 변환하여 저장함<br>
DataPreProcessing_okt.py: 한국어 텍스트 전처리 파일 (with Okt)<br>
pdf_crawler.py: pdf를 csv 파일로 변환하여 저장함<br>


2. 실행 코드<br>

python AbstractToTitle_krwordrank.py --data_input_path=your_input_path --data_save_path=your_save_path<br>
python AbstractToTitle_textrank.py --data_input_path=your_input_path --data_save_path=your_save_path<br>
python CleanText_mecab.py --data_input_path=your_input_path --data_save_path=your_save_path<br>

3. 시연 영상<br>
youtube link: https://www.youtube.com/channel/UCvKmqttq--wUqcg53IRIbMw

4. 프로젝트 소개 <br>

자연어 처리를 이용하여 논문 초록에서 제목을 생성하는 abstract text summarization 모델.

5. reference <br>

TextRank: https://lovit.github.io/nlp/2019/04/30/textrank/ <br>
KR-WordRank: https://lovit.github.io/nlp/2019/05/01/krwordrank_sentence/

6. 기술 블로그 내용 <br>

안건희 - pdf 크롤링, 텍스트 전처리 및 정규화, 문서 요약 (TextRank, KR-WordRank) <br>
link: https://blog.naver.com/aws_lik <br>

김지환 - 자연어처리와 추출, 생성 요약에 대한 이론적 설명 <br>
link: https://deli-ce.tistory.com/2 <br>
