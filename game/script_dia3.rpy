label dia3_start:
    python:
        # had to kill them just now mb
        felix_alive = nina_alive = joana_alive = True
        mitchell_alive = False # this one is dead fr tho
    call novo_dia
    # vai main menu mesmo fodase
    play music "main menu.mp3" if_changed

    "Isso é um sonho? Ou é só mais um truque desse lugar? Eu só me lembro de ter ido dormir."

    scene bg floresta with dissolve

    "Quem é aquele cara engraçado ali?"

    show letos normal

    noname "Como vai amigo, nesse dia maravilhoso."

    me "Eu tô bem."

    noname "Isso é bom, porque aqui na floresta do véu, ninguém é triste, o que me lembra de me apresentar."

    letos "Meu nome é [letos], eu sou o jardineiro que cuida dessa floresta."

    me "Um jardineiro? Cadê o jardim?"

    letos "Você é bem apressado amigo, mas eu entendo. Venha que eu mostro o jardim."

    scene bg jardim with dissolve

    "Então nós dois fomos até o jardim, parece ser mais um lugar tranquilo, mas por algum motivo tem uma gosma preta saindo de algumas flores."

    show letos normal

    me "[letos] tem um líquido estranho saindo daquelas flores."

    letos "Ah obrigado [my_name]."

    me "Como você sabe o meu nome?"

    hide letos normal
    "O [letos] se vira e começa a arrumar as flores."

    letos "Hora que anfitrião seria eu, se não soubesse o nome do meu convidado."

    "Isso é bem esquisito, e ele logo se levantou e olhou para mim."

    show letos normal
    letos "Eu peço perdão [my_name], parece que o jardim hoje está bem teimoso."

    me "Você se refere a esse líquido escuro?"

    "Junto com o líquido um cheiro horrível está no ar."

    letos "Infelizmente sim, porém me diga está tudo bem [my_name]?"

    me "Sim... na verdade, infelizmente não está tudo bem."

    "Do nada, mais do líquido negro aparece, e com ele o cheiro piora."

    letos "O quê?! Isso é não positivo, você tem que pensar positivo."

    menu:
        "Não, não está tudo bem.":
            me "A [diana] morreu, o mundo está destruido, e eles não estão mais aqui!"
            # XXX: (O cenário vai ficando cada vez mais apodrecido)

            hide letos normal
            show letos assustado
            letos "Não diga isso, não diga isso!!"

            me "Mas isso é a verdade, eu não posso mais fingir que está tudo bem."

            me "Eu fugi dessa verdade, por isso eu tô te dizendo, muita coisa está errada."

            letos "Não, não, não, não, não, porque você está falando isso."

            # XXX: geen tijd voor dis shit
            # "Logo o [letos] começa a derreter e apodrecer, e uma garota vestindo um vestido branco com detalhes em verde."
            "Logo o [letos] começa a derreter e apodrecer."
            jump dia3_real_start

        "Provavelmente, eu de fato deveria.":
            letos "Muito bom, isso. Pense de modo positivo."
            jump dia3_real_start


label dia3_real_start:
    scene black with dissolve
    scene bg quarto with dissolve
    play music tema_suspense loop if_changed

    "O que foi aquilo? deve ser só um sonho, mas esse é o primeiro que foi mais vívido..."
    "Bem, de todo modo eu devo descobrir algo sobre os meus poderes."

    jump escolhas_tribunal

label dia3_sala_recreacao:
    scene bg sala_recreacao with dissolve
    # play music tema_sala_recreacao if_changed
    if first_time_sala_recreacao:
        "[thiago] e [sofia] estão na sala de recreação."
        $ first_time_sala_recreacao = False
    menu:
        "Falar com alguém?"
        "[thiago]":
            jump dia3_thiago
        "[sofia]":
            jump dia3_sofia
        "Voltar":
            jump escolhas_tribunal

label dia3_thiago:
    return

label dia3_sofia:
    return

label dia3_cozinha:
    scene bg cozinha with dissolve
    # play music tema_cozinha if_changed
    menu:
        "[clint] está na cozinha."
        "Falar com ele":
            jump dia3_clint
        "Voltar":
            jump escolhas_tribunal

label dia3_clint:
    return

label dia3_biblioteca:
    scene bg biblioteca with dissolve
    play music tema_biblioteca if_changed
    if first_time_biblioteca:
        "[aisha], [nina] e [felix] estão na biblioteca."
        $ first_time_biblioteca = False
    menu:
        "Falar com um deles?"
        "[aisha]":
            jump dia3_aisha
        "[nina]":
            jump dia3_nina
        "[felix]":
            jump dia3_felix
        "Voltar":
            jump escolhas_corredor

label dia3_aisha:
    return

label dia3_nina:
    return

label dia3_felix:
    return

label dia3_quadra:
    scene bg quadra with dissolve
    play music tema_quadra if_changed
    menu:
        "[joana] está na quadra."
        "Falar com ela":
            jump dia3_joana
        "Voltar":
            jump escolhas_corredor

label dia3_joana:
    return

label dia3_quarto:
    return

