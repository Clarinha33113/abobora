
label dia2_acusar_mitchell:
    show minato normal
    me "Pessoal, não percebem que essa discussão não está indo a lugar nenhum?"
    me "O verdadeiro culpado está tão claro como esse lugar, claramente foi o [mitchell]!"

    hide minato normal
    show mitchell seila

    mitchell "texto dele"

    call escolhas_acusar(
        personagem = 'mitchell',
        passivo = '',
        agressivo = '',
        assertivo = '',
        passivo_agressivo = ''
    ) from _call_escolhas_acusar_7

    call escolhas_acusar(
        personagem = 'mitchell',
        passivo = '',
        agressivo = '',
        assertivo = '',
        passivo_agressivo = ''
    ) from _call_escolhas_acusar_8

    call get_most_selected_choice from _call_get_most_selected_choice_3

    # XXX: fazer algo diferente baseado em 'most_often_choice'

    mitchell "você escolheu mais comunicação [most_often_choice]!"

    return


label dia2_acusar_mitchell_passivo1:
    return

label dia2_acusar_mitchell_agressivo1:
    return

label dia2_acusar_mitchell_assertivo1:
    return

label dia2_acusar_mitchell_passivo_agressivo1:
    return

label dia2_acusar_mitchell_passivo2:
    return

label dia2_acusar_mitchell_agressivo2:
    return

label dia2_acusar_mitchell_assertivo2:
    return

label dia2_acusar_mitchell_passivo_agressivo2:
    return

