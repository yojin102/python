# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

number = 9

if number > 10:
    print("입력한 숫자는 10보다 큽니다.")
else:
    print("입력한 숫자는 10보다 작습니다.")
    
#사용자로부터 무게 입력 받기
weight = int(input("상품의 무게(g): "))

if weight > 500:
    shipping_cost = 5000
else:
    shipping_cost = 2000
    
print("배송비 :", shipping_cost)

#중첩if문
score = int(input("점수를 입력하세요. (0-100): "))
if score >= 60:
    print("합격")
    
    if score >= 90:
        print("우수한 성적입니다!")
    else:
        print("좋은 성적입니다.")
else:
    print("불합격")
    
    if score < 40:
        print("더 많이 공부하세요.")
        
#부울 변수
age = int(input("나이 입력: "))

is_adult = (age >= 18)
print(is_adult)

if is_adult:
    print("성인")
else:
    print("미자")
    
#문자열 비교
password = input("비밀번호 입력: ")

correct_password = "sleepy942"

if password == correct_password:
    print("비밀번호 일치, 로그인 성공")
else:
    print("비밀번호 불일치, 다시 시도하세요.")
