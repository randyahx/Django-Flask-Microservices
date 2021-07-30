FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

<<<<<<< Updated upstream
CMD python3 manage.py runserver 0.0.0.0:8000
=======
CMD mysql -u mysql
CMD update user set Password=root('new-password' where user = 'root')
CMD flush privileges
CMD exit  
CMD python manage.py runserver 0.0.0.0:8000
>>>>>>> Stashed changes
