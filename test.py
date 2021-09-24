import pytest
import user

# First test.
# Add user, get user info and compare them.
def test_addUser():
    user.createUser('userlogin', 'useremail@gmail.com', 'userpassword')
    userInfo = user.getUser('userlogin')
    assert userInfo['login'] == 'userlogin' and userInfo['email'] == 'email'

# Second test.
# Update user info, get user info and compare them.
def test_updateUser():
    user.updateUser('userlogin2', 'useremail2@gmail.com', 'userpassword2')
    userInfo = user.getUser('userlogin2')
    assert userInfo['login'] == 'userlogin2' and userInfo['email'] == 'email2'