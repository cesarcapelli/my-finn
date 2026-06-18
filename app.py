from flask import Flask, render_template, request, redirect

app = Flask(__name__)

lista_de_cartoes = [
    {"nome": "Nubank", "final": "4567", "bandeira": "Mastercard", "cor": "bg-purple-600"},
    {"nome": "Banco Inter", "final": "1234", "bandeira": "Mastercard", "cor": "bg-orange-500"},
    {"nome": "Itaú Personnalité", "final": "8901", "bandeira": "Visa", "cor": "bg-gray-800"},
    {"nome": "Banco do Brasil", "final": "9988", "bandeira": "Elo", "cor": "bg-yellow-500"},
    {"nome": "Bradesco Prime", "final": "3344", "bandeira": "Visa", "cor": "bg-red-600"},
    {"nome": "Santander Select", "final": "5566", "bandeira": "Mastercard", "cor": "bg-red-500"},
    {"nome": "C6 Bank Carbon", "final": "7788", "bandeira": "Mastercard", "cor": "bg-gray-900"},
    {"nome": "Caixa Econômica", "final": "1122", "bandeira": "Elo", "cor": "bg-blue-500"},
    {"nome": "XP Visa Infinite", "final": "0099", "bandeira": "Visa", "cor": "bg-slate-800"},
    {"nome": "BTG Pactual", "final": "4433", "bandeira": "Mastercard", "cor": "bg-blue-900"},
    {"nome": "Neon", "final": "2211", "bandeira": "Visa", "cor": "bg-cyan-500"},
    {"nome": "Banco Next", "final": "6677", "bandeira": "Visa", "cor": "bg-emerald-500"},
    {"nome": "Banco Pan", "final": "8899", "bandeira": "Mastercard", "cor": "bg-sky-500"},
    {"nome": "Mercado Pago", "final": "3322", "bandeira": "Visa", "cor": "bg-blue-400"},
    {"nome": "PicPay Card", "final": "5544", "bandeira": "Mastercard", "cor": "bg-green-500"},
    {"nome": "Sicoob", "final": "7766", "bandeira": "Mastercard", "cor": "bg-teal-700"},
    {"nome": "Sicredi", "final": "9900", "bandeira": "Visa", "cor": "bg-green-600"},
    {"nome": "Porto Seguro", "final": "1133", "bandeira": "Visa", "cor": "bg-blue-700"},
    {"nome": "Will Bank", "final": "2244", "bandeira": "Mastercard", "cor": "bg-yellow-400"},
    {"nome": "Iti Itaú", "final": "5577", "bandeira": "Visa", "cor": "bg-pink-500"}
]



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
    return render_template('cartoes.html', meus_cartoes=lista_de_cartoes)

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
    novo_cartao = {
        "nome": nome_digitado,
        "final": final_digitado,
        "bandeira": "Visa", # Fixo por enquanto...
        "cor": "bg-teal-500" # Uma cor verde-água para os novos cartões. 
    }

    # 3. Adicionamos esse novo cartão na nossa lista global, ou "lista_de_cartoes"
    lista_de_cartoes.append(novo_cartao)

    # 4. Mandamos o navegador voltar para a tela de cartões para ver o resultado assim que o usuário clica em "Adicionar Cartao"
    return redirect('/cartoes')

if __name__ == '__main__':
    app.run(debug=True)
