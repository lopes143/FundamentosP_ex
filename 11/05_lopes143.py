def procura(word, file):
    f = open(file, 'r')
    for i in f.readlines():
        if word in i:
            print(i)
procura('ficheiro', 'fich.txt')