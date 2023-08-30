import phonenumbers

# input('Please enter your number')

number1 = input('Please enter your number: (with your phone code) ')

from phonenumbers import geocoder

number = phonenumbers.parse(number1)
print(geocoder.description_for_number(number,'tr'))

from phonenumbers import carrier
number = phonenumbers.parse(number1)
print(carrier.name_for_number(number,'tr'))