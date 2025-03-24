print('hello, world')
print ('안녕')
print('코딩')
import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

def load_tickers():
    """
    예시로 NASDAQ 상위 10개 종목을 가정합니다.
    실제로는 NASDAQ 상위 500개 종목 리스트(티커)를 CSV나 DB에서 불러오면 됩니다.
    """
    # 예시 티커 (시가총액 기준 일부 대표 종목)
    tickers = [
        "AAPL", "MSFT", "AMZN", "GOOGL", "GOOG",
        "NVDA", "TSLA", "META", "ADBE", "NFLX",
        # 실제로는 500개 목록 필요
    ]
    return tickers

def fetch_market_data(tickers, start_date, end_date):
    """
    yfinance 라이브러리를 통해 특정 기간 동안 각 티커의 시가총액(Market Cap) 및 주가 데이터를 가져옵니다.
    yfinance는 시가총액을 직접 제공하지 않으므로, 예시에서는 단순히 시가, 종가 등을 사용합니다.
    실제로는 추가 데이터 소스가 필요할 수 있습니다.
    """
    data = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        # 주가 히스토리
        hist = stock.history(start=start_date, end=end_date)
        
        # 시가총액이 필요한 경우, yfinance의 info 데이터를 참조(단, 완전 일치하지 않을 수 있음)
        # market_cap = stock.info.get('marketCap', None)
        
        # 열린 값(Open), 종가(Close), 거래량(Volume)을 DataFrame으로 저장
        hist_df = hist[['Open', 'Close', 'Volume']].copy()
        hist_df['Ticker'] = ticker
        
        # 간단 예시를 위해 최근 종가와 거래량, 티커만 담아서 저장
        if len(hist_df) > 0:
            latest_data = hist_df.iloc[-1].to_dict()
            data[ticker] = latest_data
    
    return pd.DataFrame.from_dict(data, orient='index')

def calculate_index(df):
    """
    간단한 '추정 지수' 계산 예시:
    각 종목의 종가 * 거래량의 총합을 모든 종목 합과 비교하여 비율을 구하고,
    이를 통해 지수를 산술적으로 구성합니다.
    """
    if df.empty:
        return 0
    
    # 시뮬레이션된 '시가총액' 개념: (종가 * 거래량)
    df['Market_Value'] = df['Close'] * df['Volume']
    total_market_value = df['Market_Value'].sum()
    
    # 모든 종목의 '시가총액'을 합산, 임의 기준값(base)를 1000으로 설정하고,
    # (각 종목시가총액 / 전체시장시가총액) * base를 다 더한 값을 지수처럼 활용
    # 단순 합 계산도 가능하지만 가중치를 주어 합치는 것으로 해석
    df['Weight'] = df['Market_Value'] / total_market_value

    # 지수 = base * ∑(weight_i)
    base = 1000
    index_value = base * df['Weight'].sum()
    return index_value

def main():
    st.title("간단한 S&P 500 유사 추정 지수 웹 앱 (NASDAQ 기반 예시)")
    
    # 날짜 입력 받기
    start_date = st.date_input("시작 날짜:", datetime.date(2023, 1, 1))
    end_date = st.date_input("종료 날짜:", datetime.date.today())
    
    # Ticker 리스트 로드
    tickers = load_tickers()
    st.write(f"현재 샘플 티커 수: {len(tickers)}개")
    
    # 데이터 가져오기
    df = fetch_market_data(tickers, start_date, end_date)
    
    if not df.empty:
        st.write("가져온 데이터 일부 미리 보기:")
        st.dataframe(df.head())
        
        # 지수 계산
        index_val = calculate_index(df)
        st.subheader("추정 지수 결과:")
        st.write(f"추정 지수: {index_val:.2f}")
    else:
        st.warning("데이터가 없습니다. 날짜 범위나 티커 리스트를 확인하세요.")

if __name__ == "__main__":
    main()
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
