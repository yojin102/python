# -*- coding: utf-8 -*-

from tkinter import *
import random

answer = random.randint(1, 100)  # 정답을 1에서 100 사이의 난수로 설정
count = 0  # 시도 횟수
max_count = 10  # 최대 시도 횟수

def set_difficulty(level): # 난이도에 따른 최대 시도 횟수 설정
    global max_count
    if level == "쉬움":
        max_count = 15
    elif level == "보통":
        max_count = 10
    elif level == "어려움":
        max_count = 5
    reset()  # 난이도 설정 후 게임을 초기화

def guessing():
    global count
    guess = int(guessField.get())
    count += 1  # 시도 횟수 증가
    
    if count > max_count:  # 시도 횟수 초과 시 게임 종료
        resultLabel["text"] = "게임 종료! 최대 시도 횟수 초과. 재시도시 초기화 버튼을 누르세요."
        guessField.delete(0, END)
        guessField.config(state="disabled")  # 입력 비활성화
        return

    if guess > answer:
        msg = "정답 보다 높음"
    elif guess < answer:
        msg = "정답 보다 낮음"
    else:
        msg = f"정답! {count}번 만에 맞췄습니다!"
    
    resultLabel["text"] = msg  # 메시지를 출력
    hintLabel["text"] = f"시도 횟수 : {count} / {max_count}"  # 힌트 라벨 초기화
    guessField.delete(0, END)  # 입력 필드 초기화

def reset():  # 정답을 다시 설정
    global answer, count
    answer = random.randint(1, 100)
    count = 0  # 시도 횟수 초기화
    resultLabel["text"] = "결과"
    hintLabel["text"] = f"시도 횟수 : 0 / {max_count}"
    guessField.config(state="normal")  # 입력 활성화

def show_hint():  # 힌트를 제공
    lower_bound = max(1, answer - 10)
    upper_bound = min(100, answer + 10)
    hintLabel["text"] = f"{lower_bound} ~ {upper_bound} 사이 값"

# GUI 설정
window = Tk()
window.configure(bg="white")
window.title("숫자를 맞춰보세요!")
window.geometry("700x250")

# Canvas 추가 (상단 제목 표시)
canvas = Canvas(window, width=600, height=70, bg="lightblue")
canvas.create_text(300, 40, text="분반:1, 학번:20232297, 이름:최요진", font=("Arial", 23))
canvas.pack()

# 제목 라벨
titleLabel = Label(window, text="1부터 100 사이의 숫자를 입력하시오.", bg="white", font=("Arial", 12))
titleLabel.pack()

# 난이도 선택 프레임
difficultyFrame = Frame(window, bg="white")
difficultyFrame.pack(pady=5)

easyButton = Button(difficultyFrame, text="쉬움", bg="lightgreen", font=("Arial", 10), command=lambda: set_difficulty("쉬움"))
easyButton.pack(side="left", padx=5)

normalButton = Button(difficultyFrame, text="보통", bg="yellow", font=("Arial", 10), command=lambda: set_difficulty("보통"))
normalButton.pack(side="left", padx=5)

hardButton = Button(difficultyFrame, text="어려움", bg="red", fg="white", font=("Arial", 10), command=lambda: set_difficulty("어려움"))
hardButton.pack(side="left", padx=5)

# 입력과 버튼, 라벨을 하나로 묶는 프레임
frame = Frame(window, bg="white")
frame.pack(pady=7)

# 입력 필드 및 버튼
guessField = Entry(frame, font=("Arial", 12))
guessField.pack(side="left", padx=5)

tryButton = Button(frame, text="시도", fg="green", bg="white", font=("Arial", 10), command=guessing)
tryButton.pack(side="left", padx=1)

resetButton = Button(frame, text="초기화", fg="red", bg="white", font=("Arial", 10), command=reset)
resetButton.pack(side="left", padx=1)

hintButton = Button(frame, text="힌트", fg="blue", bg="white", font=("Arial", 10), command=show_hint)
hintButton.pack(side="left", padx=1)

# 결과 및 힌트 라벨
resultLabel = Label(window, text="결과", bg="darkgray", font=("Arial", 12))
resultLabel.pack()

hintLabel = Label(frame, text=f"시도 횟수 : 0 / {max_count}", bg="darkgray", font=("Arial", 12))
hintLabel.pack(side="left", padx=1)

# 메인 루프 실행
window.mainloop()