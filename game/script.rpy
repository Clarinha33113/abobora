define me = Character("[my_name]")
define vince = Character("Vince")
define clint = Character("Clint")
define aisha = Character("Aisha")
define sofia = Character("Sofia")
define thiago = Character("Thiago")
define mitchell = Character("Mitchell")
define nina = Character("Nina")
define felix = Character("Felix")
define joana = Character("Joana")
define diana = Character("Diana")

label start:
    python:
        DEFAULT = 'Minato'
        my_name = renpy.input('Qual seu nome?', default=DEFAULT, length=32).strip()

        if not my_name:
            my_name = DEFAULT

    jump prologo_start
