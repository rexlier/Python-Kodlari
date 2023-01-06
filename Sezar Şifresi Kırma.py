print("Sezar Şifresi Kırma Programına Hoşgeldiniz.")
sifresiz=input(""T3 Akademi; Türkiye Teknoloji Takımı Vakfı tarafından hayata geçirilen Teknofest, Deneyap, Bilim Türkiye, Deneyapkart, Keşif Kampüsü, Girişim Merkezi, T3 Podcast içeriklerinin yayınlandığı bir çevrimiçi öğrenme sistemidir. T3 Akademi’de ayrıca bilgi teknolojileri ve yazılım, dijital içerik ve medya kişisel gelişim, girişimcilik, eğitim bilimleri, dil öğrenimi, sosyal bilimler gibi birçok farklı kategoride eğitim içeriği de yer almaktadır."

:")
def sifrele(metin):
    sifrelimetin=""
    for harf in metin:
        asciikod=ord(harf)
        asciikod=asciikod-3
        karakterkod=chr(asciikod)
        sifrelimetin=sifrelimetin+karakterkod
    print("Şifresiz:",metin,"Şifreli:",sifrelimetin)

sifrele(sifresiz)
