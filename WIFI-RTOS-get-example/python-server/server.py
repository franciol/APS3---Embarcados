from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}



#class TodoSimple(Resource):
#    def get(self, todo_id):
#        return {todo_id: todos[todo_id]}
#
#    def put(self, todo_id):
#        todos[todo_id] = request.form['data']
#        return {todo_id: todos[todo_id]}


@app.route('/hi',methods=['GET'])
def hello():
    return 'Opa!!!!!'

@app.route('/connect',methods = ['POST'])
def connect():
    timestamp = request.form['timestamp']
    machine = request.form['machine']
    digitalVal = request.form['digital']
    analogVal = request.form['analog']
    print('POST: Time: ',timestamp,' \nmachine: ',machine,'\ndigtal: ',digitalVal,'\nanalog: ',analogVal)
    return 'Connected'

@app.route('/connect',methods = ['GET'])
def connect_get():
    timestamp = request.args.get('timestamp')
    machine = request.args.get('machine')
    digitalVal = request.args.get('digital')
    analogVal = request.args.get('analog')
    print('GET:\nTime: ',timestamp,'\nmachine: ',machine,'\ndigtal: ',digitalVal,'\nanalog: ',analogVal)
    return 'Connected'





if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
    #app.run(debug=True)

