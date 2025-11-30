import console_gfx

def to_hex_string(data):
    var = ""
    for val in data:
        if val == 10:
            var += "a"
        elif val == 11:
            var += "b"
        elif val == 12:
            var += "c"
        elif val == 13:
            var += "d"
        elif val == 14:
            var += "e"
        elif val == 15:
            var += "f"
        else:
            var += str(val)
    return var

def count_runs(flat_data):
    if flat_data == []:
        return 0
    runs = 0
    current_value = flat_data[0]
    current_length = 0
    for val in flat_data:
        if val == current_value and current_length < 15:
            current_length += 1 
        else:
            runs += 1
            current_value = val
            current_length = 1
    runs += 1 
    return runs

def encode_rle(flat_data):
    if flat_data == []:
        return []
    rle = []
    current_value = flat_data[0]
    current_length = 0
    for val in flat_data:
        if val == current_value and current_length < 15:
            current_length += 1 
        else:
            rle.append(current_length)
            rle.append(current_value)
            current_value = val
            current_length = 1
    rle.append(current_length)
    rle.append(current_value)
    return rle

def get_decoded_length(rle_data):
    total = 0
    i = 0
    while i < len(rle_data):
        count = rle_data[i]
        total += count
        i += 2
    return total 

def decode_rle(rle_data):
    decoded = []
    i = 0
    while i < len(rle_data):
        count = rle_data[i]
        value = rle_data[i + 1]
        for j in range(count):
            decoded.append(value)
        i += 2
    return decoded

def string_to_data(data_string):
    var = []
    for val in data_string:
        if val == "a":
            var.append(10)
        elif val == "b":
            var.append(11)
        elif val == "c":
            var.append(12)
        elif val == "d":
            var.append(13)
        elif val == "e":
            var.append(14)
        elif val == "f":
            var.append(15)
        else:
            var.append(int(val))
    return var

def to_rle_string(rle_data):
    if rle_data == []:
        return ""
    var = ""
    i = 0
    while i < len(rle_data):
        count = rle_data[i]
        value = rle_data[i + 1]
        if value == 10:
            value_hex = "a"
        elif value == 11:
            value_hex = "b"
        elif value == 12:
            value_hex = "c"
        elif value == 13:
            value_hex = "d"
        elif value == 14:
            value_hex = "e"
        elif value == 15:
            value_hex = "f"
        else:
            value_hex = str(value)
        var += str(count) + value_hex
        if i < len(rle_data) - 2:
            var += ":"
        i += 2
    return var

def string_to_rle(rle_string):
    if rle_string == "":
        return []
    var = []
    hex_value = ""
    for char in rle_string:
        if char == ":":
            count = int(hex_value[:-1])
            last_char = hex_value[-1].lower()
            if last_char == "a":
                value = 10
            elif last_char == "b":
                value = 11
            elif last_char == "c":
                value = 12
            elif last_char == "d":
                value = 13
            elif last_char == "e":
                value = 14
            elif last_char == "f":
                value = 15
            else:
                value = int(last_char)

            var.append(count)
            var.append(value)
            hex_value = ""
        else:
            hex_value += char
    if hex_value != "":
        count = int(hex_value[:-1])
        last_char = hex_value[-1].lower()
        if last_char == "a":
            value = 10
        elif last_char == "b":
            value = 11
        elif last_char == "c":
            value = 12
        elif last_char == "d":
            value = 13
        elif last_char == "e":
            value = 14
        elif last_char == "f":
            value = 15
        else:
            value = int(last_char)
        var.append(count)
        var.append(value)
    return var

def display_menu():
    print("\nRLE Menu\n"
    "--------")
    print('''0. Exit
1. Load File
2. Load Test Image
3. Read RLE String
4. Read RLE Hex String
5. Read Data Hex String
6. Display Image
7. Display RLE String
8. Display Hex RLE Data
9. Display Hex Flat Data
''')

def main():
    print("Welcome to the RLE image encoder!")
    print()
    print("Displaying Spectrum Image:")
    console_gfx.display_image(console_gfx.test_rainbow)
    image_data = None
    width = None
    height = None
    pixels = None
    while True:
        display_menu()
        option = int(input("Select a Menu Option: "))
        if option == 0:
            break
        elif option == 1:
            file_name = input("Enter name of the file to load: ")
            image_data = console_gfx.load_file(file_name)
            width = image_data[0]
            height = image_data[1]
            pixels = image_data[2:]
        elif option == 2:
            image_data = console_gfx.test_image
            print("Test image data loaded.")
            width = image_data[0]
            height = image_data[1]
            pixels = image_data[2:]
        elif option == 3:
            rle_str = input("Enter an RLE string to be decoded: ")
            rle = string_to_rle(rle_str)
            image_data = decode_rle(rle)
            if len(image_data) >= 2:
                width = image_data[0]
                height = image_data[1]
                pixels = image_data[2:]
            else:
                width = None
                height = None
                pixels = None
        elif option == 4:
            hex_str = input("Enter the hex string holding RLE data: ")
            rle = string_to_data(hex_str)
            image_data = decode_rle(rle)
            if len(image_data) >= 2:
                width = image_data[0]
                height = image_data[1]
                pixels = image_data[2:]
            else:
                width = None
                height = None
                pixels = None
        elif option == 5:
            hex_str = input("Enter the hex string holding flat data: ")
            image_data = string_to_data(hex_str)
            if len(image_data) >= 2:
                width = image_data[0]
                height = image_data[1]
                pixels = image_data[2:]
            else:
                width = None
                height = None
                pixels = None
        elif option == 6:
            print("Displaying image...")
            if width is None or height is None or pixels is None:
                print("(no data)")
            else:
                console_gfx.display_image([width, height] + pixels)
        elif option == 7:
            print("RLE representation:", end=" ")
            if image_data is None:
                print("(no data)")
            else:
                rle = encode_rle(image_data)
                print()
                print(to_rle_string(rle))
        elif option == 8:
            print("RLE hex values:", end=" ")
            if image_data is None:
                print("(no data)")
            else:
                rle = encode_rle(image_data)
                print()
                print(to_hex_string(rle))
        elif option == 9:
            print("Flat hex values:", end=" ")
            if width is None or height is None or pixels is None:
                print("(no data)")
            else:
                print()
                print(to_hex_string([width, height] + pixels))
        else:
            print("Error! Invalid input.")
if __name__ == "__main__":
    main()
