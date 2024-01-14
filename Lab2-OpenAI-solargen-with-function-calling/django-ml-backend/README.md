# django-ml-backend

## Create a virtual environment

```
python -m venv venv

source venv/bin/activate
```

## Install dependencies

```
pip install -r requirements.txt
```

## Start the app

```
  uvicorn app:app --host 0.0.0.0 --port 8001
```

## Ask Question

```
curl -X POST "http://localhost:8001/ask/?query=$(echo -n "who is the borrower in this agreement?" | xxd -plain | tr -d '\n' | sed 's/\(..\)/%\1/g')" -H "accept: application/json" -F "file=@file.pdf"
```
