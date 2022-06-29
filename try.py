def problem():
    # function ask and store user problem
    main_problem = input('Tell me what is the problem? \n')
    return main_problem


def decisions(list_of_decisions):
    # function that ask user about possible decisions
    while True:
        decision = input('Enter your possible decision: \n')
        print("Type 'quit' if you are done with decisions")
        if decision == 'quit':
            break
        list_of_decisions.append(decision)


def steps(solution, list_of_steps):
    # creating steps for each decision
    print('Your solution is ' + solution + '.')
    while True:
        step = input('Enter step of a problem displayed above: \n'
                     '(if you are done type "quit") \n'
                     ': ')
        if step.lower() == 'quit':
            break
        else:
            list_of_steps.append(step)




print('This is decision tree program')
# calling problem function
user_problem = problem()
# calling decision function
decisions_list = []
decisions(decisions_list)
x = -1

list_of_steps_for_decision = []
for item in decisions_list:
    steps(item, list_of_steps_for_decision)
print(list_of_steps_for_decision)
