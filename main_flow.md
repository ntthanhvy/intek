# MAIN FLOW
## In this note I will cover some main flow of the shell project

```
def main():
	print('intek-sh$', end=' ')
	while True:
		input = input()
		commands = parse_input(input)
```
### *Input should be parse follow these rules:*
+ When the input is key_UP or key_DOWN, the history is call to navigate between commands was call. Ex:
```
	intek-sh$  echo abc
	abc
	intek-sh$  ^[[A  # this is key_UP
	intek-sh$  echo abc
```
+ When the key_LEFT or key_RIGHT is pressed, should move the cursor backward or forward. Ex:
```
	intek-sh$  cat file.sh|  # the cursor is at the end if the line
	intek-sh$  ^[[D^[[D  # the key_LEFT is pressed twice
	intek-sh$  cat file.|sh  # the cursor should move the right of the '.'
```
+ When there are any signals from keyboard while previous command is running are pass to input, should handle the signal properly. Ex:
	+ Key press for Ctrl+C or Ctrl+Z or Ctrl+D: all this signal should stop running command and displpay the signal or error that occur when input is pass.
	+ ...
+ Priority when handle command from input:
	+ If there are any mark that seperated command (|, &&, ||, <, >, <<, >>): seperate the input by these marks first.
	+ Handle the (`) mark that call another command inside a command. Ex:
			`intek-sh$  echo "it is `echo $?` then"`
		This will first do the 'echo $?' command then pass the output to the 'echo' command outside.
	+ 
