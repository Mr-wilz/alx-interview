#!/usr/bin/python3
# A method that determines if a given dataset represents a valid UTF-8 encoding.

def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        mask = 1 << 7  # Reset the mask to check the first bit

        if num_bytes == 0:
            # Determine the number of bytes in this UTF-8 character
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # For 1 byte characters, num_bytes should be 0
            if num_bytes == 0:
                continue

            # UTF-8 can be 1 to 4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # If we are in the middle of a UTF-8 character,
            # the byte should start with 10xxxxxx.
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement num_bytes for each byte in the current character
        num_bytes -= 1

    # If all characters were properly encoded, num_bytes should be 0
    return num_bytes == 0
