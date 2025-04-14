import os
import time
import random
import sys

# ANSI 이스케이프 시퀀스를 사용한 텍스트 스타일링
class Style:
    # 텍스트 색상
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # 밝은 색상
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # 배경 색상
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # 텍스트 스타일
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    
    # 스타일 초기화
    RESET = '\033[0m'

# 화면 지우기 함수
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# 텍스트를 천천히 타이핑하는 효과
def typewriter_print(text, delay=0.03, style=""):
    for char in text:
        sys.stdout.write(style + char + Style.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# 텍스트 중앙 정렬
def center_text(text, width=80):
    return text.center(width)

# 박스 테두리로 텍스트 감싸기
def print_box(text, width=60, title="", style=Style.CYAN):
    # 테두리 문자
    h_line = "═"
    v_line = "║"
    tl = "╔"
    tr = "╗"
    bl = "╚"
    br = "╝"
    
    # 상단 테두리 출력
    print(style + tl + h_line * width + tr + Style.RESET)
    
    # 제목이 있으면 출력
    if title:
        padding_left = (width - len(title)) // 2
        padding_right = width - padding_left - len(title)
        print(style + v_line + " " * padding_left + 
              Style.BOLD + Style.YELLOW + title + 
              Style.RESET + style + " " * padding_right + v_line + Style.RESET)
        print(style + v_line + h_line * width + v_line + Style.RESET)
    
    # 텍스트 여러 줄 처리
    lines = text.strip().split('\n')
    for line in lines:
        if len(line) > width:
            # 너무 긴 라인 자르기
            chunks = [line[i:i+width] for i in range(0, len(line), width)]
            for chunk in chunks:
                padding = width - len(chunk)
                print(style + v_line + Style.RESET + chunk + " " * padding + 
                      style + v_line + Style.RESET)
        else:
            padding = width - len(line)
            print(style + v_line + Style.RESET + line + " " * padding + 
                  style + v_line + Style.RESET)
    
    # 하단 테두리 출력
    print(style + bl + h_line * width + br + Style.RESET)

# 로딩 애니메이션
def loading_animation(text="로딩 중", duration=2, style=Style.CYAN):
    start_time = time.time()
    spinner = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    i = 0
    
    print()
    while time.time() - start_time < duration:
        sys.stdout.write(f'\r{style}{text} {spinner[i % len(spinner)]} {Style.RESET}')
        sys.stdout.flush()
        i += 1
        time.sleep(0.1)
    print(f'\r{style}{text} 완료!{Style.RESET}')
    print()

# 동물 아스키 아트
class Animals:
    CAT = ["""
 /\\_/\\
( o.o )
 > ^ <
/     \\
\\     /
 \\___/
""", """
 /\\_/\\
(  o.o )
 > ^ <
""", """
 /\\_/\\
( .o.o )
 > ^ <
"""]

    DOG = ["""
   __      _
  / /\\____/_
 /           \\
/ (*)     (*) \\
/      |        \\
\\      /        /
 \\_____\\_______/
""", """
  / \\__
 (    @\\___
  /         O
 /   (_____/
/_____/   U
"""]

    RABBIT = ["""
 (\\(\\_
 (=' :')   
(,(')(')
""", """
  (\\(\\
  (='.')
 o(")_(")
"""]

    BIRD = ["""
   \\\\
   (o>
\\\\_//)
 \\_/_)
  _|_
"""]

    TURTLE = ["""
      _____     ____
     /      \\  |  o | 
    |        |/  ___|
    |_________/
    |_|_| |_|_|
"""]

# 메뉴 출력 함수
def print_menu(options, title="메뉴"):
    menu_text = f"\n{title}\n"
    menu_text += "=====================\n"
    
    for key, value in options.items():
        menu_text += f"{key}. {value}\n"
    
    menu_text += "====================="
    
    print_box(menu_text, width=30, title=title, style=Style.GREEN)

# 동물 출력 함수
def print_animal(animal_art, animal_name, animate=True):
    if isinstance(animal_art, list) and len(animal_art) > 1 and animate:
        # 애니메이션 출력
        for i in range(3):  # 3번 반복
            for art in animal_art:
                clear_screen()
                print(Style.BOLD + Style.CYAN + animal_name + Style.RESET)
                print(Style.YELLOW + art + Style.RESET)
                time.sleep(0.2)
    else:
        # 단일 이미지 출력
        art = animal_art[0] if isinstance(animal_art, list) else animal_art
        print(Style.BOLD + Style.CYAN + animal_name + Style.RESET)
        print(Style.YELLOW + art + Style.RESET)

# 동물 선택 및 출력 함수
def display_animal(animal_name):
    clear_screen()
    
    # 로딩 애니메이션
    loading_animation(f"{animal_name} 로딩 중", duration=1.5, style=Style.CYAN)
    
    # 동물 이름 헤더 출력
    header = f"✧･ﾟ: *✧･ﾟ {animal_name} ✧･ﾟ: *✧･ﾟ"
    print(Style.BOLD + Style.CYAN + center_text(header) + Style.RESET)
    print()
    
    # 동물 아트 선택 및 출력
    if animal_name == "고양이":
        print_animal(Animals.CAT, animal_name)
    elif animal_name == "강아지":
        print_animal(Animals.DOG, animal_name)
    elif animal_name == "토끼":
        print_animal(Animals.RABBIT, animal_name)
    elif animal_name == "새":
        print_animal(Animals.BIRD, animal_name)
    elif animal_name == "거북이":
        print_animal(Animals.TURTLE, animal_name)
    else:
        print(Style.RED + f"해당 동물({animal_name})은 지원되지 않습니다." + Style.RESET)
        return
    
    # 랜덤 메시지 출력
    messages = [
        f"{animal_name}와(과) 즐거운 시간 보내세요!",
        f"{animal_name}가 당신을 반겨요!",
        f"귀여운 {animal_name}입니다!",
        f"{animal_name}와(과) 함께하는 행복한 하루!",
        f"멋진 {animal_name} 아스키 아트입니다!"
    ]
    
    print()
    typewriter_print(random.choice(messages), delay=0.05, style=Style.BRIGHT_CYAN)
    print()

# 한 번의 동물 선택 및 출력 (play() 함수)
def play():
    clear_screen()
    print_box("아스키 아트 동물 출력 프로그램", width=50, title="동물 그림 출력", style=Style.CYAN)
    
    # 메뉴 옵션
    options = {
        "1": "고양이",
        "2": "강아지",
        "3": "토끼",
        "4": "새",
        "5": "거북이",
        "0": "종료"
    }
    
    print_menu(options, title="동물 선택")
    
    try:
        choice = input(f"\n{Style.WHITE}선택하세요 (0-5): {Style.RESET}")
        
        if choice == "0":
            print()
            typewriter_print("프로그램을 종료합니다...", delay=0.05, style=Style.BRIGHT_RED)
            time.sleep(1)
            return False
        elif choice in options and choice != "0":
            animal_name = options[choice]
            display_animal(animal_name)
        else:
            print(f"\n{Style.RED}잘못된 선택입니다! 0-5 사이의 숫자를 입력하세요.{Style.RESET}")
        
        input(f"\n{Style.GREEN}계속하려면 엔터 키를 누르세요...{Style.RESET}")
        return True
    except ValueError:
        print(f"\n{Style.RED}숫자만 입력해주세요!{Style.RESET}")
        input(f"\n{Style.GREEN}계속하려면 엔터 키를 누르세요...{Style.RESET}")
        return True

# 5번 반복 프로그램
def fixed_repeat_program():
    clear_screen()
    print_box("5회 반복 동물 출력 프로그램", width=50, title="5회 반복", style=Style.CYAN)
    
    # 진행 상황 표시 기호
    progress_symbols = ["□", "□", "□", "□", "□"]
    
    for i in range(5):
        # 진행 상황 업데이트
        progress_symbols[i] = "■"
        progress_bar = " ".join(progress_symbols)
        
        print(f"\n{Style.CYAN}[{i+1}/5] 회차 실행중...{Style.RESET}")
        print(f"{Style.YELLOW}진행상황: {progress_bar}{Style.RESET}")
        
        time.sleep(0.5)
        if not play():
            break
    
    # 종료 애니메이션
    clear_screen()
    print_box("프로그램 종료", width=50, title="완료", style=Style.CYAN)
    
    finish_text = "5회 반복 프로그램 완료!"
    print(Style.BRIGHT_GREEN + center_text(finish_text) + Style.RESET)
    
    print()
    print(Style.CYAN + center_text("~ 이용해주셔서 감사합니다 ~") + Style.RESET)
    print()
    
    # 간단한 종료 애니메이션
    for i in range(3):
        sys.stdout.write("\r" + Style.MAGENTA + center_text("*  *  *") + Style.RESET)
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\r" + Style.MAGENTA + center_text(" *  *  ") + Style.RESET)
        sys.stdout.flush()
        time.sleep(0.3)
    
    print("\n")
    time.sleep(1)

# 무한 반복 프로그램 (0 입력시 종료)
def infinite_program():
    clear_screen()
    print_box("무한 반복 동물 출력 프로그램", width=50, title="무한 반복", style=Style.CYAN)
    
    typewriter_print("프로그램을 종료하려면 언제든지 '0'을 입력하세요.", 
                  delay=0.03, style=Style.YELLOW)
    time.sleep(1)
    
    count = 1
    while True:
        # 회차 정보 출력
        print(f"\n{Style.BOLD}{Style.CYAN}{'='*20}")
        print(f" {count}번째 실행")
        print(f"{'='*20}{Style.RESET}")
        
        if not play():
            break
        count += 1
    
    # 종료 메시지
    clear_screen()
    print_box("프로그램 종료", width=50, title="완료", style=Style.CYAN)
    
    count_msg = f"총 {count-1}번 실행했습니다!"
    print(Style.BOLD + Style.GREEN + center_text(count_msg) + Style.RESET)
    print()
    
    end_msg = "무한 반복 프로그램이 종료되었습니다!"
    typewriter_print(center_text(end_msg), delay=0.05, style=Style.BOLD + Style.YELLOW)
    print()
    
    thank_you = "이용해주셔서 감사합니다 ♥"
    print(Style.BOLD + Style.MAGENTA + center_text(thank_you) + Style.RESET)
    print()

# 시작 애니메이션
def start_animation():
    clear_screen()
    
    # 환영 메시지 애니메이션
    welcome_msg = "아스키 아트 동물 출력 프로그램"
    
    # 중앙에 위치시키기 위한 계산
    left_padding = (80 - len(welcome_msg)) // 2
    
    # 상단 여백
    for _ in range(5):
        print()
    
    # 타이핑 효과로 환영 메시지 출력
    sys.stdout.write(" " * left_padding)
    for char in welcome_msg:
        sys.stdout.write(Style.BOLD + Style.CYAN + char + Style.RESET)
        sys.stdout.flush()
        time.sleep(0.1)
    print()
    
    # 로딩 애니메이션
    print()
    loading_animation("프로그램 초기화 중", duration=2, style=Style.GREEN)
    
    # 간단한 아스키 아트 동물들 모음
    all_animals = """
 /\\_/\\          / \\__          (\\(\\           \\\\
( o.o )        (    @\\___      (='.')         (o>
 > ^ <          /         O    o(")_(")    \\\\_//)
    """
    
    # 동물 미리보기 출력
    print()
    print(Style.YELLOW + center_text(all_animals) + Style.RESET)
    print()
    
    typewriter_print(center_text("곧 시작합니다..."), delay=0.05, style=Style.WHITE)
    time.sleep(1)

# 메인 프로그램
def main():
    # 시작 애니메이션
    start_animation()
    
    # 메인 메뉴
    clear_screen()
    print_box("아스키 아트 동물 출력 프로그램", width=60, title="메인 메뉴", style=Style.CYAN)
    
    options = {
        "1": "5회 반복 프로그램",
        "2": "무한 반복 프로그램 (0 입력시 종료)",
        "0": "바로 종료"
    }
    
    print_menu(options, title="실행 모드 선택")
    
    try:
        choice = input(f"\n{Style.WHITE}선택: {Style.RESET}")
        
        if choice == "1":
            fixed_repeat_program()
        elif choice == "2":
            infinite_program()
        elif choice == "0":
            typewriter_print("\n프로그램을 종료합니다...", delay=0.05, style=Style.BOLD + Style.RED)
            time.sleep(1)
        else:
            print(f"\n{Style.RED}잘못된 선택입니다! 다시 실행해주세요.{Style.RESET}")
            time.sleep(2)
    except ValueError:
        print(f"\n{Style.RED}숫자만 입력해주세요! 다시 실행해주세요.{Style.RESET}")
        time.sleep(2)
    
    # 프로그램 종료
    clear_screen()
    print(f"\n\n{Style.BOLD}{Style.CYAN}")
    print(center_text("프로그램이 종료되었습니다!"))
    print(f"{Style.RESET}\n\n")
    time.sleep(1)

# 프로그램 실행
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print(f"\n\n{Style.RED}프로그램이 강제 종료되었습니다.\n{Style.RESET}")
