num=int(input('Digite seu ano:'))
bi=num % 4
if bi==0 :
    print('O ano de {} e bissexto'.format(num))
else:
    print('O ano de {} não e bissexto'.format(num))