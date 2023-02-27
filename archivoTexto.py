#f=open('alumnos.txt','w')
#nombres=f.read()
#print(nombres)
# con seek se controla la posición del cursor
#f.seek(9)
#nombres2=f.read()
#print(nombres2)


#Con esta función se lee linea por linea
#nombres=f.readline()

#nombres= f.readlines()

#for item in nombres:
#    print(item,end='')

#f.write('\n','Hola mundo')
#f.close
f = open('alumnos.txt', 'a')
f.write('\nHola mundo')
f.close()