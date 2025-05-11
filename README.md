Web-Based Hangman Game 

An interactive web-based Hangman game built using the Flask web framework.
This project allows users to enter their name, choose a difficulty level (Easy, Medium, Hard), and guess letters to reveal a randomly selected word. 
Sessions track player progress, wins and losses.

 Features:
- Player name input with session tracking
- Difficulty selection (easy, medium, hard)
- Tracks wins and losses in real-time
- Prevents repeated guesses (client-side + server-side)
- Modular word list support using `.txt` files
- Clean, responsive interface


- Python 3
- Flask (Web Framework)
- Jinja2 (Template Rendering)
- HTML/CSS/JavaScript (Frontend)
- Flask Session (For tracking state)
- File I/O (Word list loading from files)

 Structure:
  
├── Hangman.py
├── templates/
│ ├── name.html
│ ├── index.html
│ └── game.html
├── word_lists/
│ ├── easy.txt
│ ├── medium.txt
│ └── hard.txt


