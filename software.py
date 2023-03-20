import cmd
from riposte import Riposte
import time
import sys
import pandas as pd
pd.options.display.max_rows=999999


BANNER= """

list of commands: \n 1. Display all records \n 2. Test 2 \n 3. Test 3 \n 0. Exit

"""
Command = Riposte(prompt="Superstore:-$ ", banner=BANNER)

def delay_print(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.03)

@Command.command("1")
def DisplayAll():
	df = pd.read_csv('Sample - Superstore.csv', encoding='windows-1252')
	new_df = df.dropna()
	print(new_df.to_string())

@Command.command("2")
def test2():
	print("test 2")

@Command.command("3")
def test3():
	print("test 3")

@Command.command("0")
def exit():
	sys.exit(0)

Command.run()
