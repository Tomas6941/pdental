from flask import Flask, render_template, request, redirect, url_for, flash, session
from functools import wraps
import json, os

app = Flask(__name__)
app.secret_key = 'dental_pro_2024'

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')

def load_data():
    default = {'turnos': [], 'contactos': [], 'config': {'titulo': 'DentalPro', 'subtitulo': 'Tu sonrisa, nuestra pasión'}}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for k, v in default.items():
                if k not in data:
                    data[k] = v
            return data
    return default

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('admin'):
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated

@app.route('/')
def index():
    data = load_data()
    return render_template('index.html', config=data['config'])

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/equipo')
def equipo():
    return render_template('equipo.html')

@app.route('/turnos', methods=['GET', 'POST'])
def turnos():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        email = request.form.get('email', '').strip()
        telefono = request.form.get('telefono', '').strip()
        servicio = request.form.get('servicio', '')
        fecha = request.form.get('fecha', '')
        hora = request.form.get('hora', '')
        mensaje = request.form.get('mensaje', '')
        if nombre and email and servicio and fecha and hora:
            data = load_data()
            data['turnos'].append({
                'id': len(data['turnos']) + 1,
                'nombre': nombre, 'email': email, 'telefono': telefono,
                'servicio': servicio, 'fecha': fecha, 'hora': hora,
                'mensaje': mensaje, 'estado': 'pendiente'
            })
            save_data(data)
            flash('¡Turno solicitado! Te confirmaremos por email o teléfono.', 'success')
            return redirect(url_for('turnos'))
        flash('Completá todos los campos requeridos.', 'error')
    return render_template('turnos.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        email = request.form.get('email', '').strip()
        mensaje = request.form.get('mensaje', '').strip()
        if nombre and email and mensaje:
            data = load_data()
            data['contactos'].append({'nombre': nombre, 'email': email, 'mensaje': mensaje})
            save_data(data)
            flash('¡Mensaje recibido! Te contactamos en menos de 24 hs.', 'success')
            return redirect(url_for('contacto'))
        flash('Completá todos los campos.', 'error')
    return render_template('contacto.html')

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        if request.form.get('usuario') == 'admin' and request.form.get('password') == 'dental2024':
            session['admin'] = True
            return redirect(url_for('admin_panel'))
        flash('Credenciales incorrectas.', 'error')
    return render_template('admin_login.html')

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin', None)
    return redirect(url_for('index'))

@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin_panel():
    data = load_data()
    if request.method == 'POST':
        data['config']['titulo'] = request.form.get('titulo', data['config']['titulo'])
        data['config']['subtitulo'] = request.form.get('subtitulo', data['config']['subtitulo'])
        save_data(data)
        flash('Configuración actualizada.', 'success')
        return redirect(url_for('admin_panel'))
    return render_template('admin.html', turnos=data['turnos'], contactos=data['contactos'], config=data['config'])

if __name__ == '__main__':
    app.run(debug=True)
