def encode(text):
    encoded = ""
    pointer = 0
    
    previous_character = text[0]
    incrementator = 1

    while pointer < len(text):
        if (text[pointer] == previous_character):
            incrementator += 1
        else:
            if (incrementator == 1):
                encoded += previous_character
                continue

            # Add the values to the encoded string
            encoded += previous_character
            encoded += str(incrementator)

            # Reset back the two variables
            previous_character = text[pointer]
            incrementator = 1

        pointer += 1

    return encoded

def decode(text):
    decoded = ""
    pointer = 0

    previous_character = text[0]
    
    while pointer < len(text):
        if (text[pointer] in "0123456789"):
            number_of_times = int(text[pointer])
            for _ in number_of_times:
                decoded += previous_character

        else:
            previous_character = text[pointer]

        pointer += 1

    return decoded