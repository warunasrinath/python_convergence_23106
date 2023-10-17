# def increment_numbers(input_string1, k):
 
#     words=input_string1.split()   
#     modified_words=[]

#     for word in words:
#         if word.isnumeric():
#             modifiedword=str(int(word) + k)
    
#         else:
#             modifiedword=word

#         modified_words.append(modifiedword)
    
#     result_string=''.join(modified_words)

#     return result_string
    
# input_string1 = input('Enter a String:')
# k=int(input('Enter a K value:'))

# result = increment_numbers(input_string1, k)
# print('Modified code: ',result)

def increment_numbers(input_string, k):
    words = input_string.split()   
    modified_words = []

    for word in words:
        if word.isnumeric():
            modified_word = str(int(word) + k)
        else:
            modified_word = word

        modified_words.append(modified_word)
    
    result_string = ' '.join(modified_words)
    return result_string

input_string = input('Enter a String:')
k = int(input('Enter a K Number:'))

result = increment_numbers(input_string, k)
print('Modified code:', result)

