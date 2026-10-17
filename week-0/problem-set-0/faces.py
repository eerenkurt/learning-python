def convert(text):
    return text.replace(":)","🙂").replace(":(","🙁")



def main():
    user_input = input("write here: ")
    print(convert(user_input))

main()