# Testing
Trying to nail down a Python bug with hierarchies or something

---
OK, so here's how this repository is intended to work. `main.py` in the topmost level calls `firstlevel.secondlevel.firstdependency` two levels down. Then `firstlevel.secondlevel.firstdependency` is supposed to call `firstlevel.seconddependency` one level down (it doesn't actually, but pretend it does for now). Finally, `firstlevel.seconddependency` prints `SUCCESS`.

The problem here is that this doesn't work, in part because `firstlevel.secondlevel.firstdependency` *actually* calls `seconddependency` instead of `firstlevel.seconddependency`.

Currently I know of two ways to fix this: either edit `firstlevel.secondlevel.firstdependency` to call `firstlevel.seconddependency`, or to move `main.py` into `firstlevel` and edit it to call `secondlevel.firstdependency` instead. However, neither of these are particularly good for my usecase. Namely, someone else has written a module (in this case, `firstlevel` but with way way way more files and folders) and I'm having trouble integrating it into my code; the first option would require me to edit basically every single file in that module, and the second option would result in a mess of files in the top level of the repository. Is there some way to make this work without moving `main.py` and without changing the code of either `firstlevel.secondlevel.firstdependency` or `firstlevel.seconddependency`?
