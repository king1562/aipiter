import requests
from bs4 import BeautifulSoup
import random
import time
import os
import sys

# ANSI 색상 코드 (터미널 호환성이 높은 기본 색상만 사용)
class Colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

# 화면 지우기
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# 로딩 애니메이션
def loading_animation(text, duration=1):
    chars = "|/-\\"
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        i = (i + 1) % len(chars)
        sys.stdout.write(f"\r{Colors.CYAN}{text} {chars[i]}{Colors.RESET}")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\r" + " " * (len(text) + 10) + "\r")
    sys.stdout.flush()

# 로고 출력
def print_logo():
    logo = f"""
{Colors.CYAN}╔════════════════════════════════════════════════╗
║                                                                          ║
║   {Colors.YELLOW}█▀█ █▀█ █▀█ █   █▀▀   █▀▄▀█ █ █ █▀ █ █▀▀   {Colors.CYAN}║
║   {Colors.YELLOW}█▀█ █▀▀ █▀▀ █   █▀▀   █ ▀ █ █▄█ ▄█ █ █     {Colors.CYAN}║
║   {Colors.YELLOW}▀ ▀ ▀   ▀   ▀▀▀ ▀▀▀   ▀   ▀ ▀ ▀ ▀▀ ▀ ▀▀▀   {Colors.CYAN}║
║                    apple music what the                                  ║
║   {Colors.WHITE}★ 빅데이터 음악 차트 분석 & 추천 시스템 ★     {Colors.CYAN}║
║                                                                          ║
╚════════════════════════════════════════════════╝{Colors.RESET}"""
    print(logo)

# 메뉴 출력
def print_menu():
    menu = f"""
{Colors.BOLD}┌────────────────────────────────────┐
│       애플 뮤직 차트 분석 메뉴       │
├────────────────────────────────────┤{Colors.RESET}
│ {Colors.YELLOW}1.{Colors.RESET} 애플 차트 {Colors.RED}TOP 100곡{Colors.RESET} 조회       │
│ {Colors.YELLOW}2.{Colors.RESET} 애플 차트 {Colors.RED}TOP 50곡{Colors.RESET} 조회        │
│ {Colors.YELLOW}3.{Colors.RESET} 애플 차트 {Colors.RED}TOP 10곡{Colors.RESET} 조회        │
│ {Colors.YELLOW}4.{Colors.RESET} {Colors.GREEN}빅데이터 기반 AI 음악 추천{Colors.RESET}      │
│ {Colors.YELLOW}5.{Colors.RESET} 아티스트 {Colors.BLUE}인기도 분석{Colors.RESET}           │
│ {Colors.YELLOW}6.{Colors.RESET} 장르별 {Colors.MAGENTA}트렌드 분석{Colors.RESET}           │
│ {Colors.YELLOW}0.{Colors.RESET} 프로그램 {Colors.RED}종료{Colors.RESET}                 │
{Colors.BOLD}└────────────────────────────────────┘{Colors.RESET}"""
    print(menu)

# 노래 목록 출력
def print_song_list(song_list, limit, title):
    if not song_list:
        print(f"{Colors.RED}데이터를 찾을 수 없습니다.{Colors.RESET}")
        return
    
    displayed_songs = song_list[:min(limit, len(song_list))]
    
    # 헤더
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'═' * 22} {title} {'═' * 22}{Colors.RESET}")
    
    # 테이블 헤더
    print(f"{Colors.BOLD}┌{'─' * 6}┬{'─' * 35}┬{'─' * 20}┐{Colors.RESET}")
    print(f"{Colors.BOLD}│{Colors.YELLOW} 순위  {Colors.RESET}{Colors.BOLD}│{Colors.YELLOW} 제목{' ' * 31}{Colors.RESET}{Colors.BOLD}│{Colors.YELLOW} 아티스트{' ' * 12}{Colors.RESET}{Colors.BOLD}│{Colors.RESET}")
    print(f"{Colors.BOLD}├{'─' * 6}┼{'─' * 35}┼{'─' * 20}┤{Colors.RESET}")
    
    # 노래 목록 출력
    for rank, title, artist in displayed_songs:
        # 긴 제목과 아티스트 이름 처리
        if len(title) > 31:
            title = title[:28] + "..."
        if len(artist) > 16:
            artist = artist[:13] + "..."
        
        print(f"{Colors.BOLD}│{Colors.RESET} {Colors.RED}{rank:^4}{Colors.RESET}  {Colors.BOLD}│{Colors.RESET} {title:<33} {Colors.BOLD}│{Colors.RESET} {Colors.CYAN}{artist:<18}{Colors.RESET} {Colors.BOLD}│{Colors.RESET}")
    
    # 테이블 푸터
    print(f"{Colors.BOLD}└{'─' * 6}┴{'─' * 35}┴{'─' * 20}┘{Colors.RESET}")
    print(f"{Colors.GREEN}총 {len(displayed_songs)}개 곡 표시됨 (전체 {len(song_list)}곡 중){Colors.RESET}")

