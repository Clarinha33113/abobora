label dia3_start:
    python:
        # had to kill them just now mb
        felix_alive = nina_alive = joana_alive = True
        mitchell_alive = False # this one is dead fr tho
    call novo_dia
    # vai main menu mesmo fodase
    play music "lethos.mp3" loop if_changed

    "Isso é um sonho? Ou é só mais um truque desse lugar? Eu só me lembro de ter ido dormir."

    scene bg floresta with dissolve

    "Quem é aquele cara engraçado ali?"

    show letos normal

    noname "Como vai, amigo, neste dia maravilhoso?"

    me "Eu tô bem."

    noname "Isso é bom, porque aqui na Floresta do Véu ninguém é triste. O que me lembra de me apresentar."

    letos "Meu nome é [letos]. Eu sou o jardineiro que cuida desta floresta."

    me "Um jardineiro? Cadê o jardim?"

    letos "Você é bem apressado, amigo, mas eu entendo. Venha que eu mostro o jardim."

    scene bg jardim with dissolve

    "Então nós dois fomos até o jardim. Parece ser mais um lugar tranquilo, mas, por algum motivo, tem uma gosma preta saindo de algumas flores."

    show letos normal

    me "[letos], tem um líquido estranho saindo daquelas flores."

    letos "Ah, obrigado, [my_name]."

    me "Como você sabe o meu nome?"

    hide letos normal
    "O [letos] se vira e começa a arrumar as flores."

    letos "Que tipo de anfitrião eu seria se não soubesse o nome do meu convidado?"

    "Isso é bem esquisito. Logo depois, ele se levantou e olhou para mim."

    show letos normal
    letos "Eu peço perdão, [my_name]. Parece que o jardim hoje está bem teimoso."

    me "Você se refere a esse líquido escuro?"

    "Junto com o líquido, um cheiro horrível toma conta do ar."

    letos "Infelizmente, sim. Porém, me diga: está tudo bem, [my_name]?"

    me "Sim... na verdade, infelizmente, não está tudo bem."

    "De repente, mais do líquido negro aparece, e com ele o cheiro piora."

    letos "O quê?! Isso não é positivo. Você tem que pensar positivo."

    menu:
        "Não, não está tudo bem.":
            me "A [diana] morreu. O mundo está destruído, e eles não estão mais aqui!"
            # XXX: (O cenário vai ficando cada vez mais apodrecido)

            hide letos normal
            show letos assustado
            letos "Não diga isso! Não diga isso!!"

            me "Mas isso é a verdade. Eu não posso mais fingir que está tudo bem."

            me "Eu fugi dessa verdade. Por isso eu tô te dizendo: muita coisa está errada."

            letos "Não, não, não, não... por que você está falando isso?"

            # XXX: geen tijd voor dis shit
            # "Logo o [letos] começa a derreter e apodrecer, e uma garota vestindo um vestido branco com detalhes em verde."
            "Logo o [letos] começa a derreter e apodrecer."
            jump dia3_real_start

        "Provavelmente... eu de fato deveria.":
            letos "Muito bom, isso. Pense de modo positivo."
            jump dia3_real_start


label dia3_real_start:
    scene black with dissolve
    scene bg quarto with dissolve
    play music tema_suspense loop if_changed

    "O que foi aquilo? Deve ter sido só um sonho, mas esse foi o primeiro que pareceu tão vívido..."
    "Bem, de todo modo, eu devo descobrir algo sobre os meus poderes."
    jump escolhas_tribunal


label dia3_sala_recreacao:
    scene bg sala_recreacao with dissolve
    play music tema_recreacao loop if_changed
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
    me "Oi [thiago]. Precisa de algo?"
    thiago "Nã... na verdade, sim. Eu gostaria."
    thiago "Poderia pegar para mim aquela almofada, por gentileza?"
    me "Claro."
    thiago "Obrigado. É que eu tive insônia."
    me "Eu entendo, bom descanso."
    thiago "Muito obrigado."
    jump dia3_sala_recreacao

label dia3_sofia:
    show sofia normal
    sofia "Precisa de algo, [minato]?"
    me "Não exatamente. Eu só estava passando e queria dar um oi."
    sofia "Oi, então."
    sofia "Quer jogar palavras cruzadas?"
    menu:
        "Jogar":
            jump dia3_jogar_sofia
        "Não jogar":
            me "Não posso, eu ainda tenho coisas para fazer."
            sofia "Ok, então."
    jump dia3_sala_recreacao

label dia3_jogar_sofia:
    me "Claro."
    "Então nós começamos. Eu joguei muito pouco palavras cruzadas, porém, comparado a ela, eu sou bem lento."
    sofia "Muito impressionante. Para um amador, você tem potencial."
    sofia "Continue treinando, e creio que vai chegar perto de mim um dia."
    me "Claro, [sofia]."
    jump dia3_sala_recreacao

label dia3_cozinha:
    scene bg cozinha with dissolve
    play music tema_cozinha loop if_changed
    menu:
        "[clint] está na cozinha."
        "Falar com ele":
            jump dia3_clint
        "Voltar":
            jump escolhas_tribunal

