from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy # Tradutor de python para SLQ para nosso banco de dados

app = Flask(__name__)

# Avisamos ao flask onde o banco vai ficar
# 'sqlite://banco.db' significa: crie um arquivo chamado banco.db na mesma pasta do projeto
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Ligar o tradutor no nosso aplicativo
db = SQLAlchemy(app)

class Cartao(db.Model):
    # Definimos as colunas da nossa tabela de cartões
    id = db.Column(db.Integer, primary_key=True) # Cada cartão tera seu ID ÚNICO mesmo
    nome = db.Column(db.String(100), nullable=False) # Texto (até 100 letras), não pode ser vazio
    final = db.Column(db.String(4), nullable=False) # até 4.... quase que autoexplicativo.
    bandeira = db.Column(db.String(50), nullable=False)
    cor = db.Column(db.String(50), nullable=False)

# Esse comando cria o arquivo físico do banco de dados
with app.app_context():
    db.create_all()



@app.route('/')
def inicio():
    meu_saldo = "12.500,00"
    meus_gastos = "3.150,00"
    faturas_pendentes = 1

    lista_gastos = [
        {"categoria": "Alimentação", "icone": "🍔", "valor": "1.200,00", "cor_barra": "bg-orange-500", "largura": "w-3/5"},
        {"categoria": "Transporte", "icone": "🚗", "valor": "450,00", "cor_barra": "bg-blue-500", "largura": "w-1/4"},
        {"categoria": "Lazer", "icone": "🍿", "valor": "300,00", "cor_barra": "bg-purple-500", "largura": "w-1/6"}
    ]

    # Enviamos todas as variáveis antigas + a nova lista de gastos
    return render_template('visao_geral.html', 
                           saldo_tela=meu_saldo, 
                           gasto_tela=meus_gastos,
                           faturas_tela=faturas_pendentes,
                           meus_gastos_categoria=lista_gastos) # Envia a lista para o HTML
                            
@app.route('/cartoes')
def cartoes():
    # Busca no banco:pega todos os registros da tabela cartao
    cartoes_do_banco = Cartao.query.all()

    # Enviamos para o HTML a lista que veio do banco
    return render_template('cartoes.html', meus_cartoes=cartoes_do_banco)

@app.route('/perfil')
def perfil():

    nome_usuario = "César Capelli"
    cidade_usuario = "Mairinque, SP"
    status_conta = "Conta VIP"

    return render_template('perfil.html',
                           nome_tela=nome_usuario,
                           local_tela=cidade_usuario,
                           status_tela=status_conta)

@app.route('/adicionar_cartao', methods=['POST'])
def adicionar_cartao():
    # 1. Lemos os dados que o HTML enviou pelo atributo name dos inputs vindo do formulário de adicionar cartôes
    nome_digitado = request.form.get('nome_cartao')
    final_digitado= request.form.get('final_cartao')

    # 2. Mosntamos o "molde" do novo cartão usando o que o usuário digitou lá no formulário
    novo_cartao = Cartao(
        nome=nome_digitado,
        final=final_digitado,
        bandeira="Visa",
        cor="bg-teal-500"
    )

    # 3. Colocamos na fila: Avisamos o banco de dados que queremos adicionar isso
    db.session.add(novo_cartao)

    # 4. Salvamos de verdade: O botão de "Salvar" salva definitivo no servidor/disco rigido
    db.session.commit()

    return redirect('/cartoes')

if __name__ == '__main__':
    app.run(debug=True)
