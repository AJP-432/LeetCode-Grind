def my_func(s):
    words, current_longest = [], ""
        
    for i in range(len(s)): 

        for word in words: 
            word += s[i]
            if word == word[::-1] and len(word) > len(current_longest): 
                current_longest = word

        words.append(s[i])

    return current_longest

    

print(my_func("racecar"))