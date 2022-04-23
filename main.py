# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import hashlib
import pickle


def check_client_info(params):
    cUsername = params[0]
    cPassword = params[1]

    client_infos = open("client_info.txt", "rb")
    client_database = pickle.load(client_infos)
    print(cUsername)
    print(cPassword)
    print(str(client_database))
    if client_database[cUsername] == cPassword:
        print("yes")
    else:
        print("no")


def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    hash_object = hashlib.md5("123".encode())
    md5_hash = hash_object.hexdigest()

    dict = {"J":md5_hash,
            "g":hashlib.md5("r".encode()).hexdigest()}
    file = open("client_info.txt", "wb")
    pickle.dump(dict, file)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """Username = "J"
    Password = "123"
    hash_object = hashlib.md5(Password.encode())
    md5_hash = hash_object.hexdigest()
    check_client_info([Username, md5_hash])"""
    print_hi()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
