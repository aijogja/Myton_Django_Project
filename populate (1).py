import os


def find_buy_price(retail_price, discount_code):

    # Trim the discount code as we only need the second letter to work out our
    # discount code letter

    discount_code = discount_code[1]

    length_of_discount_code = len(discount_code)
    print "Length of Discount Code = " + str(length_of_discount_code)
    # Check to make sure tha the discount code is one letter - otherwise
    # report an error
    if length_of_discount_code == 1:

        if discount_code == "A":
            discount_percent = 0.00
        elif discount_code == "B":
            discount_percent = 0.00
        elif discount_code == "C":
            discount_percent = 2.5
        elif discount_code == "D":
            discount_percent = 5.00
        elif discount_code == "E":
            discount_percent = 14.50
        elif discount_code == "F":
            discount_percent = 10.00
        elif discount_code == "G":
            discount_percent = 13.50
        elif discount_code == "H":
            discount_percent = 16.50
        elif discount_code == "I":
            discount_percent = 16.50
        elif discount_code == "J":
            discount_percent = 19.00
        elif discount_code == "K":
            discount_percent = 19.00
        elif discount_code == "L":
            discount_percent = 12.50
        elif discount_code == "M":
            discount_percent = 22.00
        elif discount_code == "N":
            discount_percent = 27.00
        elif discount_code == "O":
            discount_percent = 20.00
        elif discount_code == "P":
            discount_percent = 28.00
        elif discount_code == "U":
            discount_percent = 32.00
        elif discount_code == "V":
            discount_percent = 0.00
        elif discount_code == "W":
            discount_percent = 38.00
        elif discount_code == "Z":
            discount_percent = 0.00
    else:
        print "Discount Code Size Error, Discount Code Reported is " + str(discount_code)

    print "Discount Code is : " + str(discount_code)
    print "Discount Percentage is : " + str(discount_percent)
    retail_price = float(retail_price)
    # work out the buy price using the discount percentage and retail price

    buy_price_1 = retail_price / 100
    buy_price_2 = discount_percent * buy_price_1
    buy_price = retail_price - buy_price_2

    return buy_price


def populate():
    f = open("populate/thisone.prl")
    # Set count to 1
    count = 1

    for line in f.xreadlines():
        line = line.strip()
        line = line.replace(" ", "")

        part_info_array = line.split(",")

        # unpack list into variables
        part_number = part_info_array[0]
        part_description = part_info_array[1]
        retail_price = part_info_array[2]
        quantity_issued_in = part_info_array[3]
        discount_code = part_info_array[4]
        unknown = part_info_array[5]
        surcharge = part_info_array[6]

        # Bug in system found - 01.05.2014
        # Prices seem to be wrong when the part quantity issued in is more than 1.
        # new script that alters the retail price if the quantity is more than
        # 1

        if int(quantity_issued_in) > 1:
            retail_price = float(quantity_issued_in) * float(retail_price)

        # increment count so that we know how many parts the program has
        # processed
        count = count + 1

        print "START OF PART **************************************************************"
        # call functions to get the results we need
        print "Number: " + str(count)
        print "Part Number : " + part_number
        print "Part Description : " + part_description
        print "Retail Price : " + str(retail_price)
        print "Discount Code : " + discount_code

        # A small test to make sure that the discount code is valid and not
        # empty or too small
        if len(discount_code) == 0 or len(discount_code) >= 3:
            print "Error Found, discount code is either too short or too big"
            # error report into the file (or another file so that we know that
            # this part is invalid

        else:
            buy_price = find_buy_price(retail_price, discount_code)

        print "Myton Buy Price : " + str(buy_price)
        print "END OF PART *****************************************************************"
        # write to the database here

        add_part(part_num=part_number,
                 part_name=part_description,
                 retail_price=retail_price,
                 weight=0.0,
                 buy_price=buy_price,
                 surcharge=surcharge)

    f.close()


def add_part(part_num, part_name, retail_price, weight, buy_price, surcharge):
    p = Part.objects.get_or_create(
        part_number=part_num, description=part_name, rrp_price=retail_price, weight=weight,
        buy_price=buy_price, surcharge=surcharge)[0]
    return p


# Start execution here!
if __name__ == '__main__':
    print "Starting Myton Parts population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Myton_Django.settings')
    from trade.models import Part

    populate()
