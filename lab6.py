from flask import Blueprint, render_template, request, session, jsonify

lab6 = Blueprint('lab6', __name__)

offices = []
for i in range(1, 11):
    offices.append({
        "number": i, 
        "tenant": "", 
        "price": 900 + i * 100,  
        "is_public": True,  
        "is_favorite": False  
    })

@lab6.route('/lab6/')
def lab():
    return render_template('lab6/lab6.html')

@lab6.route('/lab6/api', methods=['POST'])
def api():
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                'jsonrpc': '2.0',
                'error': {'code': -32700, 'message': 'No JSON data'},
                'id': None
            })
        
        method = data.get('method')
        id = data.get('id')
        
        print(f"API called: method={method}, id={id}")
        
        if method == 'info':
            sorted_offices = sorted(offices, key=lambda x: (-x['is_favorite'], x['number']))
            return jsonify({
                'jsonrpc': '2.0',
                'result': sorted_offices,
                'id': id
            })
        
        elif method == 'booking':
            login = session.get('login')
            if not login:
                return jsonify({
                    'jsonrpc': '2.0',
                    'error': {'code': 1, 'message': 'Unauthorized'},
                    'id': id
                })
            
            office_number = data.get('params')
            for office in offices:
                if office['number'] == office_number:
                    if office['tenant']:
                        return jsonify({
                            'jsonrpc': '2.0',
                            'error': {'code': 2, 'message': 'Office already booked'},
                            'id': id
                        })
                    office['tenant'] = login
                    return jsonify({
                        'jsonrpc': '2.0',
                        'result': 'success',
                        'id': id
                    })
            
            return jsonify({
                'jsonrpc': '2.0',
                'error': {'code': 5, 'message': 'Office not found'},
                'id': id
            })
        
        elif method == 'cancellation':
            login = session.get('login')
            if not login:
                return jsonify({
                    'jsonrpc': '2.0',
                    'error': {'code': 1, 'message': 'Unauthorized'},
                    'id': id
                })
            
            office_number = data.get('params')
            for office in offices:
                if office['number'] == office_number:
                    if not office['tenant']:
                        return jsonify({
                            'jsonrpc': '2.0',
                            'error': {'code': 3, 'message': 'Office not booked'},
                            'id': id
                        })
                    if office['tenant'] != login:
                        return jsonify({
                            'jsonrpc': '2.0',
                            'error': {'code': 4, 'message': 'Not your office'},
                            'id': id
                        })
                    office['tenant'] = ""
                    return jsonify({
                        'jsonrpc': '2.0',
                        'result': 'success',
                        'id': id
                    })
            
            return jsonify({
                'jsonrpc': '2.0',
                'error': {'code': 5, 'message': 'Office not found'},
                'id': id
            })
        
        elif method == 'toggle_favorite':
            office_number = data.get('params')
            for office in offices:
                if office['number'] == office_number:
                    office['is_favorite'] = not office['is_favorite']
                    return jsonify({
                        'jsonrpc': '2.0',
                        'result': 'success',
                        'id': id
                    })
        
        return jsonify({
            'jsonrpc': '2.0',
            'error': {'code': -32601, 'message': 'Method not found'},
            'id': id
        })
    
    except Exception as e:
        return jsonify({
            'jsonrpc': '2.0',
            'error': {'code': -32603, 'message': f'Internal error: {str(e)}'},
            'id': data.get('id') if data else None
        })