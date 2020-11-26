import binascii

print "Please Enter The String You Would Like To Encrypt In Base 64"
userinput = raw_input(">>>")
holder = 0

ascii = []

for things in userinput:
  ascii.append(ord(userinput[holder]))
  holder += 1


print "Values In ASCii:"
print ascii
print "---"

binhold = ""
count = 0
binhold = []


for things in ascii:
  h = (str(bin(ascii[count])))
  h = h[2:8]
  h = h.zfill(8)
  binhold.append(h)  
  count += 1
print "Values in 8-bit binary"
print binhold
print "---"

string_binhold = ""
for things in binhold:
  string_binhold += things

print string_binhold
print "---"

sixcheck = True
while sixcheck == True:
  length = len(string_binhold)
  if length % 6 == 0:
    print len(string_binhold)
    sixcheck = False
  else:
    string_binhold = string_binhold + "0"
    print "The string is too short..."


six_bits = []

front = 0 
back = 6
done = False

while done == False:
    six_bits.append(string_binhold[front:back])
    if back == len(string_binhold):
        done = True
    
    else:
        front+= 6
        back += 6
print "String in 6-bit binary"
print six_bits
print "---"

counter = 0
hold = ""
final = []


for things in six_bits:
    hold = int(six_bits[counter],2)
    final.append(hold)
    counter += 1
print "Base64 Numbers"
print final
print "---"

base64 =["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "/"]


counter = 0
hold = ""
final64 = ""





for things in six_bits:
    final64 += base64[final[counter]]
    counter += 1

print "-----------------------------------------------------------------------------------"
print "The Final Base64 String is:"
print final64
print "-----------------------------------------------------------------------------------"
