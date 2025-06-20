import csv
import unicodedata

def remover_acentos(texto):
    if texto is None:
        return ''
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

input_file = 'lista filial.csv'
output_file = 'lista filial_sem_acentos.csv'  # Melhor não sobrescrever o original

with open(input_file, mode='r', encoding='latin1') as infile, \
     open(output_file, mode='w', newline='', encoding='utf-8') as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for row in reader:
        nova_linha = [remover_acentos(campo) for campo in row]
        writer.writerow(nova_linha)

print("✅ Arquivo gerado:", output_file)
