
label dia2_acusar_joana:
    show minato normal
    me "Pessoal, não percebem que essa discussão não está indo a lugar nenhum?"
    me "O verdadeiro culpado está tão claro como esse lugar, claramente foi a [joana]!"

    hide minato normal
    show joana irritada

    joana "texto dela"

    hide joana irritada
    show joana normal

    call escolhas_acusar(
        personagem = 'joana',
        passivo = '',
        agressivo = '',
        assertivo = '',
        passivo_agressivo = ''
    )

    call escolhas_acusar(
        personagem = 'joana',
        passivo = '',
        agressivo = '',
        assertivo = '',
        passivo_agressivo = ''
    )

    call get_most_selected_choice

    # XXX: fazer algo diferente baseado em 'most_often_choice'

    joana "você escolheu mais comunicação [most_often_choice]!"

    return


label dia2_acusar_joana_passivo1:
    return

label dia2_acusar_joana_agressivo1:
    return

label dia2_acusar_joana_assertivo1:
    return

label dia2_acusar_joana_passivo_agressivo1:
    return

label dia2_acusar_joana_passivo2:
    return

label dia2_acusar_joana_agressivo2:
    return

label dia2_acusar_joana_assertivo2:
    return

label dia2_acusar_joana_passivo_agressivo2:
    return

