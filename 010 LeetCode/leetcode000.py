for i in range(1,51):
    if i%(3*5)==0:
        print('FizzBuzz')
        continue
    elif i%3==0:
        print('Fizz')
        continue
    elif i%5==0:
        print('Buzz')
        continue
    else:
        print(i)