from flask import Flask, render_template, request

from calculatrice import addition, soustraction, multiplication, division

app = Flask(__name__)
def executer_calcul(a, b, operation):
    if operation == 'add':
        return addition(a, b)
    elif operation == 'sub' :
        return soustraction(a, b)
    elif operation == 'mul' :
        return multiplication(a, b)
    elif operation == 'div' :
        return division(a, b)
    return "Opération invalide"

@app.route('/', methods=['GET', 'POST'])
def index():
    resultat = None
    if request.method == 'POST':
        try:
            num1 = float(request.form.get('num1'))
            num2 = float(request.form.get('num2'))
            operation = request.form.get('operation')
            
            res = executer_calcul(num1, num2, operation)
            if isinstance(res, (int, float)):
                resultat = f"{res:g}"
            else : 
                resultat = res
        except (ValueError, TypeError):
            resultat = "Erreur : Veuillez entrer des nombres valides"
            
    return render_template('index.html', resultat = resultat)

if __name__ == '__main__':
    app.run(debug=True)