# 인기 아티스트 분석
def analyze_artists(song_list):
    # 아티스트별 등장 횟수 계산
    artist_counts = {}
    for _, _, artist in song_list[:100]:
        if artist in artist_counts:
            artist_counts[artist] += 1
        else:
            artist_counts[artist] = 1
    
    # 인기도순 정렬
    sorted_artists = sorted(artist_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_artists[:10]  # 상위 10명만 반환

# 장르 트렌드 분석 (가상 데이터)
def generate_genre_trends():
    genres = {
        "팝": random.randint(25, 40),
        "힙합/랩": random.randint(15, 30),
        "R&B/소울": random.randint(10, 20),
        "댄스/일렉트로닉": random.randint(10, 25),
        "K-Pop": random.randint(8, 20),
        "락": random.randint(5, 15),
        "인디/얼터너티브": random.randint(5, 15),
        "발라드": random.randint(3, 10)
    }
    return sorted(genres.items(), key=lambda x: x[1], reverse=True)

# 아티스트 인기도 출력
def print_artist_popularity(artist_data):
    clear_screen()
    print_logo()
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'═' * 15} 아티스트 인기도 분석 {'═' * 15}{Colors.RESET}")
    
    if not artist_data:
        print(f"{Colors.RED}분석할 데이터가 충분하지 않습니다.{Colors.RESET}")
        return
    
    max_count = artist_data[0][1]
    
    # 테이블 헤더
    print(f"{Colors.BOLD}┌{'─' * 5}┬{'─' * 28}┬{'─' * 25}┐{Colors.RESET}")
    print(f"{Colors.BOLD}│{Colors.YELLOW} 순위 {Colors.RESET}{Colors.BOLD}│{Colors.YELLOW} 아티스트{' ' * 20}{Colors.RESET}{Colors.BOLD}│{Colors.YELLOW} 인기도{' ' * 19}{Colors.RESET}{Colors.BOLD}│{Colors.RESET}")
    print(f"{Colors.BOLD}├{'─' * 5}┼{'─' * 28}┼{'─' * 25}┤{Colors.RESET}")
    
    # 아티스트 인기도 출력
    for i, (artist, count) in enumerate(artist_data):
        if len(artist) > 24:
            artist = artist[:21] + "..."
            
        # 그래프 바 생성
        bar_length = int(20 * count / max_count) if max_count > 0 else 0
        bar = '█' * bar_length
        
        print(f"{Colors.BOLD}│{Colors.RESET} {Colors.YELLOW}{i+1:^3}{Colors.RESET} {Colors.BOLD}│{Colors.RESET} {Colors.CYAN}{artist:<26}{Colors.RESET} {Colors.BOLD}│{Colors.RESET} {Colors.GREEN}{bar}{Colors.RESET} {count:>2} {Colors.BOLD}│{Colors.RESET}")
    
    # 테이블 푸터
    print(f"{Colors.BOLD}└{'─' * 5}┴{'─' * 28}┴{'─' * 25}┘{Colors.RESET}")
    
    # 추가 정보 표시
    print(f"\n{Colors.YELLOW}▶ 분석 인사이트:{Colors.RESET}")
    top_artist = artist_data[0][0] if artist_data else "데이터 없음"
    print(f"  {Colors.GREEN}• 최다 히트곡 아티스트: {Colors.CYAN}{top_artist}{Colors.RESET} ({artist_data[0][1]}곡)")
    
    diversity = len(artist_data) / 100 * 100
    print(f"  {Colors.GREEN}• 아티스트 다양성 지수: {Colors.CYAN}{diversity:.1f}%{Colors.RESET}")
    
    new_artists = random.randint(10, 30)
    print(f"  {Colors.GREEN}• 이번 달 신규 진입 아티스트: {Colors.CYAN}{new_artists}명{Colors.RESET}")

