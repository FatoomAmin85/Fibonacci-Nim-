import random
num1=0
player1=True
num2=560
coins=int(input("enter the number of coins: "))
num1=int(input("player1:enter a number less than  the number of coins"))
while num1>coins:
	num1=int(input("player1:enter another nomber"))
coins=coins-num1
player1=False
def game(player1,coins,num2,num1):
	if player1 == True:
		print("coins  is",coins)
		num1=int (input("player1: enter a number: "))
		while num1> coins or num1>(2*num2):
			num1=int(input("enter another number: "))
		coins-=num1
		player1=False
		winner(player1,coins,num2,num1)
	else:
		 print("coins is",coins)
		 num2=int (input("player2: enter a number: "))
		 while num2> coins or num2>(2*num1):
		 	num2=int(input("player2: enter another number: "))
		 coins-=num2
		 player1=True
		 winner(player1,coins,num2,num1)
		 
		 	
def winner(me,coins,c,num1):
		if coins==0 and me==True:
			print("player2 won the game")
			return 
			
		elif coins==0 and me==False:
			print("player1 won the game")
			return
		else:
		    game(me,coins,num2,num1)		
game(player1,coins,num2,num1)