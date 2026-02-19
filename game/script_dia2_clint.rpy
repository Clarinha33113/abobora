
label dia2_acusar_clint:
    show minato normal
    me "Pessoal, não percebem que essa discussão não está indo a lugar nenhum?"
    me "O verdadeiro culpado está tão claro quanto este lugar. Claramente, foi o [clint]!"

    hide minato normal
    show clint normal

    clint "Como é que é? Você acha que eu sou o assassino?!"

    # XXX: no name substitution here what the hell
    call escolhas_acusar(
        personagem = 'clint',
        passivo = 'Eu não tenho certeza, mas há detalhes estranhos sobre você, especialmente o seu título. Isso levanta dúvidas.',
        agressivo = 'Sim, e você sabe exatamente porquê.',
        assertivo = 'Sim. Existem pistas que levam até você, e eu não posso ignorá-las.',
        passivo_agressivo = 'Eu não sei... mas é curioso um cara chamado Pistoleiro não ter ameaçado ninguém com, sei lá, a própria pistola.',
    )

    call escolhas_acusar(
        personagem = 'clint',
        passivo = 'Porque meus instintos estão apontando para você.',
        agressivo = 'Para trazer justiça pelo que você fez. Pode até tentar esconder, mas logo todos vão ver quem você realmente é.',
        assertivo = 'Você sabe que essa atitude só te torna ainda mais suspeito.',
        passivo_agressivo = 'Vejam todos o desespero dele... parece alguém que foi pego no flagra.'
    )

    hide clint normal
    jump dia2_depois_de_acusar

#Dialogos 1:

label dia2_acusar_clint_passivo1:
    clint "Você não tem certeza, então por que está me acusando?"
    "Todos parecem confusos."
    return

label dia2_acusar_clint_agressivo1:
    me "Seu nome é compartilhado por algumas das pessoas mais violentas do mundo, e você facilmente poderia estar tentando manipular todo mundo com essa atitude de bom colega."
    clint "Sua acusação é infundada. E pra que toda essa violência?"
    "Todos olham para mim com desconfiança e raiva."
    return

label dia2_acusar_clint_assertivo1:
    me "Primeiro, você se chama [clint]. Isso indica que você facilmente poderia ter usado sua arma ou faca para ameaçá-la a se matar."
    clint "Em primeiro lugar, isso é um absurdo. Eu nem tenho mais a minha arma, algum bastardo a roubou. Além do mais, eu não escondo que quero fugir deste lugar."
    "Os olhares se voltam para o [clint] com desconfiança."
    return

label dia2_acusar_clint_passivo_agressivo1:
    clint "Espero que não esteja insinuando o que eu imagino, seu bastardo."
    "Todos olham para mim, surpresos, mas não de um modo positivo."
    return

#Dialogos 2:

label dia2_acusar_clint_passivo2:
    me "Você pode estar escondendo um álibi para matar, pois eu suponho, pelo seu nome, que você sabe matar melhor do que todos aqui."
    clint "Eu sei, mas jamais faria isso."
    "Agora todo mundo parece totalmente perdido."
    return

label dia2_acusar_clint_agressivo2:
    clint "Você perdeu a cabeça? Eu não fiz aquilo!"
    "Ninguém parece acreditar em mim."
    return

label dia2_acusar_clint_assertivo2:
    me "Você pode dizer isso, mas facilmente pode estar fingindo querer sair ou ajudar, só para passar a imagem de aliado dedicado."
    clint "Isso não é verdade. Eu garanto a todos que não fiz aquilo."
    "Todos olham para ele com ainda mais suspeita."
    return

label dia2_acusar_clint_passivo_agressivo2:
    me "Você parece estar contra a parede. Suas mentiras estão caindo. Você parecia dedicado, mas provavelmente sua máscara caiu, e agora sabemos quem você realmente é."
    clint "O mesmo pode ser dito sobre você. É você quem está determinado a ganhar."
    "Todos olham para você com forte suspeita."
    return

