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
define letos    = Character("Letos")

define clint_alive    = True
define aisha_alive    = True
define sofia_alive    = True
define thiago_alive   = True
define mitchell_alive = True
define nina_alive     = True
define felix_alive    = True
define joana_alive    = True

define believe_felix = False

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

define accused_person = ''
define current_choices = {}
define last_picked_choice = ''
define most_often_choice = ''

define first_time_sala_recreacao = True
define first_time_cozinha = True
define first_time_biblioteca = True
define first_time_quadra = True

define audio.tema_mitchell   = 'mitchell.mp3'
define audio.tema_biblioteca = 'biblioteca.mp3'
define audio.tema_quadra     = 'quadra.mp3'
define audio.tema_suspense   = 'suspense.mp3'
define audio.tema_medonha    = 'medonha.mp3'
define audio.tema_tribunal   = 'tribunal.mp3'

label start:
    # python:
    #     DEFAULT = 'Minato'
    #     my_name = renpy.input('Qual seu nome?', default=DEFAULT, length=32).strip()

    #     if not my_name:
    #         my_name = DEFAULT

    stop music
    $ my_name = 'Minato'
    jump prologo_start

label escolhas_tribunal:
    scene bg tribunal with dissolve
    play music tema_suspense if_changed
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
    play music tema_suspense if_changed

    menu:
        "Posso ir a biblioteca ou a quadra."

        "Biblioteca":
            jump expression f"dia{dia}_biblioteca"
        "Quadra":
            jump expression f"dia{dia}_quadra"
        "Voltar":
            jump escolhas_tribunal

label resetar_escolhas:
    python:
        current_choices = { CS_PASSIVO: 0, CS_AGRESSIVO: 0, CS_ASSERTIVO: 0, CS_PASSIVO_AGRESSIVO: 0 }
        dialog_count = 0
    return

label escolhas_quem_acusar:
    $ dialog_count = 0
    menu:
        "Quem deseja acusar?"

        "[clint]" if clint_alive:
            $ accused_person = '[clint]'
            jump expression f"dia{dia}_acusar_clint"
        "[aisha]" if aisha_alive:
            $ accused_person = '[aisha]'
            jump expression f"dia{dia}_acusar_aisha"
        "[sofia]" if sofia_alive:
            $ accused_person = '[sofia]'
            jump expression f"dia{dia}_acusar_sofia"
        "[thiago]" if thiago_alive:
            $ accused_person = '[thiago]'
            jump expression f"dia{dia}_acusar_thiago"
        "[mitchell]" if mitchell_alive:
            $ accused_person = '[mitchell]'
            jump expression f"dia{dia}_acusar_mitchell"
        "[nina]" if nina_alive:
            $ accused_person = '[nina]'
            jump expression f"dia{dia}_acusar_nina"
        "[felix]" if felix_alive:
            $ accused_person = '[felix]'
            jump expression f"dia{dia}_acusar_felix"
        "[joana]" if joana_alive:
            $ accused_person = '[joana]'
            jump expression f"dia{dia}_acusar_joana"


label escolhas_acusar(personagem, passivo, agressivo, assertivo, passivo_agressivo, **kwargs):
    $ extra = kwargs['extra'] if 'extra' in kwargs else ''
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
        "[extra]" if extra:
            call aumentar_ponto(CS_PASSIVO, 0)
            jump expression f"dia{dia}_acusar_{personagem}_extra{dialog_count}"


label aumentar_ponto(tipo, quantidade = 1):
    python:
        communication_style_points[tipo] += quantidade
        current_choices[tipo] += quantidade
        last_picked_choice = tipo
        dialog_count += 1
    return

label get_most_selected_choice:
    python:
        for key, val in current_choices.items():
            if val > 1:
                most_often_choice = key
                break
            else:
                most_often_choice = last_picked_choice
                break
    return

