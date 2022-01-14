from flask import Flask, jsonify, request

app=Flask(__name__)

contacts=[
    {
        'id':1,
        'name': 'abc',
        'contact':'3475928475',
        'status':False
    },
    {
        
        'id':2,
        'name': 'xyz',
        'contact':'9812456431',
        'status':False
    }
]


@app.route("/getCont")
def getCont():
    return jsonify(
        {
            "data":contacts,
            "message":"success"
        }
    )

@app.route("/addCont",methods=["POST"])
def addCont():
    contact={
        'id':contacts[-1]['id']+1,
        'name': request.json['name'],
        'contact': request.json['cont'],
        'status':False
    }
    contacts.append(contact)
    return jsonify(
        {
            "data":contact,
            "message":"task added success"
        }
    )





if __name__ == '__main__':
    app.run()