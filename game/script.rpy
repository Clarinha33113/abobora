define me = Character("[my_name]")
define vince = Character("Vince")
define clint = Character("O Pistoleiro Pessoal")
define aisha = Character("A Governante")
define sofia = Character("A Contadora")
define thiago = Character("Magnífico Esperto")
define mitchell = Character("O Dançarino")
define nina = Character("A Confeiteira")
define felix = Character("O Apostador")
define joana = Character("A Atleta")
define diana = Character("A Desenhista")

label start:
    python:
        DEFAULT = 'Minato'
        my_name = renpy.input('Qual seu nome?', default=DEFAULT, length=32).strip()

        if not my_name:
            my_name = DEFAULT

    jump prologo_start
