words= ['Sky','Apple','Rythm','Fly','Orange']
for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f" '{word}' contains the vowel '{letter}'")
            break
        else:
            print(f"'{word}' has no vowels")
