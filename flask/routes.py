from init import *

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
    
@app.route('/personas/<personas_id>', methods=['GET', 'PUT', 'DELETE'])
def route_personas_id(personas_id):
    if request.method == 'GET':
        personas = PERSONA.query.filter_by(id=personas_id).first()
        return jsonify(personas)
    
    elif request.method == 'PUT':
        persona=request.get_json()
        new_id=persona.get('id')
        new_correo=persona.get('correo')
        new_username=persona.get('username')
        new_password=persona.get('password')
        
        persona_pre=PERSONA.query.get(personas_id)
        if not persona_pre:
            return f'La persona con el ID {personas_id} no existe'
        
        persona_pre.id=new_id
        persona_pre.correo=new_correo
        persona_pre.username=new_username
        persona_pre.password=new_password
        db.session.commit()
        return 'SUCCESS'
    
    elif request.method == 'DELETE':
        persona=PERSONA.query.get_or_404(personas_id)
        db.session.delete(persona)
        db.session.commit()
        return 'SUCCESS'

#STICKER
@app.route('/stickers', methods = ['GET', 'POST', 'DELETE'])
def route_stickers():
    if request.method=='GET':
        stickers = STICKER.query.all()
        return jsonify(stickers)
    
    elif request.method == 'POST':
        data = request.get_json()
        sticker = STICKER(idsticker=data["idsticker"], nombre=data["nombre"],descripcion=data["descripcion"], categoria=data["categoria"], likes = 0, Foto=data["Foto"], FechaSubida=func.now())
        db.session.add(sticker)
        db.session.commit()
        return 'SUCCESS'
    
    elif request.method == 'DELETE':
        stickers = STICKER.query.all()
        for sticker in stickers:
            db.session.delete(sticker)
        db.session.commit()
        return 'SUCCESS'

@app.route('/stickers/creador/<creador_id>', methods = ['GET', 'DELETE'])
def route_stickers_creador_id(creador_id):
    session = Session()
    filas = STICKER.query.get_or_404(creador_id)
    if method=='GET':
        return jsonify(filas)
    elif method == 'DELETE':
        for fila in filas:
            db.session.delete(fila)
        db.commit()
        return 'SUCCESS'

#@app.route('/stickers/<sticker_id>', methods = ['GET', 'PUT', 'DELETE'])

#@app.route('/stickers/comentario/<sticker_id>', methods = ['GET', 'DElETE', 'POST'])

#@app.route('/comentario/<sticker_id>', methods = ['PUT', 'DELETE'])

if __name__ == '__main__':
    #app.run(debug=True, port=5000, host='192.168.18.14')
    app.run()