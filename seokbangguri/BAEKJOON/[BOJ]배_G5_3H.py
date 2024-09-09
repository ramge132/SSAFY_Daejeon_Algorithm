import heapq

N = int(input())
crains = sorted(list(map(int, input().split())), reverse = True)

M = int(input())
boxes = list(map(lambda x: -1 * int(x), input().split()))

heapq.heapify(boxes)

minutes = 0
cannot_move = False

while boxes:
    if cannot_move:
        break

    temp_boxes = []
    for idx, crain in enumerate(crains):
        if not boxes:
            break

        box = heapq.heappop(boxes)

        # 가장 큰 크레인으로도 박스를 옮길 수 없는 경우 모든 박스를 옮길 수 없음
        if idx == 0 and crain < box[1]:
            print(-1)
            cannot_move = True
            break
        
        # 이 부분 수정 필요함
        elif crain < box[1]:
            not_working = True
            temp_boxes.append(box)
            while boxes:
                box = heapq.heappop(boxes)
                if crain >= box[1]:
                    now_working = False
                    break
                temp_boxes.append(box)

            
            if not_working:
                continue

    boxes += temp_boxes
    heapq.heapify(boxes)

    minutes += 1

if not cannot_move:
    print(minutes)
            




