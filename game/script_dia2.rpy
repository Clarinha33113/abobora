label dia2_start:
    scene black with dissolve
    show text "Dia 2" with Pause(2)
    scene black with dissolve

    me "Essa noite foi diferente.Não tive aquele sonho.Em vez disso, vi uma garota assustada"
    
    me "À sua frente, havia uma figura…parecia ter controle sobre ela,fazendo-a tirar a própria vida"

    scene bg cozinha_torre with dissolve

    "[my_name] acorda com um grito, e logo ele segue outros até a cozinha."

    # ao entrar uma música sinistra começa a tocar e vemos todos assustados

    me "A [diana], ela, ela tá morta com uma faca no peito, uma expressão de agonia em sua face"
    me "eu não sei o que dizer, tem tanto sangue que eu-"

    scene bg tribunal with dissolve

    "Subitamente todos aparecem no tribunal e no meio [vince]"

    show vince normal
    vince "Bom dia a todos, por que as caras feias neste dia tão adorável?"

    hide vince normal
    show sofia decepcionada
    sofia "É porque tem um corpo morto aqui seu gato estúpido."

    hide sofia decepcionada
    show vince normal

    vince "Para que tanta agressividade, [sofia]?"
    vince "vocês todos deveriam estar felizes, pois vocês escolheram o final bom!!"

    # tocar musica de comemoração

    hide vince normal
    show nina enojada
    nina "Bom?! A [diana] foi morta, como isso é bom?!"

    hide nina enojada
    show vince normal
    vince "É simples, quando alguém morre isso significa que vocês escolheram ficar!!"

    hide vince normal
    show clint irritado

    clint "Mas isso não é justo!"

    hide clint irritado
    show vince normal

    vince "Regras são regras."
    vince "Agora vocês têm a manhã para descobrir quem é o assassino"
    vince "e se conseguirem vocês avançam para o próximo nível."

    vince "Mas se falharem escolhendo a pessoa errada..."

    hide vince normal

    scene bg tudo_vermelho_lmao with dissolve
    show vince emo_idk

    show text "{b}Vocês todos morrem e o assassino vence.{/b}" with Pause(4)

    hide vince emo_idk
    scene bg tribunal with dissolve

    show vince normal

    vince "Agora vocês estão dispensados."

    jump dia2_cena1_escolhas

label dia2_cena1_escolhas:
    scene bg tribunal with dissolve

    menu:
        me "Para onde vou?"

        "Direta":
            jump dia2_cena1_direita
        "Centro":
            jump dia2_cena1_centro
        "Esquerda":
            jump dia2_cena1_esquerda
        "Quarto":
            jump dia2_cena1_quarto

    return

label dia2_cena1_direita:
    scene bg cozinha_torre with dissolve

    menu:
        "[clint], [felix] e [aisha] estão na cozinha."

        "Falar com eles":
            pass
        "Voltar":
            jump dia2_cena1_escolhas

    show felix pensativo
    felix "Pobrezinha, ela provavelmente não aguentou a pressão"
    felix "mas por que ela faria isso, porque ela não esperou?"

    hide felix pensativo
    show minato normal
    me "Ela parecia estar bem desesperada ontem, mas e se ela foi assassinada?"

    hide minato normal
    show felix pensativo
    felix "Isso mudaria o cenário drasticamente, mas faria sentido considerando o que o Vince disse"
    felix "é que só de olhar soa que ela se matou"

    hide felix pensativo
    show minato normal
    me "Você suspeita de alguém?"

    hide minato normal
    show felix pensativo
    felix "Sinceramente sim, eu falei com todo mundo e aquele [thiago] soa o mais suspeito"
    felix "ele foi muito indiferente a morte dela"

    hide felix pensativo
    # transição????

    show clint feliz
    clint "Olá [minato], eu estava analisando o cadáver dela, e percebi um detalhe relevante"

    hide clint feliz
    show minato assustado
    me "Que seria?"

    hide minato assustado
    show clint normal
    clint "Ela foi perfurada 17 vezes, mas todos de um modo totalmente desesperado e amador"
    clint "O que indica que ou o assassino é muito desleixado ou ela se matou"

    hide clint normal
    show minato normal
    me "Pelo que o [vince] disse é mais provável que ela tenha sido assassinada"

    hide minato normal
    show clint normal
    clint "Definitivamente é justamente por isso que eu acredito que ela foi coagida a fazer isso ou só ameaçada mesmo"

    hide clint normal

    # TRANSIÇÃO??????????

    show aisha pensativa
    aisha "Uma pena que as coisas chegaram a esse ponto, ela foi indiscutivelmente assassinada"
    aisha "Mas a morte dela me indicou algumas pontas soltas"    

    aisha "Primeiro que ela provavelmente foi forçada a fazer esse ato"
    aisha "E considerando as pequenas manchas no chão tinha mais alguém"
    aisha "Um detalhe pequeno que o [clint] falhou em notar"

    hide aisha pensativa
    show minato normal
    me "E você conseguiu identificar alguma outra informação?"

    hide minato normal
    show aisha normal
    aisha "Sim, quem fez isso usa sapatos"

    hide aisha normal
    show minato normal
    me "E como você sabe disso se a mancha é tão pequena"

    hide minato normal
    show aisha normal
    aisha "É simples, diferente de qualquer um aqui eu notei o formato da sola"

    # ......

    menu:
        "Voltar":
            jump dia2_cena1_escolhas

    return

