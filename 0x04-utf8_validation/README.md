# UTF-8 Validation Project

Welcome to the **UTF-8 Validation** project! 🎉

## Overview
This project validates UTF-8 encoding, a widely used format for text data that supports every character in the Unicode standard. In this script, we determine if a given dataset correctly represents UTF-8 encoding by checking each byte with bitwise operations. It’s an exciting dive into encoding schemes and Python’s powerful bit manipulation capabilities!

## How It Works
UTF-8 characters can be 1 to 4 bytes long. This program:
- Checks each byte for the correct UTF-8 patterns.
- Ensures multi-byte sequences start with a specific pattern and that each subsequent byte begins with `10`.
- Returns `True` if the dataset is valid UTF-8 encoding, and `False` otherwise.

from utf8_validation import validUTF8

