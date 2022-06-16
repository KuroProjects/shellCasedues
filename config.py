import os

w = open('config.json', 'w+')
w.write('{')
w.write('\n')
w.write('    "5132355893:AAEVLCm-feroZN1Q5PzpQJ42bWkf2nmDTCc": "'+os.getenv('BOT_TOKEN')+'",')
w.write('\n')
w.write('    "2104912596": '+os.getenv('OWNER_ID'))
w.write('\n')
w.write('}')
