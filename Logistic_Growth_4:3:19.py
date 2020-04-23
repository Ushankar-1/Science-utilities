import random
import time

#Logistic Growth: AP Biology chapter 40.
#I'm only doing this so I can get the concept really really well. No better
# way to learn something inside and out than to create it.
#Also, it seemed fun.

print('Logistic Growth: Chapter 40 of AP Biology.\n')
time.sleep(1.5)
print('This program simulates the logistic growth of a population, given the\n'
      'proper parameters.\n')
time.sleep(1.5)
o = input('Please enter the plural name of an organism.\n'
          'Leave blank to use a generic organism. ')
o = o.lower()
if o == '':
    o = 'Mendaliens'



time.sleep(1.5)
N = int(input('\nHow large do you want your initial population to be?\n'
              'Respond with "0" for a randomized number. '))
while N < 0 or N > 10000:
    N = int(input('Please enter a natural, nonzero integer less than 10,000. '))
if N == 0:
    i = random.randint(2,10000)
    N = i


    
time.sleep(1.5)
K = int(input('\nWhat do you deem to be the carrying capacity of the environment?\n'
              'I would not advise values significantly lower than your initial\n'
              'population. Respond with "0" for a randomized number. '))
while K < 0 or K > 10000000:
    K = int(input('Please enter a natural, nonzero integer less than 10,000,000. '))
if K == 0:
    i = random.randint(1,10000000)
    K = i



time.sleep(1.5)
r = float(input('\nWhat is the growth rate of your chosen species? I would not\n'
          'advise values under 0.1 or over 5.\nRespond with "0" for a randomized number. '))
while r < 0 or r > 100:
    r = int(input('Please enter a natural, REASONABLE nonzero integer. '))
if r > 10:
    time.sleep(2)
    print('\nOkay, I guess... You do know your head\'s going to explode, right?\n')
    time.sleep(1.5)
if r == 0:
    i = random.randint(1,30)
    r = i/10

print('\n\n\n')

time.sleep(1.5)
print('You are simulating a population of',N,o,'that reproduce at\n'
      'a rate of',r,'per capita, in an environment with a carrying capacity\n'
      'of roughly',K,o,'.\n')


time.sleep(1.5)
t = int(input('What number of some arbitrary unit of time do you want to check in\n'
          'on this population after? Respond with "0" for a randomized number. '))
while t < 0 or t > 1000:
    t = int(input('Please enter a natural, nonzero integer less than 1,000. '))
if t == 0:
    i = random.randint(1,1000)
    t = i


i = 0

    
time.sleep(1.5)
if t <= 50:
    print('Here\'s your simulation:')

    while i != (t + 1):
        if i == 0:
            pop = N
        else:
            pop = int(N + (r*N*(K - N)/K))
        if pop < 0:
            
            print('\n')
            time.sleep(3)
            print('...')
            
            time.sleep(1)
            print('\n')
            time.sleep(1)
            print('\n')
            time.sleep(1)
            print('\n')
            print('...?!?!?!?!?')
            time.sleep(6)
            print('\n\n\n...And the population went NEGATIVE.')
            time.sleep(3)
            print('\nCongrats. You broke it.')
            time.sleep(2)
            print('\nShouldn\'t have had such a high growth rate or a\n'
                  'carrying capacity significantly lower than the initial\n'
                  'population, I guess.')
            time.sleep(2.5)
            break
        elif pop >= 0:
            print('\nAt time',i,': Population of',pop,)
            N = pop
            i +=1

elif t > 50:
    time.sleep(2)
    print('...Okay I\'m not printing all of THAT.')
    while i != (t + 1):
        if i == 0:
            pop = N
        else:
            pop = int(N + (r*N*(K - N)/K))
        N = pop
        i +=1

    time.sleep(2)
    print('At arbitrary unit of time',t,', there are',pop,o,'.')

input('\nPress the "enter" key to exit.')


#Pseudocode:
#Choose an organism, carrying capacity, and existing population.
#   include options for randomly generating these.
#Choose between finding how many of X organism there are after Y units of time,
# and finding how much of X there is up to and including Y.
