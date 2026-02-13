label dia3_start:
    python:
        # had to kill them just now mb
        felix_alive = nina_alive = joana_alive = True
        mitchell_alive = False # this one is dead fr tho
    call novo_dia
    # vai main menu mesmo fodase
    play music "main menu.mp3" if_changed

    "Isso é um sonho? Ou é só mais um truque desse lugar? Eu só me lembro de ter ido dormir."

    scene bg floresta with dissolve

    "Quem é aquele cara engraçado ali?"

    show letos normal

    noname "Como vai amigo, nesse dia maravilhoso."

    me "Eu tô bem."

    noname "Isso é bom, porque aqui na floresta do véu, ninguém é triste, o que me lembra de me apresentar."

    letos "Meu nome é [letos], eu sou o jardineiro que cuida dessa floresta."

    me "Um jardineiro? Cadê o jardim?"

    letos "Você é bem apressado amigo, mas eu entendo. Venha que eu mostro o jardim."

    scene bg jardim with dissolve

    "Então nós dois fomos até o jardim, parece ser mais um lugar tranquilo, mas por algum motivo tem uma gosma preta saindo de algumas flores."

    show letos normal

    me "[letos] tem um líquido estranho saindo daquelas flores."

    letos "Ah obrigado [my_name]."

    me "Como você sabe o meu nome?"

    hide letos normal
    "O [letos] se vira e começa a arrumar as flores."

    letos "Hora que anfitrião seria eu, se não soubesse o nome do meu convidado."

    "Isso é bem esquisito, e ele logo se levantou e olhou para mim."

    show letos normal
    letos "Eu peço perdão [my_name], parece que o jardim hoje está bem teimoso."

    me "Você se refere a esse líquido escuro?"

    "Junto com o líquido um cheiro horrível está no ar."

    letos "Infelizmente sim, porém me diga está tudo bem [my_name]?"

    me "Sim... na verdade, infelizmente não está tudo bem."

    "Do nada, mais do líquido negro aparece, e com ele o cheiro piora."

    letos "O quê?! Isso é não positivo, você tem que pensar positivo."

    menu:
        "Não, não está tudo bem.":
            me "A [diana] morreu, o mundo está destruido, e eles não estão mais aqui!"
            # XXX: (O cenário vai ficando cada vez mais apodrecido)

            hide letos normal
            show letos assustado
            letos "Não diga isso, não diga isso!!"

            me "Mas isso é a verdade, eu não posso mais fingir que está tudo bem."

            me "Eu fugi dessa verdade, por isso eu tô te dizendo, muita coisa está errada."

            letos "Não, não, não, não, não, porque você está falando isso."

            # XXX: geen tijd voor dis shit
            # "Logo o [letos] começa a derreter e apodrecer, e uma garota vestindo um vestido branco com detalhes em verde."
            "Logo o [letos] começa a derreter e apodrecer."
            jump dia3_real_start

        "Provavelmente, eu de fato deveria.":
            letos "Muito bom, isso. Pense de modo positivo."
            jump dia3_real_start


label dia3_real_start:
    scene black with dissolve
    scene bg quarto with dissolve
    play music tema_suspense loop if_changed

    "O que foi aquilo? deve ser só um sonho, mas esse é o primeiro que foi mais vívido..."
    "Bem, de todo modo eu devo descobrir algo sobre os meus poderes."
    jump escolhas_tribunal


label dia3_sala_recreacao:
    scene bg sala_recreacao with dissolve
    # play music tema_sala_recreacao if_changed
    if first_time_sala_recreacao:
        "[thiago] e [sofia] estão na sala de recreação."
        $ first_time_sala_recreacao = False
    menu:
        "Falar com alguém?"
        "[thiago]":
            jump dia3_thiago
        "[sofia]":
            jump dia3_sofia
        "Voltar":
            jump escolhas_tribunal

label dia3_thiago:
    show thiago normal
    "O [thiago] parece bem cansado."
    thiago "Olá [minato]."
    me "Oi [thiago], Precisa de algo?"
    thiago "Nã...na verdade sim, eu gostaria."
    thiago "Poderia pegar para mim aquela almofada por gentileza?"
    me "Claro."
    thiago "Obrigado, é que eu tive uma insônia."
    me "Eu entendo, bom descanso."
    thiago "Muito obrigado."
    jump dia3_sala_recreacao

