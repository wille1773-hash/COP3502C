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
         
