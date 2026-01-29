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
    hide vince normal

    "Logo ao centro um ser semelhante a um gato de pelúcia estranho aparece."

    vince "Nossos convidados de honra, sejam bem vindos a torre branca dos desejos, meu nome é Vince e serei o apresentador deste tribunal."

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
    aisha "Olá a todos eu sou A Governante."

    me "Ela falou esse título com uma pausa, soa que não era isso que ela ia falar."

    hide aisha normal
    show sofia normal

    sofia "E eu sou A Contadora."

    me "Essa garota fez a mesma pausa, será que somos incapazes de falar nossos nomes?"

    hide sofia normal
    show clint normal
    clint "Eu Me chamo O Pistoleiro Pessoal."

    hide clint normal
    show thiago normal
    thiago "E Eu sou o Magnífico Esperto!"

    hide thiago normal
    show minato normal
    me "Eu me chamo O Espectador."

    hide minato normal
    show mitchell normal
    mitchell "Sou O Dançarino."

    hide mitchell normal
    show nina normal
    nina "Olá A todos, sou A Confeiteira."

    hide nina normal
    show felix normal
    felix "Eu sou O Apostador."

    hide felix normal
    show joana normal
    joana "É bom conhecê-los, eu sou A Atleta."

    hide joana normal
    show diana normal
    diana "E eu sou A Desenhista."

    hide diana normal

    menu:
        me "pai ta cansado pa onde q eu vo (texto placeholder)"

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
    # cena antes do return
    "O Minato chega em uma sala de recreaçao onde aqui estao Thiago,Sofia,Clint e Diana"
    #Falar com um deles ou voltar 

    thiago "Ola meu caro Espectador"

    minato "Oi,o que esta fazendo?"

    thiago "Apenas observando esse belo quadro, eu nunca vi nada parecido, é tão intrigante e sofisticado ao mesmo tempo"

    minato "Sim ele é, me diga o que achou do tal Vince?"

    thiago "Sinceramente ele é meio bizarro, e peculiar demais, mas para um anfitrião ele até tem um bom jeito de apresentar as coisas, porém eu não confiaria a minha vida a ele"

    minato "E o que acha desse lugar?"

    thiago "Com certeza muito desconfortável, esse branco todo ao redor dá dor de cabeça, os móveis são até bons e charmosos ao seu próprio modo, porém se dependesse de mim eu não ficaria nesse lugar,"

    minato "Obrigado por compartilhar sua opinião, Thiago: Ah não a de que, fique atento Espectador."

    "Ele parece um cara legal, mas eu tô com uma sensação estranha relacionada a ele."

    sofia "O que tá olhando?"

    minato "Nada, eu só queria perguntar sua opinião sobre o Vince"

    sofia "Aquele Gato estúpido, ele é insolente e pretencioso, ele acha que vai ficar barato nos sequestrar, além do mais a ideia de matar para ganhar um desejo não me atrai muito,"

    minato "E quanto a esse lugar"

    sofia "Esse lugar é horrível e deprimente, só alguém com mal gosto iria gostar dessa espelunca, não tem cores e tudo é tão artificial"

    mianto "Obrigado por compartilhar sua opinião"

    sofia "Tanto faz só saia da minha frente se não for pedir muito."

    "Já vejo que ela será bem desagradável e difícil de lidar, tomara que eu não tenha que enfrentar ela."

    clint "Como vai amigo?"

    minto "Bem, eu queria te perguntar se não é muito incômodo Sr. Pistoleiro, o que acha daquele Vince?"

    clint "Um sujeito estranhamente assustador para um gato de pelúcia, o maldito roubou o meu revólver"

    minato "Talvez para você não ter vantagem sobre os outros"

    clint "É bem provável, ca entre nós esse gato vai provavelmente tentar matar todos nós, igual alguns aqui"

    minato "Tem certeza?"

    clint "total é só olhar para todo mundo, alguns aqui estão cogitando esse desejo, não confiaria tão facilmente em qualquer um"

    minato "E o que acha desse lugar?"
    
    clint "Lugarzinho desconfortante, mas creio que posso tentar me acostumar de um certo modo"

    minato "Obrigado por compartilhar sua opinião"

    clint "Não a de que."

    "Esse Pistoleiro, parece ser um cara legal, e ele tem um ponto válido"

    "Se o jogador tentar se aproximar da Diana essa descrição aparece

    Descrição: Ao tentar me aproximar da Desenhista ele se encolheu no canto, coitada dela deve estar em choque maior que qualquer um"

    return


