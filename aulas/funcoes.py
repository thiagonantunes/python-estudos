def clients(client, lista=None):
    if lista is None:
        lista = []
    lista.extend(client)
    return lista

clientes1 = clients(['Thiago', 'Simone', 'Otto'])
clientes2 = clients(['Fábio', 'Josi', 'Sofia', 'Giulia'])

print(clientes1)
print(clientes2)



def show_op(todo_list):
    print()
    print('Tarefas: ')
    print(todo_list)
    print()

def do_undo(todo_list, undo_list):
    if not todo_list:
        print('Nada a fazer')
        return
    last_todo = todo_list.pop()
    redo_list.append(last_todo)

def do_redo(todo_list, redo_list):
    if not redo_list:
        print('Nada a fazer')
        return
    last_redo = redo_list.pop()
    todo_list.append(last_redo)

def do_add(todo, todo_list):
    todo_list.append(todo)


# Progrma principal
if __name__ == '__main__':
    todo_list = []
    redo_list = []

  while True:
        todo = input('Tarefa, undo, redo ou lista: ')

    if todo == 'lista':
        show_op(todo_list)
        continue
    elif todo == 'undo':
        do_undo(todo_list, redo_list)
        continue
    elif todo == 'redo':
        do_redo(todo_list, redo_list)
        continue
    
    do_add(todo, todo_list)
    