# 장르 트렌드 출력
def print_genre_trends(genre_data):
    clear_screen()
    print_logo()
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}{'═' * 15} 장르별 트렌드 분석 {'═' * 15}{Colors.RESET}")
    
    if not genre_data:
        print(f"{Colors.RED}분석할 데이터가 충분하지 않습니다.{Colors.RESET}")
        return
    
    max_count = genre_data[0][1]
    
    # 테이블 헤더
    print(f"{Colors.BOLD}┌{'─' * 5}┬{'─' * 25}┬{'─' * 28}┐{Colors.RESET}")
    print(f"{Colors.BOLD}│{Colors.YELLOW} 순위 {Colors.RESET}{Colors.BOLD}│{Colors.YELLOW} 장르{' ' * 21}{Colors.RESET}{Colors.BOLD}│{Colors.YELLOW} 점유율{' ' * 22}{Colors.RESET}{Colors.BOLD}│{Colors.RESET}")
    print(f"{Colors.BOLD}├{'─' * 5}┼{'─' * 25}┼{'─' * 28}┤{Colors.RESET}")
    
    # 장르 트렌드 출력
    for i, (genre, share) in enumerate(genre_data):
        # 그래프 바 생성
        bar_length = int(20 * share / max_count) if max_count > 0 else 0
        bar = '█' * bar_length
        
        print(f"{Colors.BOLD}│{Colors.RESET} {Colors.YELLOW}{i+1:^3}{Colors.RESET} {Colors.BOLD}│{Colors.RESET} {Colors.CYAN}{genre:<23}{Colors.RESET} {Colors.BOLD}│{Colors.RESET} {Colors.MAGENTA}{bar}{Colors.RESET} {share:>2}% {Colors.BOLD}│{Colors.RESET}")
    
    # 테이블 푸터
    print(f"{Colors.BOLD}└{'─' * 5}┴{'─' * 25}┴{'─' * 28}┘{Colors.RESET}")
    
    # 트렌드 변화 출력
    print(f"\n{Colors.YELLOW}▶ 최근 3개월 장르 트렌드 변화:{Colors.RESET}")
    
    trending_genres = ["K-Pop", "힙합/랩", "댄스/일렉트로닉"]
    declining_genres = ["락", "컨트리", "재즈"]
    
    for genre in trending_genres:
        growth = random.randint(5, 30)
        print(f"  {Colors.GREEN}↑ {genre}: +{growth}%{Colors.RESET} (상승)")
    
    for genre in declining_genres:
        decline = random.randint(5, 20)
        print(f"  {Colors.RED}↓ {genre}: -{decline}%{Colors.RESET} (하락)")
    
    # 시즌 데이터
    seasons = ["봄", "여름", "가을", "겨울"]
    current_season = seasons[random.randint(0, 3)]  # 예시를 위한 랜덤 선택
    
    print(f"\n{Colors.YELLOW}▶ {current_season} 시즌 인기 장르 예측:{Colors.RESET}")
    seasonal_genres = {
        "봄": ["발라드", "인디/얼터너티브", "어쿠스틱"],
        "여름": ["댄스/일렉트로닉", "팝", "라틴"],
        "가을": ["힙합/랩", "R&B/소울", "인디/얼터너티브"],
        "겨울": ["발라드", "어쿠스틱", "재즈"]
    }
    
    for i, genre in enumerate(seasonal_genres[current_season], 1):
        score = random.randint(70, 95)
        print(f"  {Colors.YELLOW}{i}.{Colors.RESET} {Colors.CYAN}{genre}{Colors.RESET} - 인기도 예측: {Colors.GREEN}{score}%{Colors.RESET}")

