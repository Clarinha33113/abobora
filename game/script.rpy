define me = Character("[my_name]")
define vince = Character("Vince")
define clint = Character("Clint")
define aisha = Character("Aisha")
define sofia = Character("Sofia")
define thiago = Character("Thiago")
define mitchell = Character("Mitchell")
define nina = Character("Nina")
define felix = Character("Felix")
define joana = Character("Joana")
define diana = Character("Diana")

label start:
    python:
        DEFAULT = 'Minato Yuki'
        my_name = renpy.input('Qual seu nome?', default=DEFAULT, length=32).strip()

        if not my_name:
            my_name = DEFAULT

    scene black with dissolve
    show text "Prólogo\nUma manhã inexperada" with Pause(2)
    scene black with dissolve

    "Outra noite, com mais melancolia no ar."

    "Eu sinto o vento no meu rosto, o calor da cama, porém isso é tão facilmente esquecido..."

    "Quando aquele sonho começa, o mesmo sonho que me lembra porque eu estou aqui, porque as coisas são o que são..."

    scene bg quarto_escuro with dissolve
    show minato quando_acorda

    me "Aquele sonho de novo... Por que aquele sonho?"

    me "Por que eu não consigo me livrar dele? Já faz 10 anos com esse mesmo maldito sonho."

    scene black with dissolve

    hide minato quando_acorda

    me "Esse corredor longo e escuro... Logo será esquecido, como tudo o que veio antes. Pois na luz a minha manhã de mais um dia começa."

    # Ele na cozinha

    scene bg cozinha with dissolve

    show minato normal

    me "O que será hoje? Creio que uma boa panqueca pode melhorar as coisas. Esse cheiro sempre me ajuda nas manhãs, e com um achocolatado pode se tornar melhor."

    me "Hoje teremos mais uma aula de matemática e vou precisar de energia para aguentar aquela aula, porque não temos aula de história no lugar de matemática, uma pena a vida ser assim, tão monótona."

    # Ele fora de casa

    scene bg cidade_manha with dissolve

    hide minato normal

    "Essa luz na pele é tão boa, é como um abraço. Essa estrada me lembra do velho mundo, tantas ruinas que um dia foram o local de trabalho de tantos, ou a casa de alguém, especialmente aquele lugar."

    # Ele em frente a um predio em ruinas

    "Difícil imaginar as coisas voltarem a ser como eram antes, eu queria poder estar aqui para ver antes."

    scene bg armarios_escola with dissolve

    "Certas coisas nunca mudam, como a escola. Ela é interessante do seu próprio modo, o calor do sol é ainda melhor em um lugar onde o potencial pode despertar."

    # Ele em frente ao seu armario

    me "O que é isso dentro do meu armário?"

    "[my_name] encontrou uma carta peculiar, o símbolo era desconhecido para ele, apesar disso ele abre a carta e lê:"

    "{i}Prezado(a) [my_name]{/i}"

    # Talvez mostrar uma imagem com as passagens na tela também?

    "[my_name] vê três passagens para um belo campo florido com um rio, um lugar que lembrava tranquilidade para ele."

    "{i}Gostaríamos de parabenizá-lo por ter sido selecionado para uma viajem com tudo pago para um lugar especial, para você e sua família descansarem, basta apenas assinar essa carta e poderá usar essas passagens.{/i}"

    me "Isso é estranho, as passagens são verdadeiras, e as férias de verão estão logo ai, o vovô e a vovó vão gostar, e isso deve ser daquele sorteio nacional."

    "Ao olhar [my_name] percebe que a assinatura pede um título ao invés do nome, então ele pensa e escreve:"

    "{b}O Espectador{/b}"

    "De repente ele é teletransportado para uma sala escura..."

    jump dia1_start

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

    vince "{b}Um de vocês precisa se tornar o assassino perfeito.{/b}"

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

    return
