import time
print("--------------------------------------------------")
#Welcome the user
print("Selamat Datang ke Permaianan Uji Minda Sejarah!")
time.sleep(1)
print("--------------------------------------------------")

#Chances
chances=1
print("Anda dikehendaki membuat pilihan jawapan", chances,"untuk jawapan yang betul.\nAnda akan mendapat satu markah .\n")
time.sleep(2)

#score
score=0

#question 1
print("==================================================")
question_1=print("1) SIAPAKAH PENGASAS KESULTANAN MELAYU MELAKA?\n(A) Parameswara\n(B) Hang Tuah\n(C) Hang Jebat\n(D) Tun Perak\n\n")
answer_1= "a"

for i in range(chances):
    answer = input("JAWAPAN: ")
    if (answer.lower() == answer_1):
        print("TAHNIAH! !\n")
        score = score + 1
        break
    else:
        print("SALAH!\n")
        time.sleep(0.5)
        print("JAWAPAN YANG BETUL IALAH", answer_1, "\n\n")

time.sleep(2)

#question 2
print("==================================================")
question_2 = print("2)PADA TAHUN BILAKAN TANAH MELAYU MENCAPAI KEMERDEKAAN?\n(A) 1945\n(B) 1963\n(C) 1957\n(D) 1970\n\n")  
answer_2 = "c"

for i in range(chances):
    answer = input("JAWAPAN: ")
    if (answer.lower() == answer_2):
        print("TAHNIAH!\n")
        score = score + 1
        break
    else:
        print("SALAH!\n ")
        time.sleep(0.5)
        print("JAWAPAN YANG TEPAT IALAH", answer_2, "\n\n")

time.sleep(2)

#question 3
print("==================================================")
question_3 =print("3) SIAPAKAH PERDANA MENTERI MALAYSIA YANG PERTAMA?\n(A) Tun Abdul Razak\n(B) Tun Huessein Onn\n(C) Tun Dr Mahathir\n(D) Tunku Abdul Rahman\n\n")
answer_3= "d"

for i in range(chances):
    answer = input("Jawapan: ")
    if (answer.lower() == answer_3):
        print("TAHNIAH!\n")
        score = score + 1
        break
    else:
        print("TIDAK TEPAT!\n")
        time.sleep(0.5)
        print("JAWAPAN YANG TEPAT IALAH", answer_3, "\n\n")

time.sleep(2)

#question 4
print("==================================================")
question_4 =print("4)  DIMANAKAH TERLETAKNYA KOTA A FAMOSA ?\n(A) Melaka\n(B) Perak\n(C) Kedah\n(D) Pulau Pinang\n\n")
answer_4= "a"

for i in range(chances):
    answer = input("JAWAPAN: ")
    if (answer.lower() == answer_4):
        print("TAHNIAH!\n")
        score = score + 1
        break
    else:
        print("TIDAK TEPAT!\n")
        time.sleep(0.5)
        print("JAWAPAN YANG TEPAT IALAH ",answer_4, "\n\n")

time.sleep(2)

#question 5
print("==================================================")
question_5 =print("5)  APAKAH NAMA PENJAJAH YANG PERTAMA TIBA DI TANAH MELAYU?\n(A) Belanda\n(B) Portugis\n(C) British\n(D) Jepun\n\n")
answer_5= "b"

for i in range(chances):
    answer = input("Jawapan: ")
    if (answer.lower() == answer_5):
        print("TAHNIAH!\n")
        score = score + 1
        break
    else:
        print("TIDAK TEPAT!\n")
        time.sleep(0.5)
        print("JAWAPAN YANG TEPAT IALAH", answer_5, "\n\n")

time.sleep(2)

#print the score
print("==================================================")
while score >=2:
    print("TAHNIAH! JUMLAH MARKAH ANDA IALAH", score)
    break

while score <2:
    print("CUBA LAGI DI LAIN MASA! JUMLAH MARKAH ANDA IALAH",score)
    break

#Goobye message
print("TERIMA KASIH KERANA MENCUBA PERMAINAN UJI MINDA SEJARAH!")
