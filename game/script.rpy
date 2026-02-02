define me       = Character("[my_name]")
define minato   = Character("Espectador")
define vince    = Character("Vince")
define clint    = Character("Pistoleiro")
define aisha    = Character("Governante")
define sofia    = Character("Contadora")
define thiago   = Character("Esperto")
define mitchell = Character("Dançarino")
define nina     = Character("Confeiteira")
define felix    = Character("Apostador")
define joana    = Character("Atleta")
define diana    = Character("Desenhista")

define text_centro   = "Centro"
define text_direita  = "Direita"
define text_esquerda = "Esquerda"
define dia           = 1

define first_time_sala_recreacao = True
define first_time_cozinha = True
define first_time_biblioteca = True
define first_time_quadra = True

label start:
    python:
        DEFAULT = 'Minato'
        my_name = renpy.input('Qual seu nome?', default=DEFAULT, length=32).strip()

        if not my_name:
            my_name = DEFAULT

    jump prologo_start

label escolhas_tribunal:
    scene bg tribunal with dissolve
    menu:
        me "Para onde vou?"

        "[text_centro]":
            $ text_centro = "Sala de recreação"
            jump expression "dia" + str(dia) + "_sala_recreacao"
        "[text_direita]":
            $ text_direita = "Cozinha"
            jump expression "dia" + str(dia) + "_cozinha"
        "[text_esquerda]":
            $ text_esquerda = "Corredor"
            jump escolhas_corredor
        "Quarto":
            jump expression "dia" + str(dia) + "_quarto"


label escolhas_corredor:
    scene bg corredor with dissolve

    menu:
        "Posso ir a biblioteca ou a quadra."

        "Biblioteca":
            jump expression "dia" + str(dia) + "_biblioteca"
        "Quadra":
            jump expression "dia" + str(dia) + "_quadra"
        "Voltar":
            jump escolhas_tribunal

