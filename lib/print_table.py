a=""
width=[6,6,6,6,6,6,6,6]

table_head=["id","1","2","3","4","5","7","8"]
titile="one"
d=12
table_list=[('pass',2,3,4,5,6,7,8,9),('fail',2,3,4,5,6,7,8,9),('result','ok','fail','ok','fail','fail','ok','ok','ok')]


#table_list=[[0 for i in range(4)] for i in range(9)]
print(table_list)

def gen_report_append_table(c,title,table_head,table_list,width):
    c=c+("# " + titile+'\r\n')


    fmt = '|' +  '|'.join(['{:<%d}'%w for w in width]) + '|\n'
    print((*table_head))
    c=c+(fmt.format(*table_head))
    c=c+(fmt.format(*[ '-'*w for w in width]))
    item_count = 0
    i=0
    for a in table_list:

       #print(a)
        item_count += 1
        #c=c+(fmt.format(*map(str, a)))
        print((*map(str, a)))
        c=c+(fmt.format(*map(str, a)))
      #  print((fmt.format(*map(str, a))))
        
    #if(table_list == None or item_count == 0):   
    #     c=c+(fmt.format(*[ ' '*w for w in width]))
         
    print(c)

gen_report_append_table(a,titile,table_head,table_list,width)
