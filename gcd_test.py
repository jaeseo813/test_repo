## 박규탁, 202300328, 컴퓨터공학부
## pull requests, by gyutak Park
def gcd_sub(a, b):
    while(a != 0 and b != 0):
        if a>b:
            a = a-b
        elif b>a:
            b = b-a
        elif a == b:
            a = a-b
    return a+b
def gcd_mod(a, b):
    while(a != 0 and b != 0):
        if a>b:
            a = a%b
        elif b>a:
            b = b%a
		elif a == b:
            a = a-b
    return a+b

def gcd_rec(a, b):
    return gcd_sub(a,b)
	
# a, b를 입력받는다
a, b =map(int, input(). split(" "))

x = gcd_sub(a,b)
y = gcd_mod(a,b)
z = gcd_rec(a,b)
# gcd_sub, gcd_mod, gcd_rec을 각각 호출하여, x, y, z에 리턴값을 저장한다

print(x, y, z)
