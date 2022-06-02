
# Decision Tree Project
list_count = []
list_numb = ['first', 'second', 'third']
x = -1
y = -1
z = -1
output = ''
dec_count = 0
decisions_list = []
steps = [[]]
print('This is decision tree program')
problem = input('Tell me what is the problem? \n')
another_option = 'y'
end = 0
while another_option == 'y':
    if another_option.lower() != 'y':
        pass

    else:
        decisions = input('Enter your possible decision: \n')
        decisions_list.append(decisions)
        another_option = input('Do you have another option?(y or n): ')

print('\n Now we will define steps for each solution')
for item in decisions_list:
    x = x + 1
    print('Your ' + str(list_numb[x]) + ' problem is ' + item)
    while step.lower() != 'break':
        z = z + 1
        while True:
            step = input('Enter step of a problem displayed above: \n'
                         '(if you are done type "break") \n'
                         ': ')
            if step.lower() == 'break':
                break
            else:
                steps[z].append(step)


for decision_1 in decisions_list:
    y = y + 1
    print('Decision :' + decision_1 + 'require ' + str(list_count[y]) + ' steps, which is : ')
    for each_step in steps:
        print(each_step)



