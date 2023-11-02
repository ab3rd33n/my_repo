#!/usr/bin/ipython3

ip = input('''Введите ип-адресс в формате X.X.X.X 
''')
oct1, oct2, oct3, oct4 = ip.split('.')

#Вывод инфы
result = '''
IP-address в десятичном виде:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
Ip-address в двоичном виде:
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''

#END result
print(result.format(int(oct1), int(oct2), int(oct3), int(oct4)))