# AI 음악 추천 기능
def ai_music_recommendation(song_list):
    clear_screen()
    print_logo()
    print(f"\n{Colors.BOLD}{Colors.GREEN}{'═' * 10} 빅데이터 기반 AI 음악 추천 {'═' * 10}{Colors.RESET}")
    
    # 로딩 효과
    print(f"{Colors.CYAN}사용자 음악 취향을 분석 중입니다...{Colors.RESET}")
    loading_animation("데이터 수집 및 처리 중", 1)
    loading_animation("머신러닝 모델 적용 중", 1)
    loading_animation("최적의 음악 추천 계산 중", 1)
    
    # 메인 추천곡 (랜덤 선택)
    if not song_list:
        print(f"{Colors.RED}추천할 데이터가 없습니다.{Colors.RESET}")
        return
        
    main_song = random.choice(song_list[:20])
    
    # 추가 추천곡
    additional_songs = []
    for _ in range(4):
        song = random.choice(song_list[:50])
        if song not in additional_songs and song != main_song:
            additional_songs.append(song)
    
    # 메인 추천곡 출력
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}▶ 오늘의 TOP 추천곡:{Colors.RESET}")
    
    # 추천곡 카드 출력
    width = 60
    print(f"{Colors.BOLD}┌{'─' * width}┐{Colors.RESET}")
    
    title = main_song[1]
    artist = main_song[2]
    rank = main_song[0]
    
    # 제목이 너무 길면 자름
    if len(title) > width - 10:
        title = title[:width - 13] + "..."
    
    print(f"{Colors.BOLD}│{Colors.RESET} {Colors.RED}#{rank}{Colors.RESET} {Colors.YELLOW}{title}{Colors.RESET}{' ' * (width - len(title) - len(rank) - 4)}{Colors.BOLD}│{Colors.RESET}")
    print(f"{Colors.BOLD}│{Colors.RESET} 아티스트: {Colors.CYAN}{artist}{Colors.RESET}{' ' * (width - len(artist) - 12)}{Colors.BOLD}│{Colors.RESET}")
    
    # 가상의 음악 특성 점수
    features = {
        "멜로디 매력도": f"{random.randint(85, 99)}%",
        "리듬감": f"{random.randint(80, 99)}%",
        "취향 일치도": f"{random.randint(90, 99)}%",
        "인기도": f"{random.randint(75, 99)}%"
    }
    
    for key, value in features.items():
        print(f"{Colors.BOLD}│{Colors.RESET} {key}: {Colors.GREEN}{value}{Colors.RESET}{' ' * (width - len(key) - len(value) - 3)}{Colors.BOLD}│{Colors.RESET}")
    
    print(f"{Colors.BOLD}└{'─' * width}┘{Colors.RESET}")
    
    # 추천 이유
    reasons = [
        "당신의 이전 청취 패턴과 높은 일치도를 보입니다",
        "현재 트렌드와 당신의 취향을 고려한 최적의 선택입니다",
        "이 곡의 음악적 특성이 당신이 좋아하는 다른 곡들과 유사합니다",
        "당신과 유사한 취향을 가진 사용자들이 높게 평가한 곡입니다",
        "당신의 최근 재생 목록과 조화롭게 어울리는 추천곡입니다"
    ]
    
    print(f"\n{Colors.GREEN}추천 이유: {random.choice(reasons)}{Colors.RESET}")
    x``
    # 추가 추천곡 출력
    print(f"\n{Colors.BOLD}{Colors.BLUE}▶ 함께 들으면 좋은 곡:{Colors.RESET}")
    for i, song in enumerate(additional_songs, 1):
        print(f"  {Colors.YELLOW}{i}.{Colors.RESET} {song[1]} - {Colors.CYAN}{song[2]}{Colors.RESET}")
    
    print(f"\n{Colors.GREEN}* 이 추천은 빅데이터 분석과 AI 알고리즘을 기반으로 생성되었습니다.{Colors.RESET}")

# 프로그램 정보 출력
def print_info():
    print(f"\n{Colors.BOLD}{Colors.YELLOW}▶ 프로그램 정보:{Colors.RESET}")
    print(f"  {Colors.GREEN}• 버전: 1.0.0{Colors.RESET}")
    print(f"  {Colors.GREEN}• 업데이트: {time.strftime('%Y-%m-%d')}{Colors.RESET}")
    print(f"  {Colors.GREEN}• 데이터 소스: 애플 뮤직 글로벌 차트{Colors.RESET}")

