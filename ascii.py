from PIL import Image


# Ordered from thinnest to densest
ASCII = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

MAX_PIXEL_VALUE = 255

im = Image.open("fern.png")


def get_matrix(img):
    img.thumbnail((200, 200))
    pixels = list(img.getdata())
    tempArr = []
    for i in range(0, len(pixels), img.width):
        tempArr.append(pixels[i: i + img.width])
    return tempArr

def get_brightness(matrix):
    tempMatrix = []
    for r in matrix:
        tempRow = []
        for p in r:
            brightness = (p[0] + p[1] + p[2]) // 3
            tempRow.append(brightness)
        tempMatrix.append(tempRow)
    return tempMatrix

def convert_to_ascii(brightness):
    res = ""
    for r in brightness:
        rowString = ""
        for c in r:
            rowString += ASCII[c // 5] * 3
        rowString += "\n"

        res += (rowString)
    return res
            

matrix = get_matrix(im)
brightness = get_brightness(matrix)
print(convert_to_ascii(brightness))





    
