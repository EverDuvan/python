
def es_palindromo():
    word = "ama"
    if word == word[::-1]:
        print(word[::-1] + " es palindromo")
    else:
        print("no es palindromo")

es_palindromo()