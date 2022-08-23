# удаление порта после : в файле Proxy1.txt в новый файл ProxyX.txt
with open('Proxy1.txt', 'r') as f1, open('ProxyX.txt', 'w') as f2:
    lines = f1.readlines()

    for line in lines:
        line = line.strip()
        sep = ':'
        f2.write(line.split(sep, 1)[0] + '\n')
