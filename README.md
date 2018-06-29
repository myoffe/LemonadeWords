## Requirements
- pipenv (https://docs.pipenv.org/#install-pipenv-today)

## How to run this?
```
git clone git@github.com:myoffe/LemonadeWords.git
cd LemonadeWords
pipenv sync
pipenv run start
```

## API examples
```
POST http://localhost:5000/count
{
  "file": "app.py"
}

POST http://localhost:5000/count
{
  "text": "Hi! My name is (what?), my name is (who?), my name is Slim Shady"
}

POST http://localhost:5000/count
{
  "url": "https://www.lemonade.com/"
}

GET http://localhost:5000/stats/my
GET http://localhost:5000/stats/lemonade
GET http://localhost:5000/stats/everything
```
