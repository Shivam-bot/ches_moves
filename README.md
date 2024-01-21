# chess_moves

For Linux user:- Run these commands :- sudo chmod 774 chess.sh ./chess.sh Now you are ready to use

For Window user:- pip install virtualenv py -m venv venv venv/Scripts/activate   pip install -r req.txt python manage.py runserver Now you are ready to use

TO Access through Dockerfile:-

sudo docker build --tag chess_moves :1--file Dockerfile .   >>>> to create image
sudo docker images -q chess_moves:1  >>> get image id>> container_id
sudo docker run --network host container_id  >>>> to run server

VALID OPTIONS :- 


B>>>>> BLACK
W>>>> WHITE


KING = ['BKing', 'WKing']
QUEEN = ['BQueen', 'WQueen']
ROOK = ['BRook', 'WRook']
BISHOP = ['BBishop', 'WBishop']
KNIGHT = ['BKnight', 'WKnight']
PAWN = ['BPawn', 'WPawn']
