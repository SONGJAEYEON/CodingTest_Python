def solution(prices):
    answer = [0 for _ in range(len(prices))]
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i]<=prices[j]:
                answer[i]+=1
            else:
                answer[i]=j-i
                break
    return answer