import phonenumbers
from phonenumbers import geocoder, carrier, timezone
phone_number = input()
phone_number = phonenumbers.parse(phone_number)

print(f"Cauntry  {geocoder.description_for_number(phone_number,'uz')}")

print(f"Company  {carrier.name_for_number(phone_number,'uz')}")

print(f"Timezone {timezone.time_zones_for_number(phone_number)}")

print(f"Valid Mobile Number: {phonenumbers.is_valid_number(phone_number)}")

print(f"Checking possiblity of Number : {phonenumbers.is_possible_number(phone_number)}")
