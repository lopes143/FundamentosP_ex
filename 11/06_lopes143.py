def corta(input_file, output_file, count):
    i = open(input_file, 'r')
    o = open(output_file, 'w')
    counter = 0
    for char in i.read():
        if counter<count:
            o.write(char)
            counter+=1
    i.close()
    o.close()
    
corta('teste', 'saida', 20)