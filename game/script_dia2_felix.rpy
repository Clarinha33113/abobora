
label dia2_acusar_felix:
    show minato normal
    me "Pessoal, não percebem que essa discussão não está indo a lugar nenhum?"
    me "O verdadeiro culpado está tão claro como esse lugar, claramente foi o [felix]!"

    hide minato normal
    show felix pensativo

    felix "texto dele"

    call escolhas_acusar(
        personagem = 'felix',
        passivo = '',
        agressivo = '',
        assertivo = '',
        passivo_agressivo = ''
    )

    call escolhas_acusar(
        personagem = 'felix',
        passivo = '',
        agressivo = '',
        assertivo = '',
        passivo_agressivo = ''
    )

    call get_most_selected_choice

    # XXX: fazer algo diferente baseado em 'most_often_choice'

    felix "você escolheu mais comunicação [most_often_choice]!"

    return


label dia2_acusar_felix_passivo1:
    return

label dia2_acusar_felix_agressivo1:
    return

label dia2_acusar_felix_assertivo1:
    return

label dia2_acusar_felix_passivo_agressivo1:
    return

label dia2_acusar_felix_passivo2:
    return

label dia2_acusar_felix_agressivo2:
    return

label dia2_acusar_felix_assertivo2:
    return

label dia2_acusar_felix_passivo_agressivo2:
    return

