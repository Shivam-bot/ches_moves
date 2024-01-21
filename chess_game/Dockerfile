FROM ubuntu:18.04


ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1



RUN apt-get update &&\
	 apt-get install -y git &&\
	 	apt-get install -y python3 
	
		 	
RUN apt-get install -y python3-pip
	 		
WORKDIR /home

COPY ./ ./
 	
RUN git clone https://github.com/Shivam-bot/chess_moves.git

WORKDIR /home/chess_moves

WORKDIR /home/chess_moves/chess_game

RUN apt-get install -y python3-venv

RUN python3 -m venv venv

RUN . /home/chess_moves/chess_game/venv/bin/activate


RUN pip3 install Django

RUN pip3 install djangorestframework


EXPOSE 8000

CMD ["python3", "manage.py", "runserver"]

 
