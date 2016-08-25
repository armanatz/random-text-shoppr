import random
import string
import os

### FUNCTIONS ###

# let's define a function for creating a string of random alphanumerical characters
def random_alphanumerics():
    length = random.randint(5, 30) # define the length of the alphanumeric string randomly between a range
    output = ''
    for i in range(length):
        output += random.choice(string.ascii_lowercase + string.digits) # create our alphanumeric string
    x = random.randint(0, 9) # the whitespaces before shouldn't be more than 9
    y = random.randint(0, 9) # the whitespaces after shouldn't be more than 9
    output = ' '*x + output + ' '*y # put them altogether
    return output

# let's define a function for creating a string of random alphabetical characters
def random_string():
    length = random.randint(5, 30) # define the length of the alphabetical string randomly between a range
    output = ''.join(random.choice(string.ascii_lowercase) for x in range(length)) # we are using ascii lowercase so that encoding doesn't cause our file size to be unpredictable
    return output

# let's define a function for creating a random integers and converting them to a string
def random_int():
    output = random.randint(0, 10000)
    intToStr = '{}'.format(output)
    return intToStr

# let's define a function for creating random floats and converting them to a string
def random_float():
    length = random.randint(1, 10) # let's make sure the float is between a randomly chosen decimal place
    output = round(random.uniform(0.0, 10000.0), length)
    floatToStr = '{}'.format(output)
    return floatToStr

### time to write to our file!!! ###

# let's define our file name first
fileName = 'output_file.txt'

# we shall create and open our file
open(fileName, 'w')

# let's check the initial size of the file which should be 0
fileSize = os.stat(fileName).st_size

# alright let's open the file and append data to it
with open(fileName, 'a') as myFile:
    print('Random data write has started in ' + fileName + '...')
    while fileSize < 10485760: # run the loop until fileSize is 10485760 bytes which should be shown as 10MB in any OS but in reality it is 10.48MB in actuality
        function_list = [random_alphanumerics, random_string, random_int, random_float] # put our functions into a list
        dataType = random.choice(function_list) # randomly choose a function to run
        output = dataType()
        myFile.write(output + ', ')
        fileSize += len(output) + 2
    # once loop is done, print final file size and close file
    print('Final file size:', fileSize / 1000000, 'MB')
    myFile.close()
