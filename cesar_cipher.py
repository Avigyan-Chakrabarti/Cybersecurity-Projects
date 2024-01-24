import streamlit as st

def encrypt(text,s):
	result = ""
	# traverse text
	for i in range(len(text)):
		char = text[i]
		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr((ord(char) + s - 65) % 26 + 65)
		# Encrypt lowercase characters
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)
	return result

def decrypt(text,s):
	result = ""
	# traverse text
	for i in range(len(text)):
		char = text[i]
		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr((ord(char) - s - 65) % 26 + 65)
		# Encrypt lowercase characters
		else:
			result += chr((ord(char) - s - 97) % 26 + 97)
	return result

def main():
    st.title("Caesar Cipher with Streamlit")

    # User input for text and shift
    text = st.text_area("Enter the text:")
    s = st.slider("Select the shift value:", min_value=1, max_value=25, value=3)

    # Encrypt button
    if st.button("Encrypt"):
        encrypted_text = encrypt(text, s)
        st.success(f"Encrypted Text: {encrypted_text}")

    # Decrypt button
    if st.button("Decrypt"):
        decrypted_text = decrypt(text, s)
        st.success(f"Decrypted Text: {decrypted_text}")
if __name__ == "__main__":
    main()