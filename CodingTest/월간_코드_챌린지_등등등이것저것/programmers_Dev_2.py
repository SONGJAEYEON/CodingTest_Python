#2
# n    groups    result
# 10    [[1, 5],[2, 7],[4, 8],[3, 6]]    4
# 7    [[6, 7],[1, 4],[2, 4]]    3
# 100    [[1, 50],[1,100],[51, 100 ]]    1

#아 이건 진짜 어떻게 해야될지 모르겠더라,,, 

n=10
groups=[[1, 5],[2, 7],[4, 8],[3, 6]]
[g.append(abs(g[1]-g[0])) for g in groups]
groups=sorted(groups,key=lambda x:(-x[2],-x[1],x[0]))
print(groups)
    
    
