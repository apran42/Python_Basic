def attack(name, location, damage):
    print(f"{name} : {location} 방향으로 적군을 공격합니다. [공격력 {damage}]")

# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
marine_name = "마린"  # 유닛의 이름
marine_hp = 40  # 유닛의 체력
marine_damage = 5  # 유닛의 공격력

print(f"{marine_name} 유닛이 생성되었습니다.")
print(f"체력 {marine_hp}, 공격력 {marine_damage}\n")

# 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print(f"{tank_name} 유닛이 생성되었습니다.")
print(f"체력 {tank_hp}, 공격력 {tank_damage}\n")

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print(f"{tank2_name} 유닛이 생성되었습니다.")
print(f"체력 {tank2_hp}, 공격력 {tank2_damage}\n")

attack(marine_name, "1시 방향", marine_damage)
attack(tank_name, "1시 방향", tank_damage)
attack(tank2_name, "1시 방향", tank2_damage)

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성되었습니다.")
        print(f"체력 {self.hp}, 공격력 {self.damage}")

# marine = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print(f"유닛 이름 : {wraith1.name}, 공격력 : {wraith1.damage}")    # 멤버 변수에 접근

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # 객체에 추가로 변수를 외부에서 사용 가능

if wraith2.clocking:
    print(f"{wraith2.name}는 현재 클로킹 상태입니다.")
