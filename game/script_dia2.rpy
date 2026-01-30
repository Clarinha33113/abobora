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

        "Direto":
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

    felix "Pobrezinha, ela provavelmente não aguentou a pressão"
    felix "mas por que ela faria isso, porque ela não esperou?"

    me "Ela parecia estar bem desesperada ontem, mas e se ela foi assassinada?"

    felix "Isso mudaria o cenário drasticamente, mas faria sentido considerando o que o Vince disse"
    felix "é que só de olhar soa que ela se matou"

    me "Você suspeita de alguém?"

    felix "Sinceramente sim, eu falei com todo mundo e aquele Esperto soa o mais suspeito"
    felix "ele foi muito indiferente a morte dela"

    clint "Olá Espectador, eu estava analisando o cadáver dela, e percebi um detalhe relevante"

    me "Que seria?"

    clint "Ela foi perfurada 17 vezes, mas todos de um modo totalmente desesperado e amador"
    clint "O que indica que ou o assassino é muito desleixado ou ela se matou"

    me "Pelo que o Vince disse é mais provável que ela tenha sido assassinada"

    clint "Definitivamente é justamente por isso que eu acredito que ela foi coagida"
    clint "A fazer isso ou só ameaçada mesmo"

    aisha "Uma pena que as coisas chegaram a esse ponto, ela foi indiscutivelmente assassinada"
    aisha "Mas a morte dela me indicou algumas pontas soltas"    

    aisha "Primeiro que ela provavelmente foi forçada a fazer esse ato"
    aisha "E considerando as pequenas manchas no chão tinha mais alguém"
    aisha "Um detalhe pequeno que o Clint falhou em notar"

    me "E você conseguiu identificar alguma outra informação?"

    aisha "Sim, quem fez isso usa sapatos"

    me "E como você sabe disso se a mancha é tão pequena"

    aisha "É simples, diferente de qualquer um aqui eu notei o formato da sola"

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


    "Nina tá bem abalada, e a Joana felizmente está consolando ela"

    joana "Olá Espectador, veio ver a Confeiteira?"

    me "Sim, como ela está, você acha que ela vai se recuperar?"

    joana "Creio que sim, eu só me pergunto que tipo monstro faria aquilo"
    joana "A Desenhista não machucaria ninguém"
    joana "Agora o assassino tentou fazer parecer que ela tirou a própria vida"

    me "Conhecendo a humanidade eu não duvido de nada"
    me "Eu tô feliz que você esteja ajudando a Confeiteira, se depender de mim eu vou achar o culpado"

    joana "Por favor faça isso"

    mitchell "E ai Espectador tá investigando a garota morta?"

    me "Sim, você não parece muito preocupado"

    mitchell "É que diferente de vocês eu não tenho medo desse assassino"

    me "Você é bem confiante"

    mitchell "Mas é claro, se o assassino vir atrás de mim"
    mitchell "eu vou arrebentar a cara dele com os meus passos"

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

    "[sofia] e [thiago] estao na biblioteca."

    sofia "Livros estúpidos, livros inúteis"

    "A Contadora está lendo e jogando vários livros no chão ao ponto de formar uma pilha" 
    "eu consigo ver que são vários livros de investigação ou detetives"  

    me "Contadora, você não descobriu nada pelo que posso ver"

    sofia "E o que isso deveria significar!"

    me "É que você tá jogando vários livros no chão"

    sofia "Ah sim, é que esses livros são todos inúteis"

    me "Por que?"

    sofia "Porque são todos livros infantis" 
    sofia "E romances policiais tão exagerados que é óbvio que nada disso funciona na realidade"

    sofia "O que não serve de nada em um lugar onde temos que investigar assassinos"

    me "Você tem uma ideia sobre o assassino?"

    sofia "Mas é claro, esse assassino é tão ignorante ao acreditar que eu não saberia o quão óbvio"
    sofia "E o crime dele"

    sofia "O assassino claramente forçou ela a se matar"
    sofia "Colocando contra a parede onde ela não tinha escolha"

    me "Você definitivamente está bem determinada a encontrar ele, mais que todo mundo"

    sofia "Pode apostar que eu estou, nenhum assassino estúpido vai me enganar"

    thiago "Como vai meu caro companheiro Espectador!"

    me "Bem, o que tá fazendo só olhando as prateleiras?"

    thiago "Mas é claro que não"
    thiago "eu estava procurando alguma boa leitura que auxilie todos nós nesta investigação."

    me "Boa, encontrou algo?"

    thiago "Infelizmente não, mas eu vou continuar não se preocupe meu amigo"

    "Isso foi estranho"

    "Última opção é voltar ao quarto para esperar o horário do tribunal"

    menu:
        "Voltar":
            jump dia2_cena1_escolhas

    return

label dia2_cena1_quarto:
    scene bg quarto
    menu:
        "Dormir":
            pass
        "Voltar":
            jump dia2_cena1_escolhas
    
    return
