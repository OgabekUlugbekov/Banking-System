
users = {}
transactions = []

def create_account():
    print("Akkaunt yaratish")
    name = input("Ismingizni kiriting: ").lower()
    last_name = input("Sharifingizni kiriting: ").lower()
    email = input("Elektron manzilingizni kiriting: ").lower()
    password = input("Parol kiriting: ")

    if email in users:
        print("Ushbu elektron manzil band!")
        return

    users[email] = {
        'name': name,
        'last_name': last_name,
        'password': password,
        'balance': 0.0
    }
    print("Akkaunt muvaffaqiyatli yaratildi!")


def check_login(email, password):
    if email in users and users[email]['password'] == password:
        return True
    return False



def balance():
    print("Balansni boshqarish uchun akkauntga kiring")
    email = input("Elektron manzilingizni kiriting: ").lower()
    password = input("Parolingizni kiriting: ")

    if not check_login(email, password):
        print("Manzil yoki parol xato!")
        return

    while True:
        print("Balans")
        print(f"Hozirgi balans: ${users[email]['balance']:.2f}")
        print("1. Deposit qo'yish")
        print("2. Pul chiqarish")

        choice = input("Yuqoridagi raqamlardan birini tanlang: ")

        if choice == '1':
            amount = float(input("Pul miqdorini kiriting: $"))
            if amount > 0:
                users[email]['balance'] += amount
                print(f"${amount:.2f} miqdordagi deposit qo'yildi")
            else:
                print("Miqdor musbat bo'lishi kerak!")

        elif choice == '2':
            amount = float(input("Nechi pul olmoqchisiz?: $"))
            if amount > 0:
                if amount <= users[email]['balance']:
                    users[email]['balance'] -= amount
                    print(f"${amount:.2f} qiymatda pul chiqarildi")
                else:
                    print("Yetarli mablag' mavjud emas!")
            else:
                print("Miqdor musbat bo'lishi kerak!")

def forgot_password():
    print("Parolingizni unutgan bo'lsangiz")
    name = input("Ismingizni kiriting: ").lower()
    last_name = input("Sharifingizni kiriting: ").lower()

    for email, user in users.items():
        if user['name'] == name and user['last_name'] == last_name:
            print(f"Elektron manzilingiz topildi: {email}")
            new_password = input("Yangi parol kiriting: ")
            users[email]['password'] = new_password
            print("Parol qaytadan yaratildi!")
            return
    print("Akkaunt topilmadi!")

def transfer():
    print("Pul o'tkazish")
    email = input("Elektron manzilingiz: ").lower()
    password = input("Parolingiz: ")

    if not check_login(email, password):
        print("Xato!")
        return

    amount = float(input("Yubormoqchi bo'lgan miqdorni kiriting: $"))
    address = input("Yuborish manzilini kiriting: ")
    if amount > 0:
        if amount <= users[email]['balance']:
            users[email]['balance'] -= amount
            print(f"Pul {address}ga yuborildi!")
        else:
            print("Yetarli mablag' mavjud emas!")
    else:
        print("Miqdor musbat bo'lishi keral!")


def main():
    while True:
        print("Bank ilovasiga xush kelibsiz")
        print("1. Akkaunt yaratish")
        print("2. Balans")
        print("3. Pul o'tkazmalari")
        print("4. Parolni unutgan bo'lsangiz")
        print("5. Chiqish")

        choice = input("Yuqoridagilardan birini tanlang: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            balance()
        elif choice == '3':
            transfer_money()
        elif choice == '4':
            forgot_password()
        elif choice == '5':
            print("Xayr!")
            break
        else:
            print("Berilgan sonlardan tanlang!")
main()