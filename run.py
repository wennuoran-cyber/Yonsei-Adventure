import json

settings = {
    "난이도": "보통" 
}

player = {
    "현재위치": "연대앞 버스정류장",
    "상태": "배고픔",
    "HP": 10.0, 
    "잔액": 10000,
    "가방": [],
    "임무목록": []
}

current_time = "11:00"
world_map = {
    (0, 0): "연대앞 버스정류장",
    (1, 0): "정문",
    (2, 0): "스타벅스",
    (3, 0): "세브란스병원",
    (1, 1): "백양로1",
    (1, 2): "백양로2",
    (2, 2): "백주년기념관",
    (2, 1): "독수리상",
    (2, 3): "학생회관",
    (0, 5): "이윤재관",
    (2, 4): "본관" 
}

current_pos = [0, 0]

print("게임 시작!")

while True:
    current_location = world_map.get(tuple(current_pos), "알 수 없는 곳")
    print(f"\n현재 위치: {current_location}")
    print(f"상태: HP {player['HP']}, 잔액 {player['잔액']}원")
    
    move = input("명령(동,서,남,북,상태,상호작용,가방,임무,저장,불러오기,종료): ")

    if move == "종료":
        print("게임을 종료합니다.")
        break
    
    elif move in ["동", "서", "남", "북"]:
        next_pos = current_pos[:]
        if move == "동": next_pos[0] += 1
        elif move == "서": next_pos[0] -= 1
        elif move == "남": next_pos[1] -= 1
        elif move == "북": next_pos[1] += 1

        if tuple(next_pos) in world_map:
            current_pos = next_pos
            hp_loss = 1.0
            if settings["난이도"] == "쉬움": hp_loss = 0.5
            elif settings["난이도"] == "어려움": hp_loss = 2.0
            
            player['HP'] -= hp_loss
            print(f"{move}쪽으로 이동. HP가 {hp_loss}만큼 감소했습니다.")
        else:
            print("그 방향은 막혔어.")

    elif move == "상태":
        print(f"상세 상태")
        print(f"계좌 잔액: {player['잔액']}원")
        print(f"현재 HP: {player['HP']}")
        print(f"가방: {player['가방']}")
        print(f"진행중인 임무: {player['임무목록']}")

    elif move == "상호작용":
        if current_location == "학생회관":
            print("1) 두쫀쿠(5000원) 2) 카페라떼(3000원)")
            choice = input("번호 선택: ")
            price = 5000 if choice == "1" else 3000
            name = "두쫀쿠" if choice == "1" else "카페라떼"
            if player["잔액"] >= price:
                player["잔액"] -= price
                player["가방"].append(name)
                print(f"{name} 구매 완료.")
            else:
                print("잔액 부족.")
        elif current_location == "스타벅스":
            print("스타벅스 할인: 1) 두쫀쿠(4000원) 2) 카페라떼(2000원)")
        else:
            print("이곳엔 상호작용할 대상이 없습니다.")

    elif move == "가방":
        if not player["가방"]:
            print("가방이 비어있습니다.")
        else:
            for i, item in enumerate(player["가방"]):
                print(f"{i+1}) {item}")
            idx = input("사용할 번호(0은 취소): ")
            if idx.isdigit() and int(idx) > 0:
                item = player["가방"].pop(int(idx)-1)
                heal = 10 if item == "두쫀쿠" else 5
                player["HP"] += heal
                print(f"{item} 사용! HP {heal} 회복.")

    elif move == "임무":
        if current_location == "정문":
            print("독수리상으로 가보세요.")
            if "독수리상 방문" not in player["임무목록"]:
                player["임무목록"].append("독수리상 방문")
        elif current_location == "독수리상":
            print("1) 부조리 수사 2) 위생 수사")
            q_choice = input("선택: ")
            q_name = "부조리 수사" if q_choice == "1" else "위생 수사"
            player["임무목록"].append(q_name)
            print(f"{q_name} 임무 수락.")
        elif current_location == "이윤재관":
            if not player["임무목록"]:
                print("축하합니다! 수업에 도착하여 게임을 클리어했습니다.")
                break
            else:
                print("남은 임무를 완료해야 합니다.")

    elif move == "저장":
        with open("savegame.json", "w", encoding="utf-8") as f:
            json.dump({"player": player, "pos": current_pos}, f, ensure_ascii=False)
        print("저장되었습니다.")

    elif move == "불러오기":
        try:
            with open("savegame.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                player, current_pos = data["player"], data["pos"]
            print("데이터를 불러왔습니다.")
        except:
            print("파일이 없습니다.")

    if player['HP'] <= 0:
        print("HP가 0입니다. 게임 오버!")
        break