FROM python:3.9    
ENV PYTHONUNBUFFERED 1  
WORKDIR /app    
COPY requirements.txt /app/requirements.txt  
RUN pip uninstall flask-cors
RUN pip uninstall flask-migrate  
RUN pip install -r requirements.txt
COPY . /app  

CMD python main.py  