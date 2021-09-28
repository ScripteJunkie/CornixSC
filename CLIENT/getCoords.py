import time
#import pyperclip
from flask import Flask, render_template
app = Flask(__name__)

while(True):
    #data = pyperclip.waitForNewPaste()
    data = "Coordinates: x:-18930450466.131271 y:-2610440131.656021 z:-0.087822 Time:20210120014707"
    data = data.split(' ')
    data.pop(0)
    data = float(data[0][2:]), float(data[1][2:]), float(data[2][2:])
    data = time.time(), data[0], data[1], data[2]
    print(data)

@app.route('/')
def main():
    if request.method == 'POST':
            if request.form.get('action1') == 'VALUE1':
                pass # do something
            elif  request.form.get('action2') == 'VALUE2':
                pass # do something else
            else:
                pass # unknown
        elif request.method == 'GET':
            return render_template('index.html', form=form)
    return render_template('index.html', time = time.time(), x = data[0], y = data[1], z = data[2])

if __name__ == '__main__':
   app.run()