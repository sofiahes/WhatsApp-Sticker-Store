from index import *


@app.route('/personas',methods=['GET', 'POST'])
def route_personas():
    if request.method=='GET':
        personas = PERSONA.query.all()
        return jsonify(personas)
    
    elif request.method == 'POST':
        data = request.get_json()
        persona = PERSONA(id=data["id"], correo=data["correo"],username=data["username"], password=data["password"])
        db.session.add(persona)
        db.session.commit()
        return 'SUCCESS'