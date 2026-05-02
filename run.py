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

    if move == "임무":
        if current_location == "정문":
            print("[정문 알림] 학교 소식은 독수리상에서 알아보세요!")
            player.setdefault("임무목록", []).append("독수리상 방문하기") 
        
        elif current_location == "독수리상":
            print("--- 독수리상 임무 받기 ---")
            print("1) 교내 부조리 수사 (본관 보고)")
            print("2) 교내 위생사건 수사 (세브란스 보고)")
            q_choice = input("임무 번호를 입력하세요: ")
            if q_choice == "1":
                player.setdefault("임무목록", []).append("교내 부조리 수사") 
                print("부조리 수사 임무를 받았습니다.")
            elif q_choice == "2":
                player.setdefault("임무목록", []).append("교내 위생사건 수사") 
                print("위생사건 수사 임무를 받았습니다.")
        
        elif current_location == "이윤재관":
            if "교내 부조리 수사" in player.get("임무목록", []) or "교내 위생사건 수사" in player.get("임무목록", []):
                print("임무를 모두 완료하셨나요? 본관이나 세브란스에서 먼저 보고하세요.")
            else:
                print("축하합니다! 수업에 도착했습니다. 게임 종료!") 
                break
        else:
            print("이곳에는 진행할 임무가 없습니다.")

    elif move == "상태":
        print(f"--- 현재 상태 ---")
        print(f"계좌 잔액: {player['잔액']}원") 
        print(f"HP: {player['HP']}") 
        print(f"현재 위치: {current_location}") 
        print(f"동서남북: 주변 확인 가능") 

