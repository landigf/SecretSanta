from flask import Flask, render_template, request
import random
import smtplib

app = Flask(__name__)

def send_email(togift):
    oggetto = "Subject: Santa Secret\n\n"
    contenuto = f"Pensa al regalo da fare a {togift[0]}"
    messaggio = oggetto + contenuto
    email = smtplib.SMTP("smtp.gmail.com", 587)
    email.ehlo()
    email.starttls()
    email.login("santasecretbyng@gmail.com", "ulpo bsfd cgjb dddl")
    email.sendmail("santasecretbyng@gmail.com", togift[1], messaggio)
    email.quit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/secretsanta', methods=['POST'])
def secretsanta():
    n_persone = int(request.form['n_persone'])
    partecipanti = {}
    for i in range(n_persone):
        nome = request.form.get(f'nome_{i}', '')
        email = request.form.get(f'email_{i}', '')
        partecipanti[nome] = email

    lista_persone = list(partecipanti.keys())
    for persona in lista_persone:
        while (curr := random.choice(lista_persone)) == persona:
            pass
        togift = [persona, partecipanti[curr]]
        send_email(togift)
        del(partecipanti[curr])

    return render_template('success.html', partecipanti=lista_persone)

if __name__ == '__main__':
    app.run(debug=True)
