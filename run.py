settings = {
    "난이도": "보통" 
}

player = {
    "현재위치": "연대앞 버스정류장",
    "상태": "배고픔",
    "HP": 10,  
    "잔액": 10000 
}

current_time = "11:00"

print(f"--- 게임 시작 ---")
print(f"현재 시각: {current_time}")
print(f"현재 위치: {player['현재위치']}")
print(f"주인공 상태: {player['상태']} (HP: {player['HP']})")

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
    (0, 5): "이윤재관"        
}

current_pos = [0, 0]  # (x, y) 좌표

while True:
    print(f"\n현재 위치: {world_map.get(tuple(current_pos), '알 수 없는 곳')}")
    print(f"상태: HP {player['HP']}, 잔액 {player['잔액']}원")
    
    move = input("어디로 갈까요? (동, 서, 남, 북, 상태, 종료): ")

    if move == "종료":
        print("게임을 종료합니다.")
        break
    
    next_pos = current_pos[:]

    if move == "동":
        next_pos[0] += 1
    elif move == "서":
        next_pos[0] -= 1
    elif move == "남":
        next_pos[1] -= 1
    elif move == "북":
        next_pos[1] += 1
    elif move == "상태":
        print(f"현재 위치: {world_map.get(tuple(current_pos))}")
        continue
    else:
        print("잘못된 입력입니다.")
        continue

    if tuple(next_pos) in world_map:
        current_pos = next_pos
        player['HP'] -= 1
        print(f"{move}쪽으로 한 칸 이동했습니다.")
    else:
        print("그 방향은 막혔어.") 

    if player['HP'] <= 0:
        print("HP가 0이 되어 더 이상 움직일 수 없습니다. 게임 오버!")
        break

    current_location = world_map.get(tuple(current_pos))
    
    if move == "상호작용":
        if current_location == "학생회관":
            print("--- 학생회관 상점 ---")
            print("1) 두쫀쿠 (5000원, HP +10)")
            print("2) 카페라떼 (3000원, HP +5)")
            choice = input("구매할 물건의 번호를 입력하세요: ")
            
            if choice == "1":
                if player["잔액"] >= 5000:
                    player["잔액"] -= 5000
                    player.setdefault("가방", []).append("두쫀쿠")
                    print("두쫀쿠를 구매하여 가방에 넣었습니다.")
                else:
                    print("잔액이 부족합니다.")
            elif choice == "2":
                if player["잔액"] >= 3000:
                    player["잔액"] -= 3000
                    player.setdefault("가방", []).append("카페라떼")
                    print("카페라떼를 구매하여 가방에 넣었습니다.")
                else:
                    print("잔액이 부족합니다.")
        
        elif current_location == "스타벅스":
            print("--- 스타벅스 ---")
            print("1) 두쫀쿠 (4000원, HP +10)")
            print("2) 카페라떼 (2000원, HP +5)")
        else:
            print("이곳에서는 상호작용할 것이 없습니다.")

    elif move == "가방":
        if not player.get("가방"):
            print("가방이 비어 있습니다.")
        else:
            print("가방 목록")
            for i, item in enumerate(player["가방"]):
                print(f"{i+1}) {item}")
            
            item_choice = input("사용할 물건 번호를 입력하세요 (취소는 0): ")
            if item_choice.isdigit() and int(item_choice) > 0:
                idx = int(item_choice) - 1
                if idx < len(player["가방"]):
                    used_item = player["가방"].pop(idx)
                    if used_item == "두쫀쿠":
                        player["HP"] += 10
                    elif used_item == "카페라떼":
                        player["HP"] += 5
                    print(f"{used_item}을(를) 사용했습니다! HP가 회복되었습니다.")