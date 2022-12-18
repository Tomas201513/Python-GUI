with open('h.txt','r') as f:
    x=f.readlines()[-1]
    if x!="m":
        print('yes')
    f.close()