
label dia2_acusar_mitchell:
    define got_caught = False
    show minato normal
    me "Pessoal, não percebem que essa discussão não está indo a lugar nenhum?"
    me "O verdadeiro culpado está tão claro como esse lugar, claramente foi o [mitchell]!"

    hide minato normal
    show mitchell normal

    play music tema_mitchell

    mitchell "Como é, eu sou culpado? Hahahahahaha, isso é sério?"

    call escolhas_acusar(
        personagem = 'mitchell',
        passivo = 'Sim é sério, eu suspeito que pode ser você.',
        agressivo = 'Mas é claro que é, você é de longe o mais suspeito.',
        assertivo = 'Sim é sério, você é o mais suspeito e provavelmente o culpado.',
        passivo_agressivo = 'Não, eu tô só brincando.'
    )

    call escolhas_acusar(
        personagem = 'mitchell',
        passivo = 'Nenhuma, mas tem algo errado com você.',
        agressivo = 'Isso não importa, quando se tem provas concretas.',
        assertivo = 'Isso é só uma desculpa, vindo do culpado.',
        passivo_agressivo = 'Talvez, mas se todos forem espertos sabem a verdade.'
    )

    hide mitchell normal
    if got_caught:
        jump dia2_final
    else:
        jump dia2_depois_de_acusar

label dia2_acusar_mitchell_passivo1:
    me "Devido a sua total indiferença a morte da [diana], além que você não quis ajudar na investigação, e os meus instintos me dizem isso."
    mitchell "Seus instintos. Você tem alguma prova ou vai se basear em instintos, pois qual investigação se baseia nisso."
    "Ninguém parece acreditar em mim."
    return

label dia2_acusar_mitchell_agressivo1:
    me "Você é totalmente indiferente a morte dela, você falou disso como se não fosse nada, o tipo de atitude que um assassino teria."
    mitchell "Eu sou realista, não adianta chorar pelo leite derramado, assim como não adianta gritar achando que vai provar algo."
    "Ninguém parece acreditar em mim, eles parecem irritados."
    return

label dia2_acusar_mitchell_assertivo1:
    me "Você agiu com completa indiferença a morte dela, e falou de um modo tão frio que chega a ser insensível, e nem ajudou na investigação."
    mitchell "Eu só agi assim pois não fico chorando pelo leite derramado, e eu só não sou bom nesse negócio de detetive."
    "Todos olham para ele suspeitando dele."
    return

label dia2_acusar_mitchell_passivo_agressivo1:
    me "É claro que é sério, você é o mais suspeito, sua atitude tão gentil, quando você diz sobre a \"garota morta\", você foi tão sensível."
    mitchell "Esse sarcasmo seu não prova nada, você acha que alguém se convence por isso."
    "Ninguém parece acreditar em mim."
    return

label dia2_acusar_mitchell_passivo2:
    me "Afinal o seu nome é o [mitchell], você poderia ser aquele que forçou a [diana] a se matar, com provavelmente uma ameaça."
    mitchell "Provavelmente? Você quer acreditar nisso?"
    "Ninguém me levou a sério."
    return

label dia2_acusar_mitchell_agressivo2:
    me "Não basta sua atitude, como não seria estranho um [mitchell] fazer movimentos estranhos, além de usar sapatos e um casaco!"
    mitchell "Posso até usar, mas você fala de um jeito tão determinado a me acusar, levanta a voz como se buscasse desviar a atenção para mim."
    "Todos me olham com suspeita."
    return

label dia2_acusar_mitchell_assertivo2:
    me "Pessoal olhem bem, o nome dele é o [mitchell] que se encaixa nos movimentos estranhos, ele veste um casaco e usa sapatos."
    hide mitchell normal
    show mitchell seila
    mitchell "O que! Isso é um absurdo, eu não fiz nada!"
    "Todos olham para ele com desconfiança."
    me "É mesmo, pois você me parece bem desesperado."
    mitchell "Eu só estou assim porque vocês estão me olhando assim, e é sua culpa!!"
    me "Só me diz por que você escolheu ela?"
    mitchell "Eu não escolhi nada, porque não fui eu!"
    me "Sério, é tão difícil admitir, apenas diga \"eu matei ela.\""
    hide mitchell seila
    show mitchell irritado
    "Ele me olha com muita raiva, parece que consegui achar o assassino e ainda expor ele."
    hide mitchell irritado
    $ got_caught = True
    return

label dia2_acusar_mitchell_passivo_agressivo2:
    me "Afinal você também usa sapatos e casacos, e quem mais foi descrito assim."
    mitchell "Você é um cara bem desagradável, [minato]."
    "Todos olham para mim com raiva."
    return

