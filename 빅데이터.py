import time
import random

# 게임 변수 초기화
portfolio_value = 100000  # 초기 자본 $100,000
investment_score = 0  # 투자 점수 (호감도 대신)

def update_investment_score(change):
    global investment_score
    investment_score += change
    if investment_score > 100:
        investment_score = 100
    elif investment_score < -100:
        investment_score = -100
    print(f"현재 투자 점수: {investment_score}")

# S&P 500 주식 데이터
stock_data = {
    'AAPL': {'name': 'Apple', 'price': 199.20, 'sector': 'Technology'},
    'NVDA': {'name': 'NVIDIA', 'price': 145.00, 'sector': 'Technology'},
    'MSFT': {'name': 'Microsoft', 'price': 450.00, 'sector': 'Technology'},
    'GOOGL': {'name': 'Google', 'price': 175.00, 'sector': 'Technology'},
    'TSLA': {'name': 'Tesla', 'price': 250.00, 'sector': 'Electric Vehicle'},
    'JPM': {'name': 'JPMorgan', 'price': 210.00, 'sector': 'Finance'},
    'JNJ': {'name': 'Johnson & Johnson', 'price': 160.00, 'sector': 'Healthcare'},
    'PLTR': {'name': 'Palantir', 'price': 135.19, 'sector': 'Big Data'}
}

print('💰 S&P 500 주식 투자 시뮬레이션 💰')
name = ['1.게임 시작', '2.투자하지 않기', '3.나가기']
print(f"{name} ")
user = input('선택: ')
for i in range(2):
    print('.')
    time.sleep(1)

#1. 투자자 소개-------------------------------
print('📱 (투자 앱 알림)')
for i in range(1):
    time.sleep(1)
print('📱 (투자 앱 알림)')
for i in range(1):
    time.sleep(1)
print('📱 (투자 앱 알림)')
for i in range(1):
    time.sleep(1)

print('📱 투자앱: 어..아침부터 주식이 움직이네..')
for i in range(2):
    time.sleep(1)

print('내 이름은..')
for i in range(2):
    time.sleep(1)
name1 = input('이름을 적어주세요: ')
for i in range(1):
    time.sleep(1)
print(f"(내 이름은, {name1}! 25살 직장인이다.)")
for i in range(1):
    time.sleep(1)
print('(드디어 모은 돈 10만 달러로 S&P 500 투자를 시작하게 되었다.)')
for i in range(2):
    time.sleep(1)
print('(하지만 내 투자 목표는 하나..)')
for i in range(2):
    time.sleep(1)
print('(부자 되기!)')
for i in range(2):
    time.sleep(1)
print(f"{name1}: 주식으로 망하지만 않았으면 좋겠다")
for i in range(2):
    time.sleep(1)

print('📱 (투자 앱 알림)')
for i in range(1):
    time.sleep(1)
print('📱 (투자 앱 알림)')
for i in range(1):
    print('.')
    time.sleep(1)
print('📊 -월스트리트 분석가')
for i in range(2):
    time.sleep(1)
print('📊: 안녕하세요 투자자 여러분 저는 김애널리스트입니다.')
for i in range(2):
    time.sleep(1)
print('📊: 오늘 AI 관련 주식들이 급등하고 있으니 관심있는 분들은 주목해주세요~')
for i in range(2):
    time.sleep(1)

print(f"{name1}: 음..이분이 유명한 분석가님이신가?")
for i in range(2):
    time.sleep(1)
print(f"{name1}: 헐 근데 AI 주식..? 아 어떻게 투자하지?")
for i in range(2):
    time.sleep(1)

print('Q1. 첫 투자 어떻게 할까..?')
for i in range(2):
    print('.')
    time.sleep(1)

options = ['1.AI 관련주에 올인! NVIDIA 매수하자', '2.아 위험한데..안전한 애플로 가자...']
print(f"{options} ")
choice = input("어..어떡하지..?: ")
for i in range(2):
    time.sleep(1)

if choice == "1":
    print(f"{name1}: 그래 AI 시대다! NVIDIA 사자!")
    for i in range(2):
        time.sleep(1)
    print("- NVIDIA 주가가 15% 급등했습니다! 투자 점수가 20 증가합니다")
    update_investment_score(20)
    portfolio_value *= 1.15

elif choice == "2":
    print(f"{name1}: 아..뭔 AI야..애플이 안전하지..")
    for i in range(2):
        time.sleep(1)
    print("- 애플 주가가 2% 상승했습니다. 투자 점수가 5 증가합니다")
    update_investment_score(5)
    portfolio_value *= 1.02
    for i in range(1):
        time.sleep(1)
