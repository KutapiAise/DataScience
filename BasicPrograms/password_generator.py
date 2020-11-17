
import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="[]{}()*;/,._-"
_all= lower+upper+numbers+symbols
length=16
password="".join(random.sample(all,length))

password="".join(random.sample(_all,length))
print(password)
