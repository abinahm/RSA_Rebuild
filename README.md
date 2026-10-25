# RSA_Rebuild

A small Python script that rebuilds an RSA private key from a public modulus by looking up its prime factors on [FactorDB](https://factordb.com), then uses that key to decrypt a ciphertext file. It's meant for CTF challenges and learning how RSA breaks when the modulus is weak.

## How It Works

RSA's security depends on the modulus `n` being impossible to factor. If `n` is small or has already been factored publicly, the private key can be recovered:

1. Convert the modulus (hex) to an integer
2. Query FactorDB for its prime factors `p` and `q`
3. Compute `phi = (p - 1)(q - 1)`
4. Compute the private exponent `d = e⁻¹ mod phi`
5. Decrypt the ciphertext with `m = c^d mod n`
6. Convert the result back to bytes and print the flag

## Requirements

- Python 3.9+
- [pycryptodome](https://pypi.org/project/pycryptodome/)
- [factordb-pycli](https://pypi.org/project/factordb-pycli/)

```bash
pip install pycryptodome factordb-pycli
```

## Usage

1. Clone the repo:

   ```bash
   git clone https://github.com/<your-username>/RSA_Rebuild.git
   cd RSA_Rebuild
   ```

2. Open the script and paste your modulus into the `modulus` variable. Hex is accepted with or without a `0x` prefix, and colon-separated output (as printed by OpenSSL) works too:

   
   a) You can get the modulus by running the commands

   ```bash
   openssl rsa -in private.key -modulus -noout
   ```

   ```bash
   openssl rsa -in private.key -text -noout
   ```

   Output of First Command
   ```python
   modulus = "FA4..."
   ```
   
   Ouput of Second Command
   ```python
   modulus = "00:c3:7a:..."
   publicexponent = 65537
   ```


4. Place the encrypted file in the same folder and name it `msg.enc`.

5. Run the script:

   ```bash
   python rsa_rebuild.py
   ```

### Getting the modulus from a public key

If you have a PEM public key, OpenSSL can print the modulus and exponent:

```bash
openssl rsa -pubin -in public.pem -text -noout
```

## Example Output

```
[+] Modulus converted to decimal
[+] Searching FactorDB...
[+] p = 1234567...
[+] q = 7654321...
[+] Private key calculated

[+] FLAG: flag{example_flag_here}
```

## Limitations

- **FactorDB must already know the factors.** If the modulus isn't fully factored there, the script exits with an error.
- **Exactly two prime factors.** Multi-prime moduli aren't supported.
- **Textbook RSA only.** The script assumes raw RSA with no padding (no OAEP or PKCS#1 v1.5). Padded ciphertexts will not decode to readable text.
- The public exponent defaults to `65537`. Change `publicexponent` if your key uses a different value.

## Disclaimer

This project is for educational use and CTF competitions. Only use it on keys and data you own or are authorized to test.
