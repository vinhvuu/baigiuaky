import random

def game():
    number = random.randint(1, 100)
    attempts = 7

    print("Đoán số từ 1 đến 100!")

    for i in range(attempts):
        guess = int(input(f"Lượt {i+1}: "))

        if guess == number:
            print("Đúng rồi!")
            luu_ky_luc(i+1)
            return
        elif guess < number:
            print("Lớn hơn")
        else:
            print("Nhỏ hơn")

        # Gợi ý
        if number % 2 == 0:
            print("Gợi ý: Số chẵn")
        else:
            print("Gợi ý: Số lẻ")

    print("Thua! Số đúng là:", number)

def luu_ky_luc(score):
    try:
        with open("highscore.txt", "r") as f:
            best = int(f.read())
    except:
        best = 999

    if score < best:
        with open("highscore.txt", "w") as f:
            f.write(str(score))
        print("Kỷ lục mới! Số lượt: ", score)

game()