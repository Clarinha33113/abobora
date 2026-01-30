define me = Character("[my_name]")
define minato = Character("Espectador")
define vince = Character("Vince")
define clint = Character("Pistoleiro")
define aisha = Character("Governante")
define sofia = Character("Contadora")
define thiago = Character("Magnífico Esperto")
define mitchell = Character("Dançarino")
define nina = Character("Confeiteira")
define felix = Character("Apostador")
define joana = Character("Atleta")
define diana = Character("Desenhista")

label start:
    python:
        DEFAULT = 'Minato'
        my_name = renpy.input('Qual seu nome?', default=DEFAULT, length=32).strip()

        if not my_name:
            my_name = DEFAULT

    jump prologo_start
