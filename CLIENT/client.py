import time
#import pyperclip
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
            if request.form.get('action1') == 'VALUE1':
                print('1')
                pass # do something
            elif  request.form.get('action2') == 'VALUE2':
                print('2')
                pass # do something else
            else:
                pass # unknown
    elif request.method == 'GET':
            return render_template('index.html', form=request.form)
    return render_template('index.html', time = time.time())

if __name__ == '__main__':
   app.run()