"""
range_of_i = 5
for i in range(0, range_of_i, 1):
    for j in range(0, range_of_i -i, -1):
        print('*', end='') 
    print('')
"""

"""
n = 7.0

if(n % 2 == 0):
    False
else:
    for i in range(0, int(n/2),1):
        for j in range(0, int(n/2)- i , 1):
            print(' ')
        if(i == int(n/2)):
            print('*')
        for j in range(int(n/2), int(n/2)+i, 1):
            print(' ', end='')
"""           

n = 7.0

for i in range (0, int(n/2) + 1, 1):
    for j in range(0, int(n/2) - i, 1):
        print(' ', end='')
    for j in range(0, i+1, 1):
        print('*', end='')
    for j in range(int(n/2), int(n/2) + i, 1):
        print('*', end='')
    print('')
    
for i in range (0, int(n/2), 1):
    for j in range(0, i+1, 1):
        print(' ', end='')
    for j in range(0, int(n/2) - i, 1):
        print('*', end='')

    
    
"""
for(int i = 0; i < n/2; i++)
{
    for(int j = 0; n/2 - i ; j++)
    {
        std::cout << " ";
    }
    for(int j = 0; j < i + 1 ; j++)
    {
        std::cout << "*";
    }
    std::cout << std::endl;
}
    
    
    
"""
        
        

    