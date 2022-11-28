#Nama  = Suci Awalia Ramadani
#NIM   = D0221086

# Menghitung Luas Persegi
print("LUAS PERSEGI")
print("Rumus = sisi * sisi")
sisi1=int(input(" sisi 1= "))
sisi2=int(input(" sisi 2= "))

def luasPersegi():
  l=sisi1*sisi2
  print("Luas Persegi=",l)

luasPersegi()

#Menghitung Luas Lingkaran
print("LUAS LINGKARAN")
phi=float(input("phi ="))
jariJari1=int(input("jari-jari 1="))
jariJari2=int(input("jari-jari 2="))

def luasLingkaran():
  L=phi*jariJari1*jariJari2
  print("luas lingkaran=",L)

luasLingkaran()

#Menghitung Luas Segitiga
print("LUAS SEGITIGA")

alas=int(input("/nMasukkan Alas :"))
tinggi=int(input("/nMasukkan Tinggi :"))

def luasSegitiga():
  luas=1/2*alas*tinggi
  print("luas segitiga=",luas)

luasSegitiga()
