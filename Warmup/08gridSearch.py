def gridSearch():
    for t in range(int(raw_input())):
      r,c = map(int,raw_input().split(' '))
      grid = []
      for i in range(0,r):
          grid.append([])
          for j in range(0,c):
              grid[i].append(0)
      for i in range(0,r):
          row = map(int,raw_input())
          for j in range(0,c):
              grid[i][j] = row[j]   
      
      R, C = map(int, raw_input().split(' '))
      pattern = []
      for i in range(0,R):
          pattern.append([])
          for j in range(0,C):
              pattern[i].append(0)
      for i in range(0,R):
          row = map(int,raw_input())
          for j in range(0,C):
              pattern[i][j] = row[j]
      
      flag = False    
      for i in range(0,r-R+1):
          if flag:
              break
          for j in range(0,c-C+1):
              if flag:
                  break
              count = 0
              if grid[i][j] == pattern[0][0]:
                  for m in range(0,R):
                      for n in range(0, C):
                          if grid[m+i][n+j] == pattern[m][n]:
                              count+=1
                          else:
                              break  

                  if count == R*C:
                    flag = True
                    
      if flag:
          print 'YES'
      else:
          print 'NO'

                              
                  
        
        