else:
    print("잘못된 선택입니다. 1 또는 2를 입력하세요.")

for i in range(3):
    print('.')
    time.sleep(1)

#2. 시장 분석-------------------------------
print('#2. 투자 전략 수립')
for i in range(2):
    time.sleep(1)

print(f"{name1}: 아 오늘 포트폴리오 점검하는 날인데 뭘 더 살지?")
for i in range(2):
    time.sleep(1)
print(f"{name1}(은)는 투자 앱을 열어본다")
for i in range(2):
    time.sleep(1)
print(f"{name1}: 음..뭘 살지? 종목이 너무 많네..")
for i in range(2):
    time.sleep(1)

print('Q2. 오늘 어떤 섹터에 투자할까?')
for i in range(2):
    print('.')
    time.sleep(1)

options = ['1.기술주 추가 매수 (구글, 마이크로소프트)', '2.안전한 헬스케어 (존슨앤존슨)', '3.핫한 테슬라 전기차']
print(f"{options} ")
choice = input("음..뭘 살지?: ")
for i in range(2):
    time.sleep(1)

if choice == "1":
    print(f"{name1}: 그치~ 기술주가 대세니까 더 사야지!")
    for i in range(2):
        time.sleep(1)
    print("- 기술주들이 8% 상승했습니다! 투자 점수가 15 증가합니다")
    update_investment_score(15)
    portfolio_value *= 1.08

elif choice == "2":
    print(f"{name1}: 오 헬스케어 사두길 잘했다 안전한데~?")
    for i in range(2):
        time.sleep(1)
    print(f"- {name1}(은)는 안정적인 투자를 했습니다. 투자 점수가 10 증가합니다")
    update_investment_score(10)
    portfolio_value *= 1.03
    for i in range(1):
        time.sleep(1)

elif choice == "3":
    print(f"{name1}: 테슬라가 미래야~ 일론 머스크 믿고 간다")
    for i in range(2):
        time.sleep(1)
    print("- 테슬라 주가가 갑자기 12% 폭락했습니다. 투자 점수가 15 감소합니다")
    update_investment_score(-15)
    portfolio_value *= 0.88

for i in range(3):
    print('.')
    time.sleep(1)

#3. 시장 위기-------------------------------
print('#3. 시장 급락 상황 (월스트리트)')
for i in range(2):
    time.sleep(1)

print(f"{name1}: (우와 드디어 본격 투자한다..)")
for i in range(2):
    time.sleep(1)
print(f"{name1}: (근데 갑자기 모든 주식이 빨간색이네..뭐지?)")
for i in range(2):
    print('.')
    time.sleep(1)
print('📺 <경제뉴스>')
for i in range(2):
    time.sleep(1)
print('📺 앵커: 오늘 연준 금리 인상 발표로 주식시장이 대폭락하고 있습니다')
for i in range(2):
    time.sleep(1)

print(f"{name1}: (헉 이럴 때 어떻게 해야 하지..?)")
for i in range(2):
    print('.')
    time.sleep(1)

print('Q3. 시장 급락 상황! 어떻게 대응할까?')
for i in range(2):
    time.sleep(1)

options = ['1.패닉셀! 모든 주식 팔고 현금 보유', '2.호재다! 더 싸게 물타기 매수', '3.그냥 가만히 홀드하기']
print(f"{options} ")
choice = input("고민된다..: ")
for i in range(2):
    time.sleep(1)

if choice == "1":
    print(f"{name1}: 아 무서워! 다 팔자!")
    for i in range(2):
        time.sleep(1)
    print('📈 시장 전문가: 패닉셀은 금물입니다')
    for i in range(1):
        time.sleep(1)
    print("- 바닥에서 팔아버렸습니다. 투자 점수가 25 감소합니다")
    update_investment_score(-25)
    portfolio_value *= 0.85

elif choice == "2":
    print("📰 뉴스: 급락장에서도 용감한 개미들의 물타기가 계속되고 있습니다")
    for i in range(2):
        time.sleep(1)
    print(f"{name1}: 이때 안 사면 언제 사냐!")
    for i in range(2):
        time.sleep(1)
    print("- 며칠 후 시장이 반등했습니다! 투자 점수가 30 증가합니다")
    update_investment_score(30)
    portfolio_value *= 1.25
    for i in range(1):
        time.sleep(1)

