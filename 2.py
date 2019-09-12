listgpa = [3,2.7,2.5,4]

def gift(gpa):
    bonus = 500000
    gift = bonus*gpa
    return gift
for gpa in listgpa:
    if gpa > 3:
        print("Insentif anda adalah Rp", gift(gpa))
    else:
        print("Maaf, anda tidak dapat bonus")