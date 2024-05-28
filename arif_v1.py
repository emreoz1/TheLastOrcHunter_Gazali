import time
import random
class dusmanlar:
    def __init__(self,dusmanguc,dusmancan,dusmanceviklik,dusmandayaniklilik):
        self.dusmanguc = dusmanguc
        self.dusmancan = dusmancan
        self.dusmanceviklik = dusmanceviklik
        self.dusmandayaniklilik = dusmandayaniklilik

    def degistir(self, dusmanguc, dusmancan, dusmanceviklik, dusmandayaniklilik):
        self.dusmanguc = dusmanguc
        self.dusmancan = dusmancan
        self.dusmanceviklik = dusmanceviklik
        self.dusmandayaniklilik = dusmandayaniklilik

class oyun(dusmanlar):

    def __init__(self):
        self.pot = 0
        self.icsayac2 = 0
        self.icsayac1 = 0
        self.icsayac = 0
        self.han_metin = 0
        self.metin_sayaci = 0  
        self.hijyen_sayaci = 0
        self.bolum_sayaci = 0
        self.can = 100
        self.para = 100
        self.hijyen = 100
        self.tokluk = 100
        self.eglence = 100
        self.uykusuzluk = 0
        self.tecrube_puani = 0
        self.güc = 30
        self.ceviklik = 30
        self.dayaniklilik = 30
        self.mana = 100
        self.toplayicilik = 30
        self.tecrube_sayaci = 1
        self.dusmanlar = dusmanlar(0,0,0,0)
        self.oyuna_giris(self.can,self.para,self.hijyen,self.tokluk,self.eglence,self.uykusuzluk,self.güc,self.ceviklik,self.dayaniklilik,self.mana,self.toplayicilik,self.tecrube_puani,self.dusmanlar)
    

        
    # def degerler(self):
        # self.metin_sayaci = 0  
        # self.hijyen_sayaci = 0
        # self.bolum_sayaci = 0
        # self.can = 100
        # self.para = 100
        # self.hijyen = 100
        # self.tokluk = 100
        # self.eglence = 100
        # self.uykusuzluk = 0
        # self.tecrube_puani = 0
        # self.güc = 5
        # self.ceiklik = 5
        # self.dayaniklilik = 5
        # self.mana = 100
        # self.toplayicilik = 5        



    
    def sonuclar(self,uykusuzluk,hijyen,tokluk,eglence,can,para):
        self.uykusuzluk = uykusuzluk
        self.hijyen = hijyen
        self.tokluk = tokluk
        self.eglence = eglence
        self.can = can
        self.para = para

        if self.uykusuzluk >= 100:
            print("Uykusuzluktan dolayı yolortasında bayıldınız ve bir ork tarafından yenildiniz. Tekrar oturum açmak için lütfen oyunu başlatın.")
            exit()
        if self.hijyen <= 0:
            print("Çok kötü kokuyorsunuz ve insanlar sizden uzak duruyor. Lütfen nehire gidip temizlenin.")
        if self.tokluk <= 0:
            print("Açlıktan öldünüz. Tekrar oturum açmak için lütfen oyunu başlatın.")
            exit()
        if self.eglence <= 0:
            print("Eğlence seviyeniz çok düşük ve sıkıldınız. Lütfen gidip biraz eğlenin.")
        if self.para <=0:
            print("Paranız bittiği için bir şey alamıyorsunuz. Lütfen bir iş yaparak para kazanın.")
        if self.can <= 0:
            print("Canınız bittiği için öldünüz. Tekrar oturum açmak için lütfen oyunu başlatın.")
            exit()
        

    def icsayaci_artir(self,icsayac):
        self.icsayac = self.icsayac + 1
    
    def icsayaci_artir1(self,icsayac1):
        self.icsayac1 = self.icsayac1 + 1

    def icsayaci_artir2(self,icsayac2):
        self.icsayac2 = self.icsayac2 + 1

    def bolumsayaci_artir(self,bolum_sayaci):
        self.bolum_sayaci = self.bolum_sayaci + 1

    def han_metin_artir(self,han_metin):
        self.han_metin = self.han_metin + 1
    
    def hijyen_sayaci_artir(self,hijyen_sayaci):
        self.hijyen_sayaci = self.hijyen_sayaci + 1

    def guc_arttir(self,güc,sayi):
        # self.degerler()
        self.güc = güc + sayi    
        print("güc= ",self.güc)

    def ceviklik_arttir(self,ceviklik,sayi):
        # self.degerler()
        self.ceviklik = ceviklik + sayi
        print("ceviklik= ",self.ceviklik)

    def dayaniklilik_arttir(self,dayaniklilik,sayi):
        # self.degerler()
        self.dayaniklilik = dayaniklilik + sayi
        print("dayaniklilik= ",self.dayaniklilik)

    def mana_arttir(self,mana,sayi):
        # self.degerler()
        self.mana = mana + sayi
        if self.mana >= 100:
            self.mana = 100
        print("mana= ",self.mana)
            
    def mana_azalt(self,mana,sayi):
        # self.degerler()
        self.mana = mana - sayi
        print("mana= ",self.mana)

    def toplayicilik_arttir(self,toplayicilik,sayi):
        # self.degerler()
        self.toplayicilik = toplayicilik + sayi
        print("toplayicilik= ",self.toplayicilik)
    def tecrube_arttir(self,tecrube_puani,tecrube_sayaci,sayi):
        # self.degerler()
        self.tecrube_sayaci = tecrube_sayaci
        self.tecrube_puani = tecrube_puani + sayi
        if tecrube_puani >= 100:
            self.tecrube_puani = self.tecrube_puani - 100
            self.tecrube_sayaci = tecrube_sayaci + 3
            print(f"tebrikler seviye atladınız. {self.tecrube_sayaci} tane seviye puanınız bulunmaktadır.")
        print("tecrube= ",self.tecrube_sayaci)


    def tecrube_azalt(self,tecrube_sayaci,sayi):
        # self.degerler()
        self.tecrube_sayaci = tecrube_sayaci - sayi
        print("tecrube= ",self.tecrube_sayaci)
    def hijyen_arttir(self):
        # self.degerler()
        self.hijyen = 100
        print("hijyen= ",self.hijyen)

    def hijyen_azalt(self,hijyen,sayi):
        # self.degerler()
        self.hijyen = hijyen - sayi
        if self.hijyen <= 0:
            self.hijyen = 0
        print("hijyen= ",self.hijyen)

    def tokluk_arttir(self,tokluk,sayi):
        # self.degerler()
        self.tokluk = tokluk + sayi
        if self.tokluk >= 100:
            self.tokluk = 100
        print("tokluk= ",self.tokluk)

    def tokluk_azalt(self,tokluk,sayi):
        # self.degerler()
        self.tokluk = tokluk - sayi
        if self.tokluk <= 0:
            self.tokluk = 0
            self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
        print("tokluk= ",self.tokluk)
    def eglence_arttir(self,eglence,sayi):
        # self.degerler()
        self.eglence = eglence + sayi
        if self.eglence >= 100:
            self.eglence = 100
        print("eglence= ",self.eglence)

    def eglence_azalt(self,eglence,sayi):
        # self.degerler()
        self.eglence = eglence - sayi
        if self.eglence <= 0:
            self.eglence = 0
            self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
        print("eglence= ",self.eglence)

    def uykusuzluk_arttir(self,uykusuzluk,sayi):
        # self.degerler()
        self.uykusuzluk = uykusuzluk + sayi
        if self.uykusuzluk >= 100:
            self.uykusuzluk = 100   
            self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
        print("uykusuzluk= ",self.uykusuzluk)

    def uykusuzluk_azalt(self,uykusuzluk):
        # self.degerler()
        self.uykusuzluk = uykusuzluk 
        self.uykusuzluk = 0
        print("uykusuzluk= ",self.uykusuzluk)

    def para_ekle(self,para,sayi):
        # self.degerler()
        self.para = para + sayi
        print("para= ",self.para)

    def para_azalt(self,para,sayi):
        # self.degerler()
        self.para = para - sayi
        if self.para <= 0:
            self.para = 0
        print("para= ",self.para)

    def can_ekle(self,can,sayi):
        # self.degerler()
        self.can = can + sayi
        if self.can >= 100:
            self.can = 100
        print("can= ",self.can)
        
    def can_azalt(self,can,sayi):  
        # self.degerler()
        self.can = can - sayi
        if self.can <= 0:
            self.can = 0
            self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
        print("can= ",self.can)

    # def dusmanlar(self,dcan,dguc,dceviklik,ddayaniklilik):
    #     # self.degerler()
    #     self.dcan = dcan
    #     self.dguc = dguc
    #     self.dceviklik = dceviklik
    #     self.ddayaniklilik = ddayaniklilik


    def kamp_alani(self,ad,eglence,hijyen,tokluk,uykusuzluk,tecrube_sayaci):
        self.eglence = eglence
        self.hijyen = hijyen
        self.tokluk = tokluk
        self.uykusuzluk = uykusuzluk
        self.tecrube_sayaci = tecrube_sayaci
        #self.degerler()
        metin = "Kamp alanına giriş yaptınız."
        metin1 = f"""
        Ateşin başında bir yaşlı adam oturuyordu.{ad} merhaba dedi.
        Köylü: "Merhaba" 
        {ad}: Ben {ad} bu arada sizin adınız nedir?"
        Walt: Benim adım Walt
        {ad}: Neden buradasınız?
        Walt: Ben burada yaşamımı sürdürüyorum
        Uzun bir sohbete daldılar. Sohbetin ardından {ad} ayağa kalktı.\n
        """
        metin2 = f"""
        Ateşin başında bir gurup insan oturup şarkı söylüyorlardı ve {ad} onlara katıldı. Fazıl Say'ın Akılla Bir Konuşmam Oldu şarkısını söylüyorlardı.
        Bu zorbalar ne biçim adamlar dedim; 
        Kurt, köpek, çakal makal dedi;
        Ne , dersin bu adamlara dedim;
        Yüreksizler, kafasızlar, sosyuzlar dedi;
        ....

        {ad}: Bu şarkıyı dinlemeyeli uzun olmuştu 
        {ad} ayağa kalktı. \n
        """
        metin3 = f"""
        Ateşin başında bir grup insan hararetli bir şekilde konuşuyordu. {ad} yanlarına yaklaştı ve ne konuştuklarını 
        dinlemeye başladı. Adamlar geçen olan ork baskınından bahsediyordu.
        {ad}: Ben de oradaydım
        Herkes şaşkın bir şekilde {ad}'a baktı ve biri sordu
        Köylü: Nasıl yaşamayı becerdin?
        {ad}: Silahımı çıkardım ve onlarla savaştım. Birkaçını öldürmeyi başardım sonra diğerleri zaten kaçtı
        Ne de olsa kimse benim yalan sölediğimi anlayamaz diye içinden geçirdi {ad}. Herkes {ad}'a şaşırmış bir şeklide bakıyordu.
        ve {ad} bir süre daha onlarla sohbet etti. Daha sonra saatin ilerlediğini fark ederek ayağa kalktı.\n
        """
        self.random_metin = random.randint(1,3)
        self.oyun_yazi(metin)

        metin_nehir = f"""
        Alaros nehir kenarına gelen {ad} nehrin serin sularına girdi ve kendini suyun içerisinde biraz dinlendirdikten sonra
        nehirden çıkıp üstünü giyindi. \n
        """
        metin_yatak = f"""
        {ad} Will'in önceden gösterdiği çadıra giderek yatağına uzandı ve yeni maceralarını düşünerek uykuya daldı.\n
        """
        hata1="Geçersiz seçim \n"
        print("""
        1. Kamp ateşinin başında sohbet et.
        2. Nehirde yıkan.
        3. Çadırına girip uyu.
        4. Kale meydanına dön.
        """)
        secim = input("Seçim yapınız: ")

        if secim == "1":

            if (self.random_metin == 1) and (self.metin_sayaci == 0 or self.metin_sayaci == 2 or self.metin_sayaci == 3):
                self.oyun_yazi(metin1, delay=0.02)
                self.metin_sayaci = 1   
                self.eglence_arttir(self.eglence,20)
                self.tecrube_arttir(self.tecrube_puani,self.tecrube_sayaci,10)
                self.hijyen_azalt(self.hijyen,10)
                self.tokluk_azalt(self.tokluk,10)
                self.uykusuzluk_arttir(self.uykusuzluk,10)
                self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
                self.kamp_alani(self.ad,self.eglence,self.hijyen,self.tokluk,self.uykusuzluk,self.tecrube_sayaci)
            elif (self.random_metin == 2) and (self.metin_sayaci == 0 or self.metin_sayaci == 1 or self.metin_sayaci == 3):
                self.oyun_yazi(metin2, delay=0.02)
                self.metin_sayaci = 2
                self.eglence_arttir(self.eglence,50)
                self.tecrube_arttir(self.tecrube_puani,self.tecrube_sayaci,10)
                self.hijyen_azalt(self.hijyen,10)
                self.tokluk_azalt(self.tokluk,10)
                self.uykusuzluk_arttir(self.uykusuzluk,10)
                self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
                self.kamp_alani(self.ad,self.eglence,self.hijyen,self.tokluk,self.uykusuzluk,self.tecrube_sayaci)
            elif (self.random_metin == 3) and (self.metin_sayaci == 0 or self.metin_sayaci == 1 or self.metin_sayaci == 2):
                self.oyun_yazi(metin3, delay=0.02)
                self.metin_sayaci = 3
                self.eglence_arttir(self.eglence,20)
                self.tecrube_arttir(self.tecrube_puani,self.tecrube_sayaci,10)
                self.hijyen_azalt(self.hijyen,10)
                self.tokluk_azalt(self.tokluk,10)
                self.uykusuzluk_azalt(self.uykusuzluk)
                self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
                self.kamp_alani(self.ad,self.eglence,self.hijyen,self.tokluk,self.uykusuzluk,self.tecrube_sayaci)
            else:   
                self.oyun_yazi(hata1)
                self.kamp_alani(self.ad,self.eglence,self.hijyen,self.tokluk,self.uykusuzluk,self.tecrube_sayaci)

        elif secim == "2":
            self.oyun_yazi(metin_nehir)
            self.hijyen_arttir()
            self.eglence_azalt(self.eglence,10)
            self.tokluk_azalt(self.tokluk,10)
            self.uykusuzluk_arttir(self.uykusuzluk,10)
            self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
            self.kamp_alani(self.ad,self.eglence,self.hijyen,self.tokluk,self.uykusuzluk,self.tecrube_sayaci)
            
        elif secim == "3":
            self.oyun_yazi(metin_yatak)
            self.uykusuzluk_azalt(self.uykusuzluk)
            self.eglence_azalt(self.eglence,10)
            self.tokluk_azalt(self.tokluk,10) 
            self.hijyen_azalt(self.hijyen,10)
            self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
            self.kamp_alani(self.ad,self.eglence,self.hijyen,self.tokluk,self.uykusuzluk,self.tecrube_sayaci)
        elif secim == "4":
            don1 = "Kale meydanına dönüyorsunuz."  
            self.oyun_yazi(don1)
            self.oyun_menu(self.tecrube_puani,self.güc,self.ceviklik,self.dayaniklilik,self.toplayicilik,self.eglence,self.hijyen,self.tokluk,self.uykusuzluk,self.can,self.para,self.mana,self.tecrube_sayaci,self.dusmanlar,self.pot)
        else:
            self.oyun_yazi(hata1)
            self.kamp_alani(self.ad,self.eglence,self.hijyen,self.tokluk,self.uykusuzluk,self.tecrube_sayaci)

    def sifahane(self,can,mana,para,pot):
        self.can = can
        self.para = para
        self.mana = mana
        self.pot = pot
        mesaj = "Zaten sağlığınız tam \n"
        mesaj2 = "Zaten mana seviyeniz tam \n"
        don = "Kale meydanına dönüyorsunuz\n"
        hata = "Geçersiz seçim \n"
        #self.degerler()
        print("""
        1. Şifacıdan yaralarını sarmasını iste.     /    -20 akçe   /  +10 sağlık puanı 
        2. Şifacıdan merhem yapıp sürmesini iste.   /    -30 akçe   /  +25 sağlık puanı 
        3. Şifacıdan pekmez al.                     /    -25 akçe   /  +25 mana 
        4. Şifacıdan pot al.                        /    -30 akçe   /  +1 pot
        5. Kale meydanına dön.                          
        """)
        secim = input("Seçim yapınız: ")
        

        if secim == "1":
            if self.para <20:
                self.oyun_yazi("Paranız yetersiz")
                self.sifahane(self.can,self.mana,self.para)
            self.para_azalt(self.para,20) 
            self.can_ekle(self.can,10)
            self.sifahane(self.can,self.mana,self.para)
            print("can=",self.can)
                
        elif secim == "2": 
            if self.para <30:
                self.oyun_yazi("Paranız yetersiz")
                self.sifahane(self.can,self.mana,self.para)
            self.para_azalt(self.para,30)
            self.can_ekle(self.can,20)
            self.sifahane(self.can,self.mana,self.para)
            print("can=",self.can)
        
        elif secim == "3":
            if self.para <25:
                self.oyun_yazi("Paranız yetersiz")
                self.sifahane(self.can,self.mana,self.para)
            self.para_azalt(self.para,25)
            self.mana_arttir(self.mana,25)
            self.sifahane(self.can,self.mana,self.para)
            print("mana=",self.mana)

        elif secim == "4":
            if self.para <30:
                self.oyun_yazi("Paranız yetersiz")
                self.sifahane(self.can,self.mana,self.para)
            self.para_azalt(self.para,30)
            self.pot = self.pot + 1
            self.sifahane(self.can,self.mana,self.para)
            print("pot=",self.pot)

        elif secim == "5":
            self.oyun_yazi(don)
            self.oyun_menu(self.tecrube_puani,self.güc,self.ceviklik,self.dayaniklilik,self.toplayicilik,self.eglence,self.hijyen,self.tokluk,self.uykusuzluk,self.can,self.para,self.mana,self.tecrube_sayaci,self.dusmanlar,self.pot)
        else:
            self.oyun_yazi(hata)
            self.sifahane(self.can,self.mana,self.para)

    def Han(self,ad,para,tokluk,eglence,hijyen,uykusuzluk,han_metin,tecrube,tecrube2):
        self.para = para
        self.tokluk = tokluk
        self.eglence = eglence
        self.hijyen = hijyen
        self.uykusuzluk = uykusuzluk
        self.han_metin = han_metin
        self.tecrube_sayaci = tecrube2
        self.tecrube_puani = tecrube
        han_metni1 = f""" 
        Hana giren {ad} hancıya doğru bağırarak 
        {ad}: Hancı bana soğuk bir bira
        O sırada insanların bi çember yapıp tezahürat ettiklerini gördü ve merakla yanlarına doğru gitti.
        {ad}: Ne yapıyorlar burada 
        Ayakta tezahürat eden bir adam gözlerini ringden hiç ayırmadan 
        Tezahüratçı: Güreşiyorlar. 
        {ad}: Sanırsam üzerlerine bahis oynanmış denemekten zarar gelmez 
        {ad} organizsayonu yapan adama gidip kayıt oluşturdu. Bir sonraki maç ringe çıkarttılar ve rakibi uzun boylu bir siyahi adamdı. 
        {ad}: Ah! sanırım orklara benzeyen biriyle antreman yapmak hiç fena bir fikir değil he  
        rakibi sinirlenerek bi anda saldırsada küçük bedeniyle heman kaçıp arkadan yakaladı. Kaldırmaya çalışsa da beceremedi 
        ve adam kolundan tutup ringin diyer tarafına fırlattı. Darbeden sonra {ad}'ın burnu kanamaya başladı. Kanı temizleyip bu sefer o saldırdı.
        Koca cüsseli adam engellemeye çalışsa da küçük bedeniyle hemen kaçıp arkasına geçti ve diz kapağı kısmına tekme attı. Dengesini kaybeden adam
        tek bacak üstüne çöktü ve {ad} üstüne atlayarak koca adamı yere düşürmeyi başardı ve maçı kazanmış oldu. \n
        """       

        metin2 = f""" 
        Hana giren {ad} masaya doğru yürürken bir gurup adamın kavga ettiğini gördü. Hiç onları aldırmadı ve hancıya dönüp bira istedi. Hancı birasını hazırlarken
        {ad} arkası dönük bir şekilde düşünüyordu. Birden kafasına bira bardağı gelince 
        {ad}: Bu iş artık kişiselleşti 
        Dönüp kavga eden kalabalığın ortasına daldı.
        .... 
        Bir süre sonra herkes dağılmıştı yüzü kanlar içerisinde olan {ad} yerden dövdüğü adamlardan birinin cüzdanını aldı ve oturup birasını tek seferde içtikten 
        sonra handan ayrıldı.
        """


        mesaj = "Zaten sağlığınız tam \n"
        mesaj2 = "Zaten eğlenceniz tam \n"
        don = "Kale meydanına dönüyorsunuz \n"
        hata = "Geçersiz seçim \n"
        self.han_metin = random.randint(1,2)
        #self.degerler()
        print("""
        1. Yiyecek satın al ve ye.             /    -10 akçe   /  +50 tokluk
        2. İçecek satın al, iç ve eğlen.       /    -10 akçe   /  +10 tokluk  /  +10 eğlence
        3. Handa güreş.                        /    +10 akçe   /  +10 tecrübe puanı  
        4. Kale meydanına dön.
        """)
        secim = input("Seçim yapınız: ")
        if secim == "1":
            if self.tokluk >= 100:
                if self.para <10:
                    self.oyun_yazi("Paranız yetersiz")
                    self.Han(self.ad,self.para,self.tokluk,self.eglence,self.hijyen,self.uykusuzluk,self.han_metin,self.tecrube_puani,self.tecrube_sayaci)
                self.para_azalt(self.para,10)
                self.tokluk_arttir(self.tokluk,50)
                self.uykusuzluk_arttir(self.uykusuzluk,10)
                self.eglence_azalt(self.eglence,10)
                self.hijyen_azalt(self.hijyen,10)
                self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
                self.Han(self.ad,self.para,self.tokluk,self.eglence,self.hijyen,self.uykusuzluk,self.han_metin,self.tecrube_puani,self.tecrube_sayaci)
        elif secim == "2":
            if self.para < 10:
                self.oyun_yazi("Paranız yetersiz")
                self.Han(self.ad,self.para,self.tokluk,self.eglence,self.hijyen,self.uykusuzluk,self.han_metin,self.tecrube_puani,self.tecrube_sayaci)
            self.para_azalt(self.para,10)
            self.tokluk_arttir(self.tokluk,10)
            self.eglence_arttir(self.eglence,10)
            self.hijyen_azalt(self.hijyen,10)
            self.uykusuzluk_arttir(self.uykusuzluk,10)
            self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
            self.Han(self.ad,self.para,self.tokluk,self.eglence,self.hijyen,self.uykusuzluk,self.han_metin,self.tecrube_puani,self.tecrube_sayaci)
        
        elif secim == "3":
            if self.hijyen <= 0:
                self.oyun_yazi("Çok kötü kokuyorsunuz ve kimse sizinle güreşmek istemiyor. Lütfen nehire gidip temizlenin.")
                self.oyun_menu(self.tecrube_puani,self.güc,self.ceviklik,self.dayaniklilik,self.toplayicilik,self.eglence,self.hijyen,self.tokluk,self.uykusuzluk,self.can,self.para,self.mana,self.tecrube_sayaci,self.dusmanlar,self.pot)
            if self.han_metin == 1:
                self.oyun_yazi(han_metni1)
                self.tecrube_arttir(self.tecrube_puani,self.tecrube_sayaci,10)
                self.para_ekle(self.para,10)
                self.hijyen_azalt(self.hijyen,10)
                self.tokluk_azalt(self.tokluk,10)
                self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
                self.Han(self.ad,self.para,self.tokluk,self.eglence,self.hijyen,self.uykusuzluk,self.han_metin,self.tecrube_puani,self.tecrube_sayaci)
                

            else :
                self.oyun_yazi(metin2)
                self.eglence_arttir(self.eglence,10)
                self.tecrube_arttir(self.tecrube_puani,self.tecrube_sayaci,10)
                self.para_ekle(self.para,10)
                self.hijyen_azalt(self.hijyen,10)
                self.tokluk_azalt(self.tokluk,10)
                self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
                self.Han(self.ad,self.para,self.tokluk,self.eglence,self.hijyen,self.uykusuzluk,self.han_metin,self.tecrube_puani,self.tecrube_sayaci)
             

        elif secim == "4":
            self.oyun_yazi(don)
            self.oyun_menu(self.tecrube_puani,self.güc,self.ceviklik,self.dayaniklilik,self.toplayicilik,self.eglence,self.hijyen,self.tokluk,self.uykusuzluk,self.can,self.para,self.mana,self.tecrube_sayaci,self.dusmanlar,self.pot)

        else:
            self.oyun_yazi(hata)
            self.Han(self.ad,self.para,self.tokluk,self.eglence,self.hijyen,self.uykusuzluk,self.han_metin,self.tecrube_puani,self.tecrube_sayaci)


    def seviye_atla(self,güc,ceviklik,dayaniklilik,toplayicilik,tecrube_sayaci):
        #self.degerler()
        self.güc = güc
        self.ceviklik = ceviklik
        self.dayaniklilik = dayaniklilik
        self.toplayicilik = toplayicilik
        self.tecrube_sayaci = tecrube_sayaci

        hata = "Geçersiz seçim \n"
        don = "Kale meydanına dönüyorsunuz \n"
        puan = "Tecrübe puanınız 0 lütfen tecrübe puanı kazanın \n"

        if self.tecrube_sayaci >= 1:
            print(f""" 
        {tecrube_sayaci} tane tecrübe puanınız bulunmaktadır. Her geliştirme 1 tecrübe puanı gerektirmektedir.
        1. Gücünüzü geliştirin.           /   +5 güç
        2. Çevikliğinizi geliştirin.      /   +5 çeviklik
        3. Dayanıklılığınızı geliştirin.  / +5 dayanıklılık
        4. Toplayıcılığınızı geliştirin.  / +5 toplayıcılık
        5. Kale Meydanına Dön.
            """)
            secim = input("Seçim yapınız: ")
            if secim == "1":
                self.guc_arttir(self.güc,5)
                self.tecrube_azalt(self.tecrube_sayaci,1)
                self.seviye_atla(self.güc,self.ceviklik,self.dayaniklilik,self.toplayicilik,self.tecrube_sayaci)
            elif secim == "2":
                self.ceviklik_arttir(self.ceviklik,5)
                self.tecrube_azalt(self.tecrube_sayaci,1)
                self.seviye_atla(self.güc,self.ceviklik,self.dayaniklilik,self.toplayicilik,self.tecrube_sayaci)
            elif secim == "3":
                self.dayaniklilik_arttir(self.dayaniklilik,5)
                self.tecrube_azalt(self.tecrube_sayaci,1)   
                self.seviye_atla(self.güc,self.ceviklik,self.dayaniklilik,self.toplayicilik,self.tecrube_sayaci)
            elif secim == "4":
                self.toplayicilik_arttir(self.toplayicilik,5)
                self.tecrube_azalt(self.tecrube_sayaci,1)
                self.seviye_atla(self.güc,self.ceviklik,self.dayaniklilik,self.toplayicilik,self.tecrube_sayaci)
            elif secim == "5":
                self.oyun_yazi(don)
                self.oyun_menu(self.tecrube_puani,self.güc,self.ceviklik,self.dayaniklilik,self.toplayicilik,self.eglence,self.hijyen,self.tokluk,self.uykusuzluk,self.can,self.para,self.mana,self.tecrube_sayaci,self.dusmanlar,self.pot)
            else:
                self.oyun_yazi(hata)
                self.seviye_atla(self.güc,self.ceviklik,self.dayaniklilik,self.toplayicilik,self.tecrube_sayaci)
        elif self.tecrube_sayaci <= 0:
            self.oyun_yazi(puan)
            self.oyun_menu(self.tecrube_puani,self.güc,self.ceviklik,self.dayaniklilik,self.toplayicilik,self.eglence,self.hijyen,self.tokluk,self.uykusuzluk,self.can,self.para,self.mana,self.tecrube_sayaci,self.dusmanlar,self.pot)

    def Maceraya_atil(self,ad,silah_isim,silah_tur,bolum,can,para,hijyen,tokluk,eglence,uykusuzluk,güc,ceviklik,dayaniklilik,mana,toplayicilik,tecrube_puani,dusmanlar,icsayac,tecrube_sayaci,pot):
        self.bulum_sayaci = bolum
        self.can = can
        self.para = para
        self.hijyen = hijyen
        self.tokluk = tokluk
        self.eglence = eglence
        self.uykusuzluk = uykusuzluk
        self.güc = güc
        self.ceviklik = ceviklik
        self.dayaniklilik = dayaniklilik
        self.mana = mana
        self.toplayicilik = toplayicilik
        self.tecrube_puani = tecrube_puani
        self.dusmanlar = dusmanlar
        self.icsayac = icsayac
        self.tecrube_sayaci = tecrube_sayaci
        self.pot = pot
        #self.degerler()
        hatas = 0
        hata = "Geçersiz seçim \n"
        don = "Kale meydanına dönüyorsunuz \n"
        mesaj1 = "Şifalı bitki topladınız \n"
        mesaj2 = "Meyve buldunuz \n"
        mesaj3 = "Hayvan avladınız \n"
        mesaj4 = "Hiç bir şey bulamadınız. Değerleriniz düştü \n"

        if self.bolum_sayaci== 0:
            print("""
            1. Yakın çevreden şifalı bitki topla ve avlan. 
            2. Yeni Maceraya atıl.
            3. Kale meydanına dön.
            """)
            secim = input("Seçim yapınız: ")
        else:
            print("""
            1. Yakın çevreden şifalı bitki topla ve avlan.
            2. Maceraya devam et.
            3. Kale meydanına dön.
            """)
            secim = input("Seçim yapınız: ")
        if self.eglence <= 0:
            self.oyun_yazi("Eğlenceniz tükendiği için maceraya devam edemezsiniz. Lütfen Han'a gidip eğlenin.")
            self.oyun_menu(self.tecrube_puani,self.güc,self.ceviklik,self.dayaniklilik,self.toplayicilik,self.eglence,self.hijyen,self.tokluk,self.uykusuzluk,self.can,self.para,self.mana,self.tecrube_sayaci,self.dusmanlar,self.pot)
        if secim == "1":
            metin_toplama = f"""
            {ad} Vargun Kalesi çevresinde dolaşırken bir şifacıdan öğrendiği şifalı bitkileri toplamaya ve hayvan karar verdi. etrafta bitki ve hayvanları 
            aramaya başladı.hayvanları ve bitkileri ararken hem idman yaptı hemde kendini geliştirdi.\n
            """
            self.oyun_yazi(metin_toplama)
            oran = (self.toplayicilik*4)/100
            if random.random() < oran:
                self.oyun_yazi(mesaj1)
                self.can_ekle(self.can,10)
                self.hijyen_azalt(self.hijyen,10)
                self.tokluk_azalt(self.tokluk,10)
                self.eglence_azalt(self.eglence,10)
                self.uykusuzluk_arttir(self.uykusuzluk,10)
                self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
                self.Maceraya_atil(self.ad,self.silah_isim,self.silah,self.bolum_sayaci,self.can,self.para,self.hijyen,self.tokluk,self.eglence,self.uykusuzluk,self.güc,self.ceviklik,self.dayaniklilik,self.mana,self.toplayicilik,self.tecrube_puani,self.dusmanlar,self.icsayac,self.tecrube_sayaci,pot)
            elif random.random() < oran:
                self.oyun_yazi(mesaj2)
                self.tokluk_arttir(self.tokluk,10)
                self.hijyen_azalt(self.hijyen,10)
                self.eglence_azalt(self.eglence,10)
                self.uykusuzluk_arttir(self.uykusuzluk,10)
                self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
                self.Maceraya_atil(self.ad,self.silah_isim,self.silah,self.bolum_sayaci,self.can,self.para,self.hijyen,self.tokluk,self.eglence,self.uykusuzluk,self.güc,self.ceviklik,self.dayaniklilik,self.mana,self.toplayicilik,self.tecrube_puani,self.dusmanlar,self.icsayac,self.tecrube_sayaci,pot)
            elif random.random() < oran/2:
                self.oyun_yazi(mesaj3)
                self.tokluk_arttir(self.tokluk,10)   
                self.hijyen_azalt(self.hijyen,10)
                self.eglence_azalt(self.eglence,10)
                self.uykusuzluk_arttir(self.uykusuzluk,10)
                self.Maceraya_atil(self.ad,self.silah_isim,self.silah,self.bolum_sayaci,self.can,self.para,self.hijyen,self.tokluk,self.eglence,self.uykusuzluk,self.güc,self.ceviklik,self.dayaniklilik,self.mana,self.toplayicilik,self.tecrube_puani,self.dusmanlar,self.icsayac,self.tecrube_sayaci,pot)

            else:
                self.oyun_yazi(mesaj4)
                self.hijyen_azalt(self.hijyen,10)
                self.tokluk_azalt(self.tokluk,10)
                self.eglence_azalt(self.eglence,10)
                self.uykusuzluk_arttir(self.uykusuzluk,10)
                self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
                self.Maceraya_atil(self.ad,self.silah_isim,self.silah,self.bolum_sayaci,self.can,self.para,self.hijyen,self.tokluk,self.eglence,self.uykusuzluk,self.güc,self.ceviklik,self.dayaniklilik,self.mana,self.toplayicilik,self.tecrube_puani,self.dusmanlar,self.icsayac,self.tecrube_sayaci,pot)

        
        if secim == "2":
            bilgilendirme1 = f"""
            Hafif saldırılar her round yapabileceğiniz saldırılardır. Ağır saldırılar ise sadece sağlanan mana değeriniz varsa gerçekleşir.\n
            """
            print("            Bilgilendirme:")
            self.oyun_yazi(bilgilendirme1)
            if self.bolum_sayaci == 0:
                self.bolum1(self.ad,self.silah_isim)
                if self.icsayac == 0:
                    self.oyun_yazi(self.bolum1metin)
                else:
                    self.oyun_yazi(self.bolum1metin1)

                orkgüc = random.randint(1,5)
                orkcan = 50
                orkceviklik = random.randint(1,5)
                orkdayaniklilik = random.randint(1,5)
                self.dusmanlar.degistir(orkgüc,orkcan,orkceviklik,orkdayaniklilik)

            elif self.bolum_sayaci == 1:
                self.bolum2(self.ad,self.silah_isim)
                if self.icsayac1 == 0:
                    self.oyun_yazi(self.bolum2metin)
                else:
                    self.oyun_yazi(self.bolum2metin4)
                orkgüc = random.randint(6,10)
                orkcan = 70
                orkceviklik = random.randint(6,10)
                orkdayaniklilik = random.randint(6,10)
                self.dusmanlar.degistir(orkgüc,orkcan,orkceviklik,orkdayaniklilik)

            elif self.bolum_sayaci == 2:
                self.bolum3(self.ad,self.silah_isim)
                if self.icsayac2 == 0:  
                    self.oyun_yazi(self.bolum3metin)
                else:
                    self.oyun_yazi(self.bolum3metin4)
                orkgüc = random.randint(11,15)
                orkcan = 90
                orkceviklik = random.randint(11,15)
                orkdayaniklilik = random.randint(11,15)
                self.dusmanlar.degistir(orkgüc,orkcan,orkceviklik,orkdayaniklilik)
            
            else: 
                self.bolum4(self.ad,self.silah_isim)
                self.oyun_yazi(self.bolum4metin)
                print("""
        1. Savaş
        2. Savaş

                """)
                secim = input("Savaş ya da SAVAŞ!!! : ")
                if secim == "1" or secim == "2":
                    self.oyun_yazi(self.bolum4metin2)
                print("""
        Özel saldırı
                """)
                secim2 = input("""
        ÖLDÜR ONLARI!!! : """)
                
                self.oyun_yazi(self.bolum4metin3) 
                secim2 = input("""
        Will'i kaldır """)
                self.oyun_yazi(self.bolum4metin4)
                secim3 = input("""
        Press F to pay respects: """)
                if secim3 == "F" or "f":
                    self.oyun_yazi("Tebrikler Gizli Başarım Kazandınız")
                    print("Onurlu bir yaşam")
                else:
                    self.oyun_yazi("Tebrikler Gizli Başarım Kazandınız")
                    print("Onursuz bir yaşam")
                self.oyun_yazi(self.bolum4metin5)
                exit()

            
            print("""
        1. Savaş
        2. Kaç
                """)
            rvh = 4*self.güc
            secim = input("Savaş ya da kaç!!! : ")
            if secim == "1":

                if self.bolum_sayaci == 0:
                    self.oyun_yazi(self.bolum1metin3)
                elif self.bolum_sayaci == 1:
                    self.oyun_yazi(self.bolum2metin5)
                elif self.bolum_sayaci == 2:
                    self.oyun_yazi(self.bolum3metin5)

                if self.ceviklik == dusmanlar.dusmanceviklik:
                    basla = random.randint(1,2)
                elif self.ceviklik >= self.dusmanlar.dusmanceviklik:
                    basla = 1
                elif self.ceviklik < self.dusmanlar.dusmanceviklik:
                    basla = 2
                rvhd = 4*self.dusmanlar.dusmanguc
                if basla == 1:
                    self.oyun_yazi("Siz başlıyorsunuz \n")
                    while True:
                        print("""
        1. Hafif Saldırı
        2. Ağır Saldırı     /  -40 mana
        3. Pot kullan       /  +20 can
                            """)
                        secim = input("Hamlenizi seçiniz: ")
                        if secim == "1":
                            self.oyun_yazi("Hafif saldırı yaptınız\n")
                            kacisdusman = 2*self.dusmanlar.dusmanceviklik
                            if kacisdusman >= 50:
                                print("Ork kaçtı")
                            else:
                                orkcan = int(orkcan - (rvh - (rvh * (self.dusmanlar.dusmandayaniklilik * 4) / 100) - 1))
                                self.oyun_yazi(f"Orkun canı {orkcan}\n")
                                if orkcan <= 0:
                                    if self.bolum_sayaci == 0  and orkcan <= 0:
                                        self.bolumsayaci_artir(self.bolum_sayaci)
                                        self.tecrube_arttir(self.tecrube_puani,tecrube_sayaci,60)
                                        self.para_ekle(self.para,30)
                                        self.eglence_azalt(self.eglence,20)
                                        self.tokluk_azalt(self.tokluk,20)
                                        self.uykusuzluk_arttir(self.uykusuzluk,20)
                                        self.hijyen_azalt(self.hijyen,20)
                                        self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
                                        self.oyun_yazi(self.bolum1metin4)
                                        break

                                    elif self.bolum_sayaci == 1 and orkcan <= 0:
                                        self.oyun_yazi(self.bolum2metin2)
                                        self.bolumsayaci_artir(self.bolum_sayaci)
                                        self.tecrube_arttir(self.tecrube_puani,tecrube_sayaci,80)
                                        self.para_ekle(self.para,60)
                                        self.eglence_azalt(self.eglence,20)
                                        self.tokluk_azalt(self.tokluk,20)
                                        self.uykusuzluk_arttir(self.uykusuzluk,20)
                                        self.hijyen_azalt(self.hijyen,20)
                                        self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
                                        break

                                    elif self.bolum_sayaci == 2 and orkcan <= 0:
                                        self.oyun_yazi(self.bolum3metin2)
                                        self.bolumsayaci_artir(self.bolum_sayaci)
                                        self.tecrube_arttir(self.tecrube_puani,tecrube_sayaci,160)
                                        self.para_ekle(self.para,100)
                                        self.eglence_azalt(self.eglence,20)
                                        self.tokluk_azalt(self.tokluk,20)
                                        self.uykusuzluk_arttir(self.uykusuzluk,20)
                                        self.hijyen_azalt(self.hijyen,20)
                                        self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
                                        break

                                self.oyun_yazi("Ork size saldırdı \n")
                                kacis = 2*self.ceviklik
                                if kacis >= 50:
                                    print("Orkun saldırısından kaçtınız")
                                else:
                                    self.can_azalt(self.can, int((rvhd - (rvhd * (self.dayaniklilik * 4) / 100) - 1)))
                                    self.oyun_yazi(f"Sizin canınız {self.can} \n")
                                    if self.can <= 0 and (bolum_sayaci == 0 or bolum_sayaci == 1 or bolum_sayaci == 2):
                                        self.oyun_yazi("Öldünüz \n")
                                        self.oyun_yazi("Oyun bitti")
                                        exit()
                
                        elif secim == "2":
                            if self.mana >= 40:
                                self.oyun_yazi("Ağır saldırı yaptınız \n")
                                kacisdusman = 2*self.dusmanlar.dusmanceviklik
                                self.mana_azalt(self.mana,40)
                                if kacisdusman >= 50:
                                    print("Ork kaçtı")
                                else:
                                    orkcan = int(orkcan - (2*rvh - (rvh * (self.dusmanlar.dusmandayaniklilik * 4) / 100) - 1))
                                    self.oyun_yazi(f"Orkun canı {orkcan} \n")
                                    if self.bolum_sayaci == 0  and orkcan <= 0:
                                        self.bolumsayaci_artir(self.bolum_sayaci)
                                        self.tecrube_arttir(self.tecrube_puani,tecrube_sayaci,30)
                                        self.para_ekle(self.para,30)
                                        self.eglence_azalt(self.eglence,20)
                                        self.tokluk_azalt(self.tokluk,20)
                                        self.uykusuzluk_arttir(self.uykusuzluk,20)
                                        self.hijyen_azalt(self.hijyen,20)
                                        self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
                                        self.oyun_yazi(self.bolum1metin4)
                                        break

                                    elif self.bolum_sayaci == 1 and orkcan <= 0:
                                        self.oyun_yazi(self.bolum2metin2)
                                        self.bolumsayaci_artir(self.bolum_sayaci)
                                        self.tecrube_arttir(self.tecrube_puani,tecrube_sayaci,60)
                                        self.para_ekle(self.para,60)
                                        self.eglence_azalt(self.eglence,20)
                                        self.tokluk_azalt(self.tokluk,20)
                                        self.uykusuzluk_arttir(self.uykusuzluk,20)
                                        self.hijyen_azalt(self.hijyen,20)
                                        self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
                                        break

                                    elif self.bolum_sayaci == 2 and orkcan <= 0:
                                        self.oyun_yazi(self.bolum3metin2)
                                        self.bolumsayaci_artir(self.bolum_sayaci)
                                        self.tecrube_arttir(self.tecrube_puani,tecrube_sayaci,100)
                                        self.para_ekle(self.para,100)
                                        self.eglence_azalt(self.eglence,20)
                                        self.tokluk_azalt(self.tokluk,20)
                                        self.uykusuzluk_arttir(self.uykusuzluk,20)
                                        self.hijyen_azalt(self.hijyen,20)
                                        self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
                                        
                                        break

                                        

                                    self.oyun_yazi("Ork size saldırdı \n")
                                    kacis = 2*self.ceviklik
                                    if kacis >= 50:
                                        print("Orkun saldırısından kaçtınız")
                                    else:
                                        self.can_azalt(self.can, int((rvhd - (rvhd * (self.dayaniklilik * 4) / 100) - 1)))
                                        self.oyun_yazi(f"Sizin canınız {self.can} \n")
                                        if self.can <= 0 and (bolum_sayaci == 0 or bolum_sayaci == 1 or bolum_sayaci == 2):
                                            self.oyun_yazi("Öldünüz \n")
                                            self.oyun_yazi("Oyun bitti")
                                            exit()
                                        
                            else:
                                self.oyun_yazi("Yeterli mana yok \n")
                        
                        elif secim == "3":
                            self.can_arttir(self.can,20)
                            self.pot_azalt(self.pot,1)

                        else: 
                            self.oyun_yazi(hata)
                            
                        

                        

                    self.oyun_menu(self.tecrube_puani,self.güc,self.ceviklik,self.dayaniklilik,self.toplayicilik,self.eglence,self.hijyen,self.tokluk,self.uykusuzluk,self.can,self.para,self.mana,self.tecrube_sayaci,self.dusmanlar,self.pot)
                elif basla ==2:
                    self.oyun_yazi("Ork başlıyor")
                    while True:
                        kacis = 2*self.ceviklik
                        if kacis >= 50:
                            print("Orkun saldırısından kaçtınız")
                        else:
                            self.can_azalt(self.can, (rvhd - (rvhd * (self.dayaniklilik * 4) / 100) - 1))
                            self.oyun_yazi(f"Sizin canınız: {self.can} \n")
                            if self.can <= 0 and (bolum_sayaci == 0 or bolum_sayaci == 1 or bolum_sayaci == 2): 
                                self.oyun_yazi("Öldünüz \n")
                                self.oyun_yazi("Oyun bitti")
                                exit()
                            
                        print("""
                        1. Hafif Saldırı
                        2. Ağır Saldırı     /   40 mana
                        """)
                        secim = input("Saldırı seçiniz: ")
                        if secim == "1":
                            self.oyun_yazi("Hafif saldırı yaptınız\n")
                            kacisdusman = 2*self.dusmanlar.dusmanceviklik
                            if kacisdusman >= 50:
                                print("Ork kaçtı")
                            else:
                                orkcan = orkcan - (rvh - (rvh * (self.dusmanlar.dusmandayaniklilik * 4) / 100) - 1)
                                self.oyun_yazi(f"Orkun canı {orkcan}\n")
                                if self.bolum_sayaci == 0  and orkcan <= 0:
                                    self.bolumsayaci_artir(self.bolum_sayaci)
                                    self.tecrube_arttir(self.tecrube_puani,tecrube_sayaci,30)
                                    self.para_ekle(self.para,30)
                                    self.eglence_azalt(self.eglence,20)
                                    self.tokluk_azalt(self.tokluk,20)
                                    self.uykusuzluk_arttir(self.uykusuzluk,20)
                                    self.hijyen_azalt(self.hijyen,20)
                                    self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
                                    self.oyun_yazi(self.bolum1metin4)
                                    break
                                elif self.bolum_sayaci == 1 and orkcan <= 0:
                                    self.oyun_yazi(self.bolum2metin2)
                                    self.bolumsayaci_artir(self.bolum_sayaci)
                                    self.tecrube_arttir(self.tecrube_puani,tecrube_sayaci,60)
                                    self.para_ekle(self.para,60)
                                    self.eglence_azalt(self.eglence,20)
                                    self.tokluk_azalt(self.tokluk,20)
                                    self.uykusuzluk_arttir(self.uykusuzluk,20)
                                    self.hijyen_azalt(self.hijyen,20)
                                    self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
                                    break
                                elif self.bolum_sayaci == 2 and orkcan <= 0:
                                    self.oyun_yazi(self.bolum3metin2)
                                    self.bolumsayaci_artir(self.bolum_sayaci)
                                    self.tecrube_arttir(self.tecrube_puani,tecrube_sayaci,100)
                                    self.para_ekle(self.para,100)
                                    self.eglence_azalt(self.eglence,20)
                                    self.tokluk_azalt(self.tokluk,20)
                                    self.uykusuzluk_arttir(self.uykusuzluk,20)
                                    self.hijyen_azalt(self.hijyen,20)
                                    self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
                         
                                    break

                                self.oyun_yazi("Ork size saldırdı")
                                kacis = 2*self.ceviklik
                                if kacis >= 50:
                                    print("Orkun saldırısından kaçtınız")
                                else:
                                    self.can_azalt(self.can, (rvhd - (rvhd * (self.dayaniklilik * 4) / 100) - 1))
                                    self.oyun_yazi(f"Sizin canınız {self.can} \n")
                                    if self.can <= 0 and (bolum_sayaci == 0 or bolum_sayaci == 1 or bolum_sayaci == 2): 
                                        self.oyun_yazi("Öldünüz \n")
                                        self.oyun_yazi("Oyun bitti")
                                        exit()
                                    
                        elif secim == "2":
                            if self.mana >= 40:
                                self.oyun_yazi("Ağır saldırı yaptınız \n")
                                kacisdusman = 2*self.dusmanlar.dusmanceviklik
                                self.mana_azalt(self.mana,40)
                                if kacisdusman >= 50:
                                    print("Ork kaçtı")
                                else:
                                    orkcan = orkcan - (2*rvh - (rvh * (self.dusmanlar.dusmandayaniklilik * 4) / 100) - 1)
                                    self.oyun_yazi(f"Orkun canı {orkcan} \n")
                                    if self.bolum_sayaci == 0  and orkcan <= 0:
                                        self.bolumsayaci_artir(self.bolum_sayaci)
                                        self.tecrube_arttir(self.tecrube_puani,tecrube_sayaci,30)
                                        self.para_ekle(self.para,30)
                                        self.eglence_azalt(self.eglence,20)
                                        self.tokluk_azalt(self.tokluk,20)
                                        self.uykusuzluk_arttir(self.uykusuzluk,20)
                                        self.hijyen_azalt(self.hijyen,20)
                                        self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
                                        self.oyun_yazi(self.bolum1metin4)
                                        break

                                    elif self.bolum_sayaci == 1 and orkcan <= 0:
                                        self.oyun_yazi(self.bolum2metin2)
                                        self.bolumsayaci_artir(self.bolum_sayaci)
                                        self.tecrube_arttir(self.tecrube_puani,tecrube_sayaci,60)
                                        self.para_ekle(self.para,60)
                                        self.eglence_azalt(self.eglence,20)
                                        self.tokluk_azalt(self.tokluk,20)
                                        self.uykusuzluk_arttir(self.uykusuzluk,20)
                                        self.hijyen_azalt(self.hijyen,20)
                                        self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
                                        break

                                    elif self.bolum_sayaci == 2 and orkcan <= 0:
                                        self.bolumsayaci_artir(self.bolum_sayaci)
                                        self.tecrube_arttir(self.tecrube_puani,tecrube_sayaci,100)
                                        self.para_ekle(self.para,100)
                                        self.eglence_azalt(self.eglence,20)
                                        self.tokluk_azalt(self.tokluk,20)
                                        self.uykusuzluk_arttir(self.uykusuzluk,20)
                                        self.hijyen_azalt(self.hijyen,20)
                                        self.sonuclar(self.uykusuzluk,self.hijyen,self.tokluk,self.eglence,self.can,self.para)
                                        self.oyun_yazi(self.bolum3metin2)
                                        break

                                    self.oyun_yazi("Ork size saldırdı \n")
                                    kacis = 2*self.ceviklik
                                    if kacis >= 50:
                                        print("Orkun saldırısından kaçtınız")
                                    else:
                                        self.can_azalt(self.can, (rvhd - (rvhd * (self.dayaniklilik * 4) / 100) - 1))
                                        self.oyun_yazi(f"Sizin canınız {self.can} \n")
                                        if self.can <= 0 and (bolum_sayaci == 0 or bolum_sayaci == 1 or bolum_sayaci == 2): 
                                            self.oyun_yazi("Öldünüz \n")
                                            self.oyun_yazi("Oyun bitti")
                                            exit()
                                        
                            else:
                                self.oyun_yazi("Yeterli mana yok \n")
                        else:
                            self.oyun_yazi(hata)
                            self.Maceraya_atil(self.ad,self.silah_isim,self.silah,self.bolum_sayaci,self.can,self.para,self.hijyen,self.tokluk,self.eglence,self.uykusuzluk,self.güc,self.ceviklik,self.dayaniklilik,self.mana,self.toplayicilik,self.tecrube_puani,self.dusmanlar,self.icsayac,self.tecrube_sayaci,pot)
                            break

                    self.oyun_menu(self.tecrube_puani,self.güc,self.ceviklik,self.dayaniklilik,self.toplayicilik,self.eglence,self.hijyen,self.tokluk,self.uykusuzluk,self.can,self.para,self.mana,self.tecrube_sayaci,self.dusmanlar,self.pot)


            elif secim == "2" and self.bolum_sayaci == 0:
                if self.icsayac == 1:
                    self.oyun_yazi(self.bolum1kacis)
                    self.oyun_yazi("Tebrikler gizli başarımı açtınız. \nULTRA KORKAK")
                    exit()
                else:    
                    self.oyun_yazi(self.bolum1metin2)
                    self.icsayac = 1
                    self.oyun_menu(self.tecrube_puani,self.güc,self.ceviklik,self.dayaniklilik,self.toplayicilik,self.eglence,self.hijyen,self.tokluk,self.uykusuzluk,self.can,self.para,self.mana,self.tecrube_sayaci,self.dusmanlar,self.pot)
                

            elif secim == "2" and self.bolum_sayaci == 1:
                self.oyun_yazi(self.bolum2metin3)
                self.icsayac1 = 1
                self.oyun_menu(self.tecrube_puani,self.güc,self.ceviklik,self.dayaniklilik,self.toplayicilik,self.eglence,self.hijyen,self.tokluk,self.uykusuzluk,self.can,self.para,self.mana,self.tecrube_sayaci,self.dusmanlar,self.pot)


            elif secim == "2" and self.bolum_sayaci == 2:
                self.oyun_yazi(self.bolum3metin3)
                self.icsayac2 = 1
                self.oyun_menu(self.tecrube_puani,self.güc,self.ceviklik,self.dayaniklilik,self.toplayicilik,self.eglence,self.hijyen,self.tokluk,self.uykusuzluk,self.can,self.para,self.mana,self.tecrube_sayaci,self.dusmanlar,self.pot)
            
            elif secim == "3":
                self.oyun_yazi(don)
                self.oyun_menu(self.tecrube_puani,self.güc,self.ceviklik,self.dayaniklilik,self.toplayicilik,self.eglence,self.hijyen,self.tokluk,self.uykusuzluk,self.can,self.para,self.mana,self.tecrube_sayaci,self.dusmanlar,self.pot)

            else:
                self.oyun_yazi(hata)
                self.Maceraya_atil(self.ad,self.silah_isim,self.silah,self.bolum_sayaci,self.can,self.para,self.hijyen,self.tokluk,self.eglence,self.uykusuzluk,self.güc,self.ceviklik,self.dayaniklilik,self.mana,self.toplayicilik,self.tecrube_puani,self.dusmanlar,self.icsayac,self.tecrube_sayaci,pot)
       
            
            



    def oyun_menu(self,tecrube,güc,ceviklik,dayaniklilik,toplayicilik,eglence,hijyen,tokluk,uykusuzluk,can,para,mana,tecrube2,dusmanlar,pot):
        self.can = can
        self.para = para
        self.hijyen = hijyen
        self.tokluk = tokluk
        self.eglence = eglence
        self.uykusuzluk = uykusuzluk
        self.güc = güc
        self.ceviklik = ceviklik
        self.dayaniklilik = dayaniklilik
        self.mana = mana
        self.toplayicilik = toplayicilik
        self.tecrube_puani = tecrube
        self.tecrube_sayaci = tecrube2
        self.dusmanlar = dusmanlar 
        self.pot = pot 

        hata = "Geçersiz seçim \n"
        mesaj = "Oyundan çıkılıyor \n"
        mesaj2 = "Çıkmak istediğinize eminmisiniz? (E/H) \n: "

        print("""
        1. kamp alanı
        2. Şifahane
        3. Hana git.
        4. Maceraya atıl.
        5. Seviye atla.
        6. Durumu göster.
        7. Oyundan çık.   
        """)
        secim = input("Gitmek istediğiniz yeri seçiniz: ")
        if secim == "1" :
            self.kamp_alani(self.ad,self.eglence,self.hijyen,self.tokluk,self.uykusuzluk,self.tecrube_sayaci)
        elif secim == "2":
            self.sifahane(self.can,self.mana,self.para)
        elif secim == "3":
            self.Han(self.ad,self.para,self.tokluk,self.eglence,self.hijyen,self.uykusuzluk,self.han_metin,self.tecrube_puani,self.tecrube_sayaci)
        elif secim == "4":
            self.Maceraya_atil(self.ad,self.silah_isim,self.silah,self.bolum_sayaci,self.can,self.para,self.hijyen,self.tokluk,self.eglence,self.uykusuzluk,self.güc,self.ceviklik,self.dayaniklilik,self.mana,self.toplayicilik,self.tecrube_puani,self.dusmanlar,self.icsayac,self.tecrube_sayaci,pot)
        elif secim == "5":
            self.seviye_atla(self.güc,self.ceviklik,self.dayaniklilik,self.toplayicilik,self.tecrube_sayaci)

        elif secim == "6":
            print(self.durum(self.can,self.para,self.hijyen,self.tokluk,self.eglence,self.uykusuzluk,self.güc,self.ceviklik,self.dayaniklilik,self.mana,self.toplayicilik,self.tecrube_puani))
            self.oyun_menu(self.tecrube_puani,self.güc,self.ceviklik,self.dayaniklilik,self.toplayicilik,self.eglence,self.hijyen,self.tokluk,self.uykusuzluk,self.can,self.para,self.mana,self.tecrube_sayaci,self.dusmanlar,self.pot)
        elif secim == "7":
            self.oyun_yazi(mesaj)
            self.oyun_yazi(mesaj2)
            soru = input("")
            soru1 = soru.upper()
            if soru1 == "E":
                exit()
            else:
                self.oyun_menu(self.tecrube_puani,self.güc,self.ceviklik,self.dayaniklilik,self.toplayicilik,self.eglence,self.hijyen,self.tokluk,self.uykusuzluk,self.can,self.para,self.mana,self.tecrube_sayaci,self.dusmanlar,self.pot)
        else:
            self.oyun_yazi(hata)
            self.oyun_menu(self.tecrube_puani,self.güc,self.ceviklik,self.dayaniklilik,self.toplayicilik,self.eglence,self.hijyen,self.tokluk,self.uykusuzluk,self.can,self.para,self.mana,self.tecrube_sayaci,self.dusmanlar,self.pot)


    def durum(self,can,para,hijyen,tokluk,eglence,uykusuzluk,güc,ceviklik,dayaniklilik,mana,toplayicilik,tecrube_puani):
            self.can = can
            self.para = para
            self.hijyen = hijyen
            self.tokluk = tokluk
            self.eglence = eglence
            self.uykusuzluk = uykusuzluk
            self.güc = güc
            self.ceviklik = ceviklik
            self.dayaniklilik = dayaniklilik
            self.mana = mana
            self.toplayicilik = toplayicilik
            self.tecrube_puani = tecrube_puani
            
            return f"""
            Canınız: {self.can}
            Paranız: {self.para}
            Hijyen: {self.hijyen}
            Tokluk: {self.tokluk}
            Eğlence: {self.eglence}
            Uykusuzluk: {self.uykusuzluk}
            Gücünüz: {self.güc}
            Çevikliğiniz: {self.ceviklik}
            Dayanıklılığınız: {self.dayaniklilik}
            Mana: {self.mana}
            Toplayıcılığınız: {self.toplayicilik}
            Tecrübe puanınız: {self.tecrube_puani}"""
            # print(f"""
            # Canınız: {self.can}
            # Paranız: {self.para}
            # """)
    def oyuna_giris(self,can,para,hijyen,tokluk,eglence,uykusuzluk,güc,ceviklik,dayaniklilik,mana,toplayicilik,tecrube,dusmanlar):
        self.can = can
        self.para = para
        self.hijyen = hijyen
        self.tokluk = tokluk
        self.eglence = eglence
        self.uykusuzluk = uykusuzluk
        self.güc = güc
        self.ceviklik = ceviklik
        self.dayaniklilik = dayaniklilik
        self.mana = mana
        self.toplayicilik = toplayicilik
        self.tecrube_puani = tecrube
        self.dusmanlar = dusmanlar
        self.ad = input("Lütfen karakterin adını giriniz: ")

        hata = "Geçersiz seçim \n"
        print("""
        1. Kılıç
        2. Mızrak
        3. Balta
        
        """)
        self.silah = input("lütfen karakterinizin silahını seçiniz:")
        if self.silah == "1":
            self.silah = "Kılıç"
        elif self.silah == "2":
            self.silah = "Mızrak"
        elif self.silah == "3":
            self.silah = "Balta" 
        else:
            self.oyun_yazi(hata)
            self.oyuna_giris(self.can,self.para,self.hijyen,self.tokluk,self.eglence,self.uykusuzluk,self.güc,self.ceviklik,self.dayaniklilik,self.mana,self.toplayicilik,self.tecrube_puani,self.dusmanlar)

        self.silah_isim = input("Lütfen silahınızın ismini giriniz: ")
        self.oyun_yazi(self.oyun_giris_metini(self.ad,self.silah_isim,self.silah))
        self.oyun_menu(self.tecrube_puani,self.güc,self.ceviklik,self.dayaniklilik,self.toplayicilik,self.eglence,self.hijyen,self.tokluk,self.uykusuzluk,self.can,self.para,self.mana,self.tecrube_sayaci,self.dusmanlar,self.pot)


    def oyun_yazi(self,text,delay=0.03):

        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)

        

    def oyun_giris_metini(self,ad,kılıc_ad,silah_tur):
        self.metin = f"""
        Ork avcısı, yerdeki cesetleri kontrol ediyordu. Kanlar içerisinde, cılız bir çocuğu farketti, diğer cesetlerin aksine üzerinde
        hiçbir yara izi yoktu. Eğilerek vücudu kontrol etti ve yaşadığını farketti. Ork avcısı ayağa kalkarak,
        Ork Avcısı: Hey! kalkabilirsin orklar etrafımızda yoklar 
        Tek gözünü açıp etrafı kontrol eden cılız çocuk bir anda ayağa fırladı ve ork avcısına bakarak.
        {ad}: Ah o iğrenç yaratıklar.
        Elini uzatıp ben {ad} dedi. Avcı somurtkan bir surat ile hıh diyip diğer cesetlere doğru yürümeye başladı. 
        Ork Avıcısı"Aralarından kurtulmayı nasıl başardın" diye sordu avcı çocuğa.
        {ad}: İsmini söylersen belki sana anlatırım.
        Will: Benim adım Will.
        {ad}: Ah Will, memnun oldum. İşin gerçeği cesedlerden birinin kanını kendi üzerime sürerek ölü taklidi yaptım.
        bu sırada üstündeki kanı temizleyip ve {kılıc_ad} isimli {silah_tur} silahını yerden aldı.{ad}'ın gidecek yeri yoktu ve aklından ork avcısına katılabileceği
        geçti. Kendini toparlayıp 
        {ad}: Hey Will seninle gele... 
        Will: Hayır! 
        Will {ad}'ın sözünü keserek.
        {ad}: Lütfen gidecek hiç bir yerim yok kimsem kalmadı.
        Will: Benim yolculuğum tehlikelidir.
        {ad} Benim için tehlikeli bir şey yok .
        Will somurtarak da olsa kabul etti. Will ve {ad} macerası burada başladı.
        Will ve {ad} uzun bir yolculuktan sonra Vargun kalesine vardılar.
        Will: İşte burası Vargun kalesi.
        Will: Burada biraz dinlenelim ve sonra yola devam ederiz. \n
        """     
        self.metin2 = "dasdasdasd"
        
        return self.metin

    def bolum4(self,ad,silah_isim): 
        self.bolum4metin = f"""
        {ad} Will'i meydanda otururken gördü Will düşünceli görünüyordu yanına gidip sordu neden bu kadar düşüncelisin diye.
        Will: Urak orkları genelde bu kadar insanların olduğu yere yaklaşmazlar. 
        {ad} umursamaz bir şekilde.
        {ad}: Ne olucak yani biri yaklaştı diye? 
        Ama Will'i rahatsız eden başka bir şey vardı.
        {ad}: Hey, ne oldu anlatacakmısın artık.
        Will: Görmediğin şeyler vardı orada. Etrafta bir kaç tane kılıç vardı gördünmü? 
        {ad} kafasını sallalyarak görmediğini ifade etti.
        {ad}: Orkun öldürdüğü adamlardır ne olacak yani 
        Will: Hayır onlar normal kılıç değillerdi onlar benimki gibi birer ork kılıcıydı.
        {ad} şaşırmıştı.
        {ad}: Ork kılıcı mı? 
        Will: Evet. Her ork avcısına eğitimi tamamlama şerefine verilir bu kılıçlar. 
        {ad} bunu ilk defa duyuyordu. 
        Will: Eğer o kılıçlar oradaysa sahipleri ölmüştür demektir bu. Ama ork avcılarından hiç biri Urak orklarına ölmeyecek kadar tecrübelidir.
        {ad}: Bu ne demek oluyor yani?
        Will: Ben de bilmiyorum gidip öğreneceğim.
        {ad}: Ben de seninle geliyorum.
        Will hiç karşı çıkmadı normalde bu tarz riskli işlere {ad}'ı götürmezdi.
        ....
        Orku öldürdükleri yere geldiklerinde etrafın temiz olduklarını gördüler kılıçlar artık yoktu. 
        Will: Bu işte bir iş var temkinli ol.
        Etrafta su sesi geliyordu. Will ve {ad} su sesine doğru ilerlediler. Karşılarında gürül gürül akan bir nehir vardı. Will çok tuhaf kokular 
        alıyorum diye uyardı adı {ad} şaşırmıştı çünkü o hiç bir koku almıyordu. Will tehtitkar bir şekilde
        Will: "ÇIKIN ORTAYA".
        Ağaçların arasından aynı Will gibi giyinmiş bir gurubun çıktığını gördü {ad}, Will bu duruma hiç şaşırmamıştı. 
        Yabancı: Tekrar karşılaştık eski dostum.
        Will: Seni burada görmek beni şaşırtmadı. Ne de olsa ölmemi isteyecek ilk kişi sensin varu
        Varu: Ah neden öyle diyorsun kardeşim ben senin en iyi dostunum.
        Will yere tükürerek ne kadar tiksindiğini gösterdi. O sırada {ad} {silah_isim} eline almıştı.
        Varu: Oh bakıyorumda yeni arkadaşlar edinmişsin.
        O sırada yanındaki adamlara el hareketiyle saldırmalarını emretti. Will ve {ad} savunmaya geçtiler.kapana sıkıştırılmış gibiydiler 
        arkalarında nehir önlerinde düşman vardı hepsini öldürmeden burdan canlı çıkmaları imkansızdı.\n

        """

        self.bolum4metin2 = f"""
        {ad} ve Will çarpışırken.
        {ad}'a doğru gelen bir okun önüne atladı Will ve kolundan yaralandı. O sırada fırsattan istifade eden diğer avcılar Will'e kılıç saldırılarında bulundu.
        bir kaçı tutan kılıçlarla güçsüzleşen Will tek ayak üstüne düşmüştü Varu Will'e doğru yürüyodu onu korumak isteyen {ad} önüne çıkmak istedi ama başka
        bir avcı onu kollarından tuttup kıstırdı. Varu Will'e doğru kılıcını doğrulttu. Will arkasını dönüp {ad}'a baktı ve gülümseyerek.
        Will: Bundan sonrası sende küçük dostum.
        O anda Varu kılıç darbesini Will'e indirdi. Will kanlar içerisinde yere düştü. Sevinçli bir şekilde bağıran Varu.
        Varu: Ne oldu Will kim daha iyimiş.
        Diyerek kahkahalar atmaya başladı. {ad}'ı yere indirmişti adam 
        Varu: Onu da diğerinin yanına gönderin.
        Avcılardan biri {ad}'a kılıcını indirecekken {ad} etrafı yanmaya başladı. 
        ...\n
        """

        self.bolum4metin3 = f"""
        {ad} ne olduğunu anlamadı sadece duyduğu bir ejderha sesiydi ve etrafı alevler içerisindeydi. Varu'nun vücudunun belli kısımları yanmıştı ama hala 
        yaşıyordu.
        Varu: Demek seni bu yüzden yanında tuttu hep her zaman senin kim olduğunu biliyordu o yüzden kervanı uzaktan takip etti hep.
        Varu: HAHAH--. SEN CİDDEN ONUN İNSAN OLDUĞUNUMU DÜŞÜNDÜNDÜN HE.
        Varu: Dememek ejderha soyundan gelen sensin ve se...  
        Öksürdü ve kan kusdu. Konuşmaya çalışsa da gücü kalmadı ve acı içinde son nefesini verdi.\n 
        """

        self.bolum4metin4 = f"""

        {ad} Will'in cesedini alıp ücra bir yere götürdü. Toprağı kazıp Will'i gömdü. Will'in kılıcını alıp sırtına yerleştirdi.
        """

        self.bolum4metin5 = f"""
        Son bir kere mezarı başında durdu çömelip dua etti. O sırada göz yaşları toprağa dökülüyordu. {ad} artık tek başınaydı. Will'in kim olduğunu ve asıl önemlisi
        kendisinin ne olduğunu öğrenmek , özel gücünü araştırmak ve oradaki kılıçların sahipleri kimler olduğunu öğrenmek için yola çıktı. \n
        """



    def bolum3(self,ad,silah_isim):
        self.bolum3metin = f"""
        Son ork avlarından şuana kadar uzun bir zaman geçmişti. Will ve {ad} bu sefer Vargun Kalesi Lordu Baldwin'in yanına gitmişlerdi. Baldwin ikisi ile selamlaştıktan 
        sonra olayları anlattı. Etrafta bir kaç ork cesedine rastladıklarını ve bu cesetlerin neden kaynaklı olarak öldüğünü anlayamadıklarını anlattı. Will ve {ad} 
        bu sefer ork avlamak için iş almamıştı bu seferki işleri araştırmaydı. Will ve {ad} anlattığı yere gittiler ve dediği gibi etrafta ork cesedleri vardı.
        Will bu cesetlerin insanlar veya ork avcıları tarafından avlanılmadığını anlamıştı. 
        Will: Bu cesetlerin neden öldüğünü anlamamız gerekiyor.  
        {ad} ve Will cesedleri incelemek için yaklaştı. 
        Will: Görüyormusun cesedlerin göğüs taraflarında pençe izleri var.
        {ad} cesetleri inceledikten sonra Will'e dönüp.
        {ad}: Daha fazlası da var
        O sırada cesedin boynundaki diş izlerini gösterdi. 
        Will: Bu cesedler bu orklardan daha güçlü bir şey tarafından öldürüldü ve öldüren varlık cesedleri bir araya toplamış. 
        Ormanın deriniklerinden gelen ayak seslerini işittiler. Will {ad}'ı kolundan tutuğu gibi büyük bir kayanın arkasına götürdü. Oradan olan biteni izlemeye 
        çalıştılar. Ayak sesleri gittikçe büyüyordu ve yer sarsıntısı artıyordu. En sonunda ağaçların ikisini kırarak gelen devasa bir ork çıktı. {ad} orkun büyüklü 
        karşsında şaşkına dönmüştü.
        {ad}: Bu diğer orklara benzemiyor.
        Will: Evet bunlar Urak orkları ve bu orklar diğer orklardan daha güçlü ve daha iridir.
        Will orku izlemeye devam ederken. {ad} ve Will seçim yapmak zorundalardı ya kaçacaklardı ya da ork ile savaşacaklardı. \n
        
        """
        self.bolum3metin2 = f"""
        {ad} ve Will'in kordineli saldırılarına dayanamayan ork iki ayak üstüne düştü. {ad} bu fırsatı kaçırmak hiç istemiyordu ve orkun üzerine atladı. {silah_isim} ile
        orkun kafasına bir kaç darbe indirdi. Darbelerden sonra ork yere düşmüştü. Will {ad}'a dönüp.
        Will: Bu kadar yeter.
        Will: Unutma {ad} ne olursa olsun her canlı düzgün bir şekilde ölmeyi hak ediyor 
        {ad} şaşırmıştı çünkü Will'in bu kadar sert olmasını beklemiyordu.
        {ad}: Ama onlar bizim halkımızı öldürüyorlar.
        Will: Eğer onlar gibi olursak bizde onlardan farkımız kalmaz. 
        {ad} Will'e hak verdi ve sesiz kalmayı tercih etti. Will cesedi taşımak için atları getirdi ceset o kadar büyüktü ki iki at anca taşıyabiliyordu. 
        Will ve {ad} cesedi Vargun Kalesi'ne götürdüler ve Lord Baldwin'a teslim edip olan bitenianlattılar. Baldwin onlara tekrardan hürmetlerini gösterip 
        anlaştıklarından fazla bir para ödeyip onları uğurladı. Will ve {ad} meydana indiler. \n
        """
        self.bolum3metin3 = f"""
        Will {ad} daki tedirginliği anlayınca ona dönüp. Buradan uzaklaşıyoruz. {ad} kararı hiç ikiletmeden sesizce devasa orkdan kaçar şekilde uzaklaşmaya başladılar.\n
        """

        self.bolum3metin4 = f"""
        {ad} ve Will devasa orkun yanına gitmek için tekrardan hazırlandılar bu sefer kararlıydılar o orku öldüreceklerdi. {ad} ve Will orkun yanına vardıklarında ork 
        yerde uzanmış uyuyordu ve onları farketmemişti. 
        Will: Fırsat varken acıssız bir şekilde öldürelim diye söyledi 
        {ad} ve Will yavaşça orka doğru ilerlerken orkun aslında uyumadığını sadece onları kandırdığınıfarkettiler Will ve {ad} orka karşı silahlarını 
        hızlıca çektiler.\n
        """

        self.bolum3metin5 = f"""
        Will: kordineli bir şekilde saldırmamız gerekiyor. Beni takip et ve benimle beraber ters bir şekilde savaş ben oyalarken fırsatları kaçırma ve saldır.
        Dikkatli ol sakın yem olma.
        """

    def bolum2(self,ad,silah_isim):
        self.bolum2metin = f"""
        Will Kale Meydanında {ad}'ın yanına geldi. {ad} bir anda ürperdi çünkü Willi ne duymuştu ne de hissetmişti. Will {ad}'a dönüp.
        Will: Bize iş çıktı Tritonas Kalesi'nin lordu bize kale civarında bir kaç tane orkun saldırıya geçtiğini söyledi. Bende onları avlamak için 
        yola çıkacağım geliyormusun? 
        {ad}: Şakamı yapıyorsun tabi ki geliyorum.
        Will genelde işlere çıkarken {ad}'ı götürmezdi. {ad} Will ile olan macerasına devam etmek istiyordu çünkü onun yanındayken hiç olmadığı kadar
        huzurluydu ve onunla olan bağının güçlendiğini hissediyordu. Bir kaç saat sonra yola çıkmak için hazırlıklarını yaptılar ve Tritonas Kalesi'ne doğru
        yola koyuldular.
        ...
        ...

        Bir kaç gün sonra Tritonas Kalesi'ne vardılar. Lord onları karşıladı ve onların yol yorgunluğunun üzerinden atmaları için kalede bir oda ayarlattı.
        Odaları hazırlanırken {ad} ve Will'e civardaki orkları anlatmaya başladı. Lord onlara bir kaç kez köy halkının orklar tarafından saldırıya uğradığını
        ve bir kaç köylünün hayatını kaybettiğini anlattı. Lord bir kaç kere orkları avlamak için askerlerini gönderdiğini ama hiç birinin geri dönmediğini anlattı.
        Will ve {ad} her kısmını dikkatlice dinledikten sonra müsade isteyip odalarına çekildiler. Ertesi gün gün doğumasına bir kaç saat kala Will {ad}'ı uyandırdı
        ve yola koyuldular. {ad} ve Will orkları avlamak için Lordun dediği yere vardılar ama etrafta ork namına hiç bir iz yoktu ve {ad} ayrılıp orkları aramak için
        dağılmaları önerisini sundu. 
        Will: Bu çok tehlikeli olur.
        {ad}: Ne de olsa ilk orkumu yendim ve bir sürü antreman yaptım sorun olacağını düşünmüyorum" dedi. Will {ad}'a bakıp istemese de önerisini kabul etti.
        {ad} ve Will ayrıldılar. {ad} bir süre yürüdükten sonra yerde ayak izleri gördü ama bu izler geçen gördüğü orkun izlerine benzemiyordu. {ad} izleri 
        takip etmeye başladı ve bir süre sonra bir orkun cesedine rastladı. {ad} cesedi inceledi ve bir kaç yara izi gördü. {ad} cesedi inceledikten son ra
        ayak izinin bu orka ait olmadığını gördü. Düşünceler beyninde çalkalanırken yoluna devam ediyordu yolda giderken kan izleri ve deri parçaları görmüştü.
        bu geyik derisiydi. İleride bir tepe vardı izler o tarafa doğru gidiyordu. Ormanlık alanda tepeye doğru yürüdü ve tepeye vardığında aşağıda iki ork vardı.
        Orklar geyiği parçalamış yiyorlardı. {ad} sesizce geriye çekilip Will'e haber vermeye gidecekken bir dal parçasını ezdi çıkan sesden dolayı orklar {ad}'a
        bakmasına sebep oldu. {ad} artık orklar ile karşı karşıya kalmıştı ve ne yapacağını düşünmeye başladı. \n
        """

        self.bolum2metin2 = f"""
        {ad}  orklara karşı savaşırken kan ter içinde kalmıştı. Orkların gücü karşısında çok zorlanmıştı ve her yerinden kanlar akıyordu. {ad} artık sonun geldiğini
        düşünüyordu orklardan biri yere düşmüştü diğeri de düşecek gibiydi. Son bir darbe daha vurduktan sonra ork yere düşmüştü. Kanter içinde kalan {ad} yere yığıldı
        ve nefes nefese kalmıştı. {ad} bir kaç dakika boyunca daha yerde kaldıktan sonra ayaklanmak için davrandı ama bir ses yüzünden yerdeki orka baktı ork hala canlıydı. 
        {ad} artık ölüceğine emindi çünkü hiç takati kalmamıştı. Gözlerini kapadı ve son nefesini vermeden önce doğayı dinlemek istedi. Ama havayı yaran bir ıslık sesi 
        duydu. {ad} gözlerini açtığında ona nerdeyse 2 adım uzaklıktaki orkun kafasına ok yediğini gördü bir anda ork yere yığıldı. {ad} olan bitene anlam veremedi ve 
        etrafına bakınmaya başladı. Will bir çalının arasından çıkıp ona doğru yürüyordu. Elini {ad}'a uzattı ve kaldırdı. {ad} Will'e dönüp.
        {ad}: Geç kaldın.
        Will: Eğer geç kalsaydım şuan da yerde yatan sen olurdun.
        {ad} Will'in iğneleyici laflarına bile takılmadan sevinip ona sarıldı. Gözlerinden yaşlar akıyordu.
        {ad}: Bir an öleceğimi düşündüm.
        Will {ad}'a dikkatsizliğin yüzünden ölecektin az kalsın dedi. {ad} dolu gözlerle nasıl buldun beni diye sordu. Will
        Will: Tüm ormanda savaşınızın sesi yaankılanıyordu.
        Kısa süreli sesizlik sonrası {ad}'ın korkusu yavaş yavaş geçmeye başladı. 
        {ad}: Will orklar genelde tek gezmezlermi? 
        Will: Evet, bunlar çifleşme döneminde olan orklardır.Bu yüzden birliktelerdi orklar bu dönemlerde çok hırçın ve saldırgan olurlar.
        Will atları getirip orkların birini kendi attına diğerini {ad}'ın atına bağladı  ve {ad}'a dönüp Tritonas Kalesine geri dönelim dedi. 
        Will ve {ad} Tritonas Kalesine geri döndüklerinde ücretlerini alıp tekrardan Vargun Kalesine doğru yola çıktılar. \n
        """

        self.bolum2metin3 = f"""
        {ad} orklara bakıp bu orkları yenemeyeceğini düşündü ve kaçmaya karar verdi. {ad} kaçmaya başladı ama orklar onun hemen arkasından ona doğru koşuyordu. dar 
        yollardangeçerek orkları atlatmaya çalıştı. Bir kaç dakika sonra orku atlatmayı başardı ve ormanın derinliklerine doğru koşmaya başladı. Will'i en son bıraktığı 
        yere doğru koşmaya başladı. Will'i bulduğunda ona olanları anlattı ve Will {ad}'a dönüp.
        Will: iki orku yenebilecek güçte değiliz şuan.
        {ad} ve Will atlarına doğru sesizce gitmeye başladılar ve yollarını Vargun Kalesine doğru çevirdiler. \n
        """

        self.bolum2metin4 = f"""
        {ad} ve Will orkları en son gördükleri yere doğru gitmeye başladılar. Ormanda ilerlerken {ad} Will'e dönüp sol tarafında ölü geyik yiyen orkları gördüğünü
        söyleyecekti ama Will çoktan o tarafa doğru bakıyordu. Karar zamanıydı.\n
        """

        self.bolum2metin5 = f"""
        {ad}'ın orklara karşı nasıl saldıracağını çözmesi gerekiyordu ama bunun için fazla zamanı yoktu ve orklar ona doğru geliyordu. {ad} hızla {silah_isim} çekti 
        artık hayatı için savaşmak zorundaydı.
        """

    def bolum1(self,ad,silah_isim):
        #bolum1
        self.bolum1metin = f""" 
        Kısa süreli dinlenmeden sonra Will ve {ad} yola koyuldular. Will ilerideki ormanda orkların göründüğüne daire bir işaretler 
        olduğunu söyledi. {ad} o sırada etrafa göz gezdiriyordu. {ad} Will'e dönüp neden orkları avlıyorsun diye sordu.
        Will: Geçimimi böyle karşılıyorum.
        {ad} bir süre düşündü ve sonra Will'e dönüp.
        {ad}: Paranı nasıl kazanıyorsun ki?
        Will: Orkların cesetleri değerlidir tabi bununn yanı sıra lordlar ve krallar dan aldığım ödemeler de var.
        {ad}: Ödeme derken neyi kastedin?
        Will: Şöyleki ben onların kalelerini orklardan korurum onlar da bana bunun karşılığında ücret öder. 
        Will yerinde durup etrafa bakmaya başladı. ve {ad}'a dönüp sesiz kalması için işaret etti. {ad} olanlara anlam veremedi 
        çünkü ne bir ses duymuştu ne de birini görmüştü. Will etrafına bakınırken kılıcını çekti ve {ad}'a dönüp tetikte ol buradalar.
        {ad} hemen silahı {silah_isim} çekti ve etrafına bakınmaya başladı. Birden etrafta bir gürültü duyuldu ve bir ork bir anda 
        ağaçların arasından çıktı. Will ve {ad} artık bir seçim yapmak zorundalardı. \n
        .... \n
        """

        self.bolum1metin1 = f""" 
        Will ve {ad} geçen sefer karşılarına çıkan orku avlamak için tekrar ormana doğru yola koyuldular. Ormanda ilerlerken {ad} tanıdık bir ses duydu.
        {ad}: Will sanırım burada.
        Will aferin doğru tahmin dedi. Karşılarına tekrardan çıkan iri kıyım ork geçen seferki kaçışlarındaki gibi bir daha kaçmaları için izin vermeyecek 
        gibi bakıyordu onlara \n
        """

        self.bolum1kacis = f""" 
        Will {ad}'a dönüp kaç dedi. Bu sefer {ad} kaçmamak için direnmedi ve atına binmek için hızla koşmaya başladı. O sırada ork onlara doğru koca bir kaya 
        fırlattı kaya {ad}'a doğru geliyordu. Will {ad}'ı korumak için üzerine atlayıp {ad} 'ı itti. Yerde yuvarlanan {ad} kayanın altında kanlar içinde yatan
        son nefesini veren Will'e bakıyordu. Dehşet içerisinde bakarken ayak sesleri duydu. Arkasına döndüğünde orkun ona doğru geldiğini gördü. Kaçmaya çalışsa da
        ork onu yakaladı ve korku içerisinde bağıran {ad}' ın kafasını ısırdı. 
        ....  \n
        """

        self.bolum1metin2 = f"""
        Will {ad}'a dönüp kaç dedi. {ad} Will'e bakıp kaçmak istemediğini söyledi. Will {ad}'ı kollarına alıp ata bindirdi 
        ve kaçmaya başladılar. ork peşlerine düşmüşdü. Will {ad}'a dönüp şuan da bunu yenebilecek güçte olmadıklarını söyledi.
        ve atı hızla Vargun Kalesine doğru sürdü. {ad} ne kadar kendini Will'e kanıtlamaya çalışsa da korktuğunu hissetmişti.
        Will Kale kapısı görününce atı yavaşlattı ve {ad}'ı yere indirdi. 
        Will: Eğer böyle kaçtığını görürlerse seninle çok dalga geçerler.
        {ad} somurtgan bir suratla Will'le beraber Kale meydanına kadar yürüdü.
        """

        self.bolum1metin3 = f"""
        Will:Korkuyormusun {ad}? 
        {ad}: Benmi korkuyorum? HAHA güldürme beni.
        Will gizlice gülümsedi.
        Will: O zaman hadi orku avlayalım.
        {ad} Will'e bakıp başını onaylarcasına salladı.
        """

        self.bolum1metin4 = f"""
        Will {ad}'a dönüp aferin ilk orkunu yendin dedi. {ad} Will'e bakıp 
        {ad}: Bunu sana borçluyum.  
        Will: Ben sürekli yanında olmayacağım bu yüzden kendini geliştirmelisin.
        {ad} Will'e bakıp onaylarcasına kafasnı salladı.{ad} Will'e bağlarının arttığını hissediyordu sanki aralarındaki bağ yolda karşılaşan 
        iki yabancıdan daha fazlasıydı sanki baba ve oğul gibiydiler.  
        Will: Bu kadar derin ne düşünüyorsun?  
        {ad} bi an afalladı sanki Will'in içinden geçenleri okumuş gibiydi.
        {ad}: H-Hiçbir şey düşünmüyorum.
        Bu sırada Will orkun cesedini bir iple atının arkasına bağlıyordu.
        Will: Orku avladığımıza göre bu cesedi satmak için ve ödülümüzü almak için kaleye geri dönelim.
        Bu sırada {ad} Will ile yaşadıklarını düşünüyodu ve hep beraber olmaları için dua ediyordu. \n
        """

a = oyun()

