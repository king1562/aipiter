import tkinter as tk
from PIL import Image, ImageTk
import os # 파일 경로를 다루기 위해 import
import random # 랜덤 기능을 위해 추가

# --- 함수 정의 ---
def show_image(animal_type):
    """선택된 동물 타입에 맞는 이미지를 로드하여 화면에 표시하는 함수"""
    global photo_image # 이미지 참조 유지를 위한 전역 변수 사용
    
    # 'randaom'이 선택되었을 때 랜덤으로 동물 타입 선택
    if animal_type == 'randaom':
        animal_options = ['dog', 'cat', 'rabbit']
        animal_type = random.choice(animal_options)
        status_label.config(text=f"랜덤 선택: {animal_type}")
    else:
        status_label.config(text=f"선택된 동물: {animal_type}")

    # 이미지 파일 경로 설정 (스크립트와 같은 디렉토리에 있다고 가정)
    # 파일 확장자가 다를 경우 이 부분을 수정하세요 (예: .png)
    file_name = f"{animal_type}.jpg"
    file_path = os.path.join(os.path.dirname(__file__), file_name) # 스크립트 기준 상대 경로

    try:
        # Pillow를 사용하여 이미지 열기
        pil_image = Image.open(file_path)

        # (선택 사항) 이미지 크기 조정
        max_width = 400
        max_height = 350
        pil_image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)

        # Pillow 이미지를 Tkinter용 PhotoImage 객체로 변환
        photo_image = ImageTk.PhotoImage(pil_image)

        # 이미지 레이블 업데이트
        image_label.config(image=photo_image, text="") # 기존 텍스트 제거
        image_label.image = photo_image # 레이블 객체에 참조 유지 (가비지 컬렉션 방지)

        print(f"{animal_type} 이미지 로드 완료.")

    except FileNotFoundError:
        error_message = f"오류: '{file_name}' 파일을 찾을 수 없습니다.\n스크립트와 같은 폴더에 있는지 확인하세요."
        print(error_message)
        image_label.config(text=error_message, image='') # 오류 메시지 표시, 기존 이미지 제거
    except Exception as e:
        error_message = f"오류: {file_name} 이미지 로드 중 문제 발생\n{e}"
        print(error_message)
        image_label.config(text=error_message, image='') # 오류 메시지 표시, 기존 이미지 제거

# --- GUI 설정 ---
# 메인 윈도우 생성
window = tk.Tk()
window.title("나락 동물 맞추기기")
window.geometry("500x500") # 초기 창 크기
window.configure(bg="#f5f5f5") # 배경색 설정

# 전역 변수 초기화 (이미지 참조 유지를 위해)
photo_image = None

# 제목 레이블 추가
title_label = tk.Label(window, text="나락 동물 갤러리", font=("Arial", 16, "bold"), bg="#f5f5f5")
title_label.pack(pady=(15, 5))

# 버튼을 담을 프레임 생성 (버튼들을 가로로 배치하기 위함)
button_frame = tk.Frame(window, bg="#f5f5f5")
button_frame.pack(pady=10) # 상단에 여백을 주고 프레임 배치

# 버튼 스타일 설정 (공통 스타일)
button_style = {
    "width": 10,
    "font": ("Arial", 10),
    "relief": tk.RAISED,
    "padx": 5,
    "pady": 5
}

# 강아지 버튼 생성
dog_button = tk.Button(button_frame, text="강아지", bg="#4C8BF5", fg="white",
                       command=lambda: show_image('dog'), **button_style)
dog_button.pack(side=tk.LEFT, padx=5) # 프레임 왼쪽에 배치, 좌우 여백

# 고양이 버튼 생성
cat_button = tk.Button(button_frame, text="고양이", bg="#DB4437", fg="white",
                      command=lambda: show_image('cat'), **button_style)
cat_button.pack(side=tk.LEFT, padx=5) # 프레임 왼쪽에 배치, 좌우 여백

# 토끼 버튼 생성
rabbit_button = tk.Button(button_frame, text="토끼", bg="#0F9D58", fg="white",
                         command=lambda: show_image('rabbit'), **button_style)
rabbit_button.pack(side=tk.LEFT, padx=5) # 프레임 왼쪽에 배치, 좌우 여백

# 랜덤 버튼 생성 (특별히 강조)
random_button = tk.Button(button_frame, text="랜덤", bg="#F4B400", fg="white",
                         command=lambda: show_image('randaom'), **button_style)
random_button.pack(side=tk.LEFT, padx=5) # 프레임 왼쪽에 배치, 좌우 여백

# 이미지 표시 영역 프레임 생성
image_frame = tk.Frame(window, bg="white", width=450, height=350,
                      bd=2, relief=tk.SUNKEN)
image_frame.pack(pady=15, padx=10, fill=tk.BOTH, expand=True)
image_frame.pack_propagate(False)  # 프레임 크기 고정

# 이미지를 표시할 레이블 생성
image_label = tk.Label(image_frame, text="버튼을 클릭하여 동물을 선택하세요.",
                      bg="white", compound=tk.CENTER)
image_label.pack(expand=True, fill=tk.BOTH, padx=10, pady=10) # 창 크기에 맞춰 확장

# 상태 표시 레이블
status_label = tk.Label(window, text="환영합니다! 보고 싶은 동물을 선택하세요.",
                       bg="#f5f5f5", font=("Arial", 10))
status_label.pack(pady=10)

# --- 메인 루프 시작 ---
window.mainloop()
