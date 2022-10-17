import time

while True:
    time.sleep(1.0)
    with open("image-services.txt", "r+") as f:
        lines = f.read()
        if lines.isnumeric() == True:
            print("here")
            num = int(lines)
            img = num % 73
            if img == 0:
                img = 1
            f.seek(0)
            f.truncate(0)
            f.write(f"C:/Users/potts/PycharmProjects/CS361/cs361img/{str(img)}.jpg")
            print(f.read())
        f.close()

