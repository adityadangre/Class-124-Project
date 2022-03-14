from flask import Flask, jsonify, request

app = Flask(__name__)
contacts = [
    {
        'id' : 1,
        'name' : 'Ojas Holey',
        'contact' : '8767588254',
        'done' : False
    },
    {
        'id' : 2,
        'name' : 'Arnav Pathak',
        'contact' : '9561674320',
        'done' : False
    },
]

@app.route('/')

def getData():
    return jsonify({
        'data' : contacts
    })

@app.route('/add-contact', methods=['POST'])

def addTask():
    if not request.json:
        return jsonify({
            'status' : 'Error',
            'message' : 'Contact not Provided.'
        })
    contact = {
        'id' : contacts[-1]['id'] + 1,
        'name' : request.json['name'],
        'contact' : request.json.get('contact'),
        'done' : False
    }

    contacts.append(contact)

    return jsonify({
            'status' : 'Successful',
            'message' : 'Contact added Successfully'
        })

if __name__ == '__main__':
    app.run(debug = True)