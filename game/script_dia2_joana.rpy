
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
    ) from _call_escolhas_acusar_6

    joana "Olha [minato], está claro para todos que eu não sou a culpada, por favor pare pois eu garanto que o assassino quer justamente isso."

    hide joana normal
    $ joana_alive = False
    jump escolhas_quem_acusar


label dia2_acusar_joana_passivo1:
    me "Só para parecer inocente, mas pode estar escondendo uma personalidade cruel."
    joana "Isso não faz sentido, eu não estou fingindo ser outra pessoa."
    hide joana normal
    show nina infeliz
    nina "Ela tá certa, eu acredito nela."
    hide nina infeliz
    show joana normal
    "Ninguém parece acreditar em mim."
    return

label dia2_acusar_joana_agressivo1:
    me "Você claramente está fingindo ser inocente, só para apunhalar todos aqui pelas costas."
    joana "Você não pode provar isso."
    hide joana normal
    show nina infeliz
    nina "É [minato], você não pode provar isso."
    hide nina infeliz
    show joana normal
    return

label dia2_acusar_joana_assertivo1:
    me "Você pode estar utilizando uma fachada de gentil, só para abaixarmos a guarda, para você ai atacar."
    joana "Eu não estou utilizando uma fachada, eu só quero ajudar as pessoas."
    hide joana normal
    show nina infeliz
    nina "É, eu confio nela."
    hide nina infeliz
    show joana normal
    "Alguns parecem estar em dúvida, mas eu não consegui convecer a maioria."
    return

label dia2_acusar_joana_passivo_agressivo1:
    me "Nada impede você de matar alguém aqui, e depois bancar a legal, mas posso estar errado ou você é uma baita mentirosa."
    joana "Quanta frieza, eu estou tentando ajudar aqui, eu garanto que não matei ninguém."
    hide joana normal
    show nina infeliz
    nina "sim, ela é inocente eu acredito nisso."
    hide nina infeliz
    show joana normal
    "Todos desconfiam de mim pelo olhar deles."
    return

