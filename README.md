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
were added to the relevant .txt files in the data folder. 



Technologies Used

I decided to use the framework of Bootstrap to build a responsive and visually
appealing app - https://getbootstrap.com - and I will maintain a division
between the Bootstrap code and my code by creating a library of used Boostrap
code.

Python

Flask

Convert html image https://www.text-image.com/convert/ascii.html