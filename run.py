from flask import Flask, jsonify, request
import json

app = Flask(__name__)

def new_id():
    new_id = 0
    for id_number in tarefas:
        if id_number['id'] >= new_id:
            id = id_number['id'] + 1
    return id

tarefas = [
    {
        "id": 0,
        'responsavel': 'João',
        'tarefa': 'Praticar Flask',
        'status': 'Concluido'
    }
]

@app.route('/tarefas', methods=['GET', 'POST'])
def tarefas_page():
    if request.method == 'GET':
        return jsonify(tarefas)
        
    if request.method == 'POST':
        data = json.loads(request.data)
        if 'responsavel' in data and 'tarefa' in data and 'status' in data:
            id = new_id()
            data['id'] = id
            tarefas.append(data)
            response = {'status': 'ok', 'message': f"tarefa incluida com o ID: {id}"}
            return response
        else:
            response = {'status': 'erro', 'message': 'Valores informados incorretamente'}
            return response

@app.route('/tarefas/<int:id_number>', methods=['GET', 'PUT', 'DELETE'])
def tarefas_id_page(id_number):
    if request.method == 'GET':
        opt = 0
        for tarefa in tarefas:
            if tarefa['id'] == id_number:
                opt = 1
                task_return = tarefa
        if opt == 1:
            return jsonify(task_return)
        else:
            return 'id não encontrado!'

    if request.method == 'DELETE':
        opt = 0
        for tarefa in tarefas:
            if tarefa['id'] == id_number:
                opt = 1
                tarefas.remove(tarefa)
        if opt == 1:
            return jsonify({'status': 'ok', 'message': f'ID {id_number} removido!'})
        else:
            return 'id não encontrado!'

    if request.method == 'PUT':
        example_dic = {'status': 'pendente'}
        data = json.loads(request.data)
        opt = 0
        for tarefa in tarefas:
            if tarefa['id'] == id_number:
                if data.keys() == example_dic.keys():
                    tarefa['status'] = data['status']
                    opt = 1
                else:
                    opt = 2
                
        if opt == 1:
            return jsonify({'status': 'ok', 'message': f'Status ID {id_number} atualizado!'})
        elif opt == 2:
            return jsonify({'status': 'erro', 'message': f'Valores inseridos incorretamente'})
        else:
            return jsonify({'status': 'erro', 'message': f'ID {id_number} não encontrado'})

            

if __name__ == "__main__":
    app.run(debug=True)