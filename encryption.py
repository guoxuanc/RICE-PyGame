import os, struct
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import getpass


def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    """ Encrypts a file using AES (CBC Mode) with given key.

    key:
        The encryption key - a string that must be either 16, 24 or 32 bytes long. Longer the better.

    in_filename:
        Input file

    out_filename:
        if None, '(encrypted)<in_filename>.enc' will be used.

    chunksize:
        Sets the size of the chunk which the function uses to read and encrypt the file. chunksize must be divisible by 16.
    """
    if not out_filename:
        out_filename = "(encrypted)" + in_filename + ".enc"

    iv = Random.new().read(16)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, "rb") as infile:
        with open(out_filename, "wb") as outfile:
            # first records the size of original file size into output file
            outfile.write(struct.pack("<Q", filesize))
            # secondly saves a randomly generated 16-byte IV
            outfile.write(iv)

            while True:
                # read input file chunk by chunk
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break;
                elif len(chunk) % 16 != 0:
                    # pad the file to fit into a multiple of 16
                    chunk += b' ' * (16 - len(chunk) % 16)
                # encrypt file chunk by chunk
                outfile.write(encryptor.encrypt(chunk))


def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
    """ Decrypt a file using AES (CBC Mode) with given key. parameters are similar to encrypt_file, with one difference: out_filename, if not supplied will be in_filename without its last extension and first "(encrypted)" (i.e. if in_filename is "(encrypted)secret.zip.enc" then out_filename will be "secret.zip")
    """
    if not out_filename:
        out_filename = os.path.splitext(in_filename[11:])[0]

    with open(in_filename, "rb") as infile:
        # read first 8 bytes from encrypted file "infile" to obtain original unencrypted file size
        original_size = struct.unpack("<Q", infile.read(struct.calcsize("<Q")))[0]
        # then read iv from infile to correctly initialize the AES object
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, "wb") as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break;
                outfile.write(decryptor.decrypt(chunk))
            # truncate decrypted file to throw out paddings
            outfile.truncate(original_size)


def getKey(password):
    return SHA256.new(password.encode('utf-8')).digest()


def Main():
    choice = input("choose to (E)ncrypt or (D)ecrypt: ")
    if choice.strip() == "E" or choice.strip() == "e":
        filename = input("File to encrypt: ")
        password = getpass.getpass()
        encrypt_file(getKey(password), filename)
        print("file {} has been encrypted as \"(encrypted){}.enc\".".format(filename, filename))
    elif choice.strip() == "D" or choice.strip() == "d":
        filename = input("File to decrypt: ")
        password = getpass.getpass()
        decrypt_file(getKey(password), filename)
        print("file has been decrypted.")

    else:
        print("No option selected, closing...")


if __name__ == '__main__':
    Main()
