from projeto_atas.usuarios import Usuario
from projeto_atas.ata import Ata

import os


class Menu:
	@staticmethod
	def menu(lista_usuarios, lista_atas):
		while True:
			Menu.limpar_tela()
			print('''
					Sistema de Gestão de Atas
					 1 - Cadastrar Usuários	
					 2 - Atualizar usuários
					 3 - Listar usuários
					 4 - cadastrar atas
					 5 - Atualizar atas
					 6 - Listar atas
					 7 - Sair''')
			opcao = input("Opção: ")

			if opcao == '1':
				Menu.cadastrar_usuarios(lista_usuarios)
			elif opcao == '2':
				pass
			elif opcao == '3':
				Menu.listar_usuarios(lista_usuarios)
			elif opcao == '4':
				Menu.cadastrar_atas(lista_atas)
			elif opcao == '5':
				pass
			elif opcao == '6':
				Menu.listar_atas(lista_atas)
			elif opcao == '7':
				Menu.limpar_tela()
				print("Obrigado por usar o sistema")
				break
			else:
				print("Opção inválida!!")
				Menu.pegar_tecla('Tecle Enter para continuar...')
				Menu.limpar_tela()

	@staticmethod
	def cadastrar_usuarios(lista):
		Menu.limpar_tela()
		print("Cadastro de usuários")
		# matricula, nome, tipo (leitor ou redator), email (CRUD)
		matricula = int(input('Matrícula: '))
		nome = input('Nome: ')
		nome = nome.upper()
		while True:
			t = input('R - Redator; L - Leitor: ')
			t = t.upper()
			if t == 'R':
				tipo = 'Redator'
				break
			elif t == 'L':
				tipo = 'Leitor'
				break
			else:
				print("Escolha R ou L!!")

		email = input('Email: ')
		lista.append(Usuario(matricula, nome, tipo, email))
		print('Usuário %s cadastrado com sucesso' % (lista[-1]))
		Menu.pegar_tecla('Tecle Enter para continuar...')

	@staticmethod
	def listar_usuarios(lista):
		Menu.limpar_tela()
		print("Listagem de usuários")
		for i in lista:
			print(i)

		Menu.pegar_tecla('Tecle Enter para continuar...')

	@staticmethod
	def limpar_tela():
		os.system("cls")

	@staticmethod
	def pegar_tecla(texto):
		a = input(texto).split(" ")[0]


	@staticmethod
	def cadastrar_atas(lista):
		Menu.limpar_tela()
		print("Cadastro de Atas")
		# numero, data, hora, local e pauta (CRUD)
		numero = int(input('Número: '))
		data = input('Digite a data: ')
		hora = input('Digite a hora: ')
		local = input('Digite o local: ')
		pauta = input('Digite a pauta da Ata: ').upper()

		lista.append(Ata(numero, data, hora, local, pauta ))
		print(f'Ata {lista[-1]} cadastrada com sucesso')
		Menu.pegar_tecla('Tecle Enter para continuar...')

	@staticmethod
	def listar_atas(lista):
			Menu.limpar_tela()
			print("Listagem de Atas")
			for i in lista:
				print(i)

			Menu.pegar_tecla('Tecle Enter para continuar...')