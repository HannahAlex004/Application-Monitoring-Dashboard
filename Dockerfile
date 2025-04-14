FROM python:3.9 
WORKDIR /app 
COPY requirements.txt . 
RUN pip install -r requirements.txt 
COPY . . 
<<<<<<< HEAD
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"] 
=======
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
>>>>>>> 2e64151fcaa0971a5603aa030b30eda353ba2196
