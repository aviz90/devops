strlen = 7
indFirst = 0
indlast = strlen - 1
for j in range(strlen):
    mystring = ''
    for i in range(strlen):
        if i == indFirst or i == indlast:
            mystring = mystring + '*'
        else:
            mystring = mystring + ' '

    print(mystring)
    indFirst = indFirst + 1
    indlast = indlast - 1
