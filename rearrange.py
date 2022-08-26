first_num=int(input("enter first number to be swapped: "))
sec_num=int(input("enter second number to be swapped: "))

with open("/home/vishnu/Desktop/python/10_3a_random_reverse.gjf","r")as file:
########## to define the order and list of coordinates
    data=file.readlines()
    lines=(len(data))   #### to identify total number of lines in the file
    start=0             #### start
    end=lines-3         ##### to find end of coordinates may vary depending on the input file. may chamge the integer to adjust
    list=[]     #empty list of coordinates
    order=[]    #empty list of order
    for y in range(end):
        order.append(y)
    for line in range(start+9,end):
        list.append(data[line])
####### Actual Code for swapping the atoms
    with open("out.txt","w") as outf:
        first = first_num-1
        second=sec_num-1
        myorder=order
        temp=myorder[first]
        myorder[first]=myorder[second]
        myorder[second]=temp
        print(list)
        list=[ list [i in order] for i in myorder]
        for cord in (myorder):
            outf.write(myorder)
        print(list)