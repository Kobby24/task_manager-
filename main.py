import json
from datetime import datetime
from pprint import pprint

print('Task Manager App')


def exit__():
    print('Done for today')
    return None


def error_():
    print('Invalid Input')
    begin()


def begin():
    user_input = input('Whats on you mind today?\n'
                       '1.Add a new task\n'
                       '2.Update a task\n'
                       '3.Delete a task\n'
                       '4.List my tasks\n'
                       '5.Exist\n')
    try:
        user_input = int(user_input)

    except ValueError:
        error_()

    else:
        if user_input == 1:
            add()
        elif user_input == 2:
            update()
        elif user_input == 3:
            delete_task()
        elif user_input == 4:
            list_task_input()
        elif user_input == 5:
            exit__()
        else:
            error_()


def list_task(n):
    if n == 5:
        begin()
    elif n == 6:
        exit__()
    else:
        if 0 < n <= 4:
            try:
                with open('data.json', 'r') as f:
                    data = json.load(f)
            except FileNotFoundError:
                print("There is No Task yet")
                add()
                list_task_input()
            else:
                if n == 1:
                    #list ALL TASK

                    if len(data) == 0:
                        print('There are no tasks')
                    else:
                        print(f'Here are all your tasks')
                        pprint(data, sort_dicts=False)
                elif n == 2:
                    #list task that are done

                    data_ = [data[i] for i in data.keys() if data[i]['status'] == 'done']
                    if len(data_) == 0:
                        print('There are no tasks that are done')
                    else:
                        print('Here are the tasks which have been completed')
                        pprint(data_, sort_dicts=False)
                elif n == 3:
                    #list task that are not done

                    data_ = [data[i] for i in data.keys() if data[i]['status'] == 'todo']
                    if len(data_) == 0:
                        print('There are no tasks todo')
                    else:
                        print("Here are the tasks todo")
                        pprint(data_, sort_dicts=False)
                elif n == 4:
                    #list task that are in progress
                    data_ = [data[i] for i in data.keys() if data[i]['status'] == 'in-progress']

                    if len(data_) == 0:
                        print('There are no tasks that are in-progress')
                    else:
                        print("Here are the task which are still in-progress")
                        pprint(data_, sort_dicts=False)

        else:
            error_()


def list_task_input():
    list_input = input('List Menu '
                       '\n1.List all task '
                       '\n2.List tasks that are done '
                       '\n3.List task that are not done '
                       '\n4.List task that are in progress '
                       '\n5.Main Menu'
                       '\n6.Exist\n')
    try:
        list_input = int(list_input)
    except ValueError:
        error_()

    else:
        return list_task(list_input)


def add():
    add_input = input('What is the new task\n').title()
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
        last_task = int(list(data.keys())[-1][-1])
        last_task += 1
    except:
        last_task = 1

    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        with open('data.json', 'w') as file:
            d = {
                last_task: {
                    'title': add_input,

                    'createdAt': f'{datetime.now().date()} at {datetime.now().strftime("%H:%M")}',
                    'updatedAt': f'{datetime.now().date()} at {datetime.now().strftime("%H:%M")}',
                    'status': 'todo'
                }
            }
            json.dump(d, file, indent=4)

    else:
        data[last_task] = {
            'title': add_input,
            'createdAt': f'{datetime.now().date()} at {datetime.now().strftime("%H:%M")}',
            'updatedAt': f'{datetime.now().date()} at {datetime.now().strftime("%H:%M")}',
            'status': 'todo'
        }

        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
    finally:
        print("Task Added Successfully")
    #add it to the json file


def get_tasks():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("There is No Task yet")
        add()
        get_tasks()
    else:
        keys = list(data.keys())
        tasks = {i: data[i]['title'] for i in keys}
        if len(tasks) == 0:
            print("There is No Task yet")

            begin()
            return False

        else:
            pprint(tasks, sort_dicts=False)
        return True


def update():
    #list all tasks
    if get_tasks():
        update_input = input('Which task needs an update\n')
        try:

            with open('data.json', 'r') as f:
                data = json.load(f)
            data_ = data[update_input]


        except:
            error_()
        else:
            user_decison = input('What Do You What To Update\n'
                                 '1.Title\n'
                                 '2.Status\n'
                                 '3.Title and Status\n'
                                 '4.Main Menu\n'
                                 '5.Exist')
            try:
                user_decison = int(user_decison)
            except ValueError:
                error_()
            else:
                if user_decison == 4:
                    begin()
                elif user_decison == 5:
                    exit__()
                else:
                    if 0 < user_decison <= 3:
                        if user_decison == 1:
                            new_title = input('Enter the new title\n').title()
                            data_['title'] = new_title
                            data_['updatedAt'] = f'{datetime.now().date()} at {datetime.now().strftime("%H:%M")}'
                        elif user_decison == 2:
                            new_status = input('Enter the new status\n 1.todo \n2.done  \n3.in-progress\n')
                            status = ['todo', 'done', 'in-progress']
                            try:
                                new_status = int(new_status) - 1
                                if 3 > new_status >= 0:
                                    data_['status'] = status[new_status]
                                    data_['updatedAt'] = f'{datetime.now().date()} at {datetime.now().strftime("%H:%M")}'
                                else:
                                    error_()
                            except ValueError:
                                error_()
                        elif user_decison == 3:
                            new_title = input('Enter the new title\n').title()
                            data_['title'] = new_title
                            new_status = input('Enter the new status\n 1.todo \n2.done  \n3.in-progress\n')
                            status = ['todo', 'done', 'in-progress']
                            try:
                                new_status = int(new_status) + 1
                                if 3 > new_status >= 0:
                                    data_['status'] = status[new_status]
                                    data_['updatedAt'] = f'{datetime.now().date()} at {datetime.now().strftime("%H:%M")}'
                                else:
                                    error_()
                            except ValueError:
                                error_()
                    else:
                        error_()
            finally:
                with open('data.json', 'w') as f:
                    json.dump(data, f, indent=4)
                print('Task Successfully Updated')

    #update it in the jason file


def delete_task():
    #list all tasks
    if get_tasks():
        delete_input = input('Which task needs to be deleted\n')
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
            task = data[delete_input]['title']
            data.pop(delete_input, None)
        except:
            error_()
        else:
            data = {str(i + 1): value for i, value in enumerate(data.values())}
            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)

            print(f'{task} has been deleted')


begin()
