mylist=[20,30,40,50,60]
mean  = 0.0
total = 0.0
for x in mylist:
    total = sum(mylist)
    mean = total/len(mylist)
print(mean)

thelist=[2,2,4,4,6,6]
_mean=0.0
for x in range(len(thelist)):
#accumulate everything into +mean    
    _mean+= thelist[x]
_mean = _mean/len(thelist)
print(_mean)    
    
