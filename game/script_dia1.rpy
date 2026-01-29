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
    return

label dia1_cena1_direita:
    # cena antes do return
    return

label dia1_cena1_esquerda:
    # cena antes do return
    return

label dia1_cena1_quarto:
    # cena antes do return
    return
