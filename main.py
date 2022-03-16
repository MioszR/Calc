import logging
logging.basicConfig(level=logging.DEBUG)
num = 0

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