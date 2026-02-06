label dia2_acusar_felix:
    show minato normal
    me "Pessoal, não percebem que essa discussão não está indo a lugar nenhum?"
    me "O verdadeiro culpado está tão claro como esse lugar, claramente foi o [felix]!"

    hide minato normal
    show felix pensativo

    felix "Não, eu garanto que eu não fiz nada, eu posso não contribuir tanto com a investigação, mas isso não significa que eu sou o culpado."

    call escolhas_acusar(
        personagem = 'felix',
        passivo = 'Talvez, mas eu tenho uma sensação de que você não é confiável.',
        agressivo = ' A é, isso por acaso de torna inocente!',
        assertivo = 'De fato, mas isso não impede você de ser o culpado.',
        passivo_agressivo = ' É claro que você é inocente, e nada suspeito.'
    )

    call escolhas_acusar(
        personagem = 'felix',
        passivo = 'Eu não sei, poderia sim ser associado a qualquer um',
        agressivo = 'Nem tanta fugir, que se dane a sua aposta!',
        assertivo = 'É mesmo um aliado, ou um aliado que se torna um traidor.',
        passivo_agressivo = 'Aposta tentadora, mas eu recuso.'
    )

    call get_most_selected_choice

    # XXX: fazer algo diferente baseado em 'most_often_choice'

    felix "você escolheu mais comunicação [most_often_choice]!"

    return


label dia2_acusar_felix_passivo1:
    me "E que você pode estar fingindo ser inocente, afinal é suspeito alguém já ter uma frase pronta."
    felix "Poderia ser, mas isso facilmente pode ser falado para qualquer um, até mesmo você."
    "Todos parecem considerar o que ele está dizendo."

    return

label dia2_acusar_felix_agressivo1:
   me "Você facilmente poderia ser um Lobo em pele de cordeiro, apenas esperando a chance de atacar."
    felix "Qualquer um poderia, eu sou sincero sobre as minhas intenções, além do mais me diga, eu por acaso aborreci você Espectador, pra você levantar a voz assim?"
    "As pessoas me olham com desconfiança e medo."

    return

label dia2_acusar_felix_assertivo1:
    me "Pois você pode estar fingindo ser inocente, agindo agora como um cara legal o suficiente para parecer inocente, além que a sua honestidade pode apesar ser um meio para se manter oculto."
    felix "Sábias palavras, é uma pena você desperdiçar essa sabedoria, na pessoa errada pois nós dois sabemos a verdade, eu não sou o culpado mas sim um aliado."
    "Todos olham para o Apostador, alguns com desconfiança outros parecem acreditar nele."

    return

label dia2_acusar_felix_passivo_agressivo1:
    me "Ou será que não, e você é só um mentiroso esperto, que está tentando usar artimanhas para se safar do que provavelmente fez. "
    felix "Você tem uma língua afiada, mas mal direcionada, você está tentando se convencer que eu sou o assassino, mas no fundo nós dois sabemos que eu sou realmente inocente."
    me "Os outros não parecem considerar o que eu estou falando, agora parecem desconfiar de mim."
    "Independente da escolha o Felix sempre dirá"
    felix "Por favor Espectador, reconsidere você sabe que o assassino vai sair impune, porque não desiste e pense com mais calma, pois eu aposto meu ♤ vermelho que eu sou inocente."

    return

label dia2_acusar_felix_passivo2:
    me "Mas tem algo sobre você que não parece certo, existem conveniências para você tanto não ser como ser."
    felix "Muito interessante, porém você fala de um modo que soa que nem você acredita nisso, você ainda acredita que eu sou o assassino."
    "Ele pode estar certo, mas meus instintos me dizem o contrário, e ninguém parece acreditar em mim."

    return

label dia2_acusar_felix_agressivo2:
   me "você cheira a culpa, e ao mesmo tempo alguém que não é o que parece, você tem esse ar sombrio ao seu redor."
    felix "É mesmo, porém se isso é verdade, por que você está perdendo o controle, eu te pergunto se você acha mesmo isso, você prefere acreditar em instintos ou na verdade diante da sua cara."
    "Ele conseguiu fazer ninguém acreditar em mim, agora os olhas se intensificam para mim."

    return

label dia2_acusar_felix_assertivo2:
    me "Você parece estar fugindo da acusação com palavras e argumentos bonitos, que no fim não responde nada, você está disposto a fazer qualquer para que ninguém te veja como culpado, não é."
    felix "Sim, eu vou pois é só isso que eu tenho para que você acredite em mim."
    "O Felix parece assustado e nervoso, agora todos parecem convictos que ele é o assassino."

    return

label dia2_acusar_felix_passivo_agressivo2:
    
    return


