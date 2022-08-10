THE LAIR
By Douglas Kissack - https://dmk.codes/
July 2022

See Also: THE LAIR - Portfolio Project Report
Programming Language: Python

Project Description:

THE LAIR is a text-based, roguelike RPG created as a portfolio project during Nucamp's
introductory Python course.  This project demonstrates Object Oriented Programming (OOP)
and procedural generation of objects as its key features.

THE LAIR also functions as a basic RPG API - the core game loop, room functions,
classes, and procedural generation datasets can be adapted to produce similar
games quickly and easily.

Gameplay: 

In THE LAIR, the user creates a character and navigates it through a dungeon, battling
enemies, solving puzzles, acquiring loot, and learning powerful spells to aid them in 
their journey.  If the character survives through 30 Rooms, they will then encounter 
the final boss, which they must defeat to escape THE LAIR and win the game.

Roguelike & Procedural Generation: 

A roguelike game is typically characterized as a "dungeon crawl" through a series of
procedurally generated rooms or levels.  Death in a roguelike game is permanent (no
"save" or "respawn" feature), and each playthrough of the game begins at the same 
starting point and progresses toward the same ending point.

In THE LAIR, all Rooms, Enemies, Items, and Spells are populated as objects with
their attributes fully randomized (within a framework of basic rules to ensure game
balance).  There are many millions of potential combinations, such that a player is
unlikely ever to encounter the same Enemy, Item, Spell, or dungeon layout twice. 

Procedural generation is a key feature of roguelike games and enables each playthrough
to feel unique and challenging while still providing a familiarity that rewards
skill expression, resource management, and careful planning.

Running the Game: 

This repository includes a very basic game application (game.exe), but, per the
project guidelines, it was designed to be run primarily within a terminal window (in
this case, within the Visual Studio Code editor).  Despite the game.exe file's
validity, please exercise due caution when running ANY .exe file from an untrusted
source.

Comments: 

The project files feature extensive NumPy Style Python Docstrings and PEP 484 type
annotations.  These comments should be sufficient to demonstrate the purpose and
function of all aspects of the project. 

License: 

MIT License

Copyright 2022 - Douglas Kissack

Permission is hereby granted, free of charge, to any person obtaining a copy of this 
software and associated documentation files (the "Software"), to deal in the Software 
without restriction, including without limitation the rights to use, copy, modify, 
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to 
permit persons to whom the Software is furnished to do so, subject to the following 
conditions:

The above copyright notice and this permission notice shall be included in all copies 
or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION 
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.