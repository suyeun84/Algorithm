def solution(elements):
    num = set()
    
    for i in range(len(elements)):
        s = elements[i]
        num.add(s)
        
        for j in range(i+1, i+len(elements)):
            s += elements[j%len(elements)]
            num.add(s)
            
    return len(num)
