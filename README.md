# epx-text-service
Text similarity NLP score

Local docker 
```
docker image build -t epx-text .
docker run -p 5000:5000 epx-text:latest
```
Heroku Docker deployment
```
heroku container:login
heroku container:push web --app epx-text
heroku container:release web --app epx-text
```
