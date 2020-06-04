
fh = open('Output.xml','r')
str = fh.read()
dict = eval(str)
print(dict)

outerlst = []
innerlst = []
fh = open('Decompresed Output.xml','w')
def recursive(dict):
    for key,val in dict.items():
        if(type(val) == type({})):
            fh.write('<'+key+'> ')
            dict = val
            outerlst.append(key)
            recursive(dict)
        elif(type(val) is type(str)):
            fh.write('<'+key+'>'+val+'</'+key+'> ')
        else:
            def rec(key,val):
                p=0
                klst=[]
                vlst=[]
                for d in val:
                    innerlst = []
                    for i,j in d.items():
                        if(type(j) == list):
                            if( type(j[0]) is type(str)):
                                for x in j:
                                    fh.write('<'+i+'>'+x+'</'+i+'> ')
                            else:
                                key = i
                                rec(key,j)
                        elif(type(j) is type(dict)):
                            fh.write('<'+i+' ')
                            for m,n in j.items():
                                if('@' in m):
                                    fh.write(m[1:]+'="'+n+'">')
                                if('#' in m):
                                    fh.write(n)
                            fh.write('</'+i+'> ')        
                        else:
                            if('@' in i):
                                fh.write('<'+key+' ')
                                klst.append(i)
                                vlst.append(j)
                                fh.write(i[1:]+'="'+j+'"> ')
                                p=p+1
                            else:
                                if(p == 0):
                                    fh.write('<'+key+'> ')
                                    fh.write('<'+i+'>'+j+'</'+i+'> ')
                                    p=p+1
                                else:
                                    fh.write('<'+i+'>'+j+'</'+i+'> ' )
                    innerlst.append(key)
                    p=0
                    for ele in innerlst:
                        fh.write('</'+ele+'> ')
            rec(key,val)
                
                
recursive(dict)
for i in range(len(outerlst)-1, -1, -1) :
    fh.write('</'+outerlst[i]+'> ')
fh.close()
