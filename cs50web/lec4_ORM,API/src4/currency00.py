import requests

def main():
    sHttp = "http://data.fixer.io/api/latest?access_key=1fd6975fef5483b0987dfac810e3bb5a"
    sHttp = sHttp + "&base=USD&symbols=EUR"
    res = requests.get(sHttp)
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    print(data)

if __name__ == "__main__":
    main()
