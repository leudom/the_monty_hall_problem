The Monty Hall Problem (Simulation)
==============================

This project showcases a simulation of the ever-fascinating Monty Hall problem. Why fascinating? Eventough the problem itself as well as the mathematics behind is quite simple to get, the intuition of the solution is missleading in such a way, that even statisticians were challenged by this brain teaser. However, the theory behind that problem can be rigorously verified with simulations...and this repo provides you the code to play around with!

And here is the problem in short:

Let's suppose you are in *Monty Hall's* show (American television game show *Let's Make a Deal* and named after its original host, *Monty Hall*) and you are facing three closed doors (they look exactly the same). 

Everbody in the room know (including you) know, that there is **1 prize :car:** and **2 goats :goat:** behind the doors.

Now Monty wants you to pick a door of your choice (Let's say you pick door #1). This door (#1) remains closed so far. Now Monty - who knows where the car and the goats are - opens 1 of the remaining 2 doors where a goat is behind (Let's say he opens door #3). It looks like this...
![image](https://user-images.githubusercontent.com/61742123/111771901-827e4d80-88ac-11eb-8cdd-fcd4c82d86e9.png)
https://en.wikipedia.org/wiki/Monty_Hall_problem


Now Monty asks you...

**a.) If you want to stay with your initial choice (In this case door #1)**

**OR**

**b.) If you want to switch to the other door that is also still closed (door #2)**


What would you do? What would be your strategy and why?

I skip the part with the mathematical explainations here (maths on that problem turns out to be quite simple). This can be found in tons of resources on the web:

* https://en.wikipedia.org/wiki/Monty_Hall_problem
* https://de.khanacademy.org/math/precalculus/prob-comb/dependent-events-precalc/v/monty-hall-problem
* https://www.amazon.de/Monty-Hall-Problem-Remarkable-Contentious/dp/0195367898
* etc.


## Usage
I've provided a environment.yml to reproduce the environment from.

```bash
conda env create -f environment.yml
```
Activate the environment
```bash
conda activate monty_hall_env
```
The python script in *src/monty_hall_game.py* can be used as a command line tool with the argument `--trials`. This let you play the game n times, where n are the number of trials (default trials are set to 100.000).
```bash
python src/monty_hall_game.py --trials 10000
```
The output looks like that...
```bash
Start playing 10000 times...
Finished all trials in 0.126365 seconds
Absolute number of winning a game when stayed: 3299
Absolute number of winning a game when switched to the alternative door: 6701
Relative frequency of winning the prize when switching the doors: 0.6701
```
As you increase the number of trials, the relative frequency of winning the prize when switching the door approximates 1/3 (as the theory says).

Happy goating!
## Contributing
Pull requests are welcome. Feel free to fork this repo and extend the game as you like.
## License
[MIT](https://choosealicense.com/licenses/mit/)
