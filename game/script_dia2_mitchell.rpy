
label dia2_acusar_mitchell:
    define got_caught = False
    show minato normal
    me "Pessoal, não percebem que essa discussão não está indo a lugar nenhum?"
    me "O verdadeiro culpado está tão claro quanto este lugar. Claramente, foi o [mitchell]!"

    hide minato normal
    show mitchell normal

    play music tema_mitchell

    mitchell "Como é? Eu sou o culpado? Hahahahahaha... isso é sério?"

    call escolhas_acusar(
        personagem = 'mitchell',
        passivo = 'Sim, é sério. Eu suspeito que pode ser você.',
        agressivo = 'Mas é claro que é. Você é, de longe, o mais suspeito.',
        assertivo = 'Sim, é sério. Você é o mais suspeito e, provavelmente, o culpado.',
        passivo_agressivo = 'Não... eu tô só brincando.'
    )

    call escolhas_acusar(
        personagem = 'mitchell',
        passivo = 'Nenhuma prova concreta, mas há algo errado com você.',
        agressivo = 'Isso não importa quando se tem provas concretas.',
        assertivo = 'Isso soa apenas como uma desculpa... típica de um culpado.',
        passivo_agressivo = 'Talvez... mas, se todos forem espertos, sabem a verdade.'
    )

    hide mitchell normal
    if got_caught:
        jump dia2_final
    else:
        jump dia2_depois_de_acusar

label dia2_acusar_mitchell_passivo1:
    me "Devido à sua total indiferença à morte da [diana], além de você não ter ajudado na investigação. E meus instintos também apontam para isso."
    mitchell "Seus instintos? Você tem alguma prova ou vai se basear apenas nisso? Que investigação séria faz isso?"
    "Ninguém parece acreditar em mim."
    return

label dia2_acusar_mitchell_agressivo1:
    me "Você foi totalmente indiferente à morte dela. Falou como se não fosse nada, exatamente a atitude que um assassino teria."
    mitchell "Eu sou realista. Não adianta chorar pelo leite derramado, assim como não adianta gritar achando que isso vai provar alguma coisa."
    "Ninguém parece acreditar em mim. Eles parecem irritados."
    return

label dia2_acusar_mitchell_assertivo1:
    me "Você agiu com completa indiferença à morte dela e falou de forma tão fria que chegou a ser insensível. Além disso, nem ajudou na investigação."
    mitchell "Eu só agi assim porque não fico chorando pelo leite derramado. E eu simplesmente não sou bom nesse negócio de detetive."
    "Todos olham para ele com suspeita."
    return

label dia2_acusar_mitchell_passivo_agressivo1:
    me "Claro que é sério. Você é o mais suspeito. Sua atitude tão... gentil. Quando fala da \"garota morta\", soa até sensível demais."
    mitchell "Esse seu sarcasmo não prova nada. Você acha mesmo que alguém vai se convencer por isso?"
    "Ninguém parece acreditar em mim."
    return

label dia2_acusar_mitchell_passivo2:
    me "Afinal, seu nome é [mitchell]. Você poderia ser aquele que forçou a [diana] a se matar, provavelmente por meio de uma ameaça."
    mitchell "Provavelmente? Você quer mesmo acreditar nisso?"
    "Ninguém me levou a sério."
    return

label dia2_acusar_mitchell_agressivo2:
    me "Não é só sua atitude. Não seria estranho um [mitchell] fazer movimentos estranhos, além de usar sapatos e um casaco?"
    mitchell "Posso até usar, mas você fala de um jeito tão determinado a me acusar... levanta a voz como se estivesse tentando desviar a atenção para mim."
    "Todos me olham com suspeita."
    return

label dia2_acusar_mitchell_assertivo2:
    me "Pessoal, olhem bem. O nome dele é [mitchell], que combina com os movimentos estranhos descritos. Ele veste um casaco e usa sapatos."
    hide mitchell normal
    show mitchell seila
    mitchell "O quê?! Isso é um absurdo! Eu não fiz nada!"
    "Todos olham para ele com desconfiança."
    me "É mesmo? Porque você me parece bem desesperado."
    mitchell "Eu só estou assim porque vocês estão me olhando desse jeito! E é culpa sua!!"
    me "Só me diz... por que você escolheu ela?"
    mitchell "Eu não escolhi nada, porque não fui eu!"
    me "Sério? É tão difícil admitir? Apenas diga: \"eu a matei.\""
    hide mitchell seila
    show mitchell irritado
    "Ele me olha com muita raiva. Parece que consegui encontrar o assassino e ainda expô-lo."
    hide mitchell irritado
    $ got_caught = True
    return

label dia2_acusar_mitchell_passivo_agressivo2:
    me "Afinal, você também usa sapatos e casaco. E quem mais foi descrito assim?"
    mitchell "Você é um cara bem desagradável, [minato]."
    "Todos olham para mim com raiva."
    return

