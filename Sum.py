total=0
s=int(input('enter a number or "done":'))
while s!='done':
    num=int(s)
    total = total+num
    s = input('enter a number or "done":')
    print('the sum of entered number is',total)
    