# RuPaul's Best Friend Race: a RuPaul's Drag Race themed quiz app.

## Project Three - Practical Python ##

This is my third project - an application written in Flask, with the purpose of 
demonstrating my practical Python skills. 

The app is a text-based quiz, with the theme of ['RuPaul's Drag Race'](https://en.wikipedia.org/wiki/RuPaul%27s_Drag_Race) television show. The target user is someone with some knowledge of the show, however it is possible to run through the app without answering any of the questions correctly. 

The user will face 10 questions that range in difficulty, and they will receive points for correct answers, depending on which attempt they answer correctly. At the end of the game, they will be given a score card, that relates to which range their score is in. I will also include a high score board at the end, which encourages users to try the quiz again. 

### Demo: ###

A live demo can be found here: https://slc-project-three.herokuapp.com/


### Technologies and Languages: ### 

* [Python (3.0)](https://www.python.org/) - for backend code and site functionality.
* [Flask (1.0.2)](http://flask.pocoo.org/) - to deploy my web application.
* [Bootstrap (4.1.3)](https://getbootstrap.com/) - to build a responsive and visually appealing site.
* [HTML](https://en.wikipedia.org/wiki/HTML) - the language used to write and create the web app.
* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - the language used to customise and present the web app, including CSS3 media queries.
* [JSON](https://www.json.org/) - to easily store and transmit the quiz questions as a data object.
* [ASCII](https://www.text-image.com/convert/ascii.html) - to convert an image into text, add a 'retro' feel to the project.


### UX: ### 

As this was my first Python project, I wanted a simple layout for my quiz game so I could focus on the backend code. The game itself reminded me of websites I visited when I first used the internet in the late 1990's, which influenced the use of the ASCII image on the index page.

The website is for RuPaul's Drag Race fans, who want to play a simple quiz. The
quiz should have full functionality on all screen sizes. I wanted to display a customised score card at the end of the quiz, depending on the user's score.

I also wanted to encorporate the following user stories:

* As a user, I want to keep track of what number question I am on, and how many points I have, so that I can see how well I am doing.
* As a user, if I answer a question wrong, I want to see the incorrect answer so I can compare this to my next attempt.
* As a user, I want to see who has achieved the high score at the end of the quiz, so I can compare how I have done.
* As a user, I want the option to take the quiz again, so I can attempt to beat my own score, and possibly get my name as the high scorer.


### Features: ###

* High score - stores the name and score of the user who achieves the most points, and displays this on the score card at the end of the quiz, by updating a key value pair in a dictionary.
* Store and recall of data - functions that stores user input in .txt file objects, which can then be recalled and manipulated in further functions. For example, user's name is stored when they input it, which is then recalled with duplicates removed, and reversed so the most recent input is first. This is achieved using the read and write functionality in Python, as illustrated in the write_to_files function in app.py.
* The players score count - this allows users to see how they are doing. I achieved this with an 'if' statement that added points depending on the number of tries the user had at the question.
* The question index count - this allows users to see how they are progressing through the quiz, by increasing the count with input from a hidden field when the user submitted an answer.
* The question attempts count - this shows a user how many times they have attempted a question, so they know how many attempts they have left. This was also achieved by increasing the count with a hidden field when the user submitted a question, but by using an 'if' statement, I limited the attempts at each question to 3.
* Score cards - these are customised depending on how many points the user has achieved, and are implemented using an 'if' statement that takes the players score and returns the corresponding score card.
* Use of CSS3 Media queries - to make the app responsive to different screen sizes.


### Deployment: ### 

My code is deployed to GitHub, at: https://github.com/sarahcrosby/rupaulquiz

I have also deployed my code to Heroku, at: https://slc-project-three.herokuapp.com/

To run the code locally, download the files from GitHub. Then, ensure you follow the requirements.txt and install everything indicated in this. You will then be able to run the app by typing the following into the terminal, "python3 app.py run".


### Testing ### 

My first test was to ensure write_player_name functioned correctly. I did this 
with a manual test, by printing {{ player_name }} on the quiz.html page. This
displayed the name correctly, and I also checked in data/players_names.txt that
the names I had submitted had been saved.

When testing the custom CSS, I wrapped each div in different coloured margins,
so I could see exactly what happened at each screen size. These were removed
when I was happy with the design.

I manually tested the functionality added in commit 4, by adding incorrect
answers to the questions, and checking that these and the user name I chose
were added to the relevant .txt files in the data folder. For the  
duplicate function added in commit 6, I added different names on the page
and printed the no_duplicates_online_list, and also checked that the names
were still added to online_players.txt.

To test my quiz_tries and player_score counts, I printed the scores to the
terminal and ran through my app using different answers, to test what happened
when I, for example, got the answer correct the first, second, and third times, 
and also what happened when I didn't get the answer right.

I tested how the code worked on different screen sizes, by using the emulator 
function in the developer tools, and also on my mobile device, laptop and 
tablet. 

I also added automatic tests in my tests.py, which automatically test some of my functions, and also test the status of my URLs. 

Before submitting my project, I ran through the app to test that everything was working. I tried adding correct and incorrect answers into the submission box, and also an empty box, to see if anything would result in a 404 status code. I also did this to check the points function was working properly, as the points corresponded to correct or incorrect answers. I also tried different input in the 'stagename' box. 

### Version control - ### 

1. Initial commit.
2. Base template added, index.html started with basic username, submission leading to customised quiz.html.
3. Customised index.html, added style.css.
4. Loaded questions data, and functions to compare user input and save incorrect answers. Also added online player functionality.
5. Tested previous commit functions. Customised quiz.html.
6. Added function to remove duplicates. 
7. Implement scoring system, manually tested.
8. Added data to questions.json.
9. Created score cards and added functionality at end of quiz.
10. Customised score cards, added high score.
11.  Created automatic tests in tests.py.
12.  Tidied up code and layout.
13.  Added reversed online user and incorrect answer lists, to list last 10 responses only. Added media queries.
14. Updated README file. Final touches to code and Heroku deployment, including addition of requirements.txt and Procfile.
15. Updated Procfile to address bug.
16. Final commit. Diabled debug mode. Added alt attribute to image.