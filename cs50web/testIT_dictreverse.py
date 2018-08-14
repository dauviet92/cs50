dic = {"viet":1,"khanh":2, "bao":3}
inv_dic = {v:k for k,v in dic.items()}
for k,v in inv_dic.items():
    print( str(k) + ' : '+ str(v)  +'\n')
