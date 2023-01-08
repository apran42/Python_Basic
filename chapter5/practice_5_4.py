absent = [2, 5]
no_books = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_books:
        print(f"오늘 수업은 여기까지. {student}번은 교무실로 따라와")
        break
    print(f"{student}번, 책을 읽어봐")