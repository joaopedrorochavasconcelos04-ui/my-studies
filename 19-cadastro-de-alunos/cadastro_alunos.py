resposta = ""
cadastro = {}

while resposta != "4":
    print('''
      
  =======  Sistema de cadastro de Alunos =======
      
      1 - Cadastrar Aluno/Nota do aluno
      2 - Ver os alunos
      3 - Ver notas dos alunos              
      4 - Sair
      
      ''')
    
    resposta = input("Escolha uma opção: ")

    if resposta == "1":
        print('''

======== Adicionar Aluno/Nota ========
                          
   1 - Adicionar Aluno
   2 - Adicionar Nota                   

''')

        add_aluno_opcao = input("Escolha uma opção: ")

        if add_aluno_opcao == "1":
            nome = input("Digite o nome do aluno: ")

         
    elif resposta == "2":

        for aluno in cadastro:
            print(aluno)