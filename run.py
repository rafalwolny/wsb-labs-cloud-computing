from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/help')
def help():
    return "help me"

@app.route('/contact')
def contact():
    return "contact with me"



# 
# LAB SKONCZONY NA "PRACA Z TEMPLATES" (SEKCJA W LAB1.PDF)
# 
# GIT REPO STWORZONE I POLACZONE Z GITHUBEM
# 
# 
# 



if __name__ == '__main__':
    app.run(debug=True)