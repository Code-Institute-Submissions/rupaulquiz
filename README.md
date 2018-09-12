# RuPaul's Best Friend Race: a RuPaul's Drag Race themed quiz app.

This is my third project - an application written in Flask, with the purpose of 
demonstrating my practical Python skills.

commit 1 - Initial commit.
commit 2 - Base template added, index.html started with basic username.
            submission leading to customised quiz.html.
commit 3 - Customised index.html, added style.css.
commit 4 - Loaded questions data, and functions to compare user input and save incorrect answers.
            Also added online player functionality.
commit 5 - Tested previous commit functions. Customised quiz.html.
commit 6 - Added function to remove duplicates. 
commit 7 - Implement scoring system, manually tested.
commit 8 - Added data to questions.json.
commit 9 - Created score cards and added functionality at end of quiz.
commit 10 -  Customised score cards, added high score.


Testing

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

I created an automatic test in tests.py to check whether the remove_duplicate
function worked - 


Technologies Used

I decided to use the framework of Bootstrap to build a responsive and visually
appealing app - https://getbootstrap.com - and I will maintain a division
between the Bootstrap code and my code by creating a library of used Boostrap
code.

Python

Flask

Convert html image https://www.text-image.com/convert/ascii.html