label dia3_sofia:
    show sofia normal
    sofia "Precisa de algo, [minato]?"
    me "Não exatamente, eu só estava passando e queria dar um oi."
    sofia "Oi então."
    sofia "Quer jogar palavras cruzadas?"
    menu:
        "Jogar":
            jump dia3_jogar_sofia
        "Não jogar":
            me "Não posso, eu ainda tenho coisas para fazer."
            sofia "Ok então."
    jump dia3_sala_recreacao

label dia3_jogar_sofia:
    me "Claro."
    "Então nós começamos, eu joguei muito pouco de palavras cruzadas, porém comparado a ela, eu sou bem lento."
    sofia "Muito impressionante, para um amador você tem potencial."
    sofia "Continua treinando e creio que vai chegar perto de mim um dia."
    me "Claro, [sofia]."
    jump dia3_sala_recreacao

label dia3_cozinha:
    scene bg cozinha with dissolve
    # play music tema_cozinha if_changed
    menu:
        "[clint] está na cozinha."
        "Falar com ele":
            jump dia3_clint
        "Voltar":
            jump escolhas_tribunal

label dia3_clint:
    show clint feliz
    clint "E ai [minato]."
    me "Oi."
    clint "Que bom que você chegou, eu descobri uma coisa."
    hide clint feliz
    show clint normal
    clint "Eu falei com o [vince], e aquele gato disse que ele não roubou a minha arma, foi outra pessoa."
    me "Nossa, e conseguiu descobrir alguma pista?"
    clint "Infelizmente não."
    hide clint normal
    show clint feliz
    "Mas mudando de assunto você quer um sanduíche?"
    menu:
        "Aceitar":
            jump dia3_sanduba_clint
        "Recusar":
            me "Não, obrigado, eu não estou com fome."
            clint "Ok."
    jump dia3_cozinha

label dia3_sanduba_clint:
    me "Sim, por favor."
    "Então ele começou a cozinhar, fazendo um sanduíche de costelinha."
    "O sanduíche está muito bom."
    me "Minha nossa, isso tá muito bom, onde você aprendeu a fazer isso?"
    clint "Com o meu pai."
    me "Aproveitando a oportunidade, se importa se eu perguntar, por que quis se tornar um pistoleiro?"
    clint "Não tem problema, isso vem dos filmes do velho mundo."
    clint "Especialmente aquele {b}O Bom o Mal e o Feio{/b}, recomendado."
    me "Anotado, obrigado pelo sanduíche."
    clint "De nada."
    jump dia3_cozinha

label dia3_biblioteca:
    scene bg biblioteca with dissolve
    play music tema_biblioteca if_changed
    if first_time_biblioteca:
        "[aisha], [nina] e [felix] estão na biblioteca."
        $ first_time_biblioteca = False
    menu:
        "Falar com um deles?"
        "[aisha]":
            jump dia3_aisha
        "[nina]":
            jump dia3_nina
        "[felix]":
            jump dia3_felix
        "Voltar":
            jump escolhas_corredor

label dia3_aisha:
    show aisha normal
    aisha "Olá [minato]."
    me "Oi, o que você está lendo?"
    aisha "E por que você quer saber?"
    me "Por pura curiosidade."
    aisha "Nesse caso, eu estou lendo um diário de uma garota triste."
    me "É um diário real?"
    aisha "Talvez, mas eu creio que seja uma ficção pela história absurda."
    aisha "Falando nisso gostaria de jogar xadrez?"
    menu:
        "Jogar":
            jump dia3_jogar_aisha
        "Não jogar":
            me "Não, obrigado. Eu ainda tenho coisas para fazer."
            aisha "Tá bom."
    jump dia3_biblioteca

label dia3_jogar_aisha:
    me "Claro."
    "Assim nós jogamos xadrez, como eu nunca joguei xadrez, achei bem difícil mas divertido."
    "Depois de um tempo eu perdi."
    me "Ok, esse jogo é bem complicado."
    aisha "Talvez seja para quem tem pressa, e não jogo de modo estratégico."
    aisha "Veja bem, xadrez é um jogo mais amplo do que parece, a vida lembra muito um jogo de xadrez, onde cada movimento errado pode te fazer perder."
    aisha "É melhor sempre calcular seus próximos passos, [minato]."
    jump dia3_biblioteca

