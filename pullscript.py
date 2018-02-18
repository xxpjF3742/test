data = set([i.replace('\n','') for i in open('Exchanges.csv','r')])

for i in data:
    print(i)
