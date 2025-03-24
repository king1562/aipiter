def gugudan_10():
    # 1부터 10까지 각각의 단을 출력
    for dan in range(1, 11):
        print(f"=== {dan}단 ===")
        # 각 단에서 곱할 수 1부터 10까지 출력
        for i in range(1, 11):
            print(f"{dan} x {i} = {dan*i}")
        print()  # 단 사이에 공백 줄 삽입

# 함수 호출 예시
gugudan_10()