label dia3_clint:
    show clint feliz
    clint "E aí, [minato]."
    me "Oi."
    clint "Que bom que você chegou. Eu descobri uma coisa."
    hide clint feliz
    show clint normal
    clint "Eu falei com o [vince], e aquele gato disse que ele não roubou a minha arma. Foi outra pessoa."
    me "Nossa. E conseguiu descobrir alguma pista?"
    clint "Infelizmente não."
    hide clint normal
    show clint feliz
    "Mas, mudando de assunto, você quer um sanduíche?"
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
    me "Minha nossa, isso tá muito bom! Onde você aprendeu a fazer isso?"
    clint "Com o meu pai."
    me "Aproveitando a oportunidade, você se importa se eu perguntar por que quis se tornar um pistoleiro?"
    clint "Não tem problema. Isso vem dos filmes do Velho Mundo."
    clint "Especialmente aquele {b}O Bom, o Mau e o Feio{/b}. Recomendo."
    me "Anotado. Obrigado pelo sanduíche."
    clint "Por nada."
    jump dia3_cozinha

label dia3_biblioteca:
    scene bg biblioteca with dissolve
    play music tema_biblioteca loop if_changed
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
    aisha "Olá, [minato]."
    me "Oi, o que você está lendo?"
    aisha "E por que você quer saber?"
    me "Por pura curiosidade."
    aisha "Nesse caso, eu estou lendo um diário de uma garota triste."
    me "É um diário real?"
    aisha "Talvez, mas creio que seja uma ficção, pela história absurda."
    aisha "Falando nisso, gostaria de jogar xadrez?"
    menu:
        "Jogar":
            jump dia3_jogar_aisha
        "Não jogar":
            me "Não, obrigado. Eu ainda tenho coisas para fazer."
            aisha "Tá bom."
    jump dia3_biblioteca

label dia3_jogar_aisha:
    me "Claro."
    "Então nós jogamos xadrez. Como eu nunca tinha jogado, achei bem difícil, mas divertido."
    "Depois de um tempo, eu perdi."
    me "Ok, esse jogo é bem complicado."
    aisha "Talvez seja para quem tem pressa e não joga de forma estratégica."
    aisha "Veja bem, xadrez é um jogo mais amplo do que parece. A vida lembra muito um jogo de xadrez, onde cada movimento errado pode te fazer perder."
    aisha "É melhor sempre calcular seus próximos passos, [minato]."
    jump dia3_biblioteca

label dia3_nina:
    show nina feliz
    nina "Olá [minato]."
    me "Oi, você está se sentindo melhor, [nina]?"
    nina "Sim, graças a todos vocês."
    me "Que bom, está procurando algo?"
    nina "Sim. Eu descobri como meus poderes funcionam quando eu preparo comida."
    nina "Então estou procurando um livro de receitas que me ajude a entender melhor isso."
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
    "Nós passamos alguns minutos procurando, até encontrar o livro {b}'Receitas para Idiotas.'{/b}"
    nina "Deve ser esse."
    me "Que bom. Eu queria perguntar: por que você escolheu aprender a ser confeiteira?"
    nina "É porque eu já passei por um momento difícil, então o único meio que encontrei foi cozinhar."
    me "Alguma coisa em especial?"
    nina "Bolos."
    me "Obrigado por compartilhar sua história."
    nina "Não há de quê."
    jump dia3_biblioteca

label dia3_felix:
    if believe_felix:
        show felix feliz
        felix "Como vai, amigo? Precisa de algo?"
        me "Sim, você conseguiu descobrir algo sobre os poderes?"
        felix "Lendo os livros, descobri algumas coisas, mas uma em especial."
        felix "Nossos poderes têm a ver com nossos títulos."
        me "Isso faz sentido. E, fora isso, conseguiu descobrir mais alguma coisa?"
        hide felix feliz
        show felix normal
        "Ele se aproximou e cochichou no meu ouvido."
        felix "Eu também descobri que o uso tem regras, cada regra é diferente para cada um."
        me "Obrigado pela informação, [felix]."
        hide felix normal
        show felix feliz
        felix "Por nada."
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
    play music tema_quadra loop if_changed
    menu:
        "[joana] está na quadra."
        "Falar com ela":
            jump dia3_joana
        "Voltar":
            jump escolhas_corredor

label dia3_joana:
    show joana feliz
    joana "Tudo bem, [minato]?"
    me "Sim, eu queria ver como você está."
    hide joana feliz
    show joana normal
    joana "Eu estou bem. Só estava treinando, ou pelo menos tentando."
    me "Tá tentando descobrir como usar seus poderes?"
    joana "É, estou. Mas, infelizmente, as coisas não estão indo tão bem."
    joana "Aproveitando a oportunidade, [minato], você poderia me ajudar a treinar, por favor?"
    menu:
        "Ajudar":
            jump dia3_treinar_joana
        "Não ajudar":
            me "Me desculpa mas eu ainda tenho coisas para fazer."
            joana "Ah, tudo bem."
    jump dia3_quadra

label dia3_treinar_joana:
    me "Claro."
    "Então ela começa a treinar. A [joana] é bastante resiliente no treino, mas, de repente, tropeça."
    "Ela parece sentir muita dor na perna."
    me "[joana], precisa de ajuda?"
    joana "Não precisa. Isso meio que acontece com frequência."
    joana "Então não se preocupe. De toda forma, obrigada pela ajuda."
    me "Fico feliz em ajudar."
    jump dia3_quadra

label dia3_quarto:
    play music tema_quarto loop if_changed
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
    show text "{b}Obrigado à professora Elaine.{/b}"
    pause
    return

