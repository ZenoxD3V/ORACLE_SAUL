from flask import Blueprint, render_template

rituales_bp = Blueprint('rituales', __name__)

@rituales_bp.route('/')
def index():
    return render_template('rituales/index.html')

@rituales_bp.route('/abundancia')
def abundancia():
    return render_template('rituales/abundancia.html')

@rituales_bp.route('/proteccion')
def proteccion():
    return render_template('rituales/proteccion.html')
