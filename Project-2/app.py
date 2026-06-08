import streamlit as st

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

st.title("Basic Encryption & Decryption Tool")

text = st.text_input("Enter your text")
shift = st.number_input("Enter shift key", min_value=1, max_value=25, value=3)

if st.button("Encrypt"):
    encrypted = caesar_encrypt(text, shift)
    st.success(f"Encrypted Text: {encrypted}")
    st.info(f"Decrypted Text: {caesar_decrypt(encrypted, shift)}")
