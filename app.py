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

class Gasto(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    categoria = db.Column(db.String(50), nullable=False) # Ex: Alimentação, Transporte, Lazer,....
    icone =  db.Column(db.String(10), nullable=False) # Ex: 🍔, 🍿, 🚗,.....
    valor = db.Column(db.String(20), nullable=False) # Ex: 1.200,00 ....
    cor_barra = db.Column(db.String(50), nullable=False) # Ex: bg-orange-500
    largura = db.Column(db.String(20), nullable=False) # Ex: w-3/5

# Esse comando cria o arquivo físico do banco de dados
with app.app_context():
    db.create_all()


@app.route('/')
def inicio():
    # 1. Busca todos os gastos guardados no banco de dados
    gastos_do_banco = Gasto.query.all()

    # 2. (próxima feature isso também sumirá e será totalmente dinanico e editavel pelo usuario)
    meu_saldo = "12.500,00"
    meus_gastos = "3.150,00"
    faturas_pendentes = 1

    # 3. Enviamos os gastos DO BANCO para o HTML
    return render_template('visao_geral.html', 
                           saldo_tela=meu_saldo, 
                           gasto_tela=meus_gastos,
                           faturas_tela=faturas_pendentes,
                           meus_gastos_categoria=gastos_do_banco) # Envia a lista para o HTML



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


@app.route('/adicionar_gasto', methods=['POST'])
def adicionar_gasto():
    # 1. Pega os dados do formulário
    categoria_digitada = request.form.get('categoria', '')
    valor_digitado = request.form.get('valor', '')

    categoria_formatada = categoria_digitada.lower()

    # 2. Valores Padrão (Caso seja um gasto diferente)
    icone_escolhido = "💸"
    cor_escolhida = "bg-green-500"
    largura_escolhida = "w-full" # Depois irei criar a matematica para a largura real

    # 3. O Cérebro de Categrias
    if "alimentação" in categoria_formatada or "ifood" in categoria_formatada or "mercado" in categoria_formatada:
        icone_escolhido = "🍔 🥗"
        cor_escolhida = "bg-orange-500"
    elif "transporte" in categoria_formatada or "uber" in categoria_formatada or "gasolina" in categoria_formatada:
        icone_escolhido = "🚗 ⛽"
        cor_escolhida = "bg-blue-500"
    elif "lazer" in categoria_formatada or "cinema" in categoria_formatada or "barzinho" in categoria_formatada:
        icone_escolhido = "🍻 🥂"
        cor_escolhida = "bg-purple-500"
    elif "saúde" in categoria_escolhida or "farmácia" in categoria_escolhida or "academia" in categoria_escolhida:
        icone_escolhido = "💊 🏋️‍♀️"    
    elif "casa" in categoria_formatada or "conta" in categoria_formatada or "energia" in categoria_formatada or "água" in categoria_formatada or "condomínio" in categoria_formatada or "internet" in categoria_formatada or "financiamento casa" in categoria_formatada:
        icone_escolhido = "🏠"
        cor_escolhida = "bg-yellow-500"

    # 4. Cria o objeto e salva no banco
    novo_gasto = Gasto(
        categoria=categoria_digitada,
        icone=icone_escolhido,
        valor=valor_digitado,
        cor_barra=cor_escolhida,
        largura=largura_escolhida
    )

    db.session.add(novo_gasto)
    db.session.commit()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)