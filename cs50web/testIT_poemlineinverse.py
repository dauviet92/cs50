poem="""buoc toi deo ngang bong xe ta
co cay chen la da chen hoa
thang thang duoi nui tieu vai chu
lac dac ben song cho may nha
nho nuoc dau long con quoc quoc"""

def invesre_line(poem,line):
    ls = poem.splitlines()
    line_inv = ls[line-1][::-1]
    return line_inv

print(invesre_line(poem,4))
