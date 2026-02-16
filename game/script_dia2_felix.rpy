label dia2_acusar_felix:
    show minato normal
    me "Pessoal, não percebem que essa discussão não está indo a lugar nenhum?"
    me "O verdadeiro culpado está tão claro quanto este lugar. Claramente, foi o [felix]!"

    hide minato normal
    show felix pensativo

    felix "Não. Eu garanto que não fiz nada. Eu posso não contribuir tanto com a investigação, mas isso não significa que eu sou o culpado."

    call escolhas_acusar(
        personagem = 'felix',
        passivo = 'Talvez... mas eu tenho a sensação de que você não é tão confiável quanto parece.',
        agressivo = 'Ah, é? E isso por acaso te torna inocente?!',
        assertivo = 'Pode ser, mas isso não impede você de ser o culpado.',
        passivo_agressivo = 'Claro... você é completamente inocente. Nada suspeito em você.'
    )

    felix "Por favor, [minato], reconsidere. Você sabe que o assassino vai sair impune. Por que não desiste e pensa com mais calma? Eu aposto meu ♤ vermelho que sou inocente."

    call escolhas_acusar(
        personagem = 'felix',
        passivo = 'Eu não sei... qualquer um aqui poderia estar envolvido.',
        agressivo = 'Nem tente fugir! Que se dane a sua aposta!',
        assertivo = 'Você pode parecer um aliado... ou um aliado que virou traidor.',
        passivo_agressivo = 'Uma aposta tentadora... mas eu recuso.',
        extra = 'Ok. Eu acredito em você.'
    )

    hide felix pensativo
    if believe_felix:
        # lil hack, fucking kill him
        $ felix_alive = False
        jump escolhas_quem_acusar

    jump dia2_depois_de_acusar


label dia2_acusar_felix_passivo1:
    me "É que você pode estar fingindo ser inocente. Afinal, é suspeito alguém já ter uma resposta pronta."
    felix "Pode ser. Mas isso poderia ser dito sobre qualquer um aqui, inclusive você."
    "Todos parecem considerar o que ele está dizendo."
    return

label dia2_acusar_felix_agressivo1:
    me "Você poderia ser um lobo em pele de cordeiro, apenas esperando a chance de atacar."
    felix "Qualquer um poderia. Eu, pelo menos, sou sincero sobre minhas intenções."
    felix "Além do mais, me diga... eu por acaso te ofendi, [minato], para você levantar a voz assim?"
    "As pessoas me olham com desconfiança e medo."
    return

label dia2_acusar_felix_assertivo1:
    me "Você pode estar fingindo ser inocente, agindo como alguém simpático o suficiente para parecer confiável. Sua honestidade pode, inclusive, ser um meio de se manter oculto."
    felix "Sábias palavras. É uma pena você desperdiçar essa sabedoria na pessoa errada. Nós dois sabemos a verdade: eu não sou o culpado, sou um aliado."
    "Todos olham para o [felix]; alguns com desconfiança, outros parecem acreditar nele."
    return

label dia2_acusar_felix_passivo_agressivo1:
    me "Ou talvez não... talvez você seja apenas um mentiroso esperto, tentando usar artimanhas para se safar do que provavelmente fez."
    felix "Você tem uma língua afiada, mas mal direcionada. Está tentando se convencer de que eu sou o assassino, mas no fundo nós dois sabemos que sou inocente."
    "Os outros não parecem considerar o que estou dizendo. Agora parecem desconfiar de mim."
    return

label dia2_acusar_felix_passivo2:
    me "Há algo em você que não parece certo. Existem conveniências tanto para você ser quanto para não ser o culpado."
    felix "Interessante. Mas você fala de um jeito que nem parece acreditar nisso. No fundo, você ainda acha que eu sou o assassino."
    "Ele pode estar certo... mas meus instintos dizem o contrário, e ninguém parece acreditar em mim."
    return

label dia2_acusar_felix_agressivo2:
    me "Você cheira a culpa. E, ao mesmo tempo, parece alguém que não é o que demonstra ser. Há algo sombrio em você."
    felix "É mesmo? Então me diga: se isso é verdade, por que você está perdendo o controle? Você prefere acreditar nos seus instintos ou na verdade diante dos seus olhos?"
    "Ele conseguiu virar todos contra mim. Agora os olhares se intensificam sobre mim."
    return

label dia2_acusar_felix_assertivo2:
    hide felix pensativo
    show felix enojado
    me "Você está fugindo da acusação com palavras bonitas que, no fim, não respondem nada. Está disposto a fazer qualquer coisa para que ninguém te veja como culpado, não está?"
    felix "Sim, estou. Porque é tudo o que tenho para fazer você acreditar em mim."
    "O [felix] parece assustado e nervoso. Agora todos parecem convictos de que ele é o assassino."
    return

label dia2_acusar_felix_passivo_agressivo2:
    me "Você acha mesmo que eu vou confiar em você? Não adianta usar uma aposta. Você só queria soar inocente. Eu sei a verdade, e é por isso que acredito na sua culpa."
    felix "Você ficou cego pela sua própria convicção, a ponto de não enxergar a verdade. É uma pena. Você tinha o potencial de ser a peça-chave da nossa sobrevivência, mas escolheu o caminho errado. E, ironicamente, eu acredito que você não é o culpado."
    "Ninguém acredita em mim, mas também não parecem suspeitar de mim, graças ao [felix]."
    return

label dia2_acusar_felix_extra2:
    $ believe_felix = True
    felix "Muito bem. Fico feliz que você tenha entendido a verdade. Pode ficar com o meu Ás de Espadas como prova da minha aposta."
    "O [felix] joga o Ás de Espadas vermelho dele."
    "Na carta estava escrito: \'{i}O culpado é aquele com o chapéu e a indiferença gritante.{/i}\'"
    return

