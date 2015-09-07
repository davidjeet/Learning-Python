#! python3
# pw.py - An inscure password locker program.

PASSWORDS = { 'email': 'F873fh7*&5sfihgyey',
              'blog': 'JksldkHIYUY637fj99',
              'netflix': '12345'
             }
import sys
import pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to the clipboard')
else:
    print('There is no account named ' + account)
