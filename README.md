Random Quote API

About
The API returns a random quote from quote.txt file.

Instructions:

Use Flask server

One time Set-up

1. Clone the Github repository to your local enviroment.
    i. In a terminal, navigate to the directory that contains quoteservice.py.
2. Create a Python virtual enviroment. In the examples below, set the virtual enviroment .venv
    python3 -m venv .venv
3. Activate the Python  virtual enviroment 
    source .venv/bin/activate
4. Use pip to instal dependencies.
    pip install -r requirments.txt

Request data

Start the Flask API server.

    1. Run the following command 
    flask --app quoteservice.py
    2. The output will show the link where server is running. 
    The output should look similar to the one below:

        Request HTTP GET http://127.0.0.1:5000/
        Recieved HTTP GET response Quote1

Example Code to Request Data 

import requests

url = r'http://127.0.0.1:5000'
# GET Only
r = requests.get(url)
# URL, Response 
print("Request HTTP GET "+r.url)
print("Received HTTP GET response "+ r.text)


![alt text](http://url/to/UML_mokshano.JPG)
