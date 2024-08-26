
from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Ленина", "10", "15")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "5", "20")

mailing = Mailing(to_address, from_address, 250, "TR123456789")

print(mailing)
