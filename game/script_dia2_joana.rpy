
label dia2_acusar_joana:
    show minato normal
    me "Pessoal, não percebem que essa discussão não está indo a lugar nenhum?"
    me "O verdadeiro culpado está tão claro quanto este lugar. Claramente, foi a [joana]!"

    hide minato normal
    show joana irritada

    joana "O quê?! Por que eu?"

    hide joana irritada
    show joana normal

    call escolhas_acusar(
        personagem = 'joana',
        passivo = 'Porque você pode estar tentando parecer a boa moça da situação.',
        agressivo = 'Porque você está mentindo.',
        assertivo = 'Porque você pode estar fingindo. Afinal, você não é ingênua.',
        passivo_agressivo = 'Sei lá... talvez porque você pareça falsa.'
    )

    joana "Olha, [minato], está claro para todos que eu não sou a culpada. Por favor, pare. Eu garanto que o assassino quer justamente isso."

    hide joana normal
    $ joana_alive = False
    jump dia2_depois_de_acusar


label dia2_acusar_joana_passivo1:
    me "Só para parecer inocente. Mas você pode estar escondendo uma personalidade cruel."
    joana "Isso não faz sentido. Eu não estou fingindo ser outra pessoa."
    hide joana normal
    show nina infeliz
    nina "Ela tá certa. Eu acredito nela."
    hide nina infeliz
    show joana normal
    "Ninguém parece acreditar em mim."
    return

label dia2_acusar_joana_agressivo1:
    me "Você claramente está fingindo ser inocente, só para apunhalar todos aqui pelas costas."
    joana "Você não pode provar isso."
    hide joana normal
    show nina infeliz
    nina "É, [minato], você não pode provar isso."
    hide nina infeliz
    show joana normal
    return

label dia2_acusar_joana_assertivo1:
    me "Você pode estar usando uma fachada de gentileza só para abaixarmos a guarda... e então atacar."
    joana "Eu não estou usando fachada nenhuma. Eu só quero ajudar as pessoas."
    hide joana normal
    show nina infeliz
    nina "É... eu confio nela."
    hide nina infeliz
    show joana normal
    "Alguns parecem estar em dúvida, mas eu não consegui convencer a maioria."
    return

label dia2_acusar_joana_passivo_agressivo1:
    me "Nada impede você de matar alguém aqui e depois bancar a boazinha. Posso estar errado... ou você é uma baita mentirosa."
    joana "Quanta frieza... eu estou tentando ajudar aqui. Eu garanto que não matei ninguém."
    hide joana normal
    show nina infeliz
    nina "Sim, ela é inocente. Eu acredito nisso."
    hide nina infeliz
    show joana normal
    "Todos parecem desconfiar de mim pelo olhar deles."
    return

