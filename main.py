from helpers import juros_compostos

import locale
locale.setlocale(locale.LC_MONETARY, 'pt_br')

if __name__ == '__main__':
    emprestimo = float(input("Qual o valor do empréstimo: "))
    juros_anual = float(input("Qual a taxa de juros anual: "))
    prazo = int(input("Qual o prazo em anos: "))

    valor_final_a_pagar = juros_compostos(emprestimo, juros_anual, prazo)
    print(f"\nO montante a pagar é {locale.currency(valor_final_a_pagar, grouping=True)}")
    print(f"O valor da parcela ao mês: {locale.currency((valor_final_a_pagar / prazo / 12), grouping=True)}")
