poem = '''\
Программировать весело.
Если работа скучна,
Чтобы придать ей веселый тон - 
    используй Python!
    '''

f = open('poem.txt','w')#Открываем для записи 'writing'
f.write(poem)           #Записываем текст в файл
f.close()

f = open('poem.txt') #Открываем для чтения (по умолчанию режим чтения)
while True:
    line = f.readline()
    if len(line) == 0:   #Нулевая длина обозначает конец файла
        break
    print(line, end ='')
f.close()
