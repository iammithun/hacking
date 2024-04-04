import hashlib


def convert_text_to_sha1(text):
    digest=hashlib.sha1(
        text.encode()
    ).hexdigest()

    return digest




def main():
    
    user_sha1=input("Enter the SHA1 to Crack:")
    cleaned_user_sha1=user_sha1.strip().lower()
    
    with open('10-million-password-list-top-100.txt') as f:
        for line in f:
            pasword=line.strip()
            converted_sha1=convert_text_to_sha1(password)

            if cleaned_user_sha1 == cleaned_user_sha1:
                print(f"Password found:{pasword}")
                return
    print("Could not find password")
    
    
    
if __name__ == '__main__':
    main()