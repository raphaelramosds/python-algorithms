import random
import os
import msvcrt


def valor(tamanho,tentativas):
	pts = 0
	print("\n")
	

	matriz = [['X']*tamanho]*tamanho 
	
	for i in range(len(matriz)): 
		for j in range(len(matriz[i])): 
			print(matriz[i][j],end="    ")
		print("\n")

	auxiliar = tentativas
	

	colSwitch = random.randint(0,len(matriz[0])-1)  
	lineSwitch = random.randint(0,len(matriz[0])-1) 

	print(lineSwitch,colSwitch)

	while auxiliar > 0:
		userLine = int(input("Linha: "))
		userCol = int(input("Coluna: "))

		print("\n")

		if pts == 0 and userLine == lineSwitch and userCol == colSwitch:
			pts += 30
			print("30pts")
			print("\n")
			break
			
		elif userLine == lineSwitch and userCol == colSwitch:
			pts += 10
			print("10 pts")
			print("\n")
			break

		elif userLine < 0 or userLine > len(matriz) or userCol < 0 or userCol > len(matriz): 
			auxiliar -= 1
			pts -= 10
			print("-10 pts")
			print("\n")
		
		elif userLine in range(lineSwitch-1,lineSwitch+1):
			pts += 5
			auxiliar -= 1
			print("Chegou perto, +5pt")
			print("\n")
		
		elif userLine == lineSwitch and userCol != colSwitch:
			pts +=1
			auxiliar -= 1
			print("Acertou a linha, mas errou. -1pt")
			print("\n")
			
		elif userCol == colSwitch and userLine != lineSwitch:
			pts +=1
			auxiliar -= 1
			print("Você acertou a coluna, mas errou. -1pt")
			print("\n")

		else:
			pts += 1 
			auxiliar -=1
			print("Errou...")
			print("+1 pt")
			print("\n")
			
	print("Voce obteve: " + str(pts) + " pontos!")
	opcao = input("Deseja jogar novamente nessa dificuldade?(S/N)")
	aux = opcao.upper()

	if aux == 'S' and tamanho == 3:
		os.system("cls")
		valor(3,5)
	elif aux == 'S' and tamanho == 5:
		os.system("cls")
		valor(5,3)
	elif aux == 'S' and tamanho == 8:
		os.system("cls")
		valor(8,2)

def interface():

	print("Dificuldade: ")
	print("1 - Fácil")
	print("2 - Médio")
	print("3 - Difícil")
	print("4 - Sair")
	
	opcao = int(input(""))
	
	if opcao == 1:
		print("5 tentativas")
		valor(3,5) 
			
	elif opcao == 2:
		print("3 tentativas")
		valor(5,3)
			
	elif opcao == 3:
		print("2 tentativas")
		valor(8,2)

	elif opcao == 4:
		exit()

	opcao2 = input("Voltar ao menu? (S/N)")
	opcao3 = opcao2.upper()

	if opcao3 == 'S':
		os.system("cls")
		interface()
	else:
		os.system("cls")
		print("Bye")
		msvcrt.getch()
		
interface()
