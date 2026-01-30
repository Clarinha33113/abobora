label dia1_start:
    scene black with dissolve
    show text "Dia 1" with Pause(2)
    scene black with dissolve

    "Hahahahahahaha"

    me "O que está acontecendo?"

    me "O lugar é frio, o ar apesar disso é leve. E essa risada, de quem será eu não sei, porém tenho certeza que devo ter cautela..."

    scene bg sala_branca with dissolve

    show minato assustado

    me "Mas o quê?! Por que esse lugar é tão claro?"

    me "Essa sala... Ela é tão estranha, é difícil descrever a sensação de ver que não tem vida ao seu redor, tudo é tão angustiante, e parace ter apenas um caminho."

    hide minato assustado

    "Assim [my_name] avança abrindo a porta. Ele segue um corredor branco, e logo chega em uma sala que lembra um tribunal, lá várias pessoas estão, jovens."

    scene bg tribunal

    me "Um tribunal, eu realmente estou vendo isso. Claramente eu não fui o único a ser sequestrado, só espero que possamos sair sem nenhum jogo doentio."

    show vince normal

    "Logo ao centro um ser semelhante a um gato de pelúcia estranho aparece."

    vince "Nossos convidados de honra, sejam bem vindos a torre branca dos desejos, meu nome é Vince e serei o apresentador deste tribunal."

    hide vince normal
    show clint normal

    clint "Um tribunal? Estamos sendo julgados por algo? Ou isso é só algum jogo esquisito?"

    hide clint normal
    show vince normal
    vince "Uma boa pergunta, vocês estão pensando que foram sequestrados, mas isso estaria totalmente incorreto. Todos vocês foram formalmente convidados a participar desse tribunal."

    hide vince normal
    show aisha normal
    aisha "É mesmo, pois isso soa uma ladainha, eu li muito bem a carta, e não tinha nenhum aviso sobre aparecermos nesse tribunal."

    vince "Tem certeza, minha jovem? Olhe direito."

    hide aisha normal

    "Assim todos pegam as cartas e começam a ler."

    # XXX: Mostrar imagem da carta aqui

    me "Parece que coisas foram adicionadas a carta, ou sempre estiveram lá?"

    "{i}Gostaríamos de parabenizá-lo por ter sido selecionado para uma viajem com tudo pago para um lugar especial, o Tribunal da Torre dos Desejos.{/i}"
    "{i}Onde nós não nos responsabilizados por qualquer morte, para você e sua consciência lutarem pelos seu desejo, basta apenas assinar essa carta e poderá participar.{/i}"

    show minato pensativo
    me "Claro. O sorteio grátis que parecia bom demais para ser verdade agora envolve assassinatos e desejos mágicos. Por que eu não joguei aquela carta no lixo?"

    hide minato pensativo
    show aisha assustada at left
    show vince normal at right

    aisha "Da para ver que você mudou o conteúdo da carta!"

    vince "Você tem como provar esse acusação?"

    aisha "Não, mas que história é essa de desejo."

    vince "Que bom que perguntou. Todos aqui querem ir embora, eu entendo, mas se um de vocês chegar até o final poderão fazer um desejo ao Obelisco."

    hide aisha assustada
    show thiago normal at left

    thiago "Qualquer desejo?"

    vince "Exato qualquer desejo, mas para isso..."

    hide thiago normal
    hide vince normal

    scene bg tudo_vermelho_lmao with dissolve

    show text "{b}Um de vocês precisa se tornar o assassino perfeito.{/b}" with Pause(4)

    # vince "{b}Um de vocês precisa se tornar o assassino perfeito.{/b}"

    scene bg tribunal with dissolve

    show vince normal
    vince "Ou podem desistir e irem para casa agora, mas para isso devem decidir isso amanhã de manhã. Por que não aproveitam a oportunidade para se apresentarem?"

    hide vince normal
    show aisha normal
    aisha "Olá a todos eu sou {b}A [aisha]{/b}."

    me "Ela falou esse título com uma pausa, soa que não era isso que ela ia falar."

    hide aisha normal
    show sofia normal

    sofia "E eu sou {b}A [sofia]{/b}."

    me "Essa garota fez a mesma pausa, será que somos incapazes de falar nossos nomes?"

    hide sofia normal
    show clint normal
    clint "Eu Me chamo {b}O [clint]{/b}, pessoal."

    hide clint normal
    show thiago normal
    thiago "E Eu sou {b}O [thiago]{/b}!"

    hide thiago normal
    show minato normal
    me "Eu me chamo {b}O [minato]{/b}."

    hide minato normal
    show mitchell normal
    mitchell "Sou {b}O [mitchell]{/b}."

    hide mitchell normal
    show nina normal
    nina "Olá A todos, sou {b}A [nina]{/b}."

    hide nina normal
    show felix normal
    felix "Eu sou {b}O [felix]{/b}."

    hide felix normal
    show joana normal
    joana "É bom conhecê-los, eu sou {b}A [joana]{/b}."

    hide joana normal
    show diana normal
    diana "E eu sou {b}A [diana]{/b}."

    hide diana normal

    # XXX: precisa de uma transição melhor aqui

    jump dia1_cena1_escolhas

