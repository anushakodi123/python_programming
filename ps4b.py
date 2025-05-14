# Problem Set 4B
# Name:
# Collaborators:

import random


class Message(object):
    def __init__(self, input_text):
        '''
        Initializes a Message object

        input_text (string): the message's text
        '''
        self.input_text = input_text

    def __repr__(self):
        '''
        Returns a human readable representation of the object
        DO NOT CHANGE
        '''
        return f"Message('{self.get_text()}')"

    def get_text(self):
        '''
        Access the message text outside the class
        '''
        return self.input_text

    def shift_char(self, char, shift):
        '''
        Shifts a character by the given shift amount in the ASCII printable range.
        '''
        ascii_val = ord(char)
        shifted = (ascii_val - 32 + shift) % 95 + 32
        return chr(shifted)

    def apply_pad(self, pad):
        '''
        Encrypts or decrypts the message using a one-time pad.
        '''
        return ''.join(self.shift_char(c, pad[i]) for i, c in enumerate(self.input_text))


class PlaintextMessage(Message):
    def __init__(self, input_text, pad=None):
        '''
        Initializes a PlaintextMessage object.
        '''
        super().__init__(input_text)
        self.pad = pad if pad is not None else self.generate_pad()
        self.ciphertext = self.apply_pad(self.pad)

    def __repr__(self):
        '''
        Returns a human readable representation of the object
        DO NOT CHANGE
        '''
        return f"PlaintextMessage('{self.get_text()}', {self.get_pad()})"

    def generate_pad(self):
        '''
        Generates a one-time pad of random integers for each character.
        '''
        return [random.randint(0, 109) for _ in self.input_text]

    def get_pad(self):
        '''
        Returns a copy of the pad.
        '''
        return self.pad.copy()

    def get_ciphertext(self):
        '''
        Returns the ciphertext of the message.
        '''
        return self.ciphertext

    def change_pad(self, new_pad):
        '''
        Changes the pad and updates the ciphertext.
        '''
        self.pad = new_pad
        self.ciphertext = self.apply_pad(new_pad)

    def get_message_text(self):
        '''
        Returns the original message text. (Needed by ps4c.py)
        '''
        return self.input_text


class EncryptedMessage(Message):
    def __init__(self, input_text):
        '''
        Initializes an EncryptedMessage object
        '''
        super().__init__(input_text)

    def __repr__(self):
        '''
        Returns a human readable representation of the object
        DO NOT CHANGE
        '''
        return f"EncryptedMessage('{self.get_text()}')"

    def decrypt_message(self, pad):
        '''
        Decrypts the message by applying the inverse of the pad.
        '''
        inverse_pad = [-p for p in pad]
        decrypted_text = self.apply_pad(inverse_pad)
        return PlaintextMessage(decrypted_text, pad)

if __name__ == "__main__":
    msg = PlaintextMessage("Hello, World!")
    print("Original:", msg.get_text())
    print("Pad:", msg.get_pad())
    print("Ciphertext:", msg.get_ciphertext())

    encrypted = EncryptedMessage(msg.get_ciphertext())
    decrypted = encrypted.decrypt_message(msg.get_pad())
    print("Decrypted (text):", decrypted.get_message_text())
    print("Decrypted (pad):", decrypted.get_pad())
