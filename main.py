while True:
    user_action = input("Type add, show, edit, complete or exit : ")
    user_action = user_action.strip()   # cut the spaces after the input

    match user_action:
        case 'add':
            todo = input("Enter a todo : ") + "\n"

            # creating a file object & open read mode of the text file
            file = open('todos.txt', 'r')
            todos = file.readlines()
            # read the content in the file & it will create a list with that content
            # (each line will be an item of that list)
            file.close()

            todos.append(todo)
            # append the users item in that list

            # create a new file by overriding the existing file and in that file write that list
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index+1}-{item.capitalize()}"  # f"string" - to manage the spaces between number and item
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number -= 1
            new_todo = input("Enter new todo : ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number-1)
        case 'exit':
            break

print("Bye!")