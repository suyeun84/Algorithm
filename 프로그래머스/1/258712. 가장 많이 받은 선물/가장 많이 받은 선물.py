def solution(friends, gifts):
    answer = 0
    # A가 B에게 더 많은 선물 줬으면 A가 받음
    # A==B이면 선물지수 큰 사람이 받음
    # 선물지수 = 친구들에게 준 선물수 - 받은 선물수
    # 선물지수마저 같으면 다음 달에 선물을 주고받지 않음
    
    # answer = 선물을 가장 많이 받을 친구가 받을 선물의 수
    # friends: 친구들의 이름
    # gifts: 친구들이 주고받은 선물 기록
    
    index = {}
    for i in range(len(friends)):
        index[friends[i]] = i
    
    #주고 받은 선물
    arr = [[0 for _ in range(len(gifts))] for _ in range(len(gifts))]
    for gift in gifts:
        give, get = gift.split(" ")
        arr[index[give]][index[get]] += 1
    
    #선물 지수
    gift_index = {}
    for i in range(len(friends)):
        give = 0
        get = 0
        for j in range(len(friends)):
            give += arr[i][j]
            get += arr[j][i]
        gift_index[i] = give-get
        
    #가장 많이 받는 친구의 선물 개수 찾기
    for i in range(len(friends)):
        gift = 0
        for j in range(len(friends)):
            if arr[i][j] > arr[j][i]:
                gift += 1
            elif arr[i][j] == arr[j][i]:
                if gift_index[i] > gift_index[j]:
                    gift += 1
        answer = max(answer, gift)
    return answer
    
        
    
    
    return answer