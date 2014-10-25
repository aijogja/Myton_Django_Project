from apps.product.models import DiscountCode, Part
from datetime import datetime
# from django.db import transaction

# @transaction.commit_manually
def populate_product_by_files(file, supplier=None):
    count = 0
    Part.objects.filter(supplier=supplier).update(deleted=True)
    print datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for line in file.xreadlines():
        try:
            line = line.strip()
            line = line.replace(" ", "")
            part_info_array = line.split(",")

            part_number = part_info_array[0]
            part_name = part_info_array[1]
            retail_price = part_info_array[2]
            quantity_issued_in = part_info_array[3]
            discount_code = part_info_array[4]
            supersessions = part_info_array[5]
            surcharge = part_info_array[6]

            if int(quantity_issued_in) > 1:
                retail_price = float(quantity_issued_in) * float(retail_price)

            count = count + 1
            if discount_code:
                discount_code_leter = discount_code[1]
            else:
                discount_code_leter = 'A'

            try:
                discount = DiscountCode.objects.get(code=discount_code_leter)
            except:
                discount = DiscountCode.objects.get(code='A')

            # Calculate buy price
            buy_price = calculate_buy_price(retail_price, discount)
            # Save to the database
            # print str(count) + ' - ' + part_number
            part, created = Part.objects.get_or_create(part_number=part_number)
            part.name = part_name
            part.retail_price = retail_price
            part.buy_price = buy_price
            part.surcharge = surcharge
            part.supersessions = supersessions
            part.discount_code = discount
            part.deleted = False
            if supplier :
                part.supplier = supplier
            part.save()
        except:
            pass
    # transaction.commit()
    print datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def calculate_buy_price(retail_price, discount_code):
    buy_price_1 = float(retail_price) / 100
    buy_price_2 = float(discount_code.discount) * buy_price_1
    buy_price = float(retail_price) - buy_price_2

    return buy_price