label dia1_cena1_direita:
    # cena antes do return

    "O jogador verá uma cozinha chique e uns pufs ao lado, aqui tem a Aisha e a Nina"

    aisha "Não fala nada e olhar julgando"

    minato "Me desculpa por encomodar  Governante, eu queria te perguntar o que você acha do Vince?"

    aisha "Aquele Desprezível e arrogante Gato, ele realmente teve a coragem de falar na nossa cara, que aqueles termos sempre estiveram lá, e trás essa ideia repugnante de Assassino perfeito, isso é horrível, de depender de mim todos aqui saíram" 

    minato "E o que você acha desse lugar?" 

    aisha "Desagradável"

    aisha "Todo esse branco e essa luz me incomodam"

    aisha "Mas poderia ser pior"

    aisha"Não vou reclamar tanto." 

    minato "Muito obrigado por compartilhar sua opinião" 

    aisha "Claro"

    "Ela é bem intimidadora, eu nem sei se devo confiar nela ou não"

    nina "Olá, posso te ajudar com algo?" 

    minato "Ah sim, eu queria saber o que você acha daquele Vince?" 

    nina "Ele é assustador, eu não quero participar desse jogo de assassinato" 

    minato "Eu também não quero" 

    nina "Tomara que as pessoas sejam sensatas pelo menos" 

    minato "Confeiteira o que você acha desse lugar?" 

    nina "Poderia ser pior, mas pelo menos temos uma cozinha, eu talvez possa fazer algo depois para todo mundo" 

    minato "Isso seria bom, de todo modo obrigado por compartilhar sua opinião"  

    nina "Me procure se precisar de ajuda"

    "Ela é uma pessoa amável, só espero que esse lugar não a maltrate"

    return

label dia1_cena1_esquerda:
    # cena antes do return

    "Ao entrar, há duas escolhas:biblioteca ou quadra"

    "Felix está na biblioteca."

    "Joana e Mitchell, na quadra"

    felix "Oi Amigo precisa de ajuda?" 

    minato "Não exatamente, eu queria perguntar sua opinião sobre o Vince?" 

    felix "Aquele gato é estranho" 

    felix "Bizarro demais"

    felix "Ele não vai nos deixar ir"

    felix "Se houver saída"

    minato "E quanto a esse lugar?"  

    felix "Eu acho esse lugar um tanto assustador, uma pena não ter nenhum piano" 

    minato "Um piano?" 

    felix "Sim ai eu poderia tentar aliviar o clima todo" 

    minato "Obrigado por compartilhar a sua opinião" 

    Felix "Não a de que, sempre que precisar de ajuda é só pedir"

    "Ele parece ser legal, apesar disso espero que aquele gato bizarro nos deixe sair"   

    joana "Como vai Espectador, quer treinar comigo?" 

    minato "Eu tô bem e não obrigado, eu queria te perguntar o que você acha do Vince?" 

    joana "Ele é estranho e assustador"

    joana "Foi ele quem nos trouxe até aqui"

    joana "Não vai nos deixar ir facilmente"

    joana "Talvez exista outra saída" 

    minato "O que você achou desse lugar?" 

    joana "Interessante e único, admito que estou curiosa quanto a esse lugar" 

    minato "Obrigado por compartilhar sua opinião" 

    joana "De nada"   

    "Ela é bem diferente dos outros, parece ser a única que permaneceu calma, e quem sabe as razões dela"

    "Ele está dançando passos bem familiares por algum motivo"

    return

label dia1_cena1_quarto:
    # cena antes do return

    mitchell "O que você deseja colega" 

    minato "Eu só queria saber sua opinião quanto ao Vince?" 

    mitchell "Aquele Vince é peculiar, tem cara de pilantra que só quer ver um banho de sangue" 

    minato "E esse lugar?" 

    mitchell "Esse lugarzinho sem graça, para uma torre sem vida, esse lugar tem cara de que pode se tornar interessante" 

    minato "Obrigado pela sua opinião" 

    mitchell "Claro só lembre de dançar mais para alegrar a vida" 

    "Esse cara é um tanto peculiar, é difícil saber se ele é confiável ou não"

    "Voltar para o quarto"

    "O jogador volta para o quarto e tem duas opções voltar ou ir dormir"

    "Dormir o dia encerra"

    "Meu pior momento chegou"

    "Quando fecho as pálpebras, vejo diferente"

    "Este lugar é artificial em essência"

    "Outros passaram por aqui antes de mim"

    "Alguns não voltaram"

    "Será que parte da história do mundo foi moldada através deste lugar?"

    "Talvez"

    "Mas eu já não tenho mais energia para pensar nisso"

    return
