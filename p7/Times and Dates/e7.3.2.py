# E-7.3.2: Valid PIC

# Problem: https://programming-22.mooc.fi/part-7/3-times-and-dates#programming-exercise-how-old


# Sample output:


# Solution:
from datetime import datetime
from string import digits


def is_it_valid(pic: str):
    if len(pic) != 11:
        return False

    nums = pic[7:10]
    for x in nums:
        if x not in digits:
            return False

    remainder_index = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    remainder = int(pic[0:6] + pic[7:10]) % 31
    if pic[10] != remainder_index[remainder]:
        return False

    yy = pic[6]
    mm = pic[2:4]
    dd = pic[0:2]

    if '+' in yy:
        year = '18' + pic[4:6]
    elif '-' in yy:
        year = '19' + pic[4:6]
    elif 'A' in yy:
        year = '20' + pic[4:6]
    else:
        return False

    try:
        dob = datetime(int(year), int(mm), int(dd))
    except:
        return False

    return True


if __name__ == '__main__':
    print(is_it_valid("230827-906F"))
    print(is_it_valid("120488+246L"))
    print(is_it_valid("310823A9877"))
