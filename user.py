import requests

# This token (api-key) and header is my main problem
# I tried
token = 'e9941a557a21640c422ead9ed64587ee'
head = {
    'Authorization': 'Token token=' + token
}

url = 'https://favqs.com'

# Request to create a new user
def createUser(login, email, password):
    response = requests.post(url + '/api/users', headers=head,
                             data={'user': {'login': login, 'email': email, 'password': password}})
    return response.text

# Request to get a user
def getUser(login):
    response = requests.get(url + '/api/users/:login', params={'login': login})
    return response.text

# Request to update info about user
def updateUser(login, email, password):
    response = requests.put(url + '/api/users/:login',
                            data={'user': {'login': login, 'email': email, 'password': password}})
    return response.text
