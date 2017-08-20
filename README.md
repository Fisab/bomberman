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
* Command "MOVE" can get this arguments: UP, DOWN, LEFT, RIGHT.
* Command "PLANT" get 1 number argument. It was time to explode bomb. 0 < Time < 15
