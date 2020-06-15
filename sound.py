import string


a ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
b =' 5!@7#$6%^3&*8-=1~.,0=9|2/45!@7#$6%^3&*8-=1~.,0=9|2/4'
Q = string.maketrans(a,b)
W = string.maketrans(b,a)
order=raw_input ('enter a phrase:')
for letter in order:
    if letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(a,b)
        print('our transalator works in the above way')
        print(order)
        print order.translate(Q)
        break
for number in order:
    if number in "0123456789!@#$%^&*-=.,+|/~":
        print(b,a)
        print('our transalator works in the above way')
        print(order)
        print order.translate(W)
        break     
