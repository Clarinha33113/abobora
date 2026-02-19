
label dia2_acusar_sofia:
    show minato normal
    me "Pessoal, não percebem que essa discussão não está indo a lugar nenhum?"
    me "O verdadeiro culpado está tão claro quanto este lugar. Claramente, foi a [sofia]!"

    hide minato normal
    show sofia irritada
    sofia "Como você ousa me acusar, seu verme patético?!"

    hide sofia irritada
    show sofia decepcionada

    call escolhas_acusar(
        personagem = 'sofia',
        passivo = 'Eu só estou apontando o quão conveniente isso é para você.',
        agressivo = 'Eu só estou apontando o quão conveniente isso é para você.',
        assertivo = 'É exatamente esse tipo de atitude que te torna suspeita.',
        passivo_agressivo = 'Eu não sei... talvez eu esteja apenas apontando para o mais óbvio.'
    )

    call escolhas_acusar(
        personagem = 'sofia',
        passivo = 'Estou tentando encontrar alguma lógica. Mesmo que seja conveniente, ainda é melhor do que não ter teoria nenhuma.',
        agressivo = 'E você? Está ao menos fazendo alguma coisa? Pelo menos eu estou fazendo algo além de ficar parado!',
        assertivo = 'É justamente isso que te torna ainda mais suspeita.',
        passivo_agressivo = 'É mesmo? Ou você só está tentando se esquivar?'
    )

    hide sofia decepcionada
    jump dia2_depois_de_acusar


# Diálogos 1:

label dia2_acusar_sofia_passivo1:
    me "Você tem agido com frieza extrema em relação a todos aqui. Você não se importaria se qualquer um de nós morresse, porque, no fim, isso seria conveniente para o seu plano."
    sofia "Você vai mesmo basear sua acusação em uma suposição? O que impede que você seja o assassino?"
    "Os olhares parecem confusos diante da minha suposição."
    return


label dia2_acusar_sofia_agressivo1:
    me "Desde o início você tem intimidado todo mundo. Pouco se importa se vamos morrer. Você só liga para esse desejo acima das vidas alheias!"
    sofia "E por que eu deveria me importar com seres tão patéticos como você? E, se eu tivesse matado a Desenhista, você nunca saberia. Diferente de você, eu saberia o que estou fazendo."
    "Todos olham assustados para mim e para ela."
    return

label dia2_acusar_sofia_assertivo1:
    me "Desde o começo você nunca escondeu o quanto pouco se importa. Além disso, tomou atitudes que são convenientes apenas para você."
    sofia "Minha atitude tem sido realista diante deste lugar. Por que eu deveria me importar com pessoas que nem conheço?"
    "Todos olham para ela; alguns com raiva, outros desconfiados."
    return

label dia2_acusar_sofia_passivo_agressivo1:
    me "Você tenta parecer a vítima, mas se mostra a mais suspeita aqui. Para alguém com carinha de anjo, você é extremamente cruel. Talvez seja o resultado esperado de alguém que mataria qualquer um por poder."
    sofia "Como você tem a audácia de me acusar sem provas reais, apelando para esse sarcasmo inútil?"
    "Todos olham para mim com desconfiança."
    return

# Diálogos 2:

label dia2_acusar_sofia_passivo2:
    sofia "Isso é sério? Você acha mesmo que alguém aqui levaria isso a sério? Você não tem provas, só está se baseando na sua lógica falha, algo totalmente esperado de um idiota."
    "Ao que parece, ninguém acredita em mim."
    return

label dia2_acusar_sofia_agressivo2:
    sofia "Isso é sério? Você acha mesmo que alguém aqui levaria isso a sério? Você não tem provas, só está se baseando na sua lógica falha, algo totalmente esperado de um idiota."
    "Todos olham para mim com reprovação."
    return

label dia2_acusar_sofia_assertivo2:
    me "Com base nas informações que temos, levo a crer que você facilmente teria acesso às roupas do assassino. Além disso, pela forma como fala e lida com o público."
    me "Poderia muito bem convencer alguém, de maneira sutil ou manipuladora, a tirar a própria vida."

    sofia "Como?! Ainda assim isso não prova nada. Eu não tenho motivos para fazer isso. Seria mais fácil deixar outra pessoa fazer."

    "Todos olham para ela com desconfiança."
    return

label dia2_acusar_sofia_passivo_agressivo2:
    me "Seja sincera. É difícil admitir que a matou? Dá para ver o quão conveniente isso seria para você."
    me "A Desenhista era, de longe, a mais vulnerável aqui. Perfeita para testar seu plano... e você achou que sairia impune."

    sofia "Sua teoria é ridícula. Não faz sentido algum. Mas tenho que admitir que é conveniente... especialmente para quem está me acusando."
    return

