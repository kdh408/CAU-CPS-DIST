
p = 11
q = 13
n = p*q
phi_n = (p-1)*(q-1)

#e를 찾는 과정은 다음주 심화 과정
e = 7

#d 찾기
d = 0
mod = 0
while True:
    d += 1
    mod = (e*d) % phi_n
    if mod == 1:
        break

#encryption
# C = p^e mod n
P = "CAU CPS DIST" # plaintext
P_list = [ord(x) for x in P] #plaintext를 숫자로 바꿈 / ord: 문자 -> 숫자

# for x in p:
#    P_list.append(ord(x)) 와 같다

cipher = []
for i in P_list:
    x = (i ** e) % n # **: 제곱 의미
    cipher.append(int(x))


#decryption
# P = C^d mod n
decryted = []
for i in cipher:
    x = (i ** d) % n
    decryted.append(int(x))

print('plain text ', P_list)
print('cipher text ', cipher)
print('decryted text ', decryted)

decryted_text = ''.join([chr(x) for x in decryted]) # chr: 숫자 -> 문자/ join: 개개의 문자를 하나의 문자열 만들어 줌
print(decryted_text)
