
def wc(s):
    d = {}
    words = s.split()
    for w in words:
        if w in d:
            d[w] = d[w] + 1
    
            d[w] = 1
        return d

print(wc('a man a plan a canal, Panama'))
    

sen = 'a boy is going to the park'

word = sen.split()

print(word)

def f(x, y = 2, z = 4):
    return (x + z)

print(f(1))
print(f(1, z = 10))
print(f(x = 5))

b = 12
while True:
    print('B')
    b += 2
    if b > 15:
        break

cars = [{'name': 'exp', 'maker' : 'ford', 'pr': 2},
        {'name': 'suzuki', 'maker' : 'honda', 'pr': 7}]

cp = {}

for c in cars:
    n = c['name']
    p = c['pr']
    cp[n] = p
print(cp)

a_l = [1, 2, 3, 4]
b_l = [5, 6, 7, 8]

f_l = a_l[2:] + b_l[:2]
print(f_l)

n = 'myfile.txt'
f = open(n, 'r')

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
l1 = [5,6]
print(l2)

for i in range(3):
    for j in range(2):
        print(i, j)

r = 0
d = 0
p = 0


def interp(i,x,y):
    templ = f'Great wrok %s You scored %d out of %d.' %(i,x,y)
    print(templ)


print(interp('genius', 3, 5))


