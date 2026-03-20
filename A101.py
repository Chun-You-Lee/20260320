data=input("Please enter 3 numbers:").split()

[int(d) for d in data] #串列生成式 第三行=第五、六行

for i  in range(len(data)):
    data[i]=int(data[i])
    
#range(len(data))=range(3)=[0,1,2]
print(sum(data))

data =[int(d) for d in input("Please enter 3 numbers:").split()] #最終寫法