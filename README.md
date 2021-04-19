# Run with python 3.9
python main.py

# To run tests
python -m venv .env
.\.env\Scripts\activate
pip install -r requirements.txt

pytest main_test.py