def add_fruit(inventory, fruit, quantity=0):
    if fruit in inventory:
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity

def test(obtido, esperado):
    if obtido == esperado:
        print(f"PASSOU: {obtido} == {esperado}")
    else:
        print(f"FALHOU: obtido {obtido}, esperado {esperado}")
def main():
     # Testes
     new_inventory = {}
     add_fruit(new_inventory, 'strawberries', 10)
     test('strawberries' in new_inventory, True)
     test(new_inventory['strawberries'], 10)

     add_fruit(new_inventory, 'strawberries', 25)
     test(new_inventory['strawberries'], 35)
if __name__ == '__main__':
     main()