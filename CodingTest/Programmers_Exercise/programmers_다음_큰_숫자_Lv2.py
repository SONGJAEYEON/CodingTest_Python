#다음 큰 숫자,,, 

#조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다
#조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을때 1의 개수가 같숩니다.
#조건 3. n의 다음 큰 숫자는 조건 1,2를 만족하는 수 중 가장 작은 수 입니다 

#파일명을 세 부분으로 나눈 후 다음 기준에 따라 파일명을 정렬한다.

#파일명은 우선 head기준으로 사전순으로 정렬한다.

#그래 지금 이건 내가 머리싸메서하는게아니고 아 이렇게하는거구나 하면서 아는게중요한거지!@

#파이썬의 정규식관련 라이브러리린 re를 사용하면 쉽게 풀 수 있다

#문제의 조건대로 
#1.head와 number,tail을 구분한다 숫자를 반영해서 정렬해야 하므로 숫자 기준으로 spilt하면된다

#2. 숫자 기준으로 spilt했으면 문제에서 제공한 조건에 맞게 정렬해야한다. 
#문자 대소문자 구분을 할 필요가  없으므로 정렬기준에서 통일하고
#문자열로 되어있는 숫자를 숫자값에 맞추어 정렬한다

#3. 정렬된 리스트안에있는 spilit된 값들을 문자열로 바꾸어 출력한다.

def solution(files):
    import re
    #1. 정규식을 사용하여 head number tail을 구변한다.
    temp=[re.split(r"([0-9]+)",s) for s in files]
    print(temp)
    #2. 문제의 조건에 맞게 정렬정렬!@
    sort=sorted(temp,key=lambda x:(x[0].lower(),int(x[1])))
    print(sort)
    #3. 
    return ["".join(s) for s in sort]