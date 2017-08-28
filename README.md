# Overview

* Vamirach is turn based smartphone roguelike
* Target audience are RPG fans in public transport, playing with 1 hand
* The game should have simple visuals but deep gameplay - nearly like MUDs of the past
* The goal of the game is to survive as long as possible in randomly generated world
* Escalating difficulty ensures that survival is challenging
* It is theoretically impossible to survive for long time
* The gameplay is about collecting resources, crafting valuables and fighting enemies
* Resources can be collected from the very beginning
* Valuables are crafted from collected resources
* Enemies can be defeated with weapons crafted from resources
* To survive, the character must fulfil primary needs (to eat, to sleep, to heal injuries)
* The character becomes tired without sleep, hungry without food, and needs to heal damage taken
* Primary sources of food are collecting and hunting
* It's harder and harder to aquire enough food as the game progresses
* It's only possible to rest near fire at night, as animals afraid of fire
* The amount of tiredness removed depends on safety of the place (having walls, roof etc)
* The difficulty escalates over time, so the only way to survive is to develop more and more advanced tools
* The tools are ranging from weapons like spear to garden tools like shovel

# Installing pygame

The game is developed as gameplay prototype. The pygame is used to speedup development and focus effort on gameplay logic rather than generic game mechanics.

The code is tested and developed with python 3.6 on Mac OS. It is suggested to use homebrew to install python and then pip to install pygame itself:

    pip3 install pygame
