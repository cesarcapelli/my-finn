from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('visao_geral.html')

@app.route('/cartoes')
def cartoes():
    return render_template('cartoes.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

if __name__ == '__main__':
    app.run(debug=True)
    