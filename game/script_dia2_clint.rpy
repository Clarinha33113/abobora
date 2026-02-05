
label dia2_acusar_clint:
    show minato normal
    me "Pessoal, não percebem que essa discussão não está indo a lugar nenhum?"
    me "O verdadeiro culpado está tão claro como esse lugar, claramente foi a [clint]!"

    hide minato normal
    show clint normal

    clint "Como é que é, você acha que eu sou o assassino!?"

    call escolhas_acusar(
        personagem = 'clint',
        passivo = 'Eu não tenho certeza, mas tem detalhes estranhos sobre você, em especial o seu título que indica isso.',
        agressivo = 'É, eu acho',
        assertivo = 'Sim eu acho, pois existem pistas que levam até você.',
        passivo_agressivo = 'Eu não sei, é que soa suspeito um cara chamado [clint], não ameaçar alguém com sei lá, sua pistola.',
    )

    call escolhas_acusar(
        personagem = 'clint',
        passivo = 'Porque os meus instintos indicam isso.',
        agressivo = 'Para trazer justiça pela sua ação, você pode não demonstrar mas creio que logo todos viram quem você é.',
        assertivo = 'Você sabe que isso te torna mais suspeito.',
        passivo_agressivo = 'Vejam todos o desespero dele.'
    )

    return

#Dialogos 1:

label dia2_acusar_clint_passivo1:
    clint "Você não tem certeza, então por que você me acusa?"
    "Todos parecem confusos."
    return

label dia2_acusar_clint_agressivo1:
    me "Seu nome é compartilhado por algumas das pessoas mais violentas do mundo, e você facilmente poderia estar tentando manipular todo mundo, com essa atitude de bom colega."
    clint "Sua acusação é infundada, e pra que essa violência toda?"
    "Todos olham para mim com desconfiança e raiva."
    return

label dia2_acusar_clint_assertivo1:
    me "Primeiro você se chama o [clint], isso indica que você facilmente poderia ter usado sua arma ou faca, para ameaçar ela a se matar."
    clint "Em primeiro lugar isso é um absurdo, eu nem tenho mais a minha arma, algum bastardo roubou, além do mais eu não escondo que quero fugir desse lugar."
    "Os olhares se voltam para o [clint] com desconfiança."
    return

label dia2_acusar_clint_passivo_agressivo1:
    clint "Espero que não esteja insinuando o que eu imagino, seu bastardo."
    "Todos olham para mim, surpresos mas não de um modo positivo."
    return

#Dialogos 2:

label dia2_acusar_clint_passivo2:
    me "Você pode estar escondendo o álibi para matar, pois eu suponho pelo seu nome que você sabe matar melhor que todos aqui."
    clint "Eu sei, mas jamais faria isso."
    "Agora todo mundo parace totalmente perdidos"
    return

label dia2_acusar_clint_agressivo2:
    clint "Você perdeu a sua mente, eu não fiz aquilo."
    "Ninguém parece acreditar em mim."
    return

label dia2_acusar_clint_assertivo2:
    me "Você pode dizer isso, mas facilmente pode estar fingindo estar querendo sair ou ajudar, só para passar a imagem de aliado dedicado."
    clint "Isso não é verdade, eu garanto a todos que não fiz aquilo."
    "Todos olham para ele com ainda mais suspeita."
    return

label dia2_acusar_clint_passivo_agressivo2:
    me "Você parece estar contra a parede, suas mentiras estão caindo, você parece estar dedicado, provavelmente sua máscara caiu, e agora sabemos quem você realmente é."
    clint "O mesmo pode ser dito por você, é tu quem está determinado a ganhar."
    "Todos olham para você com uma forte suspeita."
    return

