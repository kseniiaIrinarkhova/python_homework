#import libs

import traceback

# Task 1: Diary
try:
    #open or create file
    with open('diary.txt', 'a') as file:
        #system prompt for initial command line
        system_prompt = 'What happened today? '
        # user output
        user_output = ''
        #loop until user provide special command
        while True:
            #get user output
            user_output = input(system_prompt)
            #break the loop if user commanded
            if user_output == 'done for now':
                break
            #add user's output to file
            file.write(user_output + '\n')
            #change system prompt
            system_prompt = 'What else? '
            # refresh user output
            user_output = ''

except Exception as e:
    #print type of exception
    print(f"An exception occurred {type(e).__name__}")
    # get and print exception message
    message = str(e)
    if message:
        print(f'Exception message: {message}')
    #trace back exception
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    #create a stack of commands
    for trace in trace_back:
        stack_trace.append(f'File: {trace[0]}, Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    #print stack of commands from exception
    print(f"Stack trace: {stack_trace}")
else:
    print("Diary was updated!")
