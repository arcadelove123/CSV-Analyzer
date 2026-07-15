import csv

file_name = "sales_data.csv"

date_list = list()
product_list = list()
category_list = list()
quantity_list = list()
price_list = list()
region_list = list()

def load_csv():
    try:
        with open(file_name, "r", newline="") as f:
            data = list(csv.reader(f))

            for i, value in enumerate(data[1:]):
                for i, v in enumerate(value):
                    if i == 0:
                        date_list.append(v)
                    elif i == 1:
                        product_list.append(v)
                    elif i == 2:
                        category_list.append(v)
                    elif i == 3:
                        quantity_list.append(v)
                    elif i == 4:
                        price_list.append(v)
                    elif i == 5:
                        region_list.append(v)
    except:
        print("Can't find the file")


def total_count():
    total = 0

    for i in range(len(quantity_list)):
        total += int(quantity_list[i]) * int(price_list[i])
    
    return total

def category_sales():
    non_duplicated_category_list = list(set(category_list))
    category_dic = {}
    for value in non_duplicated_category_list:
        category_dic[value] = 0
    
    for i in range(len(price_list)):
        category_dic[category_list[i]] = int(category_dic.get(category_list[i])) + int(price_list[i]) * int(quantity_list[i])

    return category_dic

def regional_sales():
    non_duplicated_region_list = list(set(region_list))
    region_dic = {}
    for value in non_duplicated_region_list:
        region_dic[value] = 0
    
    for i in range(len(price_list)):
        region_dic[region_list[i]] = int(region_dic.get(region_list[i])) + int(price_list[i]) * int(quantity_list[i])

    return region_dic

def average_prices():
    count = 0
    for value in quantity_list:
        count += int(value)

    return round(total_count()/count, 2)

def find_best_seller():
    best_seller = ""
    best_seller_price = 0

    for i in range(len(quantity_list)):
        item_price = int(quantity_list[i]) * int(price_list[i])
        if item_price > best_seller_price:
            best_seller_price = item_price
            best_seller = product_list[i]
    
    return best_seller


load_csv()

while True:
    ask = input("1. Total Revenue\n" \
    "2. Category Sales\n" \
    "3. Regional Sales\n" \
    "4. Average Price\n" \
    "5. Highest Revenue Product\n" \
    "6. Exit\n")

    if ask == "1":
        print(f"\n\nTotal avenue is ${total_count()}\n\n")
    if ask == "2":
        category_dic = category_sales()
        print("\n\nCategory Sales\n\n")
        print(f"Electronics: ${category_dic.get('Electronics')}")
        print(f"Furniture: ${category_dic.get('Furniture')}")
        print(f"Stationery: ${category_dic.get('Stationery')}\n\n")
    if ask == "3":
        region_dic = regional_sales()
        print("\n\nRegion Sales\n\n")
        print(f"East: ${region_dic.get('East')}")
        print(f"West: ${region_dic.get('West')}")
        print(f"South: ${region_dic.get('South')}")
        print(f"North: ${region_dic.get('North')}\n\n")
    if ask == "4":
        print(f"\n\nAverage Price is {average_prices()}\n\n")
    if ask == "5":
        print(f"\n\nThe higehst Revenue Product is {find_best_seller()}\n\n")
    if ask == "6":
        break

    



