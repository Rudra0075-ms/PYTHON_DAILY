def unique(num):
    count_dict={}
    for n in num:
        if n in count_dict:
            count_dict[n]+=1
        else:
            count_dict[n]=1
    for n, count in count_dict.items():
        if count==1:
            return n
print(unique([5,4,3,4,5]))
