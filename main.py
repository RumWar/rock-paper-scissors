a = input('введите одно из трех > камень, ножнеци, бумага > ')
b = input('введите одно из трех > камень, ножнеци, бумага > ')
c = {'бумага':1, 'ножнеци':2, 'камень':3}
for i in c:
    if i == a:
        m1 = c[i]
    if i == b:
        m2 = c[i]
if m1 == m2:
    print('ничья')
elif (m1 == 1 and m2 == 2) or (m1 == 2 and m2 == 3) or (m1 == 3 and m2 == 1):
    print(f"Тимур победил!")
else:
    print(f"Петя победил!")





# cd /d C:\Program Files\fastapi