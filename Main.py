from Tarefa import Tarefa
from Usuario import Usuario
from Gerenciar import Gerenciar
import json

nome=str(input('Digite o nome do usuario:'))
usuario=Usuario(nome)
usuario.carregar_tarefas()
usuario.listar_tarefas()

while True:
    print('GERENCIAR TAREFAS\n')
    print('1-Adicionar tarefa\n2-Listar tarefas\n3-Concluir tarefa\n4-Remover tarefa\n5-Sair')
    opcao=input('Digite a opção:')
    if opcao=='1':
        titulo=str(input('Titulo da tarefa:'))
        descricao=str(input('Descrição da tarefa:'))
        prazo=input('Prazo(DD-MM-AAAA) ou deixe vazio:')
        prazo=prazo if prazo.split() else None
        
        tarefa=Tarefa(titulo,descricao,prazo)
        usuario.adicionar_tarefa(tarefa)
        print('Tarefa adicionada com sucesso!')
        
    elif opcao=='2':
        print(f'Tarefas de {usuario._nome}')
        usuario.listar_tarefas()
        
    elif opcao=='3':
        usuario.listar_tarefas()
        indice=int(input('Qual tarefa deseja concluir?'))
        if 0<indice<=len(usuario._tarefas):
            usuario._tarefas[indice - 1].concluir()
            usuario.salvar_tarefas()
            print('Tarefa concluida!')
        else:
            print('Número de tarefa não existe')
    
    elif opcao=='4':
        usuario.listar_tarefas()
        indice=int(input('Qual tarefa deseja remover?'))
        if 0<indice<=len(usuario._tarefas):
            removida=usuario._tarefas.pop(indice - 1)
            usuario.salvar_tarefas()
            print(f'Tarefa {removida._titulo} removida com sucesso')
        else:
            print('Número de tarefa não existe')
    
    elif opcao=='5':
        print('Saindo do programa...')
        break
    
    else:
        print('Número inválido!')

