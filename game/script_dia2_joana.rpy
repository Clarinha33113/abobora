
label dia2_acusar_joana:
    show minato normal
    me "Pessoal, não percebem que essa discussão não está indo a lugar nenhum?"
    me "O verdadeiro culpado está tão claro como esse lugar, claramente foi a [joana]!"

    hide minato normal
    show joana irritada

    joana "Que!? Por que eu?"

    hide joana irritada
    show joana normal

    call escolhas_acusar(
        personagem = 'joana',
        passivo = 'Porque você provavelmente quer passar de boa moça.',
        agressivo = 'Porque você está mentindo.',
        assertivo = 'Porque você pode estar fingindo, afinal você não é burra.',
        passivo_agressivo = 'Sei lá, talvez por você parecer falsa.'
    )

    call get_most_selected_choice

    # XXX: fazer algo diferente baseado em 'most_often_choice'

    joana "você escolheu mais comunicação [most_often_choice]!"

    return


label dia2_acusar_joana_passivo1:
    me "Só para parecer inocente, mas pode estar escondendo uma personalidade cruel."
    joana "Isso não faz sentido, eu não estou fingindo ser outra pessoa."
    nina "Ela tá certa, eu acredito nela."
    "Ninguém parece acreditar em mim."

    return

label dia2_acusar_joana_agressivo1:
   
    me "Você claramente está fingindo ser inocente, só para apunhalar todos aqui pelas costas."
    joana "Você não pode provar isso."
    nina "É Espectador, você não pode provar isso."

    return

label dia2_acusar_joana_assertivo1:
    me "Você pode estar utilizando uma fachada de gentil, só para abaixarmos a guarda, para você ai atacar."
    joana "Eu não estou utilizando uma fachada, eu só quero ajudar as pessoas."
    nina "É, eu confio nela."
    "Alguns parecem estar em dúvida, mas eu não consegui convecer a maioria."

    return

label dia2_acusar_joana_passivo_agressivo1:
    me "Nada impede você de matar alguém aqui, e depois bancar a legal, mas posso estar errado ou você é uma baita mentirosa."
    joana "Quanta frieza, eu estou tentando ajudar aqui, eu garanto que não matei ninguém."
    nina "sim, ela é inocente eu acredito nisso."
    "Todos desconfiam de mim pelo olhar deles."
    "Independente da escolha a Joana sempre dira"
    joana "Olha Espectador, está claro para todos que eu não sou a culpada, por favor pare pois eu garanto que o assassino quer justamente isso."

    "Aí o jogador é obrigado a acusar outra pessoa"

    return
