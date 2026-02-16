label prologo_start:
    call transition("Prólogo\nUma manhã inesperada")

    # main menu pra tudo fodase
    play music "main menu.mp3" loop if_changed

    "Outra noite, com mais melancolia no ar."

    "Eu sinto o vento no meu rosto, o calor da cama, porém isso é tão facilmente esquecido..."

    "Quando aquele sonho começa, o mesmo que me lembra por que estou aqui, por que as coisas são o que são..."

    scene bg quarto_escuro with dissolve
    show minato quando_acorda

    me "Aquele sonho de novo... Por que aquele sonho?"

    me "Por que eu não consigo me livrar dele? Já faz 10 anos com esse mesmo maldito sonho."

    scene black with dissolve

    hide minato quando_acorda

    me "Esse corredor longo e escuro... logo será esquecido, como tudo o que veio antes. Pois, na luz, a minha manhã de mais um dia começa."

    scene bg cozinha_prologo with dissolve

    show minato normal

    me "O que será hoje? Creio que uma boa panqueca pode melhorar as coisas. Esse cheiro sempre me ajuda nas manhãs e, com um achocolatado, pode se tornar ainda melhor."

    me "Hoje teremos mais uma aula de matemática, e vou precisar de energia para aguentar aquela aula... Por que não temos aula de história no lugar de matemática? Uma pena a vida ser assim, tão monótona."

    # Ele fora de casa

    scene bg cidade_manha with dissolve

    hide minato normal

    "Essa luz na pele é tão boa, é como um abraço. Essa estrada me lembra do velho mundo, tantas ruínas que um dia foram o local de trabalho de tantos ou a casa de alguém, especialmente aquele lugar."

    # XXX: Ele em frente a um predio em ruinas

    "Difícil imaginar as coisas voltarem a ser como eram antes. Eu queria poder estar aqui para ver como era."

    scene bg armarios_escola with dissolve

    "Certas coisas nunca mudam, como a escola. Ela é interessante à sua própria maneira. O calor do sol é ainda melhor em um lugar onde o potencial pode despertar."

    # Ele em frente ao seu armario

    me "O que é isso dentro do meu armário?"

    "[my_name] encontrou uma carta peculiar, o símbolo era desconhecido para ele, apesar disso ele abre a carta e lê:"

    show carta1
    pause
    hide carta1

    me "Isso é estranho. As passagens são verdadeiras e as férias de verão estão logo aí. O vovô e a vovó vão gostar, e isso deve ser daquele sorteio nacional."

    "Ao olhar, [my_name] percebe que a assinatura pede um título em vez do nome. Então ele pensa e escreve:"

    "{b}O Espectador.{/b}"

    jump dia1_start
