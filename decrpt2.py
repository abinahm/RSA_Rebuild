from Crypto.Util.number import inverse, long_to_bytes


modulus = 
publicexponent =
factor1 = 
factor2 =

phi = (factor1 - 1) * (factor2 - 1)
d = inverse(publicexponent, phi)

with open("msg.enc", "rb") as f:
    ciphertext = f.read()

c = int.from_bytes(ciphertext, byteorder="big")
message = pow(c, d, modulus)


print("Flag:", long_to_bytes(message).decode(errors="ignore"))
