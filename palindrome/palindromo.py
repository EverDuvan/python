
def es_palindromo():
    word = "ama"
    if word == word[::-1]:
        print(word[::-1] + " es palindromo")
    else:
        print("no es palindromo")

es_palindromo()

# args y kwargs

def test(*args, **kwargs):
    # print(ini)
    # print(fds)
    print(args)
    print(kwargs)


b= {'f': 't', 'y': 'i'}
test(**b)