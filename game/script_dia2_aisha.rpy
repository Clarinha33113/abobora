
label dia2_acusar_aisha:
    me "Pessoal, não percebem que essa discussão não está indo a lugar nenhum?"
    me "O verdadeiro culpado está tão claro como esse lugar, claramente foi a [aisha]!"

    show aisha assustada

    aisha "Sob quais provas você afirma isso, sua afirmação é um completo absurdo, facilmente poderia ser você, só querendo desviar a atenção para mim."

    hide aisha assustada
    show aisha normal
    call escolhas_acusar(personagem = 'aisha',
        passivo = 'Eu não estou, só tô seguindo um palpite.',
        agressivo = 'Besteira, você é claramente a culpada.',
        assertivo = 'Eu não estou tentando desviar a atenção, e eu tenho provas.',
        passivo_agressivo = 'É mesmo, falou o poço de inocência.')

    call escolhas_acusar(personagem = 'aisha',
        passivo = 'Eu só estou apontando as inconsistências.',
        agressivo = 'Além da sua atitude, você exala o cheiro da culpa!',
        assertivo = 'Você afirma estar ajudando na investigação, mas o que impede você de ter adulterado as provas.',
        passivo_agressivo = 'Engraçado como tudo soa conveniente demais.')
    return


label dia2_acusar_aisha_passivo1:
    me "As provas do meu ponto de vista apontam para você, especialmente pela sua total indiferença à morte dela."
    aisha "Você fala como se só eu fosse indiferente, alguns aqui também são, você também demonstrou frieza com a morte dela."
    "Todos olham para mim com pena."
    return

label dia2_acusar_aisha_agressivo1:
    me "Você demonstra pouco se importar com qualquer um aqui, você mesma mataria qualquer um mais vulnerável, especialmente ela."
    aisha "Eu admito que você é rápido em acusar alguém, mas seu erro é que todos aqui no fim desejam o poder da torre, minha atitude não é diferente de qualquer um aqui."
    "Todos olham para mim, alguns com medo e outros irritados."
    return

label dia2_acusar_aisha_assertivo1:
    me "Eu observei toda a situação, e você dentre todos têm agido com maior indiferença, você estava perto do corpo, apenas criticando sem compartilhar nenhuma informação com o [clint]."
    aisha "O que? Como você ousa, eu estava investigando como todo mundo, o [clint] só era incompetente demais para merecer a minha ajuda!"
    "Todos olham para mim com um olhar pensativo."
    return

label dia2_acusar_aisha_passivo_agressivo1:
    me "Eu estava pensando nos detalhes, e sabe tudo, soa suspeito vindo de você, eu tô apenas seguindo a minha intuição, e de todos aqui, você soa a mais suspeita especialmente pela sua indiferença."
    aisha "Minha indiferença? Você fala como se fosse melhor, você acha que uma investigação séria usa apenas a intuição?"
    "Todos olham para mim, alguns com dúvidas e outros com desconfiança."
    return

label dia2_acusar_aisha_passivo2:
    return

label dia2_acusar_aisha_agressivo2:
    return

label dia2_acusar_aisha_assertivo2:
    return

label dia2_acusar_aisha_passivo_agressivo2:
    return

