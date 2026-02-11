label dia2_start:
    $ dia = 2
    scene black with dissolve
    show text "Dia 2" with Pause(2)
    scene black with dissolve

    me "Essa noite foi diferente. Não tive aquele sonho. Em vez disso, vi uma garota assustada"

    me "À sua frente, havia uma figura... parecia ter controle sobre ela, fazendo-a tirar a própria vida"

    scene bg cozinha_sangue with dissolve

    play sound "scream.mp3"
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
    vince "Agora vocês têm a manhã para descobrir quem é o assassino, e se conseguirem vocês avançam para o próximo nível."

    vince "Mas se falharem escolhendo a pessoa errada..."

    hide vince normal
    scene bg tudo_vermelho_lmao with dissolve
    show vince emo_idk

    show text "{b}Vocês todos morrem e o assassino vence.{/b}"
    pause

    hide vince emo_idk
    scene bg tribunal with dissolve

    show vince normal

    vince "Agora vocês estão dispensados."

    jump escolhas_tribunal


label dia2_cozinha:
    scene bg cozinha_sangue with dissolve
    if first_time_cozinha:
        "[clint], [felix] e [aisha] estão na cozinha."
        $ first_time_cozinha = False

    menu:
        "Falar com um deles?"

        "[clint]":
            jump dia2_clint
        "[felix]":
            jump dia2_felix
        "[aisha]":
            jump dia2_aisha
        "Voltar":
            jump escolhas_tribunal

label dia2_felix:
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
    jump dia2_cozinha

label dia2_clint:
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
    clint "Definitivamente. É justamente por isso que eu acredito que ela foi coagida a fazer isso ou só ameaçada mesmo"

    hide clint normal
    jump dia2_cozinha

label dia2_aisha:
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
    me "E como você sabe disso se a mancha é tão pequena?"

    hide minato normal
    show aisha normal
    aisha "É simples, diferente de qualquer um aqui eu notei o formato da sola"
    jump dia2_cozinha


label dia2_sala_recreacao:
    scene bg sala_recreacao with dissolve
    if first_time_sala_recreacao:
        "[my_name] chega na sala de recreação onde aqui estão [joana], [nina] e [mitchell]"
        $ first_time_sala_recreacao = False

    menu:
        "Falar com um deles?"

        "[joana]":
            jump dia2_joana
        "[nina]":
            jump dia2_nina
        "[mitchell]":
            jump dia2_mitchell
        "Voltar":
            jump escolhas_tribunal

label dia2_nina:
    "[nina] tá bem abalada, e a [joana] felizmente está consolando ela"
    jump dia2_sala_recreacao

label dia2_joana:
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
    jump dia2_sala_recreacao

label dia2_mitchell:
    show mitchell normal
    play music "smooth criminal.mp3"
    mitchell "E ai [minato], tá investigando a garota morta?"

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

    stop music
    jump dia2_sala_recreacao


label dia2_biblioteca:
    scene bg biblioteca with dissolve
    if first_time_biblioteca:
        "[sofia] e [thiago] estão na biblioteca."
        $ first_time_biblioteca = False

    menu:
        "Com quem falar?"

        "[sofia]":
            jump dia2_sofia
        "[thiago]":
            jump dia2_thiago
        "Voltar":
            jump escolhas_corredor

label dia2_sofia:
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
    show sofia decepcionada
    sofia "Ah sim, é que esses livros são todos inúteis"

    hide sofia decepcionada
    show minato normal
    me "Por quê?"

    hide minato normal
    show sofia decepcionada
    sofia "Porque são todos livros infantis e romances policiais tão exagerados que é óbvio que nada disso funciona na realidade"

    sofia "O que não serve de nada em um lugar onde temos que investigar assassinos"

    hide sofia decepcionada
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
    jump dia2_biblioteca

label dia2_thiago:
    show thiago normal
    thiago "Como vai meu caro companheiro [minato]!"

    hide thiago normal
    show minato normal
    me "Bem, o que tá fazendo? Só olhando as prateleiras?"

    hide minato normal
    show thiago normal
    thiago "Mas é claro que não"
    thiago "Eu estava procurando alguma boa leitura que auxilie todos nós nesta investigação."

    hide thiago normal
    show minato normal
    me "Boa, encontrou algo?"

    hide minato normal
    show thiago normal
    thiago "Infelizmente não, mas eu vou continuar, não se preocupe meu amigo."

    hide thiago normal

    me "Isso foi estranho"
    jump dia2_biblioteca


label dia2_quadra:
    scene bg quadra with dissolve
    "Não há ninguém aqui."
    jump escolhas_corredor


label dia2_quarto:
    scene bg quarto with dissolve

    me "É melhor eu descansar por enquanto, pois logo terei que garantir que o real culpado seja descoberto, ou eu e todos vamos morrer..."
    me "Pelo menos eu sei que o culpado é capaz de intimidar alguém, manipular ou controlar."

    jump dia2_tribunal