elif choice == "3":
    print(f"{name1}: (그래.. 장기 투자니까 버티자)")
    for i in range(2):
        time.sleep(1)
    print(f"{name1}: (홀드하니까 마음이 편하네)")
    for i in range(1):
        time.sleep(1)
    print("- 시장이 서서히 회복되었습니다. 투자 점수가 10 증가")
    update_investment_score(10)
    portfolio_value *= 1.05

for i in range(3):
    print('.')
    time.sleep(1)

print("(1개월 뒤)")
for i in range(2):
    time.sleep(1)

print(f"{name1}: 요즘 팰런티어(PLTR)가 핫하다던데?")
for i in range(2):
    time.sleep(1)
print("(유튜브에서 '팰런티어 대박' 영상을 보고 있다)")
for i in range(2):
    time.sleep(1)
print(f"{name1}: 헐? 대박 AI 빅데이터 회사라니.. 나도 살까?")

for i in range(3):
    print('.')
    time.sleep(1)

options = ['1.유튜버 말 믿고 팰런티어 올인', '2.다음 기회를 기다리기']
print(f"{options} ")
choice = input("음..: ")
for i in range(2):
    time.sleep(1)

if choice == "1":
    pltr_result = random.choice([True, False])  # 50% 확률
    if pltr_result:
        print("팰런티어가 정부 계약을 대량으로 따냈다는 뉴스가 나왔다!")
        for i in range(2):
            time.sleep(1)
        print("📈 PLTR: +40% 대폭등!")
        for i in range(2):
            time.sleep(1)
        print("- 대박! 투자 점수가 35 증가합니다")
        update_investment_score(35)
        portfolio_value *= 1.40
    else:
        print("팰런티어 실적이 예상보다 나빴다는 뉴스가 나왔다")
        for i in range(2):
            time.sleep(1)
        print("📉 PLTR: -25% 폭락...")
        for i in range(2):
            time.sleep(1)
        print("- 유튜버 말만 믿었다가.. 투자 점수가 20 감소합니다")
        update_investment_score(-20)
        portfolio_value *= 0.75

elif choice == "2":
    print(f"{name1}: (음..아니야..섣불리 움직이지 말자)")
    for i in range(2):
        time.sleep(1)
    print("- 신중한 선택이었습니다. 투자 점수가 5 감소합니다")
    update_investment_score(-5)

for i in range(3):
    print('.')
    time.sleep(1)

#4. 전문가 조언----------------
print("(투자 세미나에 참석한 길)")
for i in range(1):
    time.sleep(1)
print(f"{name1}: 후..세미나 드디어 끝났네")
for i in range(2):
    time.sleep(1)
print(f"{name1}: 근데 워렌 버핏 얘기가 인상깊었어.. 장기투자가 답인가?")
for i in range(2):
    time.sleep(1)
print(f"{name1}: 아니면 단기 트레이딩으로 수익을 낼까..")
for i in range(2):
    time.sleep(1)
print("(고민하다가 투자 멘토와 마주쳤다)")
for i in range(1):
    time.sleep(1)
print(f"{name1}: 어?! 선생님 안녕하세요!")
for i in range(2):
    time.sleep(1)
print("투자멘토: 안녕~ 세미나 어땠어?")
for i in range(2):
    time.sleep(1)
print(f"{name1}: 네네 좋았어요")
for i in range(2):
    time.sleep(1)
print("투자멘토: 요즘 포트폴리오는 어때? 수익 나고 있어?")
for i in range(2):
    time.sleep(1)
print(f"{name1}: 네네ㅎㅎ")
for i in range(3):
    print('.')
    time.sleep(1)

print(f"{name1}: (아..뭔가 어색해..뭐라도 말해야 하는데)")
for i in range(2):
    print('.')
    time.sleep(1)

print('Q4. 투자 멘토에게 뭐라고 말하지?')
for i in range(2):
    print('.')
    time.sleep(1)

options = ['1.그냥 인사하고 지나간다', '2.포트폴리오 조언을 구한다', '3.최근 투자 성과를 자랑한다']
print(f"{options} ")
choice = input("골라주세용: ")
for i in range(2):
    time.sleep(1)

if choice == "1":
    print(f"{name1}: 그러면 가보겠습니다(꾸벅)")
    for i in range(2):
        time.sleep(1)
    print('투자멘토: 어..그래 잘가~?')
    for i in range(1):
        time.sleep(1)
    print("- 기회를 놓쳤습니다... 투자 점수 변화 없음")
    update_investment_score(0)

