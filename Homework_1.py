def main():
    name = input("Введите ваше имя: ")
    if not name:
        print("Вы ничего не ввели. Пожалуйста, запустите программу снова и введите имя.")
        return
    print(f"Привет, {name}!")

if __name__ == "__main__":
    main()