from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():

    meu_saldo = "12.500,00"
    meus_gastos = "3.150,00"
    faturas_pendentes = 1

    return render_template('visao_geral.html',
                           saldo_tela=meu_saldo,
                           gasto_tela=meus_gastos,
                           faturas_tela=faturas_pendentes)

@app.route('/cartoes')
def cartoes():
    return render_template('cartoes.html')

@app.route('/perfil')
def perfil():

    nome_usuario = "César Capelli"
    cidade_usuario = "Mairinque, SP"
    status_conta = "Conta VIP"

    return render_template('perfil.html',
                           nome_tela=nome_usuario,
                           local_tela=cidade_usuario,
                           status_tela=status_conta)

if __name__ == '__main__':
    app.run(debug=True)
