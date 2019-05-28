""""

Задание 1

0) Повторение понятий из биологии (ДНК, РНК, нуклеотид, протеин, кодон)

1) Построение статистики по входящим в последовательность ДНК нуклеотидам
для каждого гена (например: [A - 46, C - 66, G - 23, T - 34])

2) Перевод последовательности ДНК в РНК (окей, Гугл)

3) Перевод последовательности РНК в протеин*


*В папке files вы найдете файл rna_codon_table.txt -
в нем содержится таблица переводов кодонов РНК в аминокислоту,
составляющую часть полипептидной цепи белка.


Вход: файл dna.fasta с n-количеством генов

Выход - 3 файла:
 - статистика по количеству нуклеотидов в ДНК
 - последовательность РНК для каждого гена
 - последовательность кодонов для каждого гена

 ** Если вы умеете в matplotlib/seaborn или еще что,
 welcome за дополнительными баллами за
 гистограммы по нуклеотидной статистике.
 (Не забудьте подписать оси)

P.S. За незакрытый файловый дескриптор - караем штрафным дезе.

"""

from pathlib import Path

file = Path('./files/dna.fasta')


def translate_from_dna_to_rna(dna):
    return dna.read_text().replace('T', 'U')


def count_nucleotides(dna):
    enums = ['A', 'C', 'G', 'T']
    data = ''.join([line for line in dna.read_text().splitlines() if ' ' not in line])
    return {key: data.count(key) for key in enums}


def translate_rna_to_protein(rna):

    """your code here"""

    # return protein
    pass


def main():
    rna = translate_from_dna_to_rna(file)
    print('RNA : ', rna)


if __name__ == '__main__':
    main()
