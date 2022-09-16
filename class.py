from flask import Flask

app = Flask(__name__)
@app.route('/')
def me ():
    return 'my name is arjun '

@app.route('/maybe')
def be ():
    return 'i am 14 '

if (__name__=='__main__'):
    app.run()


