import os

def good_seq(list):
    print(sorted(list))
    asc_desc = (list == sorted(list) or list == sorted(list, reverse = True))
    good = True
    for i in range(len(list)-1):
        diff = abs(list[i+1]-list[i])
        if(1 > diff or diff > 3):
            good = False
    return good and asc_desc


with open("input.txt", 'r') as f:
    s = 0
    s1 = 0
    for l in f:
        list = l.split()
        list = [int(x) for x in list]

        if(good_seq(list)):
            s+=1

        has_good_seq = False
        for skip in range(len(list)):
            new_list = list[:skip] + list[skip+1:]
            if(good_seq(new_list)):
                has_good_seq = True
                break
        if(has_good_seq):
            s1+=1
    print(s, s1)
