# Имя файла, в который будут сохраняться данные
FILE_NAME = "credentials.txt"

def save_credentials(nickname, password):
    with open(FILE_NAME, "a") as file:
        file.write(f"{nickname}: {password}\n")

# Запрос у пользователя ника и пароля
nickname = input("Введите ваш ник: ")
password = input("Введите ваш пароль: ")

# Сохранение данных
save_credentials(nickname, password)
print("Данные успешно сохранены.")
