def rect(width = 15,length = 10):
    perim = (width+length)*2
    area = width*length
    return perim,area
perim , area = rect()
print("defult: perim=",perim,"area =",area)
perim,area=rect(15)
print("length is defult: perim=",perim,"area=",area)
perim,area,rect(13,2)
print("no defult: perim=",perim,"area=",area)