label dia2_cena1_centro:
    scene bg sala_recreacao with dissolve
    menu:
        "[my_name] chega em uma sala de recreação onde aqui estão [joana], [nina] e [mitchell]"

        "Falar com um deles":
            pass
        "Voltar":
            jump dia2_cena1_escolhas


    # "Nina tá bem abalada, e a Joana felizmente está consolando ela"

    show joana normal
    joana "Olá [minato], veio ver a [nina]?"

    hide joana normal
    show minato normal
    me "Sim, como ela está, você acha que ela vai se recuperar?"

    hide minato normal
    show joana normal
    joana "Creio que sim, eu só me pergunto que tipo monstro faria aquilo"
    joana "A [diana] não machucaria ninguém"
    joana "Agora o assassino tentou fazer parecer que ela tirou a própria vida"

    hide joana normal
    show minato normal
    me "Conhecendo a humanidade eu não duvido de nada"
    me "Eu tô feliz que você esteja ajudando a Confeiteira, se depender de mim eu vou achar o culpado"

    hide minato normal
    show joana normal
    joana "Por favor faça isso"

    hide joana normal

    # transição........

    show mitchell normal
    mitchell "E ai [minato] tá investigando a garota morta?"

    hide mitchell normal
    show minato normal
    me "Sim, você não parece muito preocupado"

    hide minato normal
    show mitchell normal
    mitchell "É que diferente de vocês eu não tenho medo desse assassino"
    
    hide mitchell normal
    show minato normal
    me "Você é bem confiante"

    hide minato normal
    show mitchell normal
    mitchell "Mas é claro, se o assassino vir atrás de mim eu vou arrebentar a cara dele com os meus passos"

    # TRANSIÇÃOOOOOOOOOOOOOOOOOO
    menu:
        "Voltar":
            jump dia2_cena1_escolhas

    return

label dia2_cena1_esquerda:
    menu:
        "Posso ir há biblioteca ou a quadra."

        "Biblioteca":
            jump dia2_cena1_biblioteca
        "Quadra":
            jump dia2_cena1_quadra
        "Voltar":
            jump dia2_cena1_escolhas


label dia2_cena1_biblioteca:
    scene bg biblioteca with dissolve

    menu:
        "[sofia] e [thiago] estão na biblioteca."

        "Falar com eles":
            pass
        "Voltar":
            jump dia2_cena1_esquerda

    show sofia irritada
    sofia "Livros estúpidos, livros inúteis"

    me "A [sofia] está lendo e jogando vários livros no chão ao ponto de formar uma pilha, consigo ver que são vários livros de investigação ou detetives"

    hide sofia irritada
    show minato normal
    me "[sofia], você não descobriu nada pelo que posso ver"

    hide minato normal
    show sofia irritada
    sofia "E o que isso deveria significar!"

    hide sofia irritada
    show minato normal
    me "É que você tá jogando vários livros no chão"

    hide minato normal
    show sofia irritada
    sofia "Ah sim, é que esses livros são todos inúteis"

    hide sofia irritada
    show minato normal
    me "Por quê?"

    hide minato normal
    show sofia irritada
    sofia "Porque são todos livros infantis e romances policiais tão exagerados que é óbvio que nada disso funciona na realidade"

    sofia "O que não serve de nada em um lugar onde temos que investigar assassinos"

    hide sofia irritada
    show minato normal
    me "Você tem uma ideia sobre o assassino?"

    hide minato normal
    show sofia decepcionada
    sofia "Mas é claro, esse assassino é tão ignorante ao acreditar que eu não saberia o quão óbvio é o crime dele"

    sofia "O assassino claramente forçou ela a se matar a colocando contra a parede onde ela não tinha escolha"

    hide sofia decepcionada
    show minato normal
    me "Você definitivamente está bem determinada a encontrar ele, mais que todo mundo"

    hide minato normal
    show sofia normal
    sofia "Pode apostar que eu estou, nenhum assassino estúpido vai me enganar"

    hide sofia normal

    # TRANSIÇÃOOOOOOOOOOOOOOOOOOAAAAAAAAAAAAAAAAAASLFAKOHIHFLKASFHJKASLHJKZNV<U(@Q)THPQOWQHFASOHFAPOHOIHOGOIWF

    show thiago normal
    thiago "Como vai meu caro companheiro [minato]!"

    hide thiago normal
    show minato normal
    me "Bem, o que tá fazendo só olhando as prateleiras?"

    hide minato normal
    show thiago normal
    thiago "Mas é claro que não" # ???????????
    thiago "eu estava procurando alguma boa leitura que auxilie todos nós nesta investigação."

    hide thiago normal
    show minato normal
    me "Boa, encontrou algo?"

    hide minato normal
    show thiago normal
    thiago "Infelizmente não, mas eu vou continuar não se preocupe meu amigo"

    hide thiago normal

    me "Isso foi estranho"
    # "Última opção é voltar ao quarto para esperar o horário do tribunal"

    menu:
        "Voltar":
            jump dia2_cena1_escolhas

    return

label dia2_cena1_quarto:
    scene bg quarto

    me "É melhor eu descansar por enquanto, pois logo terei que garantir que o real culpado seja descoberto, ou eu e todos vamos morrer..."
    me "Pelo menos eu sei que o culpado é capaz de intimidar alguém, manipular ou controlar."

    jump dia2_cena2_tribunal


label dia2_cena2_tribunal:
    scene black with dissolve
    show text "Tribunal" with Pause(2)
    scene black with dissolve

    scene bg tribunal with dissolve

    "Todos são teletransportado até o tribunal"

    # som do minato caindo

    me "Eu acho que nunca vou me acostumar com essa droga de teletransporte."

    show vince normal
    vince "Senhoras e senhores sejam bem-vindos ao primeiro caso da 21° edição do tribunal do desejo, e eu serei o grande apresentador e juiz."

    return