elif choice == "2":
    print(f"{name1}: 선생님! 포트폴리오 조언 좀 해주세요!")
    for i in range(2):
        time.sleep(1)
    print("투자멘토: 음...")
    for i in range(1):
        time.sleep(1)
    print(f"{name1}: 어떤 주식이 좋을까요?")
    for i in range(2):
        time.sleep(1)
    print("- 전문가의 조언으로 리스크가 줄었습니다. 투자 점수가 15 감소합니다")
    update_investment_score(-15)
    for i in range(1):
        time.sleep(1)

elif choice == "3":
    print(f"{name1}: 선생님! 제가 최근에 NVIDIA로 대박 났어요!")
    for i in range(2):
        time.sleep(1)
    print("투자멘토: 오~ 잘했네ㅋㅋ 대단하다")
    for i in range(1):
        time.sleep(1)
    print("투자멘토: 혹시 점심 같이 할래? 투자 얘기 더 해보자")
    for i in range(1):
        time.sleep(1)
    print("- 멘토와 네트워킹을 했습니다! 투자 점수가 25점 증가합니다")
    update_investment_score(25)

for i in range(3):
    print('.')
    time.sleep(1)

#5. 마지막 결정------------------------
print("(그렇게 시간은 흐르고 흘러 1년이 지났다)")
for i in range(1):
    time.sleep(1)
print("(나는 이제 경험 많은 투자자가 되었다)")
for i in range(1):
    time.sleep(1)
print(f"{name1}: 1년 투자하니까 이제 좀 감이 오네")
for i in range(2):
    time.sleep(1)
print(f"{name1}: 마지막으로 큰 결정을 해볼까..")
for i in range(2):
    time.sleep(1)
print("📱 (투자 앱 알림)")
for i in range(1):
    time.sleep(1)
print("📱 (투자 앱 알림)")
for i in range(1):
    time.sleep(1)
print(f"투자친구: {name1}아..")
for i in range(1):
    time.sleep(1)
print(f"투자친구: 비트코인 한번 같이 해볼래?")
for i in range(1):
    time.sleep(1)

print(f"{name1}: 아니 얘는 왜 맨날 위험한 거만.. 계속 권하네..")
for i in range(2):
    time.sleep(1)

print('Q5. 마지막 투자 기회! 어떻게 할까?')
for i in range(2):
    print('.')
    time.sleep(1)

options = ['1.안전하게 S&P 500 ETF 추가 매수', '2.위험하지만 비트코인 도전', '3.그냥 현금으로 보유하기']
print(f"{options} ")
choice = input("마지막 선택...: ")
for i in range(2):
    time.sleep(1)

if choice == "1":
    print(f"{name1}: 그래! 안전하게 ETF로 가자!")
    for i in range(2):
        time.sleep(1)
    print(f"{name1}: 분산투자가 최고야!")
    for i in range(2):
        time.sleep(1)
    print('S&P 500이 연말까지 8% 상승했습니다!')
    for i in range(1):
        time.sleep(1)
    print('ETF 추천해준 친구: 대박! 같이 수익 났네!')
    for i in range(1):
        time.sleep(1)
    print('(포트폴리오가 안정적으로 성장했다)')
    for i in range(2):
        time.sleep(1)
    print("- 현명한 선택! 투자 점수가 20 증가합니다")
    update_investment_score(20)
    portfolio_value *= 1.08

elif choice == "2":
    crypto_result = random.choice([True, False])  # 50% 확률
    if crypto_result:
        print(f"{name1}: 인생은 한 방이지! 비트코인 가보자!")
        for i in range(2):
            time.sleep(1)
        print("비트코인이 갑자기 50% 폭등했습니다!")
        for i in range(2):
            time.sleep(1)
        print(f"{name1}: 대박!!! 내가 천재였어!")
        for i in range(2):
            time.sleep(1)
        print("- 운이 좋았네요! 투자 점수가 40 증가합니다")
        update_investment_score(40)
        portfolio_value *= 1.50
    else:
        print(f"{name1}: 인생은 한 방이지! 비트코인 가보자!")
        for i in range(2):
            time.sleep(1)
        print("비트코인이 갑자기 60% 폭락했습니다...")
        for i in range(2):
            time.sleep(1)
        print(f"{name1}: 아...이럴 줄 알았으면...")
        for i in range(2):
            time.sleep(1)
        print("- 너무 위험했습니다. 투자 점수가 30 감소합니다")
        update_investment_score(-30)
        portfolio_value *= 0.40

