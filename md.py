print("text")
print("text" * 3)
xn = 7
print(xn)
t = True
f = False
print(t)
print(f)
te = "test"
print(te)
text_line = """hello
world"""
print(text_line)
fl = "Hello_world"
print(len(fl))
print(fl[3])
print(fl[-5])
print(fl[0:9])
# test
w = 'hello"world'
d = 'mahdi"hajizadh'
wr = "hi\\mehdi"
name = "Mahdi_Hajizadh"
Age = 19
uni = "Azad"
all = f"""{name}
{Age}
{uni}"""
print(all)
# upper
cap = "hello mahdi"
cap_test = cap.upper()
print(cap_test)
print(cap)
# lower
low = "HI MAHDI"
low_test = low.lower()
print(low_test)
# title
ti = "say bay"
titel = ti.title()
print(titel)
# strip
str = "  hello_world   "
str_test = str.strip()
print(str_test)
# r
str_rtest = str.rstrip()
print(str_rtest)
# l
str_ltest = str.lstrip()
print(str_ltest)
# find
f = "python programming"
f_test = f.find("p")
print(f_test)
# replace
rep = "python programming"
rep_test = rep.replace("p", "z")
print(rep_test)
# upreitor
up = "python programming"
print("m" in up)
print("z" in up)
print("z" not in up)
# integer
num = 10
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
# round
ru = round(10.2)
print(ru)
print(round(3.5))
# abs
ab = abs(-10)
print(ab)
# math module
import math

print(math.ceil(10.2))
print(3 != 3)
print(3 == 3)
#app
x = input("write x : ")
x = int(x)
y = x * 4
print(f"x={x} y={y}")
