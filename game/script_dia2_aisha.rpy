
label dia2_acusar_aisha:
    show minato normal
    me "Pessoal, não percebem que essa discussão não está indo a lugar nenhum?"
    me "O verdadeiro culpado está tão claro quanto este lugar. Claramente, foi a [aisha]!"

    hide minato normal
    show aisha assustada

    aisha "Com base em quais provas você afirma isso? Sua afirmação é um completo absurdo. Facilmente poderia ser você, só querendo desviar a atenção para mim."

    hide aisha assustada
    show aisha normal

    call escolhas_acusar(
        personagem = 'aisha',
        passivo = 'Eu não estou acusando por certeza. Só estou seguindo um palpite.',
        agressivo = 'Besteira. Você é claramente a culpada.',
        assertivo = 'Eu não estou tentando desviar a atenção. E tenho provas para sustentar o que estou dizendo.',
        passivo_agressivo = 'É mesmo... falou o próprio poço de inocência...'
    )

    call escolhas_acusar(
        personagem = 'aisha',
        passivo = 'Eu só estou apontando as inconsistências da sua versão.',
        agressivo = 'Além da sua atitude, você praticamente exala culpa.',
        assertivo = 'Você afirma estar ajudando na investigação, mas o que impede você de ter adulterado as provas?',
        passivo_agressivo = 'Engraçado como tudo, quando envolve você, soa conveniente demais.'
    )

    hide aisha normal
    jump dia2_depois_de_acusar


label dia2_acusar_aisha_passivo1:
    me "As provas, do meu ponto de vista, apontam para você, especialmente pela sua total indiferença à morte dela."
    aisha "Você fala como se só eu fosse indiferente. Alguns aqui também são. Você também demonstrou frieza com a morte dela."
    "Todos olham para mim com pena."
    return

label dia2_acusar_aisha_agressivo1:
    me "Você demonstra se importar pouco com qualquer um aqui. Você mesma mataria qualquer um mais vulnerável, especialmente ela."
    aisha "Eu admito que você é rápido em acusar alguém, mas seu erro é que todos aqui, no fim, desejam o poder da torre. Minha atitude não é diferente da de qualquer um aqui."
    "Todos olham para mim; alguns com medo e outros, irritados."
    return

label dia2_acusar_aisha_assertivo1:
    me "Eu observei toda a situação, e você, dentre todos, tem agido com maior indiferença. Você estava perto do corpo, apenas criticando, sem compartilhar nenhuma informação com o [clint]."
    aisha "O quê? Como você ousa? Eu estava investigando como todo mundo. O [clint] só era incompetente demais para merecer a minha ajuda!"
    "Todos olham para mim com uma expressão pensativa."
    return

label dia2_acusar_aisha_passivo_agressivo1:
    me "Eu estava pensando nos detalhes e, sabe, tudo soa suspeito vindo de você. Eu tô apenas seguindo a minha intuição, e, de todos aqui, você soa a mais suspeita, especialmente pela sua indiferença."
    aisha "Minha indiferença? Você fala como se fosse melhor. Você acha que uma investigação séria usa apenas a intuição?"
    "Todos olham para mim; alguns com dúvidas e outros com desconfiança."
    return

label dia2_acusar_aisha_passivo2:
    me "Você não demonstra se importar com ninguém aqui. A [diana] parecia o alvo fácil, e você demonstra saber como orquestrar tudo isso."
    aisha "Você tá tentando me acusar ou sugerir que eu sou a culpada? Me digam: vocês todos realmente vão levar ele em consideração?"
    return

label dia2_acusar_aisha_agressivo2:
    me "Você tem tentado agir como uma boa samaritana, mas, no fundo, só nos vê como peões em um jogo."
    me "A [diana] era o alvo fácil no seu jogo. Para uma governante, você tem se esquecido de que também pode ser julgada!"
    aisha "Olhe o tom. Você acha mesmo que gritar vai ajudar em algo? Você não só não tem provas, como a sua suposição está errada."
    "Todos parecem ficar cada vez mais assustados."
    return

label dia2_acusar_aisha_assertivo2:
    me "No local do assassinato, você tem o álibi de alguém que gosta de agir sozinha, mas que é plenamente capaz de orquestrar tudo, e com certeza alguém que superestima a própria inteligência."
    aisha "Uma boa suposição. Eu quase me senti ameaçada. Pena que suas provas sejam tão reais quanto o [clint] é inteligente."
    "Todos olham para a [aisha] com desconfiança, e o [clint] fixa o olhar nela, visivelmente ofendido."
    return

label dia2_acusar_aisha_passivo_agressivo2:
    me "Mas é claro que a vossa inocente aqui não tem nada a ver. Mais estranho é como suas palavras são falsas. Você só queria testar o quão burros somos para tentar vencer fácil."
    aisha "Você chega a ser desprezível com esse sarcasmo, Espectador. Acha mesmo que vai convencer alguém com essa falsidade?"
    "Todos me olham; alguns com pena no olhar, já outros deixam claro seu desprezo."
    return

