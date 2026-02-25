def cipher(str1, shift):
    result = ""
    for i in str1:
        if i.isalpha():
            if i.isupper():
                result += chr((ord(i) - ord("A") + shift) % 26 + ord("A"))
            else:
                result += chr((ord(i) - ord("a") + shift) % 26 + ord("a"))
        else:
            result += i
    return result


str1 = input("Your message: ").strip()
shift = int(input("Enter the shift number: ").strip())

answer = cipher(str1, shift)
print(f'Your Caesar cipher of "{str1}" is "{answer}"')