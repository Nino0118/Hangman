from flask import Flask, render_template, request, redirect, session
import random
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here' 

@app.route('/name')
def name():
    return render_template('name.html')

@app.route('/')
def index():
    if 'player' not in session:
        return redirect('/name')

    first_login = session.pop('first_login', False)  
    return render_template('index.html', first_login=first_login)


@app.route('/setname', methods=['POST'])
def setname():
    session['player'] = request.form['player']
    session['wins'] = 0
    session['losses'] = 0
    session['first_login'] = True  
    return redirect('/')


@app.route('/reset')
def reset():
    session.pop('word', None)
    session.pop('guessed', None)
    session.pop('chances', None)
    session.pop('result_recorded', None)
    return redirect('/')


def load_words(category):
    path = f'word_lists/{category}.txt'
    if not os.path.exists(path):
        raise FileNotFoundError(f"No such category: {category}")
    with open(path, 'r') as file:
        words = [line.strip().lower() for line in file if line.strip()]
    return words

@app.route('/start', methods=['POST'])
def start():
    category = request.form['category']
    words = load_words(category)
    word = random.choice(words)
    session['word'] = word
    session['guessed'] = []
    session['chances'] = 6
    session.pop('result_recorded', None)  # reset win/loss flag
    return redirect('/game')

@app.route('/game', methods=['GET', 'POST'])
def game():
    if 'player' not in session:
        return redirect('/name')

    word = session.get('word')
    guessed = session.get('guessed', [])
    chances = session.get('chances', 6)

    if request.method == 'POST':
        guess = request.form['guess'].lower()
        if guess.isalpha() and len(guess) == 1 and guess not in guessed:
            guessed.append(guess)
            session['guessed'] = guessed
            if guess not in word:
                chances -= 1
            session['chances'] = chances

    incorrect = [letter for letter in guessed if letter not in word]
    won = set(word).issubset(set(guessed))
    lost = chances <= 0 and not won

    if (won or lost) and 'result_recorded' not in session:
        if won:
            session['wins'] = session.get('wins', 0) + 1
        elif lost:
            session['losses'] = session.get('losses', 0) + 1
        session['result_recorded'] = True

    return render_template(
        'game.html',
        word=word,
        guessed=guessed,
        chances=chances,
        incorrect=incorrect,
        won=won,
        lost=lost
    )

if __name__ == '__main__':
    app.run(debug=True, port=5001) 
