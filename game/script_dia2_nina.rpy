
label dia2_acusar_nina:
    show minato normal
    me "Pessoal, não percebem que essa discussão não está indo a lugar nenhum?"
    me "O verdadeiro culpado está tão claro como esse lugar, claramente foi a [nina]!"

    hide minato normal
    show nina enojada

    nina "texto dela"

    hide nina enojada
    show nina infeliz

    call escolhas_acusar(
        personagem = 'nina',
        passivo = '',
        agressivo = '',
        assertivo = '',
        passivo_agressivo = ''
    )

    call escolhas_acusar(
        personagem = 'nina',
        passivo = '',
        agressivo = '',
        assertivo = '',
        passivo_agressivo = ''
    )

    call get_most_selected_choice

    # XXX: fazer algo diferente baseado em 'most_often_choice'

    nina "você escolheu mais comunicação [most_often_choice]!"

    return


label dia2_acusar_nina_passivo1:
    return

label dia2_acusar_nina_agressivo1:
    return

label dia2_acusar_nina_assertivo1:
    return

label dia2_acusar_nina_passivo_agressivo1:
    return

label dia2_acusar_nina_passivo2:
    return

label dia2_acusar_nina_agressivo2:
    return

label dia2_acusar_nina_assertivo2:
    return

label dia2_acusar_nina_passivo_agressivo2:
    return

