import random
import sys
import keyboard
import time
import os

i = 0
count = 1
while i == 0:
    slp = random.uniform(3.0000, 5.0000)
    time.sleep(slp)
    keyboard.write('mizkifSleeper')
    keyboard.press_and_release('enter')

    slp = random.uniform(3.0000, 5.0000)
    time.sleep(slp)
    count = str(count)
    keyboard.write('mizkifSat ' + count)
    keyboard.press_and_release('enter')
    
    count = int(count)
    count += 1

    if count == 1001:
        #slp = random.uniform(20.0000, 30.0000)
        #time.sleep(slp)
        #keyboard.write('WRAP IT UP DOMEY 4Weird')
        #keyboard.press_and_release('enter')
        break
    
#os.system('shutdown -s')
