label dia2_acusar_felix:
    show minato normal
    me "Pessoal, não percebem que essa discussão não está indo a lugar nenhum?"
    me "O verdadeiro culpado está tão claro como esse lugar, claramente foi o [felix]!"
    define believe_him = False

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

    felix "Por favor [minato], reconsidere. Você sabe que o assassino vai sair impune, porque não desiste e pense com mais calma? Pois eu aposto meu ♤ vermelho que eu sou inocente."

    call escolhas_acusar(
        personagem = 'felix',
        passivo = 'Eu não sei, poderia sim ser associado a qualquer um.',
        agressivo = 'Nem tanta fugir, que se dane a sua aposta!',
        assertivo = 'É mesmo um aliado, ou um aliado que se torna um traidor.',
        passivo_agressivo = 'Aposta tentadora, mas eu recuso.',
        extra = 'Ok, eu acredito em você.'
    )

    call get_most_selected_choice

    # XXX: isso aqui é placeholder
    if believe_him:
        felix "Você acreditou em mim!"
    else:
        felix "Você escolheu mais comunicação [most_often_choice]!"

    return


label dia2_acusar_felix_passivo1:
    me "E que você pode estar fingindo ser inocente, afinal é suspeito alguém já ter uma frase pronta."
    felix "Poderia ser, mas isso facilmente pode ser falado para qualquer um, até mesmo você."
    "Todos parecem considerar o que ele está dizendo."
    return

label dia2_acusar_felix_agressivo1:
    me "Você facilmente poderia ser um lobo em pele de cordeiro, apenas esperando a chance de atacar."
    felix "Qualquer um poderia, eu sou sincero sobre as minhas intenções."
    felix "Além do mais, me diga, eu por acaso aborreci você, [minato], pra você levantar a voz assim?"
    "As pessoas me olham com desconfiança e medo."
    return

label dia2_acusar_felix_assertivo1:
    me "Pois você pode estar fingindo ser inocente, agindo agora como um cara legal o suficiente para parecer inocente, além que a sua honestidade pode apesar ser um meio para se manter oculto."
    felix "Sábias palavras, é uma pena você desperdiçar essa sabedoria na pessoa errada pois nós dois sabemos a verdade, eu não sou o culpado mas sim um aliado."
    "Todos olham para o [felix], alguns com desconfiança outros parecem acreditar nele."
    return

label dia2_acusar_felix_passivo_agressivo1:
    me "Ou será que não, e você é só um mentiroso esperto, que está tentando usar artimanhas para se safar do que provavelmente fez."
    felix "Você tem uma língua afiada, mas mal direcionada, você está tentando se convencer que eu sou o assassino, mas no fundo nós dois sabemos que eu sou realmente inocente."
    "Os outros não parecem considerar o que eu estou falando, agora parecem desconfiar de mim."
    return

label dia2_acusar_felix_passivo2:
    me "Mas tem algo sobre você que não parece certo, existem conveniências para você tanto não ser como ser."
    felix "Muito interessante, porém você fala de um modo que soa que nem você acredita nisso, você ainda acredita que eu sou o assassino."
    "Ele pode estar certo, mas meus instintos me dizem o contrário, e ninguém parece acreditar em mim."
    return

label dia2_acusar_felix_agressivo2:
    me "Você cheira a culpa, e ao mesmo tempo alguém que não é o que parece, você tem esse ar sombrio ao seu redor."
    felix "É mesmo, porém se isso é verdade, por que você está perdendo o controle? Eu te pergunto se você acha mesmo isso, você prefere acreditar em instintos ou na verdade diante da sua cara."
    "Ele conseguiu fazer ninguém acreditar em mim, agora os olhas se intensificam para mim."
    return

label dia2_acusar_felix_assertivo2:
    hide felix pensativo
    show felix enojado
    me "Você parece estar fugindo da acusação com palavras e argumentos bonitos, que no fim não responde nada, você está disposto a fazer qualquer coisa para que ninguém te veja como culpado, não é."
    felix "Sim, eu vou, pois é só isso que eu tenho para que você acredite em mim."
    "O [felix] parece assustado e nervoso, agora todos parecem convictos que ele é o assassino."
    return

label dia2_acusar_felix_passivo_agressivo2:
    me "Você acha mesmo que eu vou confiar em você, não adianta usar uma aposta, você só queria soar inocente, mas eu sei a verdade e é por isso que eu acredito na sua culpa."
    felix "Você realmente ficou cego pela sua convicção, ao ponto de não ver a verdade, é uma pena você tinha o potencial de ser a peça chave da nossa sobrevivência, mas você escolheu o caminho errado, eu acredito que você não é o culpado."
    "Ninguém acredita em mim, mas ao mesmo não parecem suspeitar de mim, graças ao [felix]."
    return

label dia2_acusar_felix_extra2:
    $ believe_him = True
    felix "Muito bom, eu fico feliz que você entendeu a verdade, e pode ficar com o meu Ás de espada, como um presente da minha aposta."
    "O [felix] jogou o Ás de espada vermelho dele"
    "Na carta estava escrito: \'{i}O culpado é aquele com o chapéu e a indiferença gritante.{/i}\'"
    return

