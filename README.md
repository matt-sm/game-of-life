# game-of-life
Conway's Game of Life

## Run tests
```
python3 -m venv venv
source venv/bin/activate
pip install -r dev-requirements.txt
```
## Examples
Blinker
```
python game.py -x 5 -y 5 -c 2,1 2,2 2,3
```
Toad
```
python game.py -x 6 -y 6 -c 2,2 3,2 4,2 1,3 2,3 3,3
```
Block
```
python game.py -x 4 -y 4 -c 1,1 2,1 1,2 2,2
```
Glider
```
python game.py -x 5 -y 5 -c 2,1 3,2, 1,3 2,3 3,3
```