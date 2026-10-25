from Crypto.Util.number import inverse, long_to_bytes
from factordb.factordb import FactorDB
from math import prod

modulus = ""
publicexponent = 65537

n = int(modulus.strip().replace(":", "").removeprefix("0x"), 16)

print("[+] Modulus converted to decimal")
print("[+] Searching FactorDB...")

f = FactorDB(n)
f.connect()

factors = f.get_factor_list()

if not factors or prod(factors) != n:
    raise ValueError("FactorDB does not have a complete factorization.")

if len(factors) != 2:
    raise ValueError("This script expects exactly two prime factors.")

p, q = factors

print(f"[+] p = {p}")
print(f"[+] q = {q}")

phi = (p - 1) * (q - 1)
d = inverse(publicexponent, phi)

print("[+] Private key calculated")

with open("msg.enc", "rb") as file:
    ciphertext = file.read()

c = int.from_bytes(ciphertext, byteorder="big")

message = pow(c, d, n)

print("\n[+] FLAG:", long_to_bytes(message).decode(errors="ignore"))
