import logging
logging.basicConfig(level=logging.DEBUG)
num = 0

def start(num):
    choose = input("Podaj działane, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnozenie, 4 Dzielenie :")
    if choose == "1":
        count = addition(num)
    elif choose == "2":
        count = substraction(num)
    elif choose == "3":
        count = multiplication(num)
    elif choose == "4":
        count = division(num)
    else:
        logging.warning("Nie podałeś cyfry 1-4, lub podałeś literę!")

def addition(num):
    how_many = int(input("Ile  liczby chcesz dodać: "))
    numbers = []
    add = 0
    for i in range(how_many):
        i = float(input("Podaj składnik %s: " % (i+1)))
        numbers.append(i)
        add = sum(numbers)
    logging.warning(f"Dodaję {numbers}")
    logging.info(f"Wynik to {'%.2f' % add}")
    return add

def substraction(num):
    how_many = int(input("Ile  liczby chcesz odjąć: "))
    numbers = []
    for i in range(how_many):
        i = float(input("Podaj składnik %s: " % (i+1)))
        numbers.append(i)
        subs = numbers[0]
        for n in numbers[1:]:
            subs = subs - n    
            logging.info("Wynik to %d" % subs)

    logging.warning("Odejmuje %s" % numbers)
    logging.info(f"Wynik ostateczny to {'%.2f' % subs}" )
    return subs

def multiplication(num):
    how_many = int(input("Ile  liczby chcesz pomnozyć: "))
    numbers = []
    for i in range(how_many):
        i = float(input("Podaj składnik %s: " % (i+1)))
        numbers.append(i)
        mul = 1
        for n in numbers:
            mul = mul * n
    logging.warning(f"Mnoze {numbers}")
    logging.info(f"Wynik to {'%.2f' % mul}")
    return mul

def division(num):
    how_many = int(input("Ile  liczby chcesz podzielić: "))
    numbers = []
    divi = 0
    for i in range(how_many):
        i = float(input("Podaj składnik %s: " % (i+1)))
        numbers.append(i)
        divi = numbers[0]
        for n in numbers[1:]:
            divi = divi / n    
            logging.info(f"Wynik to {'%.2f' % divi}" )

    logging.warning("Dzięlę %s" % numbers)
    logging.info(f"Wynik ostateczny to {'%.2f' % divi}")
    return divi