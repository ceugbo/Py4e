def translate(phrase):
    translation = ""
    for item in phrase:
        if item in "aeiou":
            translation = translation + "g"
        elif item in "AEIOU":
            translation = translation + "G"
        else:
            translation = translation + item
    return translation
print(translate(input("Enter a phrase: ")))