label dia2_tribunal:
    scene black with dissolve
    show text "Tribunal" with Pause(2)
    scene black with dissolve

    scene bg tribunal with dissolve

    # som de alguém caindo

    me "Eu acho que nunca vou me acostumar com essa droga de teletransporte."

    show vince normal
    vince "Senhoras e senhores! Sejam bem-vindos ao primeiro caso da 21° edição do tribunal do desejo, e eu serei o grande apresentador e juiz."

    vince "Agora vocês todos deverão apresentar todas as provas coletas!"
    vince "Que tenha justiça neste tribunal!"

    hide vince normal

    "Todos estão cruzando olhares, o clima está se transformando muito rápido."

    show clint normal

    clint "Eu tenho algumas."

    clint "Eu estive analisando os cortes, e posso confirmar pela minha experiência, que ela de fato se matou."

    clint "Dá pra saber disso pelos cortes totalmente amadores e desesperados, eu também descobri pela expressão dela e alguns outros detalhes, como ela morreu."

    clint "Ela estava vendo ou ouvindo algo tão horrível que a forçou a cometer esse ato, deu pra saber disso pelas pegadas dela."

    hide clint normal
    show aisha normal

    aisha "Eu descobri pegadas do assassino, pequenas mas ainda sim foi simples saber, que ele usava sapatos, além disso eu falei com todos aqui."

    aisha "E mais um detalhe importante, a [joana] me disse que ouviu barulhos estranhos à noite."

    hide aisha normal
    show joana normal

    joana "Sim eu ouvi sons estranhos, eu estava acordada para tomar um pouco de água, eu ia entrar na cozinha, mas voltei quando eu vi uma figura robusta, fazendo movimentos estranhos para uma figura magra."

    joana "Provavelmente a [diana]."

    hide joana normal
    show thiago normal

    thiago "Isso é meio vago, alguém descobriu mais alguma coisa?"

    hide thiago normal

    "Todos aqueles que não falaram fizeram gestos que indicam que eles não tem mais informações."

    show sofia normal
    sofia "Eu posso não ter descoberto mais nada, mas com minhas habilidades de dedução, posso dizer que o culpado é..."
    sofia "{b}O [thiago]!!{/b}"

    hide sofia normal
    show thiago assustado
    thiago "Que coisa mais absurda minha dama, você por acaso possui alguma evidência do que afirma?"

    hide thiago assustado
    show sofia normal
    sofia "Mas é claro, você usa sapatos, e tem cara de quem faria isso, eu sinto isso."

    hide sofia normal
    show thiago normal
    thiago "Isso facilmente pode se aplicar a qualquer um, pois mais da metade usa sapatos."
    thiago "Além do mais qualquer um poderia ter pego um casaco para se ocultar."

    hide thiago normal
    show clint normal
    clint "Infelizmente ele tem um ponto, qualquer um poderia ter feito isso."

    hide clint normal
    show felix normal
    felix "De fato."
    hide felix normal

    me "As discussões estão aumentando, se continuar assim todos vamos morrer, é melhor eu fazer algo... Quem poderia ser?"
    call resetar_escolhas
    jump escolhas_quem_acusar

label dia2_depois_de_acusar:
    stop music

    $ is_aggressive = current_choices[CS_AGRESSIVO] >= 4
    $ is_asshole = current_choices[CS_PASSIVO_AGRESSIVO] >= 4

    call get_most_selected_choice

    # XXX: Took some creative liberties here. May or may not be character accurate. (i didnt create em so idk)

    if is_aggressive or is_asshole:
        if accused_person == '[sofia]':
            show clint normal
            clint "Tudo bem, [minato]? Você parece meio desesperado."
            hide clint normal
        else:
            show sofia irritada
            sofia "Mas você adora ficar acusando todo mundo né?"
            sofia "E esse tom irritante também!!"
            hide sofia irritada

        show thiago normal
        thiago "Isso é meio suspeito, sim."
        hide thiago normal

        # even my boy felix gon be against you if you didn't trust him
        if felix_alive and current_choices[CS_ASSERTIVO] < 2:
            show felix normal
            felix "Ele não parece muito convincente."
            hide felix normal

        show joana normal
        joana "Pensando bem, ele tem agido de forma meio suspeita faz um tempo já."
        hide joana normal

        if current_choices[CS_ASSERTIVO] >= 2:
            show aisha normal
            aisha "Embora ele tenha feito alguns bons pontos."
            hide aisha normal
            show sofia irritada
            sofia "Pura sorte, tenho certeza!"
            hide sofia irritada
        else:
            show aisha normal
            aisha "E seus argumentos são muito incoerentes."
            hide aisha normal

        play music "smooth criminal.mp3"
        show mitchell normal
        mitchell "Hahaha esse cara está louco"
        hide mitchell normal
        stop music

        # just so they don't repeat the same things
        if accused_person != '[sofia]':
            show clint normal
            clint "Ele está claramente desesperado."
            hide clint normal
        else:
            show sofia irritada
            sofia "Esse idiota fica acusando todo mundo!"
            hide sofia irritada
            if felix_alive:
                show felix normal
                felix "De fato." # idk he's just felix. silly felix.
                hide felix normal


        show vince normal
        vince "Parece que ninguém acredita em você."
        hide vince normal

        # XXX: ts hella underwhelming but oh well
        scene bg tudo_vermelho_lmao with dissolve
        show vince emo_idk
        show text "{b}Você perdeu.{/b}"
        pause
        return

    jump escolhas_quem_acusar
    # XXX: acreditam no jogador ao fazer muitas escolhas assertivas e votam no acusado (também perdendo o jogo)


