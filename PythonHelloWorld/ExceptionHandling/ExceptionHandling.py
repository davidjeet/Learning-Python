def DoWork(denominator):
    try:
        return 42 / denominator
    except:
        print('Errorjeet!!!!!1')
        return 'I cannot do that, Dave'
print(DoWork(9))
print(DoWork(0))

def DoWork2(denominator):
       return 42 / denominator
try:
    print(DoWork2(3))
    print(DoWork2(2))
    print(DoWork2(1))
    print(DoWork2(0))
    print(DoWork2(10))
except:
    print('You had an exception so this goes no further!!!')
# Things to learn
# Errors are handled by try and except statements