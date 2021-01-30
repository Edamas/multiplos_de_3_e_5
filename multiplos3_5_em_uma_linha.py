for n in range(1, 101): print(n, {(0,0):'',(1,0):'BHUT',(0,1):'IT',(1,1):'BHUT IT'}[(n % 3 == 0),(n % 5 == 0)],end='\t')
