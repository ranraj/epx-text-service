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
REST API

Request
```
https://localhost:5000/text/similarity?text1=New%20Delhi&text2=Delhi
```
Response
```json
{
  "similarity": 71.42857142857143
}
```