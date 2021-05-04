from flask import Flask, render_template, request, redirect
app = Flask(__name__)

class Jogo:
    def __init__(self, nome, hora):
        self.nome = nome
        self.hora = hora
 
jogo1 = Jogo('Flamengo x Fluminense', '16:00') 
jogo2 = Jogo('Flamengo x Vasco', '16:00')
jogos = [jogo1, jogo2]

@app.route('/')
def index():
    return render_template('index.html', jogos=jogos)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
    
@app.route('/cadastrar', methods=['POST',])
def cadastrar():
    nome = request.form['nome']
    hora = request.form['hora']
    novo_jogo = Jogo(nome, hora)
    jogos.append(novo_jogo)
    return redirect('/')


if __name__ == '__main__':
    app.debug = True
    app.run()



