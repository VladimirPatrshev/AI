# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент a1 , разность d и количество элементов n будет задано автоматически. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

a1 = 2 
n = 3
d = 4
mass =[]
def progressive(a1,n,d):
    an = a1+(n-1)*d
    return an

for i in range (1,n+1) :
    
    mass.append (progressive(a1,i,d))
    
    
print (*mass, sep='\n')
    