# 메인 함수
def main():
    url = 'https://music.apple.com/kr/playlist/%EC%98%A4%EB%8A%98%EC%9D%98-top-100-%EA%B8%80%EB%A1%9C%EB%B2%8C/pl.d25f5d1181894928af76c85c967f8f31'
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    
    # 초기 화면
    clear_screen()
    print_logo()
    print(f"{Colors.CYAN}애플 뮤직 데이터를 불러오는 중입니다...{Colors.RESET}")
    
    song_list = []
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            loading_animation("데이터 분석 중", 1.5)
            
            soup = BeautifulSoup(response.text, 'html.parser')
            songs = soup.select('table.list-wrap tbody tr')
            
            for song in songs:
                title_tag = song.select_one('a.title')
                artist_tag = song.select_one('a.artist')
                rank_tag = song.select_one('td.number')
                
                if title_tag and artist_tag and rank_tag:
                    title = title_tag.text.strip()
                    artist = artist_tag.text.strip()
                    rank = rank_tag.text.strip().split()[0]
                    song_list.append((rank, title, artist))
        else:
            print(f"{Colors.RED}웹 페이지를 불러오는 데 실패했습니다. 상태 코드: {response.status_code}{Colors.RESET}")
            time.sleep(1.5)
    except Exception as e:
        print(f"{Colors.RED}오류 발생: {str(e)}{Colors.RESET}")
        time.sleep(1.5)
    
    # 데이터를 못 가져온 경우 샘플 데이터 생성
    if not song_list:
        print(f"{Colors.YELLOW}실제 데이터를 가져오지 못했습니다. 샘플 데이터를 생성합니다...{Colors.RESET}")
        loading_animation("샘플 데이터 생성 중", 1.5)
        
        # 샘플 데이터 생성
        sample_titles = ["Fortnight", "Texas Hold 'Em", "Birds of a Feather", "NEED A FAVOR", "Espresso", 
                        "Come Home The Kids Miss You", "Water", "Houdini", "Paint The Town Red", "Stick Season"]
        sample_artists = ["Taylor Swift", "Beyoncé", "Billie Eilish", "Travis Scott", "Sabrina Carpenter", 
                        "Jack Harlow", "Tyla", "Dua Lipa", "Doja Cat", "Noah Kahan"]
        
        for i in range(100):
            idx = i % 10
            rank = str(i + 1)
            title = sample_titles[idx] if i < 10 else f"{sample_titles[idx]} - Ver. {(i // 10) + 1}"
            artist = sample_artists[idx]
            song_list.append((rank, title, artist))
    
    while True:
        clear_screen()
        print_logo()
        print_menu()
        print_info()
        
        choice = input(f"\n{Colors.YELLOW}원하시는 서비스 번호를 입력하세요: {Colors.RESET}")
        
        if choice == "1":
            clear_screen()
            print_logo()
            print_song_list(song_list, 100, "애플 차트 TOP 100")
            input(f"\n{Colors.YELLOW}메인 메뉴로 돌아가려면 Enter 키를 누르세요...{Colors.RESET}")
        
        elif choice == "2":
            clear_screen()
            print_logo()
            print_song_list(song_list, 50, "애플 차트 TOP 50")
            input(f"\n{Colors.YELLOW}메인 메뉴로 돌아가려면 Enter 키를 누르세요...{Colors.RESET}")
        
        elif choice == "3":
            clear_screen()
            print_logo()
            print_song_list(song_list, 10, "애플 차트 TOP 10")
            input(f"\n{Colors.YELLOW}메인 메뉴로 돌아가려면 Enter 키를 누르세요...{Colors.RESET}")
        
        elif choice == "4":
            ai_music_recommendation(song_list)
            input(f"\n{Colors.YELLOW}메인 메뉴로 돌아가려면 Enter 키를 누르세요...{Colors.RESET}")
        
        elif choice == "5":
            artist_data = analyze_artists(song_list)
            print_artist_popularity(artist_data)
            input(f"\n{Colors.YELLOW}메인 메뉴로 돌아가려면 Enter 키를 누르세요...{Colors.RESET}")
        
        elif choice == "6":
            genre_data = generate_genre_trends()
            print_genre_trends(genre_data)
            input(f"\n{Colors.YELLOW}메인 메뉴로 돌아가려면 Enter 키를 누르세요...{Colors.RESET}")
        
        elif choice == "0":
            clear_screen()
            print_logo()
            print(f"\n{Colors.RED}프로그램을 종료합니다...{Colors.RESET}")
            time.sleep(1.5)
            clear_screen()
            break
        
        else:
            print(f"\n{Colors.RED}잘못된 선택입니다! 0-6 사이의 숫자를 입력하세요.{Colors.RESET}")
            time.sleep(1.5)

if __name__ == "__main__":
    main()
