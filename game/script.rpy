define me       = Character("[my_name]")
define vince    = Character("Vince")
define noname   = Character("???")
define minato   = Character("Espectador")
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
define dialog_count  = 0

define CS_ASSERTIVO = 'Assertivo'
define CS_AGRESSIVO = 'Agressivo'
define CS_PASSIVO   = 'Passivo'
define CS_PASSIVO_AGRESSIVO = 'Passivo-Agressivo'

define communication_style_points = {
    CS_PASSIVO: 0,
    CS_AGRESSIVO: 0,
    CS_ASSERTIVO: 0,
    CS_PASSIVO_AGRESSIVO: 0,
}

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
    # $ dia = 2
    # jump dia2_tribunal

label escolhas_tribunal:
    scene bg tribunal with dissolve
    menu:
        me "Para onde vou?"

        "[text_centro]":
            $ text_centro = "Sala de recreação"
            jump expression f"dia{dia}_sala_recreacao"
        "[text_direita]":
            $ text_direita = "Cozinha"
            jump expression f"dia{dia}_cozinha"
        "[text_esquerda]":
            $ text_esquerda = "Corredor"
            jump escolhas_corredor
        "Quarto":
            jump expression f"dia{dia}_quarto"


label escolhas_corredor:
    scene bg corredor with dissolve

    menu:
        "Posso ir a biblioteca ou a quadra."

        "Biblioteca":
            jump expression f"dia{dia}_biblioteca"
        "Quadra":
            jump expression f"dia{dia}_quadra"
        "Voltar":
            jump escolhas_tribunal


label escolhas_acusar(personagem, passivo, agressivo, assertivo, passivo_agressivo):
    menu:
        "[passivo]":
            call aumentar_ponto(CS_PASSIVO)
            jump expression f"dia{dia}_acusar_{personagem}_passivo{dialog_count}"
        "[agressivo]":
            call aumentar_ponto(CS_AGRESSIVO)
            jump expression f"dia{dia}_acusar_{personagem}_agressivo{dialog_count}"
        "[assertivo]":
            call aumentar_ponto(CS_ASSERTIVO)
            jump expression f"dia{dia}_acusar_{personagem}_assertivo{dialog_count}"
        "[passivo_agressivo]":
            call aumentar_ponto(CS_PASSIVO_AGRESSIVO)
            jump expression f"dia{dia}_acusar_{personagem}_passivo_agressivo{dialog_count}"


label aumentar_ponto(tipo, quantidade = 1):
    $ communication_style_points[tipo] += quantidade
    $ dialog_count += 1
    return

