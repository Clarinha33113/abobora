
label dia2_acusar_clint:
    show minato normal
    me "Pessoal, não percebem que essa discussão não está indo a lugar nenhum?"
    me "O verdadeiro culpado está tão claro como esse lugar, claramente foi a [clint]!"

    hide minato normal
    show clint normal

    clint "bruh"

    call escolhas_acusar(
        personagem = 'clint',
        passivo = '',
        agressivo = '',
        assertivo = '',
        passivo_agressivo = '',
    )

    return


label dia2_acusar_clint_passivo1:
    return

label dia2_acusar_clint_agressivo1:
    return

label dia2_acusar_clint_assertivo1:
    return

label dia2_acusar_clint_passivo_agressivo1:
    return

