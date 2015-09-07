
import pyperclip

x = ', '.join(['cats','bats','rats'])
print(x)
x = '|ABC|'.join(['cats','bats','rats'])
print(x)
x= 'Where do we you, my lovely?'
print(x.split())
print(x.split('e'))

spam = '''Dear Bolo

How are things in Boston? I hope you are
finding everything to your satisfaction

Love,

Jeet'''

y = spam.split('\n')
print(y)

print('Hello'.rjust(10, '*'))
print('Hello'.ljust(20, '-'))
print('Hello'.center(20))

spam = '    Hello World    '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())
spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam = spam.strip('ampS')
print(spam)

pyperclip.copy('Hello World from clipboardz!!!1 ')
x = pyperclip.paste()
print(x)