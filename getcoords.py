import time
import pyperclip
from flask import Flask, render_template
app = Flask(__name__)

while(True):
    data = pyperclip.waitForNewPaste()
    data = data.split(' ')
    data.pop(0)
    data = float(data[0][2:]), float(data[1][2:]), float(data[2][2:])
    data = time.time(), data[0], data[1], data[2]
    print(data)


@app.route('/')
def main():
    return render_template('index.html', data = data)

if __name__ == '__main__':
   app.run()