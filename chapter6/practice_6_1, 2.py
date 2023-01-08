def open_account():
    print("새로운 계좌가 생성되었습니다")


def deposit(balance, money):
    print(f"입금되었습니다. 잔액은 {balance + money}원 입니다")
    return balance + money


def withdraw(balance, money):
    if balance >= money:
        print(f"출금이 완료되었습니다. 잔액은 {balance - money}원 입니다")
        return balance - money
    else:
        print(f"출금이 완료되지 않았습니다. 잔액은 {balance}원 입니다")
        return balance


def withdraw_night(balance, money):
    fee = 100
    return fee, balance - money - fee


balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
fee, balance = withdraw_night(balance, 500)
print(f"수수료는 {fee} 원이며, 잔액은 {balance}원 입니다")
