label prologo_start:
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

    show carta1
    ""
    hide carta1

    # "{i}Prezado(a) [my_name]{/i}"

    # "[my_name] vê três passagens para um belo campo florido com um rio, um lugar que lembrava tranquilidade para ele."
    # Talvez mostrar uma imagem com as passagens na tela também?

    # "{i}Gostaríamos de parabenizá-lo por ter sido selecionado para uma viajem com tudo pago para um lugar especial, para você e sua família descansarem, basta apenas assinar essa carta e poderá usar essas passagens.{/i}"

    me "Isso é estranho, as passagens são verdadeiras, e as férias de verão estão logo ai, o vovô e a vovó vão gostar, e isso deve ser daquele sorteio nacional."

    "Ao olhar [my_name] percebe que a assinatura pede um título ao invés do nome, então ele pensa e escreve:"

    "{b}O Espectador{/b}"

    "De repente ele é teletransportado para uma sala escura..."

    jump dia1_start