elif choice == "3":
    print(f"{name1}: 아니야~ 현금이 최고야")
    for i in range(2):
        time.sleep(1)
    print(f"{name1}: 안전이 제일이지")
    for i in range(2):
        time.sleep(1)
    print("투자친구: 아..아쉽다")
    for i in range(2):
        time.sleep(1)
    print("- 기회비용이 발생했습니다. 투자 점수가 10점 감소합니다")
    update_investment_score(-10)

for i in range(3):
    print('.')
    time.sleep(1)

#-------------------------
# 게임 종료 후 엔딩 분기
final_return = ((portfolio_value - 100000) / 100000) * 100

if investment_score <= 20:
    print("(1년이 지나 나는 투자 경험을 쌓았다.)")
    for i in range(2):
        time.sleep(1)
    print("(1년간 투자하면서 잃은 돈이 많지만 값진 경험을 했다.)")
    for i in range(2):
        time.sleep(1)
    print("(이제는 차트 보는 법도 알고 기업분석도 할 수 있다.)")
    for i in range(2):
        time.sleep(1)
    print("(길을 걸으며 투자 공부하는 중)")
    for i in range(2):
        time.sleep(1)
    print(f"{name1}: 처음엔 주식이 쉬운 줄 알았는데")
    for i in range(1):
        time.sleep(1)
    print(f"{name1}: 1년 해보니까 정말 어렵구나.. 더 공부해야겠어")
    for i in range(1):
        time.sleep(1)
    print("📖")
    for i in range(1):
        time.sleep(1)
    print("📊")
    for i in range(1):
        time.sleep(1)
    print("📈")
    for i in range(1):
        time.sleep(1)
    print("💡")
    for i in range(1):
        time.sleep(1)
    print("성공!")
    for i in range(2):
        time.sleep(1)
    print("결국 꾸준히 공부한 덕분에 훌륭한 투자자가 되었다")
    for i in range(2):
        time.sleep(1)
    print("주인공은 나중에 투자로 큰 성공을 거두게 된다..")
    for i in range(3):
        time.sleep(1)
    print("성장 엔딩: 실패가 성공의 어머니다! 📚")

elif 21 <= investment_score <= 60:
    print("(나는 평범하게 1년째 투자를 하고 있다.)")
    for i in range(2):
        time.sleep(1)
    print("(나의 투자 생활은 겉으로는 안정적이지만)")
    for i in range(2):
        time.sleep(1)
    print("(큰 수익도 큰 손실도 없는 그저 그런 투자를 하고 있다.)")
    for i in range(2):
        time.sleep(1)
    print("(안전하게 투자했지만 특별한 성과를 내지 못하고 평범한 수익률을 기록한다)")
    for i in range(2):
        time.sleep(1)
    print("(이게 맞는 투자인 걸까?)")
    for i in range(3):
        time.sleep(1)
    print("평범 엔딩: 안전한 게 최고야? 📊")

elif 61 <= investment_score <= 100:
    print("(1년이 지나 나는 성공한 투자자가 되었다.)")
    for i in range(2):
        time.sleep(1)
    print("(투자는 어렵지만 여전히 처음처럼 투자가 재미있고 흥미롭다.)")
    for i in range(2):
        time.sleep(1)
    print("(그 동안 나는 기술주, 금융주, 헬스케어주 가리지 않고 좋은 성과를 내고 있고, 수익률도 훌륭하다!)")
    for i in range(2):
        time.sleep(1)
    print("(앞으로도 이렇게 매일이 수익이었으면 좋겠다!)")
    for i in range(3):
        time.sleep(1)
    print("성공 엔딩: 부자 되는 그날까지! 💰")

print(f"\n🎮 게임 종료!")
print(f"💰 최종 포트폴리오 가치: ${portfolio_value:,.2f}")
print(f"📈 총 수익률: {final_return:+.2f}%")
print(f"📊 최종 투자 점수: {investment_score}")

if final_return > 50:
    print("🏆 투자 천재! 워렌 버핏도 인정할 실력!")
elif final_return > 20:
    print("👍 훌륭한 투자자! 계속 이런 식으로!")
elif final_return > 0:
    print("📈 수익 달성! 나쁘지 않네요!")
elif final_return > -20:
    print("📉 약간의 손실... 다음엔 더 신중하게!")
else:
    print("💥 큰 손실... 투자는 정말 어려워요!")