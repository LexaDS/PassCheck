import requests
class Client:
    def put(self):
        url = 'http://127.0.0.1:5000/api/v1/resources/books'
        params = {"id":"", "title":"Dune","author":"Frank Herbert","first_sentence":"In saptamana dinainte plecarii din Arrakis","published":"1965"}
        p = requests.post(url, json=params)
        print(p)

    def get(self):
        url = 'http://127.0.0.1:5000/api/v1/resources/books/all'
        g=requests.get(url)
        with open ("myget.txt",'w') as x:
            x.writelines(str(g.content))

Client().get()

