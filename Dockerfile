# the dependencies can't be installed on alpine version
FROM python:3.9
WORKDIR /app
COPY . /app
#RUN pip3 install numpy
#RUN pip3 install Flask
#RUN pip3 install python-dotenv
#RUN pip3 install googlemaps
#RUN pip3 install tensorflow
RUN pip install -r requirements.txt
EXPOSE 5000
# CMD python ./app.py