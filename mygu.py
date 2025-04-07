# 숫자 두 개를 입력받아서
# +, -, *, / 를 출력하는 프로그램을 만들어 보자.

def calculate(num1, num2):
    """두 숫자에 대한 사칙연산을 수행하는 함수"""
    덧셈 = num1 + num2
    뺄셈 = num1 - num2
    곱셈 = num1 * num2
   
    # 나눗셈은 0으로 나누는 경우를 처리
    if num2 != 0:
        나눗셈 = num1 / num2
    else:
        나눗셈 = "계산할 수 없음 (0으로 나눌 수 없음)"
   
    return 덧셈, 뺄셈, 곱셈, 나눗셈

def main():
    # 사용자 입력 처리
    try:
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        num2 = float(input("두 번째 숫자를 입력하세요: "))
       
        # 계산 수행
        덧셈, 뺄셈, 곱셈, 나눗셈 = calculate(num1, num2)
       
        # 결과 출력
        print(f"\n===== 계산 결과 =====")
        print(f"{num1} + {num2} = {덧셈}")
        print(f"{num1} - {num2} = {뺄셈}")
        print(f"{num1} × {num2} = {곱셈}")
        print(f"{num1} ÷ {num2} = {나눗셈}")
       
    except ValueError:
        print("유효한 숫자를 입력해주세요.")

# 프로그램 실행
if __name__ == "__main__":
    main()