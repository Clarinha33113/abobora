label dia3_start:
    python:
        # had to kill them just now mb
        felix_alive = nina_alive = joana_alive = True
        mitchell_alive = False # this one is dead fr tho
        dia = 3
    scene black with dissolve
    show text "Dia 3" with Pause(2)
    scene black with dissolve

    # vai main menu mesmo fodase
    play music "main menu.mp3" if_changed

    "Isso é um sonho? Ou é só mais um truque desse lugar? Eu só me lembro de ter ido dormir."

    scene bg floresta with dissolve

    "Quem é aquele cara engraçado ali?"

    # XXX: show goofy dude here

    noname "Como vai amigo, nesse dia maravilhoso."

    me "Eu tô bem."

    noname "Isso é bom, porque aqui na floresta do véu, ninguém é triste, o que me lembra de me apresentar."

    letos "Meu nome é [letos], eu sou o jardineiro que cuida dessa floresta."

    me "Um jardineiro? Cadê o jardim?"

    letos "Você é bem apressado amigo, mas eu entendo. Venha que eu mostro o jardim."

    scene bg jardim with dissolve

    "Então nós dois fomos até o jardim, parece ser mais um lugar tranquilo, mas por algum motivo tem uma gosma preta saindo de algumas flores."

    me "[letos] tem um líquido estranho saindo daquelas flores."

    letos "Ah obrigado [my_name]."

    me "Como você sabe o meu nome?"

    "O [letos] se vira e começa a arrumar as flores."

    letos "Hora que anfitrião seria eu, se não soubesse o nome do meu convidado."

    "Isso é bem esquisito, e ele logo se levantou e olhou para mim."

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

            letos "Não diga isso, não diga isso!!"

            me "Mas isso é a verdade, eu não posso mais fingir que está tudo bem."

            me "Eu fugi dessa verdade, por isso eu tô te dizendo, muita coisa está errada."

            letos "Não, não, não, não, não, porque você está falando isso."

            "Logo o [letos] começa a derreter e apodrecer, e uma garota vestindo um vestido branco com detalhes em verde."

            jump dia3_real_start

        "Provavelmente, eu de fato deveria.":
            letos "Muito bom, isso. Pense de modo positivo."
            jump dia3_real_start


label dia3_real_start:
    scene black with dissolve
    scene bg quarto with dissolve
    play music tema_suspense if_changed

    "O que foi aquilo? deve ser só um sonho, mas esse é o primeiro que foi mais vívido..."
    "Bem, de todo modo eu devo descobrir algo sobre os meus poderes."

    jump escolhas_tribunal

label dia3_sala_recreacao:
    return

label dia3_cozinha:
    return

label dia3_biblioteca:
    return

label dia3_quadra:
    return

label dia3_quarto:
    return

