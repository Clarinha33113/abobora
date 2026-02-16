
label dia2_acusar_thiago:
    show minato normal
    me "Pessoal, não percebem que essa discussão não está indo a lugar nenhum?"
    me "O verdadeiro culpado está tão claro quanto este lugar. Claramente, foi o [thiago]!"

    hide minato normal
    show thiago assustado

    thiago "Que isso... por favor, nós dois sabemos que isso não é verdade."

    hide thiago assustado
    show thiago normal

    call escolhas_acusar(
        personagem = 'thiago',
        passivo = 'Você demonstra saber como usar as pessoas.',
        agressivo = 'Sabemos? Faça-me o favor! Você é quem mais sai em benefício.',
        assertivo = 'É que tudo aponta para você. Você sabe se comunicar melhor do que todo mundo aqui.',
        passivo_agressivo = 'É claro que você é inocente... com essa atitude de cara bacana.'
    )

    call get_most_selected_choice
    python: # btw i went off script here too
        is_being_a_bitch = True if most_often_choice == CS_AGRESSIVO else False
        if is_being_a_bitch:
            aggressive_text = 'Jamais? E ainda consegue afirmar usando "jamais" como resposta.'
        else:
            aggressive_text = 'Você é claramente capaz de matar alguém.'

    call escolhas_acusar(
        personagem = 'thiago',
        passivo = 'Você pode até ter um ponto, mas a gente precisa de garantia.',
        agressivo = aggressive_text,
        assertivo = 'Isso soa ainda pior...',
        passivo_agressivo = 'Eu não te odeio. Eu só quero expor quem você realmente é.',
    )

    hide thiago normal
    jump dia2_depois_de_acusar


# Diálogos 1:

label dia2_acusar_thiago_passivo1:
    me "Eu acredito que, apesar da fachada de cara legal, você poderia estar agindo apenas em benefício próprio."
    thiago "Nossa, quanta frieza... eu jamais faria isso. Eu admito que tenho pena da [diana], mas não adianta chorar pelo leite derramado. Além do mais, o desejo não me interessa."
    "As pessoas parecem céticas em relação à minha acusação, [thiago] foi bom em convencê-los."
    return

label dia2_acusar_thiago_agressivo1:
    me "Seria fácil ganhar a confiança das pessoas, para depois obrigá-las a se matar e ficar com o desejo!"
    thiago "Nossa quanta frieza, eu jamais faria isso, eu admito que tenho pena da [diana], mas não adianta chorar pelo leite derramado, além do mais o desejo não me interessa."
    "As pessoas parecem céticas à minha acusação."
    return

label dia2_acusar_thiago_assertivo1:
    me "Você também não parece totalmente confiável. Como alguém consegue se manter tão calmo depois de um assassinato?"
    thiago "Não seja assim. Eu apenas sou calmo e já tinha uma armadilha preparada, caso o assassino viesse atrás de mim."
    "Todos parecem relutantes, mas estão considerando o que eu estou dizendo."
    return

label dia2_acusar_thiago_passivo_agressivo1:
    me "Que coisa estranha... você tem as habilidades necessárias para conseguir o que quer com facilidade. Você acha mesmo que engana alguém aqui?"
    thiago "Minha nossa, quanta crueldade... e quanta falsidade. Do jeito que você fala, parece que você me odeia."
    "Todos olham para mim com desconfiança."
    return

# Diálogos 2:

label dia2_acusar_thiago_passivo2:
    me "Você poderia estar mentindo. Eu suponho que, com suas habilidades, você poderia tê-la forçado a morrer e depois agir como se nada tivesse acontecido."
    thiago "Ah, [minato]... você está tentando me acusar ou só quer sugerir que eu sou o assassino?"
    "Todos olham para mim com pena."
    return

label dia2_acusar_thiago_agressivo2:
    me "Claramente, estamos vendo do que você é capaz!"
    thiago "Mas eu não fiz isso. Eu não queria que ela morresse. Eu queria ir para casa, mas, ao que parece, você está determinado a me matar."
    "Todos olham para mim com raiva."
    return

label dia2_acusar_thiago_assertivo2:
    me "Isso soa ainda pior. Você poderia tê-la forçado a tirar a própria vida e, depois, veio aqui pagar de bom detetive só para sair impune."
    thiago "Uma boa teoria, mas eu não aprovo, porque eu nunca faria isso."
    "Todos olham para o [thiago] com total desconfiança."
    return

label dia2_acusar_thiago_passivo_agressivo2:
    me "Você não passa de um vigarista. Tenta manipular todo mundo, mas provavelmente é só mais um egoísta que quer aquele desejo a todo custo."
    thiago "[minato], eu não esperava isso de você. Que provas disso você possui? Uma, duas, três... ou só está cuspindo seu sarcasmo?"
    "Parece que todos suspeitam de mim."
    return

