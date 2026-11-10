# Atbash Cipher

A Python implementation of the classic Atbash Cipher demonstrating character mapping (ASCII), cryptographic self-inversion, and optimized string translation.

## How It Works
The Atbash Cipher is a symmetric substitution cipher that works by reversing the alphabet. The first letter maps to the last letter (`A` ↔ `Z`), the second maps to the second-to-last (`B` ↔ `Y`), and so on. 

Because the algorithm is self-inverting, passing the ciphertext back through the function automatically decrypts it into the original plaintext.

## Usage
Save the code to a file named `atbash.py` and run it from your terminal:

run using

```
python atbash.py
```
