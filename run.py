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
    (0, 5): "이윤재관",
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