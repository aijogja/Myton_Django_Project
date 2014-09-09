from apps.product.models import DiscountCode, Part

def populate_product_by_files(file):
    count = 0
    for line in file.xreadlines():
        line = line.strip()
        line = line.replace(" ", "")
        part_info_array = line.split(",")

        part_number = part_info_array[0]
        part_name = part_info_array[1]
        retail_price = part_info_array[2]
        quantity_issued_in = part_info_array[3]
        discount_code = part_info_array[4]
        surcharge = part_info_array[6]

        if int(quantity_issued_in) > 1:
            retail_price = float(quantity_issued_in) * float(retail_price)

        count = count + 1
        if discount_code:
            discount_code_leter = discount_code[1]
        else:
            discount_code_leter = 'A'
        buy_price = calculate_buy_price(retail_price, discount_code_leter)

        # Save to the database
        # print part_number
        discount = DiscountCode.objects.get(code=discount_code_leter)
        part, created = Part.objects.get_or_create(part_number=part_number)
        part.name = part_name
        part.retail_price = retail_price
        part.buy_price = buy_price
        part.surcharge = surcharge
        part.discount_code = discount
        part.save()


def calculate_buy_price(retail_price, discount_code_leter):
    # try:
    discount_code = DiscountCode.objects.get(code=discount_code_leter)
    # except:
        # print discount_code_leter

    buy_price_1 = float(retail_price) / 100
    buy_price_2 = float(discount_code.discount) * buy_price_1
    buy_price = float(retail_price) - buy_price_2

    return buy_price
