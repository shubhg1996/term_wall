# Terminal wallpaper change
## Requires:
Python >= 3.5
Terminology, Tilix or ITerm on MacOS

## Instructions:
1. `chmod a+x main.py`
2. Make directory "bin" in home and append to $PATH in .bashrc or .zshrc
3. `ln -s main.py ~/bin/twall`

## Usage:
1. Place images in "Data" directrory with name containing the searchword. Example: "pikachu_ash_charmander.png"
+ `twall pikachu`   *loads a random image with pikachu in it*
+ `twall random`    *loads a random image*

## Sample:
![alt text](https://github.com/shubhg1996/term_wall/blob/master/sample.png)
