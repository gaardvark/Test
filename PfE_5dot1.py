# Average of Numbers Entered at Prompt: Python for Everyone Exercise 5.1

import sys

iteration_cycle = 0
total_sum = 0

print '\n\n\n\n\n\nWelcome to AVERAGE OF NUMBERS ENTERED.'
print '\nThis program computes and returns the average of numbers entered. Type "done" to return the result.'

prompt = raw_input('\nPlease enter a number: ')

if prompt == 'done':
    print '\nWell, why\'d you open me in the first place?\n\n'
    sys.exit()

while prompt != 'done': 
    try: 
        prompt = float(prompt)
    except:
        print 'Bad input'
        prompt = raw_input('Please enter a number: ')
        continue
    iteration_cycle += 1
    total_sum += prompt
    prompt = raw_input('Please enter a number: ')
    
average = str(total_sum/iteration_cycle)

print '\n\nThe average of numbers entered is:', average
print '\n'

