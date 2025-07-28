# Task 1: Diary
try:
    with open('diary.txt', 'a') as file:
        system_prompt = 'What happened today? '
        user_output = ''
        while True:
            user_output = input(system_prompt)
            if user_output == 'done for now':
                break
            file.write(user_output + '\n')
            system_prompt = 'What else? '
            user_output = ''

except Exception as e:
    print(f"An exception occurred {e}")
else:
    print("Diary was updated!")
