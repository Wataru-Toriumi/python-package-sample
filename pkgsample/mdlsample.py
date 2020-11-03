import requests

def get(url='https://www.google.com/?hl=ja'):
    return requests.get(url)

def func_sample(x, y, z):
    return x + y + z
