import requests
import random
import string

def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

a = "Hey" 
chars = a + ' ' + string.ascii_letters 
size = 10


payload = {
   'content': random_string_generator(size, chars)
   
    }




header = { 
     'authorization': '*' #Authorization ID of your Account
    
    }
for i in range (0,10):
    r =requests.post('*',data=payload, headers=header) #Channel request link 
    
