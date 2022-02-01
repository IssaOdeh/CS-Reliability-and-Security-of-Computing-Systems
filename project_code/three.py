import rsa


publicKey, privateKey = rsa.newkeys(512)

# this is the string that we will be encrypting
message = "This is the message"


encMessage = rsa.encrypt(message.encode(),
						publicKey)

print("original string: ", message)
print("encrypted string: ", encMessage)


decMessage = rsa.decrypt(encMessage, privateKey).decode()

print("decrypted string: ", decMessage)
