from PIL import Image # библиотека pillow

with Image.open("C:/Users/sasha/Downloads/Main/2.jpg") as img: # свой путь
    img.load()

pixels = list(img.getdata()) # получение данных с картинки

result = []
array = []
count = 0
maxCount = 99 # количество пикселей по горизонтали
for pix in pixels: # сопоставление разных значений с различными символами и запись в массив
    r, g, b = pix
    if (count < maxCount):
        value = int((r + g + b) / 10)
        match int(value / 10):
            case 0: array.append("##")
            case 1: array.append("$$")
            case 2: array.append("++")
            case 3: array.append("&&")
            case 4: array.append("::")
            case 5: array.append("--")
            case 6: array.append("..")
            case 7: array.append("  ")
            case _:array.append(value)
        count += 1
    else:
        result.append(array)
        array = []
        count = 0

file = open("C:/Users/sasha/Downloads/Main/file.txt", "w") # указать свой путь
for elem in result:
    for number in elem:
        file.write(str(number))
    file.write("\n")
file.close()
