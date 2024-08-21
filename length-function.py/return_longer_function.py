def get_longer_word(word1:str , word2:str)->str:
    if len(word1) > len(word2):
        return word1
    
    elif len(word1) == len(word2):
        return "both are same"
    
    else:
        return word2
        
    

print('Hello mom')



print(get_longer_word('yellow' , 'yellow'))