label dia1_cena1_escolhas:
    menu:
        me "Para onde vou?"

        "centro":
            jump dia1_cena1_centro
        "direita":
            jump dia1_cena1_direita
        "esquerda":
            jump dia1_cena1_esquerda
        "quarto":
            jump dia1_cena1_quarto

    return

label dia1_cena1_centro:
    menu:
        "[my_name] chega em uma sala de recreação onde aqui estão [thiago], [sofia], [clint] e [diana]"

        "Falar com um deles":
            pass
        "Voltar":
            jump dia1_cena1_escolhas

    # Falar com um deles ou voltar 

    thiago "Ola meu caro [minato]"

    me "Oi, o que esta fazendo?"

    thiago "Apenas observando esse belo quadro, eu nunca vi nada parecido, é tão intrigante e sofisticado ao mesmo tempo"

    me "Sim ele é, me diga o que achou do tal [vince]?"

    thiago "Sinceramente ele é meio bizarro, e peculiar demais, mas para um anfitrião ele até tem um bom jeito de apresentar as coisas, porém eu não confiaria a minha vida a ele"

    me "E o que acha desse lugar?"

    thiago "Com certeza muito desconfortável, esse branco todo ao redor dá dor de cabeça, os móveis são até bons e charmosos ao seu próprio modo, porém se dependesse de mim eu não ficaria nesse lugar,"

    me "Obrigado por compartilhar sua opinião, Thiago: Ah não a de que, fique atento [minato]."

    "Ele parece um cara legal, mas eu tô com uma sensação estranha relacionada a ele."

    sofia "O que tá olhando?"

    me "Nada, eu só queria perguntar sua opinião sobre o [vince]"

    sofia "Aquele gato estúpido, ele é insolente e pretencioso, ele acha que vai ficar barato nos sequestrar, além do mais a ideia de matar para ganhar um desejo não me atrai muito."

    me "E quanto a esse lugar"

    sofia "Esse lugar é horrível e deprimente, só alguém com mal gosto iria gostar dessa espelunca, não tem cores e tudo é tão artificial"

    me "Obrigado por compartilhar sua opinião"

    sofia "Tanto faz só saia da minha frente se não for pedir muito."

    "Já vejo que ela será bem desagradável e difícil de lidar, tomara que eu não tenha que enfrentar ela."

    clint "Como vai amigo?"

    me "Bem, eu queria te perguntar se não é muito incômodo Sr. [clint], o que acha daquele [vince]?"

    clint "Um sujeito estranhamente assustador para um gato de pelúcia, o maldito roubou o meu revólver"

    me "Talvez para você não ter vantagem sobre os outros"

    clint "É bem provável, ca entre nós esse gato vai provavelmente tentar matar todos nós, igual alguns aqui"

    me "Tem certeza?"

    clint "total é só olhar para todo mundo, alguns aqui estão cogitando esse desejo, não confiaria tão facilmente em qualquer um"

    me "E o que acha desse lugar?"
    
    clint "Lugarzinho desconfortante, mas creio que posso tentar me acostumar de um certo modo"

    me "Obrigado por compartilhar sua opinião"

    clint "Não a de que."

    "Esse [clint], parece ser um cara legal, e ele tem um ponto válido"

    # "Se o jogador tentar se aproximar da [diana] essa descrição aparece"

    "Ao tentar me aproximar da [diana] ela se encolheu no canto, coitada dela deve estar em choque maior que qualquer um"

    menu:
        "Voltar":
            jump dia1_cena1_escolhas

    return


