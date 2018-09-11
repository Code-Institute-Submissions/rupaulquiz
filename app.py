import os
import json

from flask import Flask, render_template, redirect, request

app = Flask(__name__)


def write_to_file(file, name):
    """Writes data to text files"""
    with open(file, "a") as player_list:
        player_list.writelines(name)
        

def add_incorrect_answer(player_name, question, incorrect_answer):
    """Adds incorrect answer to incorrect_answers.txt"""
    write_to_file("data/incorrect_answers.txt", "{0} thinks the answer to \"{1}\" is: {2}! \n".format(
            player_name, question, incorrect_answer))
            
            
def get_all_data(file, list):
    """Collects data from .txt files"""  
    list = []
    with open(file, "r") as list:
        list = [row for row in list if len(row.strip()) > 0]
    return list
    
    
def remove_duplicates(list):
    """Iterates list to remove duplicates and create new list"""
    x = 0
    while x < len(list):
        y = x + 1
        while y < len(list):
            if list[x] == list[y]:
                del list[y]
            else:
                y += 1
        x += 1
    return list
        
    
@app.route('/', methods=["GET", "POST"])
def index():
    """Start page with instructions and user name submission"""
    if request.method == "POST":
        write_to_file("data/players_names.txt", request.form["player_name"] + "\n")
        write_to_file("data/online_players.txt", request.form["player_name"] + "\n")
        return redirect(request.form["player_name"])
    return render_template("index.html")
    

@app.route('/<player_name>', methods=["GET", "POST"])
def load(player_name):
    """Load quiz questions from json file"""
    with open("data/questions.json", "r") as json_data:
        questions= json.load(json_data)
    
    """Question count to iterate through questions"""
    question_index = 0
    
    """Counts user's attempts at question"""
    question_tries = 0
    
    """Counts number of points the user has"""
    player_score = 0
    
    
    if request.method == "POST":
        """Add user to online players list"""
        write_to_file("data/online_players.txt", player_name + "\n")
        
        """Increases counts with hidden input on user's answer form""" 
        question_index = int(request.form["question_index"])
        question_tries = int(request.form["question_tries"])
        player_score = int(request.form["player_score"])
        
        """Get the user's answer"""
        player_response = request.form["player_response"]
        
        """Compare user response to correct answer"""
        if questions[question_index]["answer"] == player_response:
            """Adds points if correct, and resets question_tries count"""
            question_index += 1
            if question_tries == 0:
                player_score += 3
            elif question_tries == 1:
                player_score += 2
            elif question_tries == 2:
                player_score += 1
        else:
            """If incorrect, adds to tries count and saves incorrect answer"""
            question_tries += 1
            add_incorrect_answer(player_name, 
                                questions[question_index]["question"], 
                                player_response)
            if question_tries == 3:
                """Moves onto next question after 3 tries"""
                question_index += 1
                question_tries -= 3
            
            
    incorrect_answers = get_all_data("data/incorrect_answers.txt", list)
    
    online_players = get_all_data("data/online_players.txt", list)
    online_list = [player for player in online_players]
    no_duplicates_online_list = remove_duplicates(online_list)
    
    return render_template("quiz.html", player_name=player_name, 
                            incorrect_answers=incorrect_answers, 
                            questions=questions, 
                            online_players=online_players, 
                            question_index=question_index,
                            question_tries=question_tries,
                            player_score=player_score,
                            no_duplicates_online_list=no_duplicates_online_list)
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'), port=int(os.environ.get('PORT', 0)), debug=True)