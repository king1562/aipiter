print('hello world')
print('하이')
print pr('하이')
import pandas as pd

# 예시로 임의 종가(Close)와 거래량(Volume) 데이터를 만듭니다.
# 실제로는 주식 API나 CSV로부터 데이터를 불러와야 합니다.
data = {
    'Ticker': ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'TSLA'],
    'Close':  [160.25, 280.11, 105.45,  95.75,  200.10],
    'Volume': [50_000_000, 35_000_000, 28_000_000, 25_000_000, 20_000_000]
}

df = pd.DataFrame(data)

# 1) 시장가치(Market Value)를 계산합니다: 종가 × 거래량
df['Market_Value'] = df['Close'] * df['Volume']

# 2) 종목별 가중치(Weight) 계산: 각 종목의 시장가치 / 전체 시장가치 합
total_market_value = df['Market_Value'].sum()
df['Weight'] = df['Market_Value'] / total_market_value

# 3) base 값을 임의로 1000이라 놓고, 가중치 합에 곱하여 추정 지수를 계산
base = 1000
index_value = base * df['Weight'].sum()

# 결과 출력
print(df)
print(f"\n추정 지수 (간단 예시): {index_value:.2f}")
