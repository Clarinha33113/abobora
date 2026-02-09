
label dia2_acusar_sofia:
    show minato normal
    me "Pessoal, não percebem que essa discussão não está indo a lugar nenhum?"
    me "O verdadeiro culpado está tão claro como esse lugar, claramente foi a [sofia]!"

    hide minato normal
    show sofia irritada
    sofia "Como você ousa me acusar, seu verme patético!"

    hide sofia irritada
    show sofia decepcionada

    call escolhas_acusar(
        personagem = 'sofia',
        passivo = 'Eu só estou apontando o quão conveniente é para você.',
        agressivo = 'Fale o que você quiser mas todos nós sabemos a verdade.',
        assertivo = 'É esse tipo de atitude que te torna suspeita.',
        passivo_agressivo = 'Eu não sei, talvez apontando para a coisa mais obvia.'
    ) from _call_escolhas_acusar_11

    call escolhas_acusar(
        personagem = 'sofia',
        passivo = 'Busco achar uma lógica, mesmo que seja conveniente, é melhor que não ter nenhuma teoria.',
        agressivo = 'É você? Está ao menos fazendo alguma coisa? Ao menos eu estou fazendo algo além de ficar parado!',
        assertivo = 'É justamente isso que te torna mais suspeita.',
        passivo_agressivo = 'É mesmo, ou você apenas está se esquivando?'
    ) from _call_escolhas_acusar_12

    call get_most_selected_choice from _call_get_most_selected_choice_5

    hide sofia decepcionada
    jump dia2_depois_de_acusar


# Diálogos 1:

label dia2_acusar_sofia_passivo1:
    me "Você tem agido com frieza extrema realicionada a todo mundo, você não se importaria se qualquer um de nós morresse, pois no fim eu suponho que seja conveniente ao seu plano."
    sofia "Você vai mesmo basear sua acusação em uma suposição, o que impede que você seja o assassino?"
    "Os olhares parecem confusos sobre a minha suposição"
    return


label dia2_acusar_sofia_agressivo1:
    me "Você desde o início tem intimidado todo mundo, você pouco se importa se vamos morrer, você só liga pra esse desejo acima das vidas alheias!"
    sofia "E porque eu deveria me importar com seres tão patéticos como você, e se eu tivesse matado a Desenhista você nunca saberia, pois diferente de você eu saberia o que eu estou fazendo."
    "Todos olham assustados pra mim e para ela."
    return

label dia2_acusar_sofia_assertivo1:
    me "Desde o começo você nunca escondeu o quanto você pouco se importa, além que você tomou atitudes que são apenas convenientes a você."
    sofia "A minha atitude tem sido realista a esse lugar, porque eu deveria ligar para pessoas que eu nem conheço?"
    "Todos olharam para ela poucos com raiva e outros desconfiados."
    return

label dia2_acusar_sofia_passivo_agressivo1:
    me "Você está tentando parecer a vítima, mas você se mostra a mais culpada aqui, para alguém com um carinha de anjo você é muito cruel, talvez um resultado esperado de um monstro sem coração, que mataria qualquer um por poder."
    sofia "Como você tem a audácia de me acusar sem provas reais, apelando para esse sarcasmo inútil."
    "Todos olham para mim com desconfiança."
    return

# Diálogos 2:

label dia2_acusar_sofia_passivo2:
    sofia "Isso é sério, você acha mesmo que alguém aqui ligaria para isso, você não tem provas, só está se baseando na sua lógica falha, algo totalmente esperado de um idiota."
    "Ao que parece ninguém acredita em mim."
    return

label dia2_acusar_sofia_agressivo2:
    sofia "É isso que você acha, eu estou investigando como todo mundo, você é só uma escória que se baseia nos seus gritos desesperados."
    "Todos olham para mim com um mau olhar."
    return

label dia2_acusar_sofia_assertivo2:
    me "Com base em nossas informações levo a crer que você facilmente tem acesso a uma das roupas do assassino, além de como você trabalha e fala com o público, poderia muito bem convencer de maneira sutil ou manipuladora que a [diana] se matasse."

    sofia "Como?! Ainda sim isso não prova nada, Eu não tenho motivos para fazer isso, é mais fácil deixar outros fazerem isso."

    "Todos olham para ela com total desconfiança."
    return

label dia2_acusar_sofia_passivo_agressivo2:
    me "Seja sincera, é difícil admitir que matou ela, dá pra ver o quão conveniente é para você, a desenhista era de longe a mais vulnerável aqui, perfeita para você fazer seu teste, ai achou que ia sair impune."

    sofia "Sua teoria é ridícula, isso não faz sentido, mas tenho que concordar que é conveniente, especialmente para quem me acusa."
    return

