todos = []

while True:
    user_action = input("Type add, show, edit or exit : ")
    user_action = user_action.strip()   #cut the spaces after the input

    match user_action:
        case 'add':
            todo = input("Enter a todo : ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index}-{item}"  # f"string" - to manage the spaces between number and item
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number -= 1
            new_todo = input("Enter new todo : ")
            todos[number] = new_todo
        case 'exit':
            break

print("Bye!")