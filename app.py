import os
import json

from flask import Flask, render_template, redirect, request

app = Flask(__name__)


def write_to_file(file, name):
    with open(file, "a") as player_list:
        player_list.writelines(name)
        

def add_incorrect_answer(player_name, incorrect_answer):
    write_to_file("data/incorrect_answers.txt", "({0}) - {1}\n".format(
            player_name, incorrect_answer))
            

def get_all_incorrect_answers():
    incorrect_answers = []
    with open("data/incorrect_answers.txt", "r") as incorrect_answers:
        incorrect_answers = [row for row in incorrect_answers if len(row.strip()) > 0]
    return incorrect_answers
        
    
@app.route('/', methods=["GET", "POST"])
def index():
    """Start page with instructions and user name submission"""
    if request.method == "POST":
        write_to_file("data/players_names.txt", request.form["player_name"] + "\n")
        return redirect(request.form["player_name"])
    return render_template("index.html")
    

@app.route('/<player_name>', methods=["GET", "POST"])
def load(player_name):
    """Load quiz questions from json file"""
    with open("data/questions.json", "r") as json_data:
        questions= json.load(json_data)
    
    """Question count to iterate through questions"""
    question_index = 0
    
    
    if request.method =="POST":
        """Add user to online players list"""
        write_to_file("data/online_players.txt", player_name + "\n")
        
        """Increase the question index by hidden field in answer submission form"""
        question_index = int(request.form["question_index"])
        
        """Get the user's answer"""
        player_response = request.form["player_response"]
        
        """Compare user response to correct naswer"""
        if questions[question_index]["answer"] == player_response:
            question_index += 1
        else:
            add_incorrect_answer(player_name, player_response +"\n")
            
    incorrect_answers = get_all_incorrect_answers()
    
    online_players_list = open("data/online_players.txt")
    online_players = [row for row in online_players_list if len(row.strip()) > 0]
    online_players_list.close()
        
    return render_template("quiz.html", player_name=player_name, 
                            incorrect_answers=incorrect_answers, 
                            questions=questions, 
                            online_players=online_players, 
                            question_index=question_index)
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'), port=int(os.environ.get('PORT', 0)), debug=True)