label dia3_nina:
    show nina feliz
    nina "Olá [minato]."
    me "Oi, você está se sentindo melhor, [nina]?"
    nina "Sim, graças a todos vocês."
    me "Que bom, está procurando algo?"
    nina "Sim, é que eu descobri como meus poderes funcionam, quando eu faço uma comida."
    nina "Então eu estou procurando um livro de receitas que ajude e entenda melhor isso."
    hide nina feliz
    show nina normal
    menu:
        nina "Falando nisso, pode me ajudar a procurar esse livro?"
        "Ajudar":
            jump dia3_ajudar_nina
        "Não ajudar":
            me "Não posso, eu ainda tenho coisas para fazer."
            nina "Não tem problema."
    jump dia3_biblioteca

label dia3_ajudar_nina:
    me "Claro, deixa eu te ajudar."
    "Nós passamos alguns minutos procurando, até encontrar o livro {b}\"Receitas para idiotas.\"{/b}"
    nina "Deve ser esse."
    me "Que bom, eu queria perguntar, afinal por que você escolheu aprender a ser uma confeiteira?"
    nina "É porque eu já estive passando por um momento difícil, então o único meio que eu encontrei foi fazer comidas."
    me "Alguma em especial?"
    nina "Bolos."
    me "Obrigado por compartilhar sua história."
    nina "Não a de que."
    jump dia3_biblioteca

label dia3_felix:
    if believe_felix:
        show felix feliz
        felix "Como vai amigo, precisa de algo?"
        me "Sim, eu queria perguntar se você descobriu algo sobre nossos poderes?"
        felix "Sim, algumas coisas."
        felix "Nossos poderes estão relacionados aos nossos títulos."
        me "Isso faz sentido, conseguiu descobrir mais alguma coisa?"
        hide felix feliz
        show felix normal
        "Ele se aproximou e cochichou no meu ouvido."
        felix "Eu também descobri que o uso tem regras, cada regra é diferente para cada um."
        me "Obrigado pela informação, [felix]."
        hide felix normal
        show felix feliz
        felix "De nada."
    else:
        show felix normal
        felix "Olá [minato], precisa de algo?"
        me "Sim, você conseguiu descobrir algo sobre os poderes?"
        felix "Muito pouco, lendo os livros eu descobri algumas coisas, mas uma em especial."
        felix "Nossos poderes tem a ver com os nossos títulos."
        me "Isso faz sentido, e fora isso conseguiu descobrir mais alguma coisa?"
        felix "Infelizmente não."
    jump dia3_biblioteca

label dia3_quadra:
    scene bg quadra with dissolve
    play music tema_quadra if_changed
    menu:
        "[joana] está na quadra."
        "Falar com ela":
            jump dia3_joana
        "Voltar":
            jump escolhas_corredor

label dia3_joana:
    show joana feliz
    joana "Tudo bem, [minato]."
    me "Sim, eu queria ver como você está."
    hide joana feliz
    show joana normal
    joana "Eu estou bem, só estava treinando, ou pelo menos tentando."
    me "Tá tentando descobrir como usa seus poderes?"
    joana "É, eu estou mas infelizmente as coisas não estão indo tão bem."
    joana "Aproveitando a oportunidade, [minato] você poderia me ajudar a treinar, por favor?"
    menu:
        "Ajudar":
            jump dia3_treinar_joana
        "Não ajudar":
            me "Me desculpa mas eu ainda tenho coisas para fazer."
            joana "Ah tudo bem."
    jump dia3_quadra

label dia3_treinar_joana:
    me "Claro."
    "Então ela começa a treinar, a [joana] é bastante resiliente em seu treino, mas do nada ela tropeçou."
    "Ela parece sentir muita dor na perna."
    me "[joana], precisa de ajuda?"
    joana "Não precisa, isso meio que acontece com frequência."
    joana "Então não se preocupe, porém de toda forma obrigada pela ajuda."
    me "Fico feliz em ajudar."
    jump dia3_quadra

label dia3_quarto:
    scene bg quarto with dissolve
    menu:
        "Dormir":
            jump dia3_dormir
        "Voltar":
            jump escolhas_tribunal

label dia3_dormir:
    scene black with dissolve
    show text "{b}Fim da demo.\nObrigado por jogar.{/b}"
    pause
    show text "[credits]"
    pause
    return

