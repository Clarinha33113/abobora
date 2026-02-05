
label dia2_acusar_thiago:
    show minato normal
    me "Pessoal, não percebem que essa discussão não está indo a lugar nenhum?"
    me "O verdadeiro culpado está tão claro como esse lugar, claramente foi a [thiago]!"

    hide minato normal
    show thiago assustado

    thiago "Que isso, por favor nós dois sabemos que isso não é verdade."

    hide thiago assustado
    show thiago normal

    call escolhas_acusar(
        personagem = 'thiago',
        passivo = 'Você demonstra saber como usar as pessoas.',
        agressivo = 'Sabemos? Faça-me o favor! Você que mais sai em benefício.',
        assertivo = 'É que tudo é lógico, você sabe se comunicar melhor que todo mundo aqui.',
        passivo_agressivo = 'É claro que você é inocente, com essa atitude de cara bacana.'
    )

    call get_most_selected_choice
    python:
        is_being_a_bitch = True if most_often_choice == CS_AGRESSIVO else False
        if is_being_a_bitch:
            aggressive_text = 'Jamais? e consegue afirmar usando "jamais" como resposta.'
        else:
            aggressive_text = 'Você é claramente capaz de matar alguém.'

    call escolhas_acusar(
        personagem = 'thiago',
        passivo = 'Você pode até ter um ponto, mas a gente tem garantia.',
        agressivo = aggressive_text,
        assertivo = 'Isso soa ainda pior...',
        passivo_agressivo = 'Eu não te odeio, eu só quero expor quem você realmente é.',
    )

    call get_most_selected_choice

    # XXX: fazer algo diferente baseado em 'most_often_choice'

    thiago "você escolheu mais comunicação [most_often_choice]!"

    return


# Diálogos 1:

label dia2_acusar_thiago_passivo1:
    me "Eu acredito que apesar da fachada de cara legal, você facilmente poderia apenas estar trabalhando para si."
    thiago "Vamos Lá colega, eu não estou fingindo, eu posso não me importar com todo mundo, mas isso porque eu mal conheço vocês."
    "Todos olham para mim com pena, o [thiago] foi bom em convencer eles."
    return

label dia2_acusar_thiago_agressivo1:
    me "Seria fácil ganhar a confiança das pessoas, para depois obrigá-las a se matar e ficar com o desejo!"
    thiago "Nossa quanta frieza, eu jamais faria isso, eu admito que tenho pena da [diana], mas não adianta chorar pelo leite derramado, além do mais o desejo não me interessa."
    "As pessoas parecem céticas à minha acusação."
    return

label dia2_acusar_thiago_assertivo1:
    me "Você também não demonstra ser totalmente confiável, como alguém consegue se manter tão calmo após um assassinato?"
    thiago "Não seja assim, eu apenas sou calmo e já tinha uma armadilha reservada, caso o assassino viesse atrás de mim."
    "Todos parecem relutantes, porém parecem estar considerando o que eu estou dizendo."
    return

label dia2_acusar_thiago_passivo_agressivo1:
    me "Mas que coisa estranha, você tem as habilidades necessárias para conseguir o que deseja com facilidade, você acha mesmo que engana alguém aqui."
    thiago "Minha nossa quanta crueldade, e tanta falsidade, do jeito que você fala parece que você me odeia."
    "Todos olham para mim com desconfiança."
    return

# Diálogos 2:

label dia2_acusar_thiago_passivo2:
    me "Você facilmente poderia só estar mentindo, eu suponho que com suas habilidades, você poderia ter forçado ela a morrer, e depois agir como se nada tivesse acontecido."
    thiago "Ah [minato] você tá tentando me acusar, ou só queria sugerir que eu sou o assassino?"
    "Todos olham para mim com pena."
    return

label dia2_acusar_thiago_agressivo2:
    me "Claramente estamos vendo o quanto você é capaz de algo!"
    thiago "Mas eu não fiz isso, Eu não queria que ela morresse, eu queria ir para casa, mas ao que parece você está determinado a me matar."
    "Todos olham para mim com raiva."
    return

label dia2_acusar_thiago_assertivo2:
    me "Isso soa ainda pior. Você facilmente poderia ter a forçado a tirar a própria vida, aí veio aqui parecer o bom detetive, só para sair impune."
    thiago "Uma boa teoria, eu não aprovo pois eu nunca faria isso."
    "Todos olham para o [thiago] com total desconfiança."
    return

label dia2_acusar_thiago_passivo_agressivo2:
    me "Você não passa de um vigarista, tenta manipular todo mundo, mas provavelmente é só mais um egoísta que quer aquele desejo a todo custo."
    thiago "[minato], eu não esperava isso de você, quais provas disso você possui, 1, 2, 3 ou só está cuspindo seu sarcasmo."
    "Parece que todos suspeitam de mim."
    return

