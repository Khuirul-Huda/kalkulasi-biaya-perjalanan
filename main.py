import math, os




items = []
items_price = []
participant = 0

# argumen tanpa return
def add_item(name: str, price: int):
    items.append(name)
    items_price.append(price)

#argumen dengan return
def average(sum: int, count: int):
    return math.ceil(int(sum)/int(count))


#tanpa argumen tanpa return
def conclusion():
    total_price = calculate_price()
    print("RINCIAN BIAYA")
    print("-------------------------")
    print("Total Peserta: " + str(participant))
    print("Total Biaya: " + format(total_price, ','))
    print("--------------------------")
    print("Biaya tiap peserta: " + format(average(total_price, participant), ','))
    print("---------------------------")
    print_items()


#tanpa argumen dengan return
def calculate_price():
    total_price = 0
    for item_price in items_price:
        total_price += int(item_price)
    return total_price

def print_items():
    for index, item in enumerate(items):
        print(item + '      ' + format(int(items_price[index]), ','))

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


clear_terminal()
print("KALKULASI BIAYA PERJALANAN WISATA")


participant = input("Masukkan jumlah peserta:")

next_input = True 
while(next_input):
    clear_terminal()
    print("Tambah Item Baru")
    print("----------")
    item = input("Nama Item: ")
    price = input("Harga/Biaya: ")
    add_item(item, price)
    restart = input("Apakah ingin menambahkan produk lagi? (Y/N)")

    if (restart == 'n' or restart == 'N'):
        next_input = False

clear_terminal()
conclusion()
