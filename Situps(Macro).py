import keyboard

keyboard.add_hotkey('ctrl+8', lambda: sleeper())
keyboard.add_hotkey('ctrl+9', lambda: sat())

def sleeper():
    keyboard.write('mizkifSleeper')
    keyboard.press_and_release('enter')

count = 0
def sat():
    global count
    count += 1
    keyboard.write('mizkifSat ' + str(count))
    keyboard.press_and_release('enter')
