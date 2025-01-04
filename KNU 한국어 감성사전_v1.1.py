import pandas as pd

# 데이터는 positive.txt와 negative.txt 파일 로드
with open('data/positive.txt', 'r', encoding='utf-8') as positive_file, open('data/negative.txt', 'r', encoding='utf-8') as negative_file:
    positive_words = [line.strip() for line in positive_file.readlines()]
    negative_words = [line.strip() for line in negative_file.readlines()]


# 감정 점수 초기화 (사전에 감정 점수가 있는 경우 사용)
sentiment_scores = {}

# CSV 파일에서 텍스트 데이터 읽기
df = pd.read_csv('data/데일리샷_AOS_reviews.csv')


# 예시 텍스트가 저장된 열 선택 (여기서는 'Text' 열 사용)
texts = df['content']


# 감정 분석 및 감정 점수 계산 함수
def sentiment_analysis(text):
    # 텍스트를 단어로 분할
    words = text.split()

    # 긍정어와 부정어 카운트 초기화
    positive_count = 0
    negative_count = 0

    # 감정 단어 딕셔너리 초기화
    sentiment_words = {'긍정어': [], '부정어': []}

    # 텍스트의 각 단어를 확인하고 긍정어와 부정어 카운트 및 딕셔너리 업데이트
    for word in words:
        if word in positive_words:
            positive_count += 1
            sentiment_words['긍정어'].append(word)
        elif word in negative_words:
            negative_count += 1
            sentiment_words['부정어'].append(word)

    # 감정 점수 계산
    sentiment_score = round((positive_count - negative_count) / len(words),3)

    return sentiment_score, sentiment_words


# "감정 분석 결과" 열을 튜플 형식으로 반환
df['감정 분석 결과'] = texts.apply(sentiment_analysis)


# 튜플을 분할하여 열을 추가
df[['감정 점수', '감정 단어']] = pd.DataFrame(df['감정 분석 결과'].to_list(), index=df.index)


# DataFrame의 처음 몇 행 출력
df.iloc[1:15, 8:]


