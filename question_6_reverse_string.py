# This code contains errors that you need to fix it. Read carefully and do necessary corrections.
# Run the code at online-python.com or IDLE PYTHON before you commit the changes at github.com

# This program is used to reverse a string.

def string_reverse(str1):
    rstr1 = ''
    
    # Calculate the length of the input string 'str1'
    length = len(str1) 
    
    # Execute a while loop 
    index = length - 1
    while index > =0:
        # Concatenate the character of 'str1' to 'rstr1'
        rstr1 += str1[index]
        
        # Decrement the 'index' by 1 for the next iteration
        index -= 1
    
    # Return the reversed string stored in 'rstr1'
    return rstr1

def main():    
    print("String reverse for \'12345abcde\' is", string_reverse(str1))

# Don't change the code below!
if __name__ == "__main__":
    main()
