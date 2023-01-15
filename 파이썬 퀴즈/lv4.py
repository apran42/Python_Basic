"""
Quiz) 행맨 게임(영어 단어 퀴즈) 프로그램을 만드시오

- 리스트에 3개 이상의 단어를 추가
ex) apple, banana, orange

- 위 리스트에서 랜덤으로 1개의 단어를 선택

- 단어의 길이에 맞게 출력
ex) apple의 경우 _____

- 사용자로부터 1글자씩 입력을 받되, 단어에 입력값이 포함되면 'Correct', 아니면 'Wrong'출력

- 매번 입력을 받을 때마다 현재까지 맞힌 글자들 표시 (맞히지 못한 글자는 밑줄 출력)
ex) a 입력 시 : a____
    p 입력 시 : app__
    c 입력 시 : app__

- 정답을 맞히면 Success 출력 후 프로그램 종료 (단, 횟수 제한은 없음)

"""
import random

words_list = ['apple', 'banana', 'cat', 'keyboard', 'mouse']

word = words_list[random.randint(0, len(words_list) - 1)]  # 단어 랜덤으로 고르기

answer = []  # 빈 배열 생성

for i in word:
    answer.append('_')  # word의 길이만큼 '_'로 채우기

while True:
    for i in answer:
        print(i, end=" ")

    letter = input("\ninput letter >> ")  # 알파벳 받기

    if letter in word:  # 받은 알파벳이 단어에 있으면
        for i in range(len(word)):
            if word[i] == letter:  # 받은 알파벳의 해당하는 인덱스값으로 answer 배열에 알파벳 저장
                answer[i] = letter
        if ''.join(answer) == word:  # answer배열(단어)과 word가 일치
            print("Success!!")
            break
        else:
            print("Correct!\n")

    else:
        print("Wrong!")
