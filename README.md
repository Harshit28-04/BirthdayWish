# Birthday App (Flask)

A tiny front-end + back-end app to wish someone a happy birthday with confetti and repeated greetings based on age.

## Quick start (local)

1. Make sure Python 3.9+ is installed.
2. `pip install -r requirements.txt`
3. `python app.py`
4. Open http://127.0.0.1:5000 in your browser.

## Deploy (quick outline)

- Push these files to a Git repo (GitHub).
- On Render / Railway / Fly.io:
  - Create a new Web Service from the repo.
  - Set start command to: `gunicorn app:app`
  - Add a build step to install: `pip install -r requirements.txt`
  - Deploy, then share the generated URL.