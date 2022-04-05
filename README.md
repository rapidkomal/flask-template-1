# Flask Template

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