label dia1_cena1_direita:
    # "O jogador verá uma cozinha chique e uns pufs ao lado, aqui tem a Aisha e a Nina"

    "[aisha] Não fala nada e olha julgando."

    me "Me desculpa por encomodar [aisha], eu queria te perguntar o que você acha do [vince]?"

    aisha "Aquele desprezível e arrogante gato, ele realmente teve a coragem de falar na nossa cara, que aqueles termos sempre estiveram lá, e trás essa ideia repugnante de assassino perfeito, isso é horrível, se depender de mim todos aqui saíram" 

    me "E o que você acha desse lugar?" 

    aisha "Desagradável"

    aisha "Todo esse branco e essa luz me incomodam"

    aisha "Mas poderia ser pior, não vou reclamar tanto." 

    me "Muito obrigado por compartilhar sua opinião" 

    aisha "Claro"

    "Ela é bem intimidadora, eu nem sei se devo confiar nela ou não"

    nina "Olá, posso te ajudar com algo?" 

    me "Ah sim, eu queria saber o que você acha daquele [vince]?" 

    nina "Ele é assustador, eu não quero participar desse jogo de assassinato" 

    me "Eu também não quero" 

    nina "Tomara que as pessoas sejam sensatas pelo menos" 

    me "Confeiteira o que você acha desse lugar?" 

    nina "Poderia ser pior, mas pelo menos temos uma cozinha, eu talvez possa fazer algo depois para todo mundo" 

    me "Isso seria bom, de todo modo obrigado por compartilhar sua opinião"  

    nina "Me procure se precisar de ajuda"

    "Ela é uma pessoa amável, só espero que esse lugar não a maltrate"

    menu:
        "Voltar":
            jump dia1_cena1_escolhas

    return

label dia1_cena1_esquerda:
    # "Ao entrar, há duas escolhas:biblioteca ou quadra"

    menu:
        "Posso ir há biblioteca ou a quadra."

        "Biblioteca":
            jump dia1_cena1_biblioteca
        "Quadra":
            jump dia1_cena1_quadra
        "Voltar":
            jump dia1_cena1_escolhas

label dia1_cena1_biblioteca:
    "[felix] está na biblioteca."

    felix "Oi Amigo precisa de ajuda?" 

    me "Não exatamente, eu queria perguntar sua opinião sobre o [vince]?" 

    felix "Aquele gato é estranho" 

    felix "Bizarro demais"

    felix "Ele não vai nos deixar ir"

    felix "Se houver saída"

    me "E quanto a esse lugar?"  

    felix "Eu acho esse lugar um tanto assustador, uma pena não ter nenhum piano" 

    me "Um piano?" 

    felix "Sim ai eu poderia tentar aliviar o clima todo" 

    me "Obrigado por compartilhar a sua opinião" 

    felix "Não a de que, sempre que precisar de ajuda é só pedir"

    "Ele parece ser legal, apesar disso espero que aquele gato bizarro nos deixe sair"   

    menu:
        "Voltar":
            jump dia1_cena1_esquerda


# XXX: Mitchel ta na quadra ou no quarto?
label dia1_cena1_quadra:
    "[joana] e [mitchell] estão na quadra."

    joana "Como vai [minato], quer treinar comigo?" 

    me "Eu tô bem e não obrigado, eu queria te perguntar o que você acha do [vince]?" 

    joana "Ele é estranho e assustador"

    joana "Foi ele quem nos trouxe até aqui"

    joana "Não vai nos deixar ir facilmente"

    joana "Talvez exista outra saída"

    me "O que você achou desse lugar?"

    joana "Interessante e único, admito que estou curiosa quanto a esse lugar"

    me "Obrigado por compartilhar sua opinião"

    joana "De nada"

    "Ela é bem diferente dos outros, parece ser a única que permaneceu calma, e quem sabe as razões dela..."

    "[mitchell] está dançando passos bem familiares por algum motivo"

    mitchell "O que você deseja colega"

    me "Eu só queria saber sua opinião quanto ao [vince]?"

    mitchell "Aquele [vince] é peculiar, tem cara de pilantra que só quer ver um banho de sangue"

    me "E esse lugar?" 

    mitchell "Esse lugarzinho sem graça, para uma torre sem vida, esse lugar tem cara de que pode se tornar interessante"

    me "Obrigado pela sua opinião"

    mitchell "Claro só lembre de dançar mais para alegrar a vida"

    "Esse cara é um tanto peculiar, é difícil saber se ele é confiável ou não."

    
    menu:
        "Voltar":
            jump dia1_cena1_esquerda

    menu:
        "Voltar":
            jump dia1_cena1_esquerda

label dia1_cena1_quarto:

    # "O jogador volta para o quarto e tem duas opções voltar ou ir dormir"

    menu:
        "Dormir":
            pass
        "Voltar":
            jump dia1_cena1_escolhas

    me "Meu pior momento chegou"

    "Quando fecho as pálpebras, vejo diferente"

    "Este lugar é artificial em essência"

    "Outros passaram por aqui antes de mim"

    "Alguns não voltaram"

    "Será que parte da história do mundo foi moldada através deste lugar?"

    "Talvez"

    "Mas eu já não tenho mais energia para pensar nisso"

    return