label dia2_final:
    show mitchell normal
    mitchell "Hahahahahaha, é parece que não tem outro jeito, eu matei ela."

    hide mitchell normal
    show clint normal
    clint "Por que? Só pelo desejo?!"

    hide clint normal
    show mitchell normal
    mitchell "Sim foi pelo desejo, mas esse era o único meio para eu recuperar o que é meu."

    hide mitchell normal
    show felix pensativo
    felix "E o que séria tão importante, pra você tirar uma vida inocente?"

    hide felix pensativo
    show mitchell seila
    mitchell "Foi pra recuperar a minha carreira, a minha chance, mas como vocês iriam entender não foram vocês, que iam perder tudo pra um pilantra que se acha bom o bastante."

    hide mitchell seila
    show sofia decepcionada
    sofia "Então no fim só foi por inveja, você é patético mesmo."

    hide sofia decepcionada
    show mitchell irritado
    mitchell "Fácil para você falar, não era você quem perderia seu sonho, não foi você quem lutou tanto, por tantos anos por esse sonho, vamos lá o que você faria no meu lugar?"

    hide mitchell irritado
    show sofia decepcionada
    sofia "Eu tentaria ser melhor que o meu rival, mas você só escolheu o caminho mais fácil, e ainda se considera um [mitchell]."

    hide sofia decepcionada
    show mitchell irritado

    mitchell "Que se dane você, todos vocês, especialmente você, [minato]."

    hide mitchell irritado
    show minato normal
    me "Antes de terminarmos isso, como você fez aquilo?"

    hide minato normal
    show mitchell normal
    mitchell "Isso é fácil, eu só usei os meus poderes, a minha dança pode forçar as pessoas fazerem o que eu quero."

    hide mitchell normal
    show clint normal

    clint "Poderes?!"

    hide clint normal
    show mitchell normal
    mitchell "Sim, o que vocês não sabiam, todos ganhamos poderes quando fomos teletransportados até aqui."

    "Todos estão olhando uns para os outros."
    "Logo o [mitchell] se aproveitando da distração, breve para fazer uma dança."

    # XXX: dançarino é enforcado por uma corda (mostrar uma imagem dos pésinhos dele sla)
    hide mitchell normal
    show vince normal
    vince "Nada de trapacear, você já perdeu."

    "O Vince pega um controle e aperta um botão vermelho."

    hide vince normal

    # XXX: como faço isso...????
    # (Agora ele é solto, e fones de ouvido são pregados nos ouvidos dele, e todo tribunal muda para uma pista de dança)

    scene bg tudo_vermelho_lmao with dissolve

    "O [mitchell] começou a dançar, e parece que o chão está ficando vermelho cada vez mais, e com a cor o calor aumenta, e logo ele começa a dançar cada vez mais rápido."

    "Logo o teto abriu e um raio caiu no [mitchell], o transformando em uma estátua de cristal."

    "Todos olham para ele em choque."

    stop music

    scene bg tribunal with dissolve
    show vince normal

    vince "E assim termina o primeiro julgamento, eu admito que estou impressionado, vocês conseguiram descobrir o assassino."

    hide vince normal
    show thiago normal
    thiago "Isso é bom, mas que história é essa de poderes?"

    hide thiago normal
    show aisha normal
    aisha "É, não acha que era algo importante de mencionar?"

    hide aisha normal
    show vince normal
    vince "Pode até ser, mas nenhum de vocês perguntou, então eu apenas não disse."

    "Rapidamente o [clint] apontou para o [vince]."

    hide vince normal
    show clint normal
    clint "Deixa de falar besteira, você deveria ter contado isso logo de cara, tendo a gente perguntado ou não!"

    hide clint normal
    show vince normal
    vince "Não adianta ficar bravo, pois agora vocês já sabem de tudo, então eu vou deixá-los descansar por hoje."

    # me "ayaya vo a mimir"
    # XXX: go back to ur room (may it has some more dialog or sum)
    jump dia3_start
