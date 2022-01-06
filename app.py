# try:
#     file = open("a_file.txt")
#     a_dict = {'key':'value'}
#     print(a_dict['key'])
#
# except FileNotFoundError:
#     file = open("a_file.txt","w")
#
# except KeyError:
#     print("Key does not exist")
#
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     raise KeyError

dict = {
    "Kohli": {
        "email": "ashwin@gmail.com",
        "password": "MMU(W4gpq5*b"
    },
    "Amazon": {
        "email": "ashwin@gmail.com",
        "password": "12AVt!%a(Uk2uK"
    }
}
print(dict['Kohli']['password'])