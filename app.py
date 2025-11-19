from flask import Flask, render_template, request, flash, redirect, url_for
import smtplib

app = Flask(__name__)
app.secret_key = 'ton_secret_key_ici'  # nécessaire pour flash messages

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Exemple simple de récupération formulaire contact
        nom = request.form.get('nom')
        email = request.form.get('email')
        message = request.form.get('message')

        # Ici tu peux mettre ta logique d'envoi email (ex: SMTP)
        # Pour test, juste afficher un message de succès
        flash("Merci pour votre message, je vous répondrai bientôt!", "success")
        return redirect(url_for('home'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
