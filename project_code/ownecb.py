from Crypto.Cipher import AES
import binascii


key = b'ABCDEFGHIJIKLMOP'

msg = (b'AAAAAAAAAAAAAAAA')

cipher = AES.new(key, AES.MODE_ECB)


msg_en = cipher.encrypt(msg)
print("       ")
print(binascii.hexlify(msg_en))


print("--------")
decipher = AES.new(key, AES.MODE_ECB)

msg_dec = decipher.decrypt(binascii.unhexlify(b"75ce1408b210410124729691da93c439")) 
print(msg_dec)
print(binascii.hexlify(msg_dec))
