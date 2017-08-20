# Info
![](https://pp.userapi.com/c841036/v841036835/17b0c/FHp7tqeHGoA.jpg)
* Grey - simple block. If explode near bomb this block will destruct
* Green - strong block. If explode near bomb nothing will happen
* Orange - it's my hero(rect)
* Black circle with small orange circle - bomb
# Install
For play this game u must install python3 and pip for python3. Then this libraries: pygame.
# Setup
Open **config.json** and u see there something like this:
```
{
   "cell_size": 30, //all cells size. You can change it
   "cell_amount": [31, 21], //amount of all cells at X and Y
   "cooldown_plant": 5, //default cooldown to plant
   "bomb_exp_ticks": 5, //bomb_explode_ticks if player dont tell at cmd file
   "bomb_exp_radius": 3, //bomb explosion raius
   "players": [
      {
         "nick": "Fisab", //player nick name
         "color": "255,69,0", //player color
         "script_path": "data\\fisab\\script.py", //player scipt path(from main.py)
         "data_file": "data\\fisab\\fisab.cmd" //command file path(from main.py)
      }
   ]
}
```
For add more players just create for their script, command file and then input this into config "players" like example. You can use any script types which can read and write from/into files.(exe, py, php....)

# Data file with info about game for player scripts:
```
{
   "walls": {
      "simple_blocks": {
         "pos": [3, 2]
      },
      "strong_blocks": {
         "pos": [0, 0]
      }
   },
   "tick": 10,
   "players": [
      {
         "name": "Fisab",
         "pos": [3, 5],
         "color": [255, 69, 0],
         "last_plant": 10
      }
   ],
   "bombs": [
      {
         "owner_name": "Fisab",
         "pos": [3, 5],
         "color": [255, 69, 0],
         "exp_radius": 3,
         "time": 3
      }
   ]
}
```

# Example command
*This commands need put into file with name: "%nick%.cmd".*
```
MOVE UP; PLANT 3;
```
You can put into your cmd file only 1 command or dont put anything.
* Command "MOVE" can get this arguments: UP, DOWN, LEFT, RIGHT.
* Command "PLANT" get 1 number argument. It was time to explode bomb. 0 < Time < 16