list(range(3, 6))            # normal call with separate arguments

args = [3, 6]
			     # call with arguments unpacked from a list
print(list(range(*args)))

def parrot(voltage : str, state='a stiff', action='voom'):
	print("-- This parrot wouldn't", action, end=' ')
	print("if you put", voltage, "volts through it.", end=' ')
	print("E's", state, "!")
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
