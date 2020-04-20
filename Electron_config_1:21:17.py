import time

#orbital values
s = 2
p = 6
d = 10
f = 14
#stop the loop variable
stopit = 0
#counter variables: L is for list position, C is for number
L = 0
C = 0

def return_value(L):
    ''' Returns the number of electrons in a certain orbital. '''
    if L == 0 or L == 1 or L == 3 or L == 5 or L == 8 or L == 11 or L == 15:
        return int(s)
    
    if L == 2 or L == 4 or L == 7 or L == 10 or L == 14 or L == 18:
        return int(p)
    
    if L == 6 or L == 9 or L == 13 or L == 17:
        return int(d)
    
    if L == 12 or L == 16:
        return int(f)
    if L >= 19:
        return int(stopit)
    
orbitals = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
num = int(input('What is your element\'s atomic number? '))

while num > 118 or num == 0 or num < 0 :
    if num > 118:
        num = int(input('\nThat element has not been discovered yet,\n'
                    'or does not exist. Try again. '))
    if num == 0:
       num = int(input('\nThat doesn\'t exist. Try again. '))
    if num < 0:
        num = int(input('\nAssuming that you\'re talking about antimatter,\n'
                        'I don\'t know how to do that. Yet. '))
        
print('Your element\'s electron configuration is:')

while num >= return_value(L):
    if L >= 19:
        break
    print(orbitals[L],return_value(L))
    num -= return_value(L)
    L += 1
    time.sleep(1)
    
if num != 0:
    print(orbitals[L],num)
    
time.sleep(2)

print('That\'s all.')



    
    


        

    
      
