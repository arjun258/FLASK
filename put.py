
from flask import Flask, jsonify, request
app = Flask(__name__)

tasks = [{
    'id':1, "title":'buyGrocery'
}, {
    'id':2, "title":'learnCoding'
}]

@app.route('/addData', methods = ['POST'])
def addTask ():
    if(not request.json):
        return jsonify ({
            'status ' : 'error',
            'message ' : 'please provide the data '
        })

    task = {
        'id' : tasks [-1] ["id"] +1,
        'title': request.json['title']

    }
    tasks.append(task)
    return jsonify ({
            'status ' : 'success',
            'message ' : 'data added successfully '
        })
@app.route('/getData')
def getData ():
    return jsonify({
        'data ': tasks
    })

if (__name__=='__main__'):
    app.run()