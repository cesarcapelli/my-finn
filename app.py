from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy  # Tradutor de Python para SQL para o nosso banco de dados

app = Flask(__name__)

# Avisamos ao Flask onde o banco vai ficar
# 'sqlite:///banco.db' significa: crie um arquivo chamado banco.db na mesma pasta do projeto
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Ligar o tradutor no nosso aplicativo
db = SQLAlchemy(app)

class Cartao(db.Model):
    # Definimos as colunas da nossa tabela de cartões
    id = db.Column(db.Integer, primary_key=True)  # Cada cartão terá seu ID ÚNICO
    nome = db.Column(db.String(100), nullable=False)  # Texto (até 100 letras), não pode ser vazio
    final = db.Column(db.String(4), nullable=False)  # Até 4 dígitos
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
    # Busca no banco: pega todos os registros da tabela cartao
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
    # 1. Lemos os dados que o HTML enviou pelo formulário
    nome_digitado = request.form.get('nome_cartao')
    final_digitado = request.form.get('final_cartao')

    nome_formatado = nome_digitado.lower()

    # COR/BANDEIRA PADRÃO PARA CARTÕES DESCONHECIDOS
    cor_escolhida = "bg-gray-800"
    bandeira_escolhida = "Visa"

    # --- CÉREBRO DE CORES (ADICIONAR) ---
    if "nubank" in nome_formatado:
        cor_escolhida = "bg-purple-600"
        bandeira_escolhida = "Mastercard"
    elif "inter" in nome_formatado:
        cor_escolhida = "bg-orange-500"
        bandeira_escolhida = "Mastercard"
    elif "itaú" in nome_formatado or "itau" in nome_formatado:
        cor_escolhida = "bg-orange-500" 
        bandeira_escolhida = "Visa"
    elif "bradesco" in nome_formatado:
        cor_escolhida = "bg-red-600"
        bandeira_escolhida = "Elo"
    elif "c6" in nome_formatado:
        cor_escolhida = "bg-gray-900"
        bandeira_escolhida = "Mastercard"
    elif "brasil" in nome_formatado or "bb" in nome_formatado:
        cor_escolhida = "bg-yellow-500"
        bandeira_escolhida = "Elo"
    elif "porto seguro" in nome_formatado or "porto" in nome_formatado:
        cor_escolhida = "bg-blue-700"
        bandeira_escolhida = "Visa"
    elif "santander" in nome_formatado:
        cor_escolhida = "bg-red-500"
        bandeira_escolhida = "Mastercard"
    elif "caixa" in nome_formatado:
        cor_escolhida = "bg-blue-500"
        bandeira_escolhida = "Elo"
    elif "xp" in nome_formatado:
        cor_escolhida = "bg-slate-800"
        bandeira_escolhida = "Visa"
    elif "btg" in nome_formatado:
        cor_escolhida = "bg-blue-900"
        bandeira_escolhida = "Mastercard"
    elif "neon" in nome_formatado:
        cor_escolhida = "bg-cyan-500"
        bandeira_escolhida = "Visa"
    elif "next" in nome_formatado:
        cor_escolhida = "bg-emerald-500"
        bandeira_escolhida = "Visa"
    elif "pan" in nome_formatado:
        cor_escolhida = "bg-sky-500"
        bandeira_escolhida = "Mastercard"
    elif "mercado pago" in nome_formatado or "mercado" in nome_formatado:
        cor_escolhida = "bg-blue-400"
        bandeira_escolhida = "Visa"
    elif "picpay" in nome_formatado or "pic" in nome_formatado:
        cor_escolhida = "bg-green-500"
        bandeira_escolhida = "Mastercard"
    elif "sicoob" in nome_formatado:
        cor_escolhida = "bg-teal-700"
        bandeira_escolhida = "Mastercard"
    elif "sicredi" in nome_formatado:
        cor_escolhida = "bg-green-600"
        bandeira_escolhida = "Visa"
    elif "will" in nome_formatado:
        cor_escolhida = "bg-yellow-400"
        bandeira_escolhida = "Mastercard"
    elif "iti" in nome_formatado:
        cor_escolhida = "bg-pink-500"
        bandeira_escolhida = "Visa"

    # 2. Montamos o objeto usando o que o Cérebro definiu
    novo_cartao = Cartao(
        nome=nome_digitado,
        final=final_digitado,
        bandeira=bandeira_escolhida,
        cor=cor_escolhida
    )

    # 3. Salvamos no banco
    db.session.add(novo_cartao)
    db.session.commit()

    return redirect('/cartoes')


@app.route('/deletar_cartao/<int:id>')
def deletar_cartao(id):
    cartao_para_deletar = Cartao.query.get_or_404(id)
    db.session.delete(cartao_para_deletar)
    db.session.commit()
    return redirect('/cartoes')


@app.route('/editar_cartao/<int:id>', methods=['GET', 'POST'])
def editar_cartao(id):
    cartao = Cartao.query.get_or_404(id)

    if request.method == 'POST':
        cartao.nome = request.form.get('nome_cartao')
        cartao.final = request.form.get('final_cartao')

        nome_formatado = cartao.nome.lower()

        # VALORES PADRÃO CASO NÃO RECONHEÇA NA EDIÇÃO
        cor_escolhida = "bg-gray-800"
        bandeira_escolhida = "Visa"

        # --- CÉREBRO DE CORES (EDIÇÃO) ---
        if "nubank" in nome_formatado:
            cor_escolhida = "bg-purple-600"
            bandeira_escolhida = "Mastercard"
        elif "inter" in nome_formatado:
            cor_escolhida = "bg-orange-500"
            bandeira_escolhida = "Mastercard"
        elif "itaú" in nome_formatado or "itau" in nome_formatado:
            cor_escolhida = "bg-orange-500" 
            bandeira_escolhida = "Visa"
        elif "bradesco" in nome_formatado:
            cor_escolhida = "bg-red-600"
            bandeira_escolhida = "Elo"
        elif "c6" in nome_formatado:
            cor_escolhida = "bg-gray-900"
            bandeira_escolhida = "Mastercard"
        elif "brasil" in nome_formatado or "bb" in nome_formatado:
            cor_escolhida = "bg-yellow-500"
            bandeira_escolhida = "Elo"
        elif "porto seguro" in nome_formatado or "porto" in nome_formatado:
            cor_escolhida = "bg-blue-700"
            bandeira_escolhida = "Visa"
        elif "santander" in nome_formatado:
            cor_escolhida = "bg-red-500"
            bandeira_escolhida = "Mastercard"
        elif "caixa" in nome_formatado:
            cor_escolhida = "bg-blue-500"
            bandeira_escolhida = "Elo"
        elif "xp" in nome_formatado:
            cor_escolhida = "bg-slate-800"
            bandeira_escolhida = "Visa"
        elif "btg" in nome_formatado:
            cor_escolhida = "bg-blue-900"
            bandeira_escolhida = "Mastercard"
        elif "neon" in nome_formatado:
            cor_escolhida = "bg-cyan-500"
            bandeira_escolhida = "Visa"
        elif "next" in nome_formatado:
            cor_escolhida = "bg-emerald-500"
            bandeira_escolhida = "Visa"
        elif "pan" in nome_formatado:
            cor_escolhida = "bg-sky-500"
            bandeira_escolhida = "Mastercard"
        elif "mercado pago" in nome_formatado or "mercado" in nome_formatado:
            cor_escolhida = "bg-blue-400"
            bandeira_escolhida = "Visa"
        elif "picpay" in nome_formatado or "pic" in nome_formatado:
            cor_escolhida = "bg-green-500"
            bandeira_escolhida = "Mastercard"
        elif "sicoob" in nome_formatado:
            cor_escolhida = "bg-teal-700"
            bandeira_escolhida = "Mastercard"
        elif "sicredi" in nome_formatado:
            cor_escolhida = "bg-green-600"
            bandeira_escolhida = "Visa"
        elif "will" in nome_formatado:
            cor_escolhida = "bg-yellow-400"
            bandeira_escolhida = "Mastercard"
        elif "iti" in nome_formatado:
            cor_escolhida = "bg-pink-500"
            bandeira_escolhida = "Visa"

        # Aplicamos o resultado do cérebro diretamente no cartão existente
        cartao.cor = cor_escolhida
        cartao.bandeira = bandeira_escolhida

        # Salva as alterações de verdade no banco
        db.session.commit()
        return redirect('/cartoes')
    
    # Se for requisição GET, renderiza a página levando os dados atuais do cartão
    return render_template('editar_cartao.html', cartao_tela=cartao)


if __name__ == '__main__':
    app.run(debug=True)