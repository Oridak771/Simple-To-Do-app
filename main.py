from functions import get_todos, write_todos
import time

now = time.strftime('%I:%M %p')
print("it is:", now)
while True:
    user_input = input("Type add, show, edit, delete or exit :")
    user_input = user_input.strip()

    if user_input.startswith('add'):
        todo = user_input[4:] + '\n'
        todos = get_todos()

        todos.append(todo)

        write_todos( todos,)

    elif user_input.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}.{item}")

    elif user_input.startswith('edit'):
        try:
            num = int(user_input[5:]) - 1
            todos = get_todos()

            edited_todo = input("enter the new todo:")
            todos[num] = edited_todo + '\n'

            write_todos( todos,)
        except ValueError:
            print("not valid command")
            continue


    elif user_input.startswith('delete'):
        try:
            number = int(user_input[7:])
            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index]. strip('\n')
            todos.pop(index)

            write_todos( todos,)
            message = f"XXX Todo: {todo_to_remove} was removed from the list XXX"
            print(message)
        except IndexError:
            print('no item with that number in the list')

    elif user_input.startswith('exit'):
        break

    else:
        print("not valid command ")



print('end.....')

