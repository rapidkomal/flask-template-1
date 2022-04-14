# Flask Template
<p align="center">
  <a href="https://www.rapidinnovation.io/" target="blank"><img src="static/images/ri_logo.jpeg" width="320" alt="RapidInnovation Logo" /></a>
</p>

Checkout *requirements.txt* for libraries used.

**Versions**
Python: 3.9.6

### Activate Virtual env
python -m venv venv
source venv/bin/activate

### Install dependencies
pip install -r requirements.txt

### Run Flask Application
**Development Mode**

_python run.py_

or

flask run

**Run Flask via Gunicorn**

_gunicorn --bind 0.0.0.0:5000 wsgi:app_
