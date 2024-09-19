import csv
import random
from faker import Faker

fake = Faker()

def csv_factory(lines):
    categories = ['Eletrônicos', 'Livros', 'Roupas', 'Brinquedos', 'Alimentos', 'Ferramentas', 'Beleza', 'Esportes']
    filename = 'csv_fabricado.csv'
    with open(filename, mode='w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Nome', 'Categoria', 'Preço', 'Descrição'])
        for i in range(1, lines+1):
            id = i
            product_name = fake.catch_phrase()
            category = random.choice(categories)
            price = round(random.uniform(10.5, 500), 2)
            description = fake.sentence(nb_words=12)

            writer.writerow([id, product_name, category, price, description])
    print(f'Arquivo {filename} gerado com sucesso!')

csv_factory(100)