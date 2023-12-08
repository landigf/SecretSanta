from flask import Flask, render_template, request
import random
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/secretsanta', methods=['POST'])
def secretsanta():
    n_persone = int(request.form['n_persone'])
    return render_template('secretsanta.html', n_persone=n_persone)

@app.route('/sendemails', methods=['POST'])
def sendemails():
    n_persone = int(request.form['n_persone'])
    partecipanti = []
    for i in range(n_persone):
        nome = request.form.get(f'nome_{i}', '')
        email = request.form.get(f'email_{i}', '')
        partecipanti.append((nome, email))

    random.shuffle(partecipanti)

    for persona, regalato in zip(partecipanti, partecipanti[1:] + [partecipanti[0]]):
        togift = [persona[0], regalato[1]]
        send_email(togift)

    return render_template('success.html', partecipanti=partecipanti)

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

if __name__ == '__main__':
    app.run(debug=True)
