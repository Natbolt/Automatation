from smartphone import Smartphone

catalog = []
phone1 = Smartphone("Samsung", "Galaxy S21", "+79123456789")
phone2 = Smartphone("Apple", "IPhone 12", "+79876543210")
phone3 = Smartphone("Xiomi", "Mi 11", "+79638527410")
phone4 = Smartphone("HONOR", "X5 Plus", "+79741852630")
phone5 = Smartphone("Poco", "C51", "+79852074163")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")