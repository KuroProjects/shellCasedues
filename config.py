import os

w = open('config.json', 'w+')
w.write('{')
w.write('\n')
w.write('    "authToken": "'+os.getenv('5576900927:AAE9taMMfLIwvSq_-BxgWUjF7-7zyRO01Fg')+'",')
w.write('\n')
w.write('    "owner": '+os.getenv('2009241549'))
w.write('\n')
w.write('}')
