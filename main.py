############################################################################################
#                                      KÜTÜPHANELER                                        #
############################################################################################

import pygame
import pygame.freetype
import pygame.mixer
import sys
import os
import random
import time
pygame.init()
pygame.mixer.init()

pygame.display.set_caption("Son Ork Avcısı")
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, 'images')
sound_path = os.path.join(current_dir, 'sounds')

############################################################################################
#                                       TANIMLAMALAR                                       #
############################################################################################

townCenterMenu = ["Şifahane", "Hana Git", "Maceraya Atıl", "Ana Menüye Dön" , "Kamp Alanı"]
campMenu = ["Kamp Ateşinin Başında Sohbet Et", "Nehirde Yıkan", "Uyu", "Meydana Dön"]
sifahaneMenu = ["Şifacıdan yaralarını sarmasını iste", "Şifacıdan merhem yapıp sürmesini iste", "Şifacıdan İlaç al", "Şifacıdan pekmez al", "Meydana Dön"]
hanMenu = ["Yiyecek satın al ve ye", "İçecek satın al ve eğlen", "Güreş", "Meydana Dön"]
maceraMenu = ["Yakın çevreden şifalı bitki topla ve avlan", "Hikaye", "Meydana Dön"]
settingsMenu = ["Tam Ekran", "Ses", "Altyazı Boyutu", "Ana Menüye Dön"]
mainMenu = ["Oyunu Başlat", "Ayarlar", "Çıkış"]
weapon_get = ["Kılıç", "Mızrak", "Balta"]
maceraSavasMenu = ["Savaş", "Kaç"]
fightMenu = ["Hafif Saldırı", "Ağır Saldırı", "Pot iç"]
exitMenu = ["Ana Menüye Dön", "İptal"]
willİknaMenu = ["Will'i İkna Et", "İkna Etme"]
chapter4Menu = ["Kurtulmaya Çalış"]
chapter4Menu1 = ["savaş", "SAVAŞ"]
chapter4Menu2 = ["Press F to pay respects"]

WIDTH = 1280
HEIGHT = 720
FONT_SIZE = 32
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (30, 30, 30)
DELAY = 30
FAST_DELAY = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, FONT_SIZE)
settings = {"Tam Ekran": False, "Ses": 50, "Altyazı Boyutu": "Küçük"}
size_mapping = {"Küçük": 30, "Orta": 40, "Büyük": 50}
subtitle_size = size_mapping[settings["Altyazı Boyutu"]]
subtitle_font = pygame.font.Font(None, subtitle_size)
sira = "player"
show_message = False
message_start_time = 0
display_time = 2000
message_text = ""
basarim1 = 0
basarim2 = 0
chapter = 0
kac = 0
dead_check = 0
ses = 0.5
fight_status = 0
iknaEtme = 0

############################################################################################
#                                          CLASSLAR                                        #
############################################################################################

class Karakter():
    def __init__(self, İsim, Can, Güç, Çeviklik, Dayanıklılık):
        self.İsim = İsim
        self.Can = Can
        self.Güç = Güç
        self.Çeviklik = Çeviklik
        self.Dayanıklılık = Dayanıklılık

class Player(Karakter):
    def __init__(self, İsim, Silah, Can, Açlık, Hijyen, Para, Eğlence, Uyku, XP, Güç, Çeviklik, Dayanıklılık, Toplama, Mana, Pot, BeceriPuani):
        super().__init__(İsim, Can, Güç, Çeviklik, Dayanıklılık)
        self.Silah = Silah
        self.Açlık = Açlık
        self.Hijyen = Hijyen
        self.Para = Para
        self.Eğlence = Eğlence
        self.Uyku = Uyku
        self.XP = XP
        self.Toplama = Toplama
        self.Mana = Mana
        self.Pot = Pot
        self.BeceriPuani = BeceriPuani

player = Player("", "", 100, 100, 100, 100, 100, 100, 0, 7, 7, 7, 7, 100, 0, 0)

statusBar = {"Can": player.Can, "Açlık": player.Açlık, "Hijyen": player.Hijyen, "Para": player.Para, "Eğlence": player.Eğlence, "Uyku": player.Uyku, "XP": player.XP, "Mana": player.Mana, "Güç": player.Güç, "Çeviklik": player.Çeviklik, "Dayanıklılık": player.Dayanıklılık, "Toplama": player.Toplama, "Pot": player.Pot}

############################################################################################
#                                        GÖRSELLEŞTİRMELER                                 #
############################################################################################

def create_menu(menuName):
   for event in pygame.event.get():
       if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for i, option in enumerate(menuName):
               if menuName == townCenterMenu or menuName == campMenu or menuName == sifahaneMenu or menuName == hanMenu or menuName == maceraMenu:
                   if i >= 2 and i < 4:
                       if (HEIGHT / 10 + (i-2) * 600 - 50) <= y <= (HEIGHT / 10 + (i-2) * 600 + 50) and (WIDTH / 5 - 125) <= x <= (WIDTH / 5 + 25):
                           return option
                   elif i < 2:
                       if (HEIGHT / 4 + i * 250 - 50) <= y <= (HEIGHT / 4 + i * 250 + 80) and (WIDTH / 2 - 75) <= x <= (WIDTH / 2 + 75):
                           return option
                   elif i == 4:
                       if (HEIGHT / 4 + 130) <= y <= (HEIGHT / 4 + 210) and (WIDTH / 2 + 325) <= x <= (WIDTH / 2 + 475):
                           return option

               elif (((HEIGHT / 2) - 20 + (i * 50)) <= y <= ((HEIGHT / 2) + 33 + (i * 40)) and ((WIDTH / 2) - 50) <= x <= ((WIDTH / 2) + 75)):
                    return option
                       
def draw_text(text, x, y, color=(255, 255, 255), font=font, bg_color=None):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    
    if bg_color:
        padding = 5
        bg_surface = pygame.Surface((text_rect.width + padding * 2, text_rect.height + padding * 2), pygame.SRCALPHA)
        bg_surface.fill((*bg_color, 128))
        bg_rect = bg_surface.get_rect(center=(x, y))
        screen.blit(bg_surface, bg_rect.topleft)

    screen.blit(text_surface, text_rect)

def Cursor(menuName):
    x, y = pygame.mouse.get_pos()
    for i, option in enumerate(menuName):
        if menuName in [townCenterMenu, campMenu, sifahaneMenu, hanMenu, maceraMenu]:
            if i >= 2 and i < 4:
                color = (255, 255, 0) if (HEIGHT / 10 + (i-2) * 600 - 50) <= y <= (HEIGHT / 10 + (i-2) * 600 + 50) and (WIDTH / 5 - 125) <= x <= (WIDTH / 5 + 25) else WHITE
                draw_text(option, WIDTH / 5 - 50, HEIGHT / 10 + (i-2) * 600, color, bg_color=(0, 0, 0))
            elif i < 2:
                color = (255, 255, 0) if (HEIGHT / 4 + i * 250 - 50) <= y <= (HEIGHT / 4 + i * 250 + 80) and (WIDTH / 2 - 75) <= x <= (WIDTH / 2 + 75) else WHITE
                draw_text(option, WIDTH / 2, HEIGHT / 4 + i * 250, color, bg_color=(0, 0, 0))
            elif i == 4:
                color = (255, 255, 0) if (HEIGHT / 4 + 130) <= y <= (HEIGHT / 4 + 210) and (WIDTH / 2 + 325) <= x <= (WIDTH / 2 + 475) else WHITE
                draw_text(option, WIDTH / 2 + 400, HEIGHT / 4 + 180, color, bg_color=(0, 0, 0))
                
        else:
            color = (255, 255, 0) if (((HEIGHT / 2) - 20 + (i * 50)) <= y <= ((HEIGHT / 2) + 33 + (i * 40)) and ((WIDTH / 2) - 50) <= x <= ((WIDTH / 2) + 75)) else WHITE
            draw_text(option, (WIDTH / 2), ((HEIGHT / 2) + (i * 50) + 10), color, bg_color=(0, 0, 0))

        if option in settings:
            draw_text(str(settings[option]), WIDTH / 2 + 150, ((HEIGHT / 2) + ((i * 50) + 10)), bg_color=(0, 0, 0))
            draw_text("ALTYAZILAR BU ŞEKİLDE GÖZÜKECEK", WIDTH / 2, HEIGHT - 100, color=(255, 255, 255), font=subtitle_font, bg_color=(0, 0, 0))

def status_bar(): 
    global ses
    if fight_status == 0:
        for i, (option, value) in enumerate(statusBar.items()):
            if i < 4:
                draw_text(f"{option}: {value:.0f}", WIDTH / 2 + ((i+1) * 130) + 50, HEIGHT / 5 - 120, WHITE, pygame.font.Font(None, 24),bg_color=(0, 0, 0))
            elif i >= 4 and i < 8:
                draw_text(f"{option}: {value}", WIDTH / 2 + ((i-3) * 130) + 50, HEIGHT / 5 - 90, WHITE, pygame.font.Font(None, 24),bg_color=(0, 0, 0))
            elif i >= 8 and i < 12:
                draw_text(f"{option}: {value}", WIDTH / 2 + ((i-7) * 130) + 50, HEIGHT / 5 - 60, WHITE, pygame.font.Font(None, 24),bg_color=(0, 0, 0))
            else:
                draw_text(f"{option}: {value}", WIDTH / 2 + ((i-11) * 130) + 60, HEIGHT / 5 - 30, WHITE, pygame.font.Font(None, 24),bg_color=(0, 0, 0))

        if player.BeceriPuani > 0:
            draw_text(f"BECERİ PUANINIZ YETENEK YÜKSELTMESİ İÇİN YETERLİDİR. İSTEDİĞİNİZ 3 YETENEĞE TIKLAYARAK YÜKSELTEBİLİRSİNİZ.", 700, HEIGHT / 5 - 30, WHITE, pygame.font.Font(None, 24), bg_color=(0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    for i, (option, value) in enumerate(statusBar.items()):
                                if i >= 8 and i < 10:
                                    if (60) <= y <= (105) and (790 + (i - 8) * 100) <= x <= (865 + (i - 8) * 100):
                                        change_attribute(player,option, 1, "add")
                                if i >= 10 and i < 12:
                                    if (60) <= y <= (105) and (1020 + ((i - 10) * 100 + 50)) <= x <= (1150 + (i - 10) * 100):
                                        change_attribute(player,option, 1, "add")
    else:
        for i, (option, value) in enumerate(statusBar.items()):
            if i == 0:
                draw_text(f"{option}: {value:.0f}", WIDTH / 2 + 350, HEIGHT / 5 - 120, WHITE, pygame.font.Font(None, 24),bg_color=(0, 0, 0))
            if i == 7:
                draw_text(f"{option}: {value:.0f}", WIDTH / 2 + 450, HEIGHT / 5 - 120, WHITE, pygame.font.Font(None, 24),bg_color=(0, 0, 0))
            if i == 12:
                draw_text(f"{option}: {value:.0f}", WIDTH / 2 + 550, HEIGHT / 5 - 120, WHITE, pygame.font.Font(None, 24),bg_color=(0, 0, 0))
    
def get_name():
    clock = pygame.time.Clock()
    input_box = pygame.Rect(540, 300, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    font = pygame.freetype.Font(None, 32)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                        text = text.capitalize()
        
        screen.fill((30, 30, 30))
        draw_text("İSMİNİZİ GİRİNİZ", 620, 280)
        txt_surface, _ = font.render(text, (255, 255, 255))
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)

def change_attribute(who, attribute, amount, type):
    global message_text, show_message, message_start_time

    if who.__dict__[attribute] < 100:
        if type == "add" and (attribute == "Can" or attribute == "Açlık" or attribute == "Hijyen" or attribute == "Para" or attribute == "Eğlence" or attribute == "Uyku" or attribute == "XP" or attribute == "Mana" or attribute == "Pot"):
            who.__dict__[attribute] += amount
            if who.__dict__[attribute] > 100:
                who.__dict__[attribute] = 100
            if who.XP >= 100:
                who.BeceriPuani = 3
                who.XP -= 100
                statusBar["XP"] = who.__dict__["XP"]
                pygame.mixer.music.load(sound_path + '/levelup.ogg')
                pygame.mixer.music.set_volume(ses)
                pygame.mixer.music.play(1)

        elif type == "add" and (attribute == "Güç" or attribute == "Çeviklik" or attribute == "Dayanıklılık" or attribute == "Toplama"):
            if who.BeceriPuani > 0:
                who.__dict__[attribute] += amount
                who.BeceriPuani -= 1
    else:
        if who.__dict__[attribute] + amount > 100:
                who.__dict__[attribute] = 100
    if type == "sub":
        who.__dict__[attribute] -= amount
    elif type == "overwrite":
        who.__dict__[attribute] = amount
    statusBar[attribute] = who.__dict__[attribute]

def dead():
    global player, dead_check,ses
    screen.fill((30, 30, 30))
    if basarim1 == 1:
        draw_text(f"Tebrikler Gizli Bir Başarım Açtınız: ULTRA KORKAK", WIDTH // 2, HEIGHT // 2, WHITE, font, bg_color=BLACK)
        sound = pygame.mixer.Sound(sound_path + '/Victory1.ogg')
        sound.play(1)
        pygame.display.flip()
        time.sleep(5)
        pygame.quit()
        sys.exit()
    elif basarim2 == 1:
        draw_text(f"Tebrikler ALTERNATİF SON'a ulaştınız.", WIDTH // 2, HEIGHT // 2, WHITE, font, bg_color=BLACK)
        sound = pygame.mixer.Sound(sound_path + '/Victory1.ogg')
        sound.play(1)
        pygame.display.flip()
        time.sleep(5)
        pygame.quit()
        sys.exit()
    elif player.Can <= 0 or player.Açlık <= 0 or player.Uyku <= 0:
        draw_text(f"Öldünüz.", WIDTH // 2, HEIGHT // 2, WHITE, font, bg_color=BLACK)
        pygame.display.flip()
        change_attribute(player, "Para", 0, "overwrite")
        change_attribute(player, "Can", 100, "overwrite")
        change_attribute(player, "Açlık", 100, "overwrite")
        change_attribute(player, "Hijyen", 100, "overwrite")
        change_attribute(player, "Eğlence", 100, "overwrite")
        change_attribute(player, "Uyku", 100, "overwrite")
        change_attribute(player, "Mana", 100, "overwrite")
        change_attribute(player, "Pot", 0, "overwrite")
        pygame.mixer.music.stop()
        dead_check = 1
        time.sleep(4)
        town_center()

def metin_yazdirma(metin, background):
    paragraphs = metin.split('\n')
    lines = [line.strip() for paragraph in paragraphs for line in paragraph.split('\n')]
    line_count = len(lines)

    current_line = 0
    current_char = 0

    pygame.time.set_timer(pygame.USEREVENT, DELAY)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                screen.fill(BLACK)
                screen.blit(background, (0, 0))

                draw_text(lines[current_line][:current_char+1], WIDTH / 2, HEIGHT - 100, color=(WHITE), font=subtitle_font, bg_color=(0, 0, 0))
                pygame.display.flip()
                current_char += 1
                if current_char > len(lines[current_line]):
                    current_char = 0
                    current_line += 1
                    if current_line >= line_count:
                        time.sleep(2)
                        return True
                        
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.time.set_timer(pygame.USEREVENT, FAST_DELAY)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    pygame.time.set_timer(pygame.USEREVENT, DELAY)

############################################################################################
#                                          BÖLÜMLER                                        #
############################################################################################

def chapter0():
    global basarim2,ses
    background = pygame.image.load(image_path + '/chapter0.png') 
    background = pygame.transform.scale(background, (1280, 720))
    player.İsim = get_name()
    screen.fill((30, 30, 30))
    while True:
        Cursor(weapon_get)
        option = create_menu(weapon_get)
        if player.Silah == "":
            if option == "Kılıç" or option == "Mızrak" or option == "Balta":
                player.Silah = option
        else:
            pygame.mixer.music.load(sound_path + '/xxx.ogg')
            pygame.mixer.music.set_volume(ses)
            pygame.mixer.music.play(-1)
            chapter0_metin = f"Ork avcısı: Yerdeki cesetleri kontrol ediyordu. \n Kanlar içerisinde, cılız bir çocuğu farketti. \n Diğer cesetlerin aksine üzerinde hiçbir yara izi yoktu. \n Eğilerek vücudu kontrol etti ve yaşadığını farketti. \n Ayağa kalkarak, Hey! Kalkabilirsin orklar etrafımızda yoklar dedi. \n {player.İsim} tek gözünü açıp etrafı kontrol eden cılız çocuk bir anda ayağa fırlayarak avcıya baktı. \n {player.İsim}: Ah o iğrenç yaratıklar. \n Elini uzatıp ben {player.İsim} dedi. \n Avcı: Somurtkan bir surat ile hıh diyip diğer cesetlere doğru yürümeye başladı. \n Aralarından kurtulmayı nasıl başardın diye sordu. \n {player.İsim}: İsmini söylersen belki sana anlatırım. \n Will: Benim adım Will. \n {player.İsim}: Ah Will, memnun oldum. \n İşin gerçeği cesedlerden birinin kanını kendi üzerime sürerek ölü taklidi yaptım. \n Bu sırada üstündeki kanı temizleyip {player.Silah} yerden aldı. \n {player.İsim}'ın gidecek yeri yoktu ve aklından Will'e katılabileceği geçti. \n {player.İsim} kendini toparlayıp: Hey Will seninle gele... \n Will: Hayır! {player.İsim}'ın sözünü keserek."
            metin_start = metin_yazdirma(chapter0_metin, background)
            if metin_start:
                while True:
                    Cursor(willİknaMenu)
                    option = create_menu(willİknaMenu) 
                    if option == "Will'i İkna Et":
                        chapter0_metin_2 = f" {player.İsim}: Lütfen gidecek hiç bir yerim yok kimsem kalmadı. \n Will: Benim yolculuğum tehlikelidir. \n {player.İsim} Benim için tehlikeli bir şey yok. \n Will somurtarak da olsa kabul etti. \n Will ve {player.İsim} macerası burada başladı."
                        metin_start = metin_yazdirma(chapter0_metin_2, background)
                        if metin_start:
                            background = pygame.image.load(image_path + '/Castle.png')  
                            background = pygame.transform.scale(background, (1280, 720))  
                            chapter0_metin_1 = f"Will ve {player.İsim} uzun bir yolculuktan sonra Vargun kalesine vardılar. \n Will: İşte burası Vargun kalesi. \n Will: Burada biraz dinlenelim ve sonra yola devam ederiz."
                            metin_start = metin_yazdirma(chapter0_metin_1, background)
                            if metin_start:
                                pygame.mixer.music.stop()
                                town_center()
                    elif option == "İkna Etme":
                        background = pygame.image.load(image_path + '/teklifight.png') 
                        background = pygame.transform.scale(background, (1280, 720))
                        chapter0_metin_3 = f"Will: Benim yolculuğum tehlikelidir. \n {player.İsim}: Benim için tehlikeli bir şey yok. \n Will: Benimle gelmek istemiyorsan git. \n {player.İsim} yalnız kalmak istemiyordu ama Will'in ona ihtiyacı yoktu. \n {player.İsim} yalnız başına yola koyuldu. \n {player.İsim} ormanda yürürken bir ork sürüsüne rastladı. \n {player.İsim} orkların arasından kaçmaya çalıştı ama orklar onu yakaladı. \n {player.İsim} orkların elindeyken bir ork ona yaklaştı ve kafasını ısırdı. \n {player.İsim} ölmüştü."
                        metin_start = metin_yazdirma(chapter0_metin_3, background)
                        if metin_start:
                            basarim2 = 1
                            dead()
                    pygame.display.flip()
        pygame.display.flip()

def chapter1():
    global enemy, message_text, chapter, basarim1, show_message, message_start_time, kac,ses
    background = pygame.image.load(image_path + '/konusurken.png')
    background = pygame.transform.scale(background, (1280, 720))
    
    pygame.mixer.music.load(sound_path + '/yolculuk.ogg')
    pygame.mixer.music.set_volume(ses)
    pygame.mixer.music.play(-1)

    if chapter == 0:
           chapter1_metin1 = f"Kısa süreli dinlenmeden sonra Will ve {player.İsim} yola koyuldular. \n Will ileride ki ormanda ork göründüğüne daire bir işaretler olduğunu söyledi. \n {player.İsim} o sırada etrafa göz gezdiriyordu. \n {player.İsim} Will'e dönüp neden orkları avlıyorsun diye sordu. \n Will: Geçimimi böyle karşılıyorum. \n {player.İsim} bir süre düşündü ve sonra Will'e dönüp. \n {player.İsim}: Paranı nasıl kazanıyorsun ki? \n Will: Orkların cesetleri değerlidir. Aynı zamanda lordlar ve krallardan aldığım ödemelerde var. \n {player.İsim}: Ödeme derken nasıl yani? \n Will: Şöyle ki ben onların kalelerini orklardan korurum onlar da bana bunun karşılığında ücret öder. \n Will yerinde durup etrafa bakmaya başladı. \n {player.İsim}'a dönüp sesiz kalması için işaret etti. \n {player.İsim} olanlara anlam veremedi çünkü ne bir ses duymuştu ne de birini görmüştü. \n Will etrafına bakınırken kılıcını çekti ve {player.İsim}'a dönüp tetikte ol dedi. \n {player.İsim} hemen {player.Silah} çekti ve etrafına bakınmaya başladı. \n Birden etrafta bir gürültü duyuldu ve bir ork ağaçların arasından çıktı. \n Will ve {player.İsim} artık bir seçim yapmak zorundalardı. \n Savaşacaklar mı yoksa kaçacaklar mı?"
           metin_start = metin_yazdirma(chapter1_metin1, background)
           chapter = 1
    if kac == 1:
           chapter1_metin2 = f"Will ve {player.İsim} geçen sefer karşılarına çıkan orgu avlamak için tekrar ormana doğru yola koyuldular. \n Ormanda ilerlerken {player.İsim} tanıdık bir ses duydu. \n {player.İsim}: Will sanırım burada. \n Will: Aferin doğru tahmin. \n Karşılarına çıkan iri kıyım ork bir daha kaçmaları için izin vermeyecek gibi bakıyordu"
           metin_start = metin_yazdirma(chapter1_metin2, background)
            
    if metin_start:
        while True:
            background = pygame.image.load(image_path + '/ikilifight.png') 
            background = pygame.transform.scale(background, (1280, 720))
            screen.blit(background, (0, 0))
            Cursor(maceraSavasMenu)
            option = create_menu(maceraSavasMenu) 
            if option == "Savaş":
                chapter1_metin4 = f"Will: Korkuyor musun {player.İsim}? \n {player.İsim}: Ben mi korkuyorum? HAHA güldürme beni. \n Will gizlice gülümsedi. \n Will: O zaman hadi ork avlayalım. \n {player.İsim} Will'e bakıp başını onaylar gibi salladı."
                metin_start = metin_yazdirma(chapter1_metin4, background)
                if metin_start:
                    pygame.mixer.music.stop()
                    fight()
            elif option == "Kaç":
                if chapter == 1 and kac == 0:
                    background = pygame.image.load(image_path + '/konusurken.png') 
                    background = pygame.transform.scale(background, (1280, 720))
                    chapter1_metin3 = f"Will {player.İsim}'a dönüp kaç dedi. \n {player.İsim} Will'e bakıp kaçmak istemediğini söyledi. \n Will {player.İsim}'ı kollarına alıp ata bindirdi ve kaçmaya başladılar. \n Ork peşlerindeydi. \n Will {player.İsim}'a dönüp şuan da bunu yenebilecek güçte olmadıklarını söyledi. \n Atı hızla Vargun Kalesine doğru sürdü. \n {player.İsim} ne kadar kendini Will'e kanıtlamaya çalışsa da korktuğunu hissetmişti. \n Will kale kapısı görününce atı yavaşlattı ve {player.İsim}'ı yere indirdi. \n Will: Eğer böyle kaçtığını görürlerse seninle çok dalga geçerler. \n {player.İsim} somurtgan bir suratla Will'le beraber kale meydanına kadar yürüdü."
                    metin_start = metin_yazdirma(chapter1_metin3, background)
                    if metin_start:
                        pygame.mixer.music.stop()
                        kac = 1 
                        town_center()
                else:
                    pygame.mixer.music.stop()
                    basarim1 += 1
                    if basarim1 == 1:
                        chapter1_kacis = f"Will {player.İsim}'a dönüp kaç dedi. \n Bu sefer {player.İsim} kaçmamak için direnmedi ve atına binmek için hızla koşmaya başladı. \n O sırada ork onlara doğru koca bir kaya fırlattı. \n Kaya {player.İsim} a doğru geliyordu. \n Will {player.İsim}ı korumak için üzerine atlayıp {player.İsim} ı itti. \n Yerde yuvarlanan {player.İsim} kayanın altında \n kanlar içinde yatan son nefesini veren Will'e bakıyordu. \n Dehşet içerisinde bakarken ayak sesleri duydu. \n Arkasına döndüğünde ork'un ona doğru geldiğini gördü. \n Kaçmaya çalışsa da ork onu yakaladı. \n Korku içerisinde bağıran {player.İsim} ın kafasını ısırdı. \n {player.İsim}ın son nefesi ile ork'un dişleri arasında kalan kafası yere düştü. \n {player.İsim} ölmüştü."
                        metin_start = metin_yazdirma(chapter1_kacis, background)
                        if metin_start:
                            player.Can = 0
                            dead()
                    else:
                        town_center()

            
            if show_message:
                draw_text(message_text, WIDTH // 2, HEIGHT // 2, WHITE, font, bg_color=BLACK)
                current_time = pygame.time.get_ticks()
                if current_time - message_start_time > display_time:
                    show_message = False
    
            pygame.display.flip()

def chapter2():
    global enemy, message_text, chapter, basarim1, show_message, message_start_time, kac,ses, iknaEtme
    background = pygame.image.load(image_path + '/tekkonusma.png') 
    background = pygame.transform.scale(background, (1280, 720)) 
            
    pygame.mixer.music.load(sound_path + '/yolculuk.ogg')
    pygame.mixer.music.set_volume(ses)
    pygame.mixer.music.play(-1)
        
    while True:
        screen.blit(background, (0, 0)) 
        Cursor(maceraSavasMenu)
        option = create_menu(maceraSavasMenu)
        if option == "Savaş":
            if kac == 2:
                if iknaEtme == 0:
                    background = pygame.image.load(image_path + '/tekkonusma.png')  
                    background = pygame.transform.scale(background, (1280, 720))  
                else:
                    background = pygame.image.load(image_path + '/konusurken.png')  
                    background = pygame.transform.scale(background, (1280, 720))
                chapter2_metin4 = f"{player.İsim} ve Will orkları en son gördükleri yere doğru gitmeye başladılar. \n Ormanda ilerlerken {player.İsim} Will'e dönüp sol tarafında ölü geyik yiyen orklar olduğunu söyleyecekti \n ama Will çoktan o tarafa doğru bakıyordu. Karar zamanıydı. \n {player.İsim}'ın orglara karşı nasıl saldıracağını çözmesi gerekiyordu. \n Bunun için fazla zamanı yoktu ve orglar ona doğru geliyordu. \n {player.İsim} hızla {player.Silah} çekti. \n Artık hayatı için savaşmak zorundaydı."
                metin_start = metin_yazdirma(chapter2_metin4, background)
                if metin_start:
                    pygame.mixer.music.stop()
                    fight()
            else:
                pygame.mixer.music.stop()
                fight()
        elif option == "Kaç":
            background = pygame.image.load(image_path + '/teklifight.png')  
            background = pygame.transform.scale(background, (1280, 720))  
            chapter2_metin3 = f"{player.İsim} orklara bakıp bu orgları yenemeyeceğini düşündü ve kaçmaya karar verdi. \n {player.İsim} kaçmaya başladı ama orklar hemen arkasından koşuyordu. \n Dar yollardan geçerek orkları atlatmaya çalıştı. \n Bir kaç dakika sonra atlatmayı başardı. \n Ormanın derinliklerine doğru Will'e koşmaya başladı."
            metin_start = metin_yazdirma(chapter2_metin3, background)
            if metin_start:
                background = pygame.image.load(image_path + '/konusurken.png')  
                background = pygame.transform.scale(background, (1280, 720))  
                chapter2_metin5 = f"Will'i bulduğunda ona olanları anlattı. \n Will {player.İsim}'a dönüp. \n Will: iki orgu yenebilecek güçte değiliz şuan. \n {player.İsim} ve Will atlarına doğru sesizce gitmeye başladılar. \n Yollarını Vargun Kalesine doğru çevirdiler."
                metin_start = metin_yazdirma(chapter2_metin5, background)
                if metin_start:
                    pygame.mixer.music.stop()
                    kac = 2
                    town_center()
        
        if show_message:
            draw_text(message_text, WIDTH // 2, HEIGHT // 2, WHITE, font, bg_color=BLACK)
            current_time = pygame.time.get_ticks()
            if current_time - message_start_time > display_time:
                show_message = False

        pygame.display.flip()

def chapter3():
    global enemy, message_text, chapter, basarim1, show_message, message_start_time, kac,ses
    background = pygame.image.load(image_path + '/Castle.png')  
    background = pygame.transform.scale(background, (1280, 720))  

    pygame.mixer.music.load(sound_path + '/yolculuk.ogg')
    pygame.mixer.music.set_volume(ses)
    pygame.mixer.music.play(-1)

    if kac == 3:
        metin_start = True

    else:
        chapter3_metin1 = f"Son ork avlarından şuana kadar uzun bir zaman geçmişti. \n Will ve {player.İsim} bu sefer Vargun Kalesi Lordu Baldwin'in yanına gitmişlerdi. \n Baldwin ikisi ile selamlaştıktan sonra olayları anlatmaya başladı. \n Etrafta bir kaç ork cesedine rastladıklarını ve \n bu cesetlerin neden kaynaklı öldüğünü anlayamadıklarını söyledi. \n Will ve {player.İsim} bu sefer ork avlamak için iş almamıştı. \n Bu sefer işleri araştırmaydı. \n Will ve {player.İsim} anlatılan yere gittiler."
        metin_start = metin_yazdirma(chapter3_metin1, background)
        if metin_start:
            background = pygame.image.load(image_path + '/konusurken.png')  
            background = pygame.transform.scale(background, (1280, 720))  
            chapter3_metin5 = f"Etrafta ork cesedleri vardı. \n Will bu cesetlerin insanlar veya ork avcıları tarafından avlanılmadığını anlamıştı.\n Will: Bu cesetlerin neden öldüğünü anlamamız gerekiyor. \n {player.İsim} ve Will cesetleri incelemek için yaklaştı. \n Will: Görüyor musun cesetlerin göğüs taraflarında pençe izleri var. \n {player.İsim} cesetleri inceledikten sonra Will'e dönerek. \n  {player.İsim}: Daha fazlası da var. \n O sırada cesetin boynundaki diş izlerini gösterdi. \n Will: Bu cesedler bu orklardan daha güçlü bir şey tarafından öldürüldü \n ve öldüren varlık cesetleri bir araya toplamış. \n Ormanın deriniklerinden gelen ayak seslerini işittiler. \n Will {player.İsim}'ı kolundan tutuğu gibi büyük bir kayanın arkasına götürdü. \n Oradan olan biteni izlemeye çalıştılar. \n Ayak sesleri gittikçe büyüyordu ve yer sarsıntısı artıyordu. \n En sonunda ağaçların ikisini kırarak gelen devasa bir ork çıktı. \n {player.İsim} ork'un büyüklüğü karşısında savaşacaklardı."
            metin_start = metin_yazdirma(chapter3_metin5, background)
            
    if metin_start:
        while True:
            background = pygame.image.load(image_path + '/konusurken.png')  
            background = pygame.transform.scale(background, (1280, 720))  
            screen.blit(background, (0, 0))  
            Cursor(maceraSavasMenu)
            option = create_menu(maceraSavasMenu)  
            if option == "Savaş":
                if kac == 3:
                    chapter3_metin4 = f"{player.İsim} ve Will devasa orgun yanına gitmek için tekrardan hazırlandılar. \n Bu sefer o ork'u öldürmek için kararlıydılar. \n {player.İsim} ve Will ork'un yanına vardıklarında ork yerde uzanmış uyuyordu ve \n onları fark etmemişti. \n Will: Fırsat varken acısız bir şekilde öldürelim. \n {player.İsim} ve Will yavaşça orga doğru ilerlerken ork'un aslında uyumadığını sadece onları kandırdığını fark ettiler. \n Will ve {player.İsim} ork'a karşı silahlarını hızlıca çektiler. \n Will: Koordineli bir şekilde saldırmamız gerekiyor. \n Beni takip et ve benimle beraber ters bir şekilde savaş \n ben oyalarken fırsatları kaçırma ve saldır. \n Dikkatli ol sakın yem olma."
                    metin_start = metin_yazdirma(chapter3_metin4, background)
                    if metin_start:  
                        pygame.mixer.music.stop()       
                        fight()
                else:
                    pygame.mixer.music.stop()
                    fight()
            elif option == "Kaç":
                kac = 3
                chapter3_metin3 = f"Will {player.İsim} daki tedirginliği anlayınca ona dönüp. \n Buradan uzaklaşıyoruz. \n {player.İsim} kararı hiç ikiletmeden sesizce devasa orgdan kaçar şekilde uzaklaşmaya başladılar."
                metin_start = metin_yazdirma(chapter3_metin3, background)
                if metin_start:
                    pygame.mixer.music.stop()
                    town_center()

            
            if show_message:
                draw_text(message_text, WIDTH // 2, HEIGHT // 2, WHITE, font, bg_color=BLACK)
                current_time = pygame.time.get_ticks()
                if current_time - message_start_time > display_time:
                    show_message = False
    
            pygame.display.flip()

def chapter4():
    global enemy, message_text, chapter, basarim1, show_message, message_start_time,ses
    background = pygame.image.load(image_path + '/chapter4_1.png')  
    background = pygame.transform.scale(background, (1280, 720))  
    
    pygame.mixer.music.load(sound_path + '/yolculuk.ogg')
    pygame.mixer.music.set_volume(ses)
    pygame.mixer.music.play(-1)

    chapter4_metin1 = f"{player.İsim} Will'i meydanda otururken gördü. \n Will düşünceli görünüyordu yanına gidip \n Neden bu kadar düşüncelisin dedi. \n Will: Urak orkları genelde bu kadar insanların olduğu yere yaklaşmazlar. \n {player.İsim} umursamaz bir şekilde. \n {player.İsim}: Ne olucak yani biri yaklaştı diye? \n Will'i rahatsız eden başka bir şey vardı. \n {player.İsim}: Hey, ne oldu anlatacak mısın artık? \n Will: Görmediğin şeyler vardı orada. \n Etrafta bir kaç tane kılıç vardı gördün mü? \n {player.İsim} kafasını sallayarak görmediğini ifade etti. \n {player.İsim}: Ork'un öldürdüğü adamlardır ne olacak yani. \n Will: Hayır onlar normal kılıç değillerdi. \n Onlar benim ki gibi birer ork kılıcıydı. \n {player.İsim} şaşırmıştı. \n {player.İsim}: Ork kılıcı mı? \n Will: Evet. Her ork avcısına eğitimi tamamlama şerefine verilir bu kılıçlar. \n  {player.İsim} bunu ilk defa duyuyordu. \n  Will: Eğer o kılıçlar oradaysa sahipleri ölmüştür demektir bu. \n Ama ork avcılarından hiç biri Urak orklarına ölmeyecek kadar tecrübelidir. \n {player.İsim}: Bu ne demek oluyor yani? \n Will: Ben de bilmiyorum gidip öğreneceğim. \n {player.İsim}: Ben de seninle geliyorum. \n Will hiç karşı çıkmadı normalde bu tarz riskli işlere {player.İsim}'ı götürmezdi."
    metin_start = metin_yazdirma(chapter4_metin1, background)
            
    if metin_start:
        background = pygame.image.load(image_path + '/konusurken.png')  
        background = pygame.transform.scale(background, (1280, 720))  
        chapter4_metin2 = f"Ork'u öldürdükleri yere geldiklerinde etrafın temiz olduklarını gördüler. \n Kılıçlar artık yoktu. \n Will: Bu işte bir iş var temkinli ol. \n Etrafta su sesi geliyordu. \n Will ve {player.İsim} su sesine doğru ilerlediler. \n Karşılarında gürül gürül akan bir nehir vardı. \n Will çok tuhaf kokular alıyorum diye uyardı. \n {player.İsim} şaşırmıştı. Çünkü o hiç bir koku almıyordu. \n Will tehtitkar bir şekilde. \n Will: ÇIKIN ORTAYA."
        metin_start = metin_yazdirma(chapter4_metin2, background)
        if metin_start:
            background = pygame.image.load(image_path + '/varuchapter4_2.png')  
            background = pygame.transform.scale(background, (1280, 720))  
            chapter4_metin8 = f"{player.İsim}, Ağaçların arasından aynı Will gibi giyinmiş bir grubun çıktığını gördü. \n Will bu duruma hiç şaşırmamıştı. \n Yabancı: Tekrar karşılaştık eski dostum. \n Will: Seni burada görmek beni şaşırtmadı. \n Ne de olsa ölmemi isteyecek ilk kişi sensin, Varu! \n Varu: Ah neden öyle diyorsun kardeşim ben senin en iyi dostunum. \n Will yere tükürerek ne kadar tiksindiğini gösterdi. \n O sırada {player.İsim} {player.Silah} eline almıştı. \n Varu: Oh bakıyorumda yeni arkadaşlar edinmişsin. \n O sırada yanındaki adamlara el hareketiyle saldırmalarını emretti."
            metin_start = metin_yazdirma(chapter4_metin8, background)
            if metin_start:
                while True:
                    Cursor(chapter4Menu1)
                    option = create_menu(chapter4Menu1)
                    if option == "savaş" or option == "SAVAŞ":
                        chapter4_metin6 = f"Will ve {player.İsim} savunmaya geçtiler. \n Kapana sıkıştırılmış gibiydiler. \n Arkalarında nehir, önlerinde düşman vardı. \n Hepsini öldürmeden burdan canlı çıkmaları imkansızdı. \n {player.İsim} ve Will çarpışırken. \n Will, {player.İsim}'a doğru gelen bir okun önüne atladı ve kolundan yaralandı. \n O sırada fırsattan istifade eden diğer avcılar Will'e kılıç saldırılarında bulundu. \n Bir kaçı tutan kılıçlarla güçsüzleşen Will tek ayak üstüne düşmüştü. \n Varu, Will'e doğru yürüyodu onu korumak isteyen {player.İsim} önüne çıkmak istedi. \n Ama başka bir avcı onu kollarından tuttup kıstırdı."
                        metin_start = metin_yazdirma(chapter4_metin6, background)
                        if metin_start:
                            background = pygame.image.load(image_path + '/varuchapter4_3.png')  
                            background = pygame.transform.scale(background, (1280, 720))  
                            while True:
                                Cursor(chapter4Menu)
                                option = create_menu(chapter4Menu)  
                                if option == "Kurtulmaya Çalış":
                                    chapter4_metin5 = f"{player.İsim} kurtulmaya çalıştı. \n Ancak adam çok iriydi. \n Varu Will'e doğru kılıcını doğrulttu. \n Will arkasını dönüp {player.İsim}'a baktı ve gülümseyerek. \n Will: Bundan sonrası sende küçük dostum. \n O anda Varu kılıç darbesini Will'e indirdi. \n Will kanlar içerisinde yere düştü."
                                    metin_start = metin_yazdirma(chapter4_metin5, background)
                                    if metin_start:
                                        background = pygame.image.load(image_path + '/varuchapter4_4.png')  
                                        background = pygame.transform.scale(background, (1280, 720))  
                                        chapter4_metin9 = f"\n Sevinçli bir şekilde bağıran Varu. \n Varu: Ne oldu Will kim daha iyimiş. \n Diyerek kahkahalar atmaya başladı. \n Adam, {player.İsim}'ı yere indirmişti. \n Varu: Onu da diğerinin yanına gönderin."
                                        metin_start = metin_yazdirma(chapter4_metin9, background)
                                        if metin_start:
                                            background = pygame.image.load(image_path + '/varuchapter4_5.png')  
                                            background = pygame.transform.scale(background, (1280, 720))  
                                            chapter4_metin3 = f"Avcılardan biri {player.İsim}'a kılıcını indirecekken {player.İsim} etrafı yanmaya başladı. \n {player.İsim} ne olduğunu anlamadı sadece duyduğu bir ejderha sesiydi ve etrafı alevler içerisindeydi. \n Varu'nun vücudunun belli kısımları yanmıştı ama hala yaşıyordu. \n Varu: Demek seni bu yüzden yanında tuttu. \n Hep her zaman senin kim olduğunu biliyordu. \n O yüzden kervanı uzaktan takip etti hep. \n Varu: HAHAH--. SEN CİDDEN ONUN İNSAN OLDUĞUNU MU DÜŞÜNDÜNDÜN HE. \n Varu: Demek ejderha soyundan gelen sensin ve se... \n Öksürdü ve kan kusdu. \n Konuşmaya çalışsa da gücü kalmadı ve acı içinde son nefesini verdi."
                                            metin_start = metin_yazdirma(chapter4_metin3, background)
                                            if metin_start:
                                                pygame.mixer.music.stop()
                                                pygame.mixer.music.load(sound_path + '/chapter4_will_dead.ogg')
                                                pygame.mixer.music.set_volume(ses)
                                                pygame.mixer.music.play(-1)
                                                background = pygame.image.load(image_path + '/varuchapter4_6.png')  
                                                background = pygame.transform.scale(background, (1280, 720))
                                                chapter4_metin4 = f" {player.İsim} Will'in cesedini alıp ücra bir yere götürdü. \n Toprağı kazıp Will'i gömdü."
                                                metin_start = metin_yazdirma(chapter4_metin4, background)
                                                if metin_start:
                                                    while True:
                                                        Cursor(chapter4Menu2)
                                                        option = create_menu(chapter4Menu2)
                                                        if option == "Press F to pay respects":
                                                            chapter4_metin7 = f"Will'in kılıcını alıp sırtına yerleştirdi. \n Son bir kere mezarı başında durdu çömelip dua etti. \n O sırada göz yaşları toprağa dökülüyordu. {player.İsim} artık tek başınaydı. \n Will'in kim olduğunu ve asıl önemlisi kendisinin ne olduğunu öğrenmek \n özel gücünü araştırmak ve oradaki kılıçların sahipleri kimler olduğunu öğrenmek için \n yola çıktı........"
                                                            metin_start = metin_yazdirma(chapter4_metin7, background)
                                                            if metin_start:
                                                                pygame.mixer.music.stop()
                                                                game_over()
                                                        pygame.display.flip()
                                pygame.display.flip()
                    pygame.display.flip()
    pygame.display.flip()

############################################################################################
#                                          MEKANLAR                                        #
############################################################################################

def town_center():
    global chapter, dead_check, iknaEtme, ses
    background = pygame.image.load(image_path + '/town_center.png')  
    background = pygame.transform.scale(background, (1280, 720))  

    while True:
        screen.blit(background, (0, 0))  
        if dead_check == 1:
            dead_metin = f"Will: {player.İsim} ne oldu? \n {player.İsim}: Beni orklar yakaladı. \n Will: Beni dinle {player.İsim} sabahtan beri buradayız. Neyden bahsediyorsun? \n {player.İsim}: Beni orklar yakaladı ve öldürdü. \n Will: {player.İsim} seni orklar öldürmedi. \n {player.İsim}: Beni orklar öldürdü. \n Will: {player.İsim} seni orklar öldürmedi. Sen bence hana git ve eğlen. \n {player.İsim} somurtarak tamam dedi."
            metin_start = metin_yazdirma(dead_metin, background)
            if metin_start:
                dead_check = 0
        else:
            Cursor(townCenterMenu)
            option = create_menu(townCenterMenu)  
            status_bar()

            if option == "Şifahane":
                sifahane()
            elif option == "Hana Git":
                han()
            elif option == "Maceraya Atıl":
                if chapter == 2:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(sound_path + '/yolculuk.ogg')
                    pygame.mixer.music.set_volume(ses)
                    pygame.mixer.music.play(-1)
                    background = pygame.image.load(image_path + '/chapter4_1.png')  
                    background = pygame.transform.scale(background, (1280, 720))  
                    chapter2_metin1 = f"Will Kale Meydanında {player.İsim}'ın yanına geldi. \n {player.İsim} bir anda ürperdi çünkü Willi ne duymuştu ne de hissetmişti. \n Will {player.İsim}'a dönüp. \n Will: Bize iş çıktı. Tritonas Kalesi'nin lordu bize kale civarında bir kaç tane ork'un saldırıya geçtiğini söyledi. \n Bende onları avlamak için yola çıkacağım geliyor musun? \n {player.İsim}: Şakamı yapıyorsun tabi ki geliyorum. \n Will genelde işlere çıkarken {player.İsim}'ı götürmezdi. \n {player.İsim} Will ile olan macerasına devam etmek istiyordu. \n Çünkü onun yanındayken hiç olmadığı kadar huzurluydu ve onunla olan bağının güçlendiğini hissediyordu. \n Bir kaç saat sonra yola çıkmak için hazırlıklarını yaptılar ve Tritonas Kalesi'ne doğru yola koyuldular."
                    metin_start = metin_yazdirma(chapter2_metin1, background)
                    if metin_start:
                        background = pygame.image.load(image_path + '/Castle.png')  
                        background = pygame.transform.scale(background, (1280, 720))  
                        screen.blit(background, (0, 0))  
                        chapter2_metin1_2 = f"Bir kaç gün sonra Tritonas Kalesi'ne vardılar. \n Lord onları karşıladı ve onların yol yorgunluğunun üzerinden atmaları için kalede bir oda ayarlattı. \n Odaları hazırlanırken {player.İsim} ve Will'e civardaki orkları anlatmaya başladı. \n Lord onlara birkaç kez köy halkının orklar tarafından saldırıya uğradığını \n ve bir kaç köylünün hayatını kaybettiğini anlattı. \n Lord orkları avlamak için askerlerini gönderdiğini \n ama hiç birinin geri dönmediğini anlattı. \n Will ve {player.İsim} her kısmını dikkatlice dinledikten sonra müsade isteyip odalarına çekildiler. \n Ertesi gün gün doğumasına bir kaç saat kala Will {player.İsim}'ı uyandırdı ve yola koyuldular."
                        metin_start = metin_yazdirma(chapter2_metin1_2, background)
                        if metin_start:
                            background = pygame.image.load(image_path + '/konusurken.png')  
                            background = pygame.transform.scale(background, (1280, 720))  
                            chapter2_metin1_3 = f"{player.İsim} ve Will orkları avlamak için Lord'un dediği yere vardılar \n ama etrafta ork namına hiç bir iz yoktu \n ve {player.İsim} ayrılıp orkları aramak için dağılmaları önerisini sundu. \n Will: Bu çok tehlikeli olur."
                            metin_start = metin_yazdirma(chapter2_metin1_3, background)
                            if metin_start:
                                while True:
                                    Cursor(willİknaMenu)
                                    option = create_menu(willİknaMenu)  
                                    if option == "Will'i İkna Et":
                                        background = pygame.image.load(image_path + '/tekkonusma.png')  
                                        background = pygame.transform.scale(background, (1280, 720))  
                                        chapter2_metin1_4 = f" {player.İsim}: Ne de olsa ilk ork'umu yendim \n ve bir sürü antreman yaptım sorun olacağını düşünmüyorum dedi. \n Will {player.İsim}'a bakıp istemese de önerisini kabul etti. \n {player.İsim} ve Will ayrıldılar. \n {player.İsim} bir süre yürüdükten sonra yerde ayak izleri gördü \n ama bu izler geçen gördüğü orgun izlerine benzemiyordu. \n {player.İsim} izleri takip etmeye başladı \n ve bir süre sonra bir ork'un cesedine rastladı. \n {player.İsim} cesedi inceledi ve bir kaç yara izi gördü. \n {player.İsim} cesedi inceledikten sonra ayak izinin bu ork'a ait olmadığını gördü. \n Düşünceler beyninde çalkalanırken yoluna devam ediyordu. \n Yolda giderken kan izleri ve geyik derisi parçaları görmüştü. \n İleride bir tepe vardı ve izler o tarafa doğru gidiyordu. \n Ormanlık alanda tepeye doğru yürüdü. \n Tepeye vardığında aşağıda iki ork vardı. \n Orklar geyiği parçalamış yiyorlardı. \n {player.İsim} sesizce geriye çekilip Will'e haber \n vermeye gidecekken bir dal parçasını ezdi. \n Çıkan ses orkların {player.İsim}'a bakmasına sebep oldu. \n {player.İsim} artık orklar ile karşı karşıya kalmıştı \n ve ne yapacağını düşünmeye başladı."
                                        metin_start = metin_yazdirma(chapter2_metin1_4, background)
                                        if metin_start:
                                            pygame.mixer.music.stop()
                                            iknaEtme = 0
                                            chapter = 3
                                            chapter2()
                                    elif option == "İkna Etme":
                                        chapter2_metin1_4 = f" {player.İsim}: Evet sen haklısın. \n Will {player.İsim}'ın bu kararından mutluydu. \n {player.İsim} ve Will yürümeye devam ettiler. \n {player.İsim} ve Will bir süre yürüdükten sonra yerde ayak izleri gördü \n ama bu izler geçen gördükleri ork'un izlerine benzemiyordu. \n {player.İsim} ve Will izleri takip etmeye başladılar \n ve bir süre sonra bir ork'un cesedi gördüler. \n {player.İsim} ve Will cesedi inceledi ve bir kaç yara izi gördü. \n Cesedi inceledikten sonra ayak izinin bu ork'a ait olmadığını gördüler. \n Düşünceler beyinlerinde çalkalanırken yolarına devam ediyorlardı. \n Yolda giderken kan izleri ve geyik derisi parçaları görmüşlerdi. \n İleride bir tepe vardı ve izler o tarafa doğru gidiyordu. \n Ormanlık alanda tepeye doğru yürüdüler. \n Tepeye vardıklarında aşağıda iki ork vardı. \n Orklar geyiği parçalamış yiyorlardı. \n {player.İsim} sesizce geriye çekilirken bir dal parçasını ezdi. \n Çıkan ses orkların {player.İsim}'a bakmasına sebep oldu. \n {player.İsim} ve Will artık orklar ile karşı karşıya kalmıştı \n ve ne yapacaklarını düşünmeye başladılar."
                                        metin_start = metin_yazdirma(chapter2_metin1_4, background)
                                        if metin_start:
                                            pygame.mixer.music.stop()
                                            iknaEtme = 1
                                            chapter = 3
                                            chapter2()
                                    pygame.display.flip()
                elif chapter == 5:
                    chapter4()
                else:
                    macera()
            elif option == "Kamp Alanı":
                camp()
            elif option == "Ana Menüye Dön":
                exit_menu()
            pygame.display.flip()

def camp():
    global show_message, message_start_time , message_text,ses
    background = pygame.image.load(image_path + '/Camp.jpg')  
    background = pygame.transform.scale(background, (1280, 720))  

    camp_metin1 = f"Ateşin başında bir yaşlı adam oturuyordu. \n {player.İsim} merhaba dedi. Köylü: Merhaba \n {player.İsim}: Ben {player.İsim} bu arada sizin adınız nedir? \n Walt: Benim adım Walt \n {player.İsim}: Neden buradasınız? \n Walt: Ben burada yaşamımı sürdürüyorum. \n Uzun bir sohbete daldılar. \n Sohbetin ardından {player.İsim} ayağa kalktı ve kendi yoluna devam etti."
    camp_metin2 = f"Ateşin başında bir gurup insan oturup şarkı söylüyorlardı \n {player.İsim} onlara katıldı. \n Fazıl Say'ın Akılla Bir Konuşmam Oldu şarkısını söylüyorlardı. \n Bu zorbalar ne biçim adamlar dedim; \n Kurt, köpek, çakal makal dedi; \n Ne, dersin bu adamlara dedim; \n Yüreksizler, kafasızlar, sosyuzlar dedi; .... \n {player.İsim}: Bu şarkıyı dinlemeyeli uzun olmuştu. \n {player.İsim} ayağa kalktı ve kendi yoluna devam etti."
    camp_metin3 = f"Ateşin başında bir grup insan hararetli bir şekilde konuşuyordu. \n {player.İsim} yanlarına yaklaştı ve ne konuştuklarını dinlemeye başladı. \n Adamlar geçen olan ork baskınından bahsediyordu. \n {player.İsim}: Ben de oradaydım. \n Herkes şaşkın bir şekilde {player.İsim}'a baktı ve biri sordu. \n Köylü: Nasıl yaşamayı becerdin? \n {player.İsim}: Silahımı çıkardım ve onlarla savaştım. \n Bir kaçını öldürmeyi başardım. Sonra diğerleri zaten kaçtı. \n {player.İsim} Ne de olsa kimse benim yalan sölediğimi anlayamaz diye içinden geçirdi. \n Herkes {player.İsim}'a şaşırmış bir şeklide bakıyordu. \n {player.İsim} bir süre daha onlarla sohbet etti. \n Daha sonra saatin ilerlediğini fark ederek ayağa kalktı. \n Kendi yoluna devam etti."
    metin_nehir = f"Alaros nehir kenarına gelen {player.İsim} nehrin serin sularına girdi \n ve kendini suyun içerisinde biraz dinlendirdikten \n  sonra nehirden çıkıp üstünü giyindi."
    metin_uyu = f"{player.İsim} Will'in önceden gösterdiği çadıra giderek yatağına uzandı. \n Yeni maceralarını düşünerek uykuya daldı."

    pygame.mixer.music.load(sound_path + '/Camp.ogg')
    pygame.mixer.music.set_volume(ses)
    pygame.mixer.music.play(-1)

    while True:
        screen.blit(background, (0, 0))  
        Cursor(campMenu)
        option = create_menu(campMenu)  
        status_bar()
        if option == "Kamp Ateşinin Başında Sohbet Et":
            metin_start = metin_yazdirma(random.choice([camp_metin1, camp_metin2, camp_metin3]), background)
            if metin_start:
                change_attribute(player,"Eğlence", 20, "add")
                change_attribute(player,"XP", 10, "add")
                change_attribute(player,"Uyku", 10, "sub")
                change_attribute(player,"Açlık", 10, "sub")
                change_attribute(player,"Hijyen", 10, "sub")
        elif option == "Nehirde Yıkan" and player.Hijyen < 100:
            metin_start = metin_yazdirma(metin_nehir, background)
            if metin_start:
                change_attribute(player,"Hijyen", 100, "overwrite")
                change_attribute(player,"Uyku", 10, "sub")
                change_attribute(player,"Açlık", 10, "sub")
                change_attribute(player,"Eğlence", 10, "sub")
        elif option == "Nehirde Yıkan" and player.Hijyen >= 100:
            message_text = f"Zaten temizsiniz"
            show_message = True
            message_start_time = pygame.time.get_ticks()
        elif option == "Uyu":
            metin_start = metin_yazdirma(metin_uyu, background)
            if metin_start:
                change_attribute(player,"Uyku", 100, "overwrite")
                change_attribute(player,"Açlık", 30, "sub")
                change_attribute(player,"Hijyen", 30, "sub")
                change_attribute(player,"Eğlence", 30, "sub")
        elif option == "Meydana Dön":       
            pygame.mixer.music.stop()                                   
            town_center()
        
        if show_message:
            draw_text(message_text, WIDTH // 2, HEIGHT // 2, WHITE, font, bg_color=BLACK)
            current_time = pygame.time.get_ticks()
            if current_time - message_start_time > display_time:
                show_message = False
        pygame.display.flip()

def sifahane():
    global show_message, message_start_time , message_text,ses
    background = pygame.image.load(image_path + '/Room3.png')  
    background = pygame.transform.scale(background, (1280, 720))  
    pygame.mixer.music.load(sound_path + '/Sifahane.ogg')
    pygame.mixer.music.set_volume(ses)
    pygame.mixer.music.play(-1)

    while True:
        screen.blit(background, (0, 0))  
        Cursor(sifahaneMenu)
        option = create_menu(sifahaneMenu)  
        status_bar()
        if option == "Şifacıdan yaralarını sarmasını iste" :
            if player.Can == 100:
                message_text = f"Zaten maksimum canınız var"
                show_message = True
                message_start_time = pygame.time.get_ticks()
            elif player.Para < 20:
                message_text = f"Yeterli Paranız Yok"
                show_message = True
                message_start_time = pygame.time.get_ticks()
            else:    
                change_attribute(player,"Can", 15, "add")
                change_attribute(player,"Para", 20,"sub")
            
        elif option == "Şifacıdan merhem yapıp sürmesini iste" :
            if player.Can >= 100:
                message_text = f"Zaten maksimum canınız var"
                show_message = True
                message_start_time = pygame.time.get_ticks()                
            elif player.Para < 30:
                message_text = f"Yeterli Paranız Yok"
                show_message = True
                message_start_time = pygame.time.get_ticks()                
            else:
                change_attribute(player,"Can", 30, "add")
                change_attribute(player,"Para", 30, "sub")
            
        elif option == "Şifacıdan İlaç al":
            if player.Pot == 3:
                message_text = f"Zaten maksimum potunuz var"
                show_message = True
                message_start_time = pygame.time.get_ticks()
            elif player.Para < 25:
                message_text = f"Yeterli Paranız Yok"
                show_message = True
                message_start_time = pygame.time.get_ticks()
            else:
                change_attribute(player,"Para", 25, "sub")
                change_attribute(player,"Pot", 1, "add")
        elif option == "Şifacıdan pekmez al":
            if player.Mana == 100:
                message_text = f"Zaten maksimum mananız var"
                show_message = True
                message_start_time = pygame.time.get_ticks()
            elif player.Para < 25:
                message_text = f"Yeterli Paranız Yok"
                show_message = True
                message_start_time = pygame.time.get_ticks()
            else:
                change_attribute(player,"Para", 25, "sub")
                change_attribute(player,"Mana", 50, "add")

        elif option == "Meydana Dön": 
            pygame.mixer.music.stop()                          
            town_center()


        if show_message:
            draw_text(message_text, WIDTH // 2, HEIGHT // 2, WHITE, font, bg_color=BLACK)
            current_time = pygame.time.get_ticks()
            if current_time - message_start_time > display_time:
                show_message = False

        pygame.display.flip()

def han():
    global show_message, message_start_time , message_text,ses
    background = pygame.image.load(image_path + '/Fort2.png')  
    background = pygame.transform.scale(background, (1280, 720))  
    pygame.mixer.music.load(sound_path + '/Han.ogg')
    pygame.mixer.music.set_volume(ses)
    pygame.mixer.music.play(-1)

    while True:
        screen.blit(background, (0, 0))  
        Cursor(hanMenu)
        option = create_menu(hanMenu)  
        status_bar()

        if option == "Yiyecek satın al ve ye":
            if player.Açlık == 100:
                message_text = f"Zaten toksunuz"
                show_message = True
                message_start_time = pygame.time.get_ticks()
            elif player.Para < 10:
                message_text = f"Yeterli Paranız Yok"
                show_message = True
                message_start_time = pygame.time.get_ticks()
            else:
                change_attribute(player,"Para", 10, "sub")
                change_attribute(player,"Açlık", 50, "add")
                change_attribute(player,"Can", 10, "add")
        elif option == "İçecek satın al ve eğlen":
            if player.Eğlence == 100:
                message_text = f"Zaten maksimum eğlence düzeyiniz var"
                show_message = True
                message_start_time = pygame.time.get_ticks()                
            elif player.Para < 15:
                message_text = f"Yeterli Paranız Yok"
                show_message = True
                message_start_time = pygame.time.get_ticks()                
            else:
                change_attribute(player,"Para", 5, "sub")
                change_attribute(player,"Açlık", 10, "add")
                change_attribute(player,"Eğlence", 50, "add")
                change_attribute(player,"Can", 10, "add")

        elif option == "Güreş" :
            if player.Hijyen <= 0:
                message_text = f"Çok pis kokuyorsunuz kimse sizinle güreşmek istemiyor"    
                show_message = True
                message_start_time = pygame.time.get_ticks()                     
            elif player.Eğlence <= 0:
                message_text = f"Yeterli Eğlenceniz Yok"
                show_message = True
                message_start_time = pygame.time.get_ticks()                
            else:
                han_metin1 = f"Hana giren {player.İsim} hancıya doğru bağırarak. \n {player.İsim}: Hancı bana soğuk bir bira. \n O sırada insanların bi çember yapıp tezahürat ettiklerini gördü \n ve merakla yanlarına doğru gitti. \n {player.İsim}: Ne yapıyorlar burada. \n Ayakta tezahürat eden bir adam gözlerini ringden hiç ayırmadan \n Tezahüratçı: Güreşiyorlar. \n  {player.İsim}: Sanırsam üzerlerine bahis oynanmış denemekten zarar gelmez. \n {player.İsim} organizsayonu yapan adama gidip kayıt oluşturdu. \n Bir sonraki maç ringe çıktı ve rakibi uzun boylu bir siyahi adamdı. \n {player.İsim}: Ah! sanırım orklara benzeyen biriyle antreman yapmak hiç fena bir fikir değil he \n Rakibi sinirlenerek bi anda saldırsada {player.İsim} küçük bedeniyle heman kaçıp arkadan yakaladı. \n Kaldırmaya çalışsa da beceremedi ve adam kolundan tutup ringin diğer tarafına fırlattı. \n Darbeden sonra {player.İsim}'ın burnu kanamaya başladı. \n Kanı temizleyip bu sefer o saldırdı. \n Koca cüsseli adam engellemeye çalışsa da küçük bedeniyle \n hemen kaçıp arkasına geçti ve diz kapağı kısmına tekme attı. \n Dengesini kaybeden adam tek bacak üstüne çöktü ve \n {player.İsim} üstüne atlayarak koca adamı yere düşürmeyi başardı. \n Maçı kazanmış oldu."       
                han_metin2 = f"Hana giren {player.İsim} masaya doğru yürürken bir gurup adamın kavga ettiğini gördü. \n Hiç onları aldırmadı ve hancıya dönüp bira istedi. \n Hancı birasını hazırlarken{player.İsim} arkası dönük bir şekilde düşünüyordu. \n Birden kafasına bira bardağı gelince \n {player.İsim}: Bu iş artık kişiselleşti Dönüp kavga eden kalabalığın ortasına daldı..... \n Bir süre sonra herkes dağılmıştı. \n Yüzü kanlar içerisinde olan {player.İsim} yerden dövdüğü adamlardan birinin cüzdanını aldı \n ve oturup birasını tek seferde içtikten sonra handan ayrıldı."       
                metin_start = metin_yazdirma(random.choice([han_metin1, han_metin2]), background)
                if metin_start:
                    change_attribute(player,"Para", 10, "add")
                    change_attribute(player,"XP", 20, "add")
                    change_attribute(player,"Eğlence", 10, "add")
                    change_attribute(player,"Uyku", 20, "sub")
                    change_attribute(player,"Açlık", 20, "sub")
                    change_attribute(player,"Hijyen", 30, "sub")
        elif option == "Meydana Dön":    
            pygame.mixer.music.stop()                                   
            town_center()

        if show_message:
            draw_text(message_text, WIDTH // 2, HEIGHT // 2, WHITE, font, bg_color=BLACK)
            current_time = pygame.time.get_ticks()
            if current_time - message_start_time > display_time:
                show_message = False

        pygame.display.flip()

def macera():
    global chapter, message_text, show_message, message_start_time
    background = pygame.image.load(image_path + '/World.png')  
    background = pygame.transform.scale(background, (1280, 720))  

    while True:
        screen.blit(background, (0, 0))  
        Cursor(maceraMenu)
        option = create_menu(maceraMenu)  
        status_bar()

        if player.Eğlence > 0:
            if option == "Yakın çevreden şifalı bitki topla ve avlan":
                macera_metin1 = f"{player.İsim} Vargun Kalesi çevresinde dolaşırken \n bir şifacıdan öğrendiği şifalı bitkileri toplamaya ve hayvan karar verdi. \n Etrafta bitki ve hayvanları aramaya başladı. \n Hayvanları ve bitkileri ararken hem idman yaptı hemde kendini geliştirdi."
                metin_start = metin_yazdirma(macera_metin1, background)
                if metin_start:
                    if ((player.Toplama * 4) / 100) >= random.random() and player.Can < 100:
                        message_text = f"Şanslısınız bitki buldunuz. Canınız 10 arttı."
                        show_message = True
                        message_start_time = pygame.time.get_ticks()
                        change_attribute(player,"Can", 10, "add")
                        change_attribute(player,"Açlık", 10, "sub")
                        change_attribute(player,"Uyku", 10, "sub")
                        change_attribute(player,"Hijyen", 10, "sub")
                        change_attribute(player,"Eğlence", 10, "sub")
                    elif (((player.Toplama * 4) / 100) / 2) >= random.random() and player.Açlık < 100:
                        message_text = f"Hayvan buldunuz. Avlayıp etini yediniz. Açlığınız 20 arttı"
                        show_message = True
                        message_start_time = pygame.time.get_ticks()
                        change_attribute(player,"Açlık", 20, "add")
                        change_attribute(player,"Uyku", 10, "sub")
                        change_attribute(player,"Hijyen", 10, "sub")
                        change_attribute(player,"Eğlence", 10, "sub")
                    else:
                        message_text = f"Şansınıza küsün bir şey bulamadınız."
                        show_message = True
                        message_start_time = pygame.time.get_ticks()
                        change_attribute(player,"Açlık", 10, "sub")
                        change_attribute(player,"Uyku", 10, "sub")
                        change_attribute(player,"Hijyen", 10, "sub")
                        change_attribute(player,"Eğlence", 10, "sub")
            elif option == "Hikaye":
                if chapter == 0 or chapter == 1:
                    chapter1()
                elif kac == 2 and chapter == 3:
                    chapter2()
                elif chapter == 4:
                    chapter3()

            elif option == "Meydana Dön":                                          
                town_center()
        else:
            message_text = f"Yeterli eğlenceniz yok"
            show_message = True
            message_start_time = pygame.time.get_ticks()

        if show_message:
            draw_text(message_text, WIDTH // 2, HEIGHT // 2, WHITE, font, bg_color=BLACK)
            current_time = pygame.time.get_ticks()
            if current_time - message_start_time > display_time:
                show_message = False

        pygame.display.flip()

def fight():
    global player, sira, message_text, chapter, show_message, message_start_time, kac,ses, fight_status, iknaEtme

    if chapter == 1:
        background = pygame.image.load(image_path + '/ikilifight.png')  
        background = pygame.transform.scale(background, (1280, 720))
        pygame.mixer.music.load(sound_path + '/Battle1.ogg')
        pygame.mixer.music.set_volume(ses)
        pygame.mixer.music.play(-1)
        enemy = Karakter("Ork", 50, random.randint(1,5), random.randint(1,5), random.randint(1,5))
    elif chapter == 3 or kac == 2:
        if chapter == 3 and iknaEtme == 0:
            background = pygame.image.load(image_path + '/teklifight_ikiliork.png')  
            background = pygame.transform.scale(background, (1280, 720))  
        else:
            background = pygame.image.load(image_path + '/ikilifight_ikiliork.png')  
            background = pygame.transform.scale(background, (1280, 720))
        pygame.mixer.music.load(sound_path + '/Battle2.ogg')
        pygame.mixer.music.set_volume(ses)
        pygame.mixer.music.play(-1)
        enemy = Karakter("Ork", 70, random.randint(6,8), random.randint(6,8), random.randint(6,8))
    elif chapter == 4 or kac == 3:
        background = pygame.image.load(image_path + '/ikilifight_urakork.png')  
        background = pygame.transform.scale(background, (1280, 720)) 
        pygame.mixer.music.load(sound_path + '/Battle1.ogg')
        pygame.mixer.music.set_volume(ses)
        pygame.mixer.music.play(-1)
        enemy = Karakter("Ork", 100, random.randint(8,13), random.randint(8,13), random.randint(8,13))

    player_damage = 4 * player.Güç
    enemy_damage = 4 * enemy.Güç
    player_defence = (enemy_damage - ((enemy_damage * ((4 * player.Dayanıklılık) / 100)) - 1))
    enemy_defence = (player_damage - ((player_damage * ((4 * enemy.Dayanıklılık) / 100)) - 1))
    player_tenacity = 2 * player.Çeviklik
    enemy_tenacity = 2 * enemy.Çeviklik
    heavy_damage = 1.5 * player_damage
    enemy_defence2 = (heavy_damage - ((heavy_damage * ((4 * enemy.Dayanıklılık) / 100)) - 1))

    if player.Çeviklik > enemy.Çeviklik:
        sira = "player"
    elif player.Çeviklik < enemy.Çeviklik:
        sira = "enemy"
    else:
        sira = "player" if random.choice([True, False]) else "enemy"

    message_text = f"{sira} savaşmaya başlıyor"
    show_message = True
    message_start_time = pygame.time.get_ticks()

    fight_status = 1

    while True:
        screen.blit(background, (0, 0))  
        Cursor(fightMenu)
        option = create_menu(fightMenu)  
        status_bar()
        draw_text(f"{enemy.İsim} Can: {enemy.Can:.0f}", 100, 100, WHITE, font, bg_color=BLACK)

        if show_message:
            draw_text(message_text, WIDTH // 2, HEIGHT // 4, WHITE, font, bg_color=BLACK)
            current_time = pygame.time.get_ticks()
            if current_time - message_start_time > display_time:
                show_message = False
                if player.Can <= 0:
                    fight_status = 0
                    dead()
                    break
                elif enemy.Can < 1:
                    fight_status = 0
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(sound_path + '/Victory1.ogg')
                    pygame.mixer.music.set_volume(ses)
                    if chapter == 1:
                        change_attribute(player, "XP", 30, "add")
                        change_attribute(player, "Para", 30, "add")
                        message_text = f"SAVAŞI KAZANDINIZ! 30 XP ve 30 Para kazandınız."
                        show_message = True
                        message_start_time = pygame.time.get_ticks()
                        pygame.mixer.music.play(1)
                        background = pygame.image.load(image_path + '/konusurken.png')  
                        background = pygame.transform.scale(background, (1280, 720))  
                        chapter1_metin5 = f"Will {player.İsim}'a dönüp aferin ilk ork'unu yendin dedi. \n {player.İsim} Will'e bakıp \n {player.İsim}: Bunu sana borçluyum. \n Will: Ben sürekli yanında olmayacağım bu yüzden kendini geliştirmelisin. \n {player.İsim} Will'e bakıp onaylarcasına kafasnı salladı. \n {player.İsim} Will'e bağlarının arttığını hissediyordu sanki aralarındaki bağ yolda karşılaşan \n iki yabancıdan daha fazlasıydı sanki baba ve oğul gibiydiler. \n Will: Bu kadar derin ne düşünüyorsun? \n {player.İsim} bi an afalladı sanki Will'in içinden geçenleri okumuş gibiydi. \n {player.İsim}: H-Hiçbir şey düşünmüyorum. \n Bu sırada Will ork'un cesedini bir iple atının arkasına bağlıyordu. \n Will: Ork'u avladığımıza göre bu cesedi satmak için ve ödülümüzü almak için kaleye geri dönelim. \n Bu sırada {player.İsim} Will ile yaşadıklarını düşünüyodu ve \n hep beraber olmaları için dua ediyordu."
                        metin_start = metin_yazdirma(chapter1_metin5, background)
                        if metin_start:
                            chapter = 2
                            town_center()
                    elif chapter == 3:
                        if iknaEtme == 0:
                            background = pygame.image.load(image_path + '/teklifight.png')  
                            background = pygame.transform.scale(background, (1280, 720))  
                            chapter2_metin2 = f"{player.İsim} orklara karşı savaşırken kan ter içinde kalmıştı. \n Orkların gücü karşısında çok zorlanmıştı ve her yerinden kanlar akıyordu. \n {player.İsim} artık sonun geldiğini düşünüyordu. \n Orklardan biri yere düşmüştü, diğeri de düşecek gibiydi. \n Son bir darbe daha vurduktan sonra ork yere düşmüştü. \n Kan ter içinde kalan {player.İsim} yere yığıldı. \n Nefes nefese kalmıştı. \n {player.İsim} bir kaç dakika boyunca daha yerde kaldıktan \n sonra ayaklanmak için davrandı \n ama bir ses yüzünden yerdeki ork'a baktı. \n Ork hala canlıydı. \n {player.İsim} artık ölüceğine emindi çünkü hiç gücü kalmamıştı. \n Gözlerini kapadı ve son nefesini vermeden önce doğayı dinlemek istedi. \n Ama havayı yaran bir ıslık sesi duydu. \n {player.İsim} gözlerini açtığında ona nerdeyse 2 adım uzaklıktaki \n ork'un, kafasına ok yediğini gördü ve bir anda ork yere yığıldı. \n {player.İsim} olan bitene anlam veremedi ve etrafına bakınmaya başladı."                        
                            metin_start = metin_yazdirma(chapter2_metin2, background)
                            if metin_start:
                                pygame.mixer.music.play(1)
                                background = pygame.image.load(image_path + '/konusurken.png')  
                                background = pygame.transform.scale(background, (1280, 720))  
                                chapter2_metin3 = f"Will bir çalının arasından çıkıp ona doğru yürüyordu. \n Elini {player.İsim}'a uzattı ve kaldırdı. \n {player.İsim} Will'e dönüp. \n {player.İsim}: Geç kaldın. \n Will: Eğer geç kalsaydım şuan da yerde yatan sen olurdun. \n {player.İsim} Will'in iğneleyici laflarına bile takılmadan sevinip ona sarıldı. \n Gözlerinden yaşlar akıyordu. \n {player.İsim}: Bir an öleceğimi düşündüm. \n Will {player.İsim}'a dikkatsizliğin yüzünden ölecektin az kalsın dedi. \n {player.İsim} dolu gözlerle nasıl buldun beni diye sordu. \n  Will: Tüm ormanda savaşınızın sesi yaankılanıyordu. \n {player.İsim}: Will'e orklar genelde tek gezmezlermi? \n Will: Evet, bunlar çifleşme döneminde olan orklardır. \n Bu yüzden birliktelerdi. \n Orklar bu dönemlerde çok hırçın ve saldırgan olurlar. \n Will atları getirip orkların birini kendi attına diğerini {player.İsim}'ın atına bağladı. \n {player.İsim}'a dönüp Tritonas Kalesine geri dönelim dedi. \n Will ve {player.İsim} Tritonas Kalesine geri döndüklerinde ücretlerini alıp tekrardan Vargun Kalesine doğru yola çıktılar."
                                metin_start = metin_yazdirma(chapter2_metin3, background)
                                if metin_start:
                                    change_attribute(player, "XP", 60, "add")
                                    change_attribute(player, "Para", 60, "add")
                                    message_text = f"SAVAŞI KAZANDINIZ! 60 XP ve 60 Para kazandınız."
                                    show_message = True
                                    message_start_time = pygame.time.get_ticks()
                                    chapter = 4
                                    town_center()
                        else:
                            change_attribute(player, "XP", 60, "add")
                            change_attribute(player, "Para", 60, "add")
                            message_text = f"SAVAŞI KAZANDINIZ! 60 XP ve 60 Para kazandınız."
                            show_message = True
                            message_start_time = pygame.time.get_ticks()
                            chapter = 4
                            town_center()
                    elif chapter == 4:
                        background = pygame.image.load(image_path + '/ikilifight_urakork.png')  
                        background = pygame.transform.scale(background, (1280, 720))  
                        chapter3_metin2 = f"{player.İsim} ve Will'in kordineli saldırılarına dayanamayan ork iki ayak üstüne düştü. \n {player.İsim} bu fırsatı kaçırmak hiç istemiyordu ve ork'un üzerine atladı. \n {player.Silah} ile ork'un kafasına bir kaç darbe indirdi. \n Darbelerden sonra ork yere düşmüştü. \n Will {player.İsim}'a dönüp. \n Will: Bu kadar yeter. \n Will: Unutma {player.İsim} ne olursa olsun her canlı düzgün bir şekilde ölmeyi hak ediyor. \n {player.İsim} şaşırmıştı. Çünkü Will'in bu kadar sert olmasını beklemiyordu. \n {player.İsim}: Ama onlar bizim halkımızı öldürüyorlar. \n Will: Eğer onlar gibi olursak bizde onlardan farkımız kalmaz. \n {player.İsim} Will'e hak verdi ve sesiz kalmayı tercih etti. \n Will cesedi taşımak için atları getirdi. \n Ceset o kadar büyüktü ki iki at anca taşıyabiliyordu."
                        metin_start = metin_yazdirma(chapter3_metin2, background)
                        if metin_start:
                            pygame.mixer.music.play(1)
                            background = pygame.image.load(image_path + '/Castle.png')  
                            background = pygame.transform.scale(background, (1280, 720))  
                            chapter3_metin2_1 = f"Will ve {player.İsim} cesedi Vargun Kalesi'ne götürdüler. \n Lord Baldwin'a teslim edip olan biteni anlattılar. \n Baldwin onlara tekrardan hürmetlerini gösterip anlaştıklarından \n fazla bir para ödeyip onları uğurladı. \n Will ve {player.İsim} meydana indiler."
                            metin_start = metin_yazdirma(chapter3_metin2_1, background)
                            if metin_start:
                                change_attribute(player, "XP", 90, "add")
                                change_attribute(player, "Para", 90, "add")
                                message_text = f"SAVAŞI KAZANDINIZ! 90 XP ve 90 Para kazandınız."
                                show_message = True
                                message_start_time = pygame.time.get_ticks()
                                chapter = 5
                                town_center()
                    else:
                        town_center()
                    break
        else:
            if sira == "player":
                if option == "Hafif Saldırı":
                    if ((random.randint(enemy_tenacity, 100)) >= 70):
                        message_text = f"{enemy.İsim} saldırıyı blokladı"
                    else:
                        sound = pygame.mixer.Sound(sound_path + '/Damage1.ogg')
                        sound.play(1) 
                        enemy.Can -= enemy_defence
                        message_text = f"Hafif Saldırı! {enemy.İsim} {enemy_defence:.0f} hasar aldı"
                    show_message = True
                    message_start_time = pygame.time.get_ticks()
                    if enemy.Can <= 0:
                        sira = "player"
                    else:
                        sira = "enemy"
                elif option == "Ağır Saldırı" and player.Mana >= 40:
                    change_attribute(player, "Mana", 40, "sub")
                    if ((random.randint(enemy_tenacity, 100)) >= 70):
                        message_text = f"{enemy.İsim} saldırıyı blokladı"
                    else:
                        sound = pygame.mixer.Sound(sound_path + '/Damage1.ogg')
                        sound.play(1)
                        enemy.Can -= enemy_defence2
                        message_text = f"Ağır Saldırı! {enemy.İsim} {enemy_defence2:.0f} hasar aldı"
                    show_message = True
                    message_start_time = pygame.time.get_ticks()
                    if enemy.Can <= 0:
                        sira = "player"
                    else:
                        sira = "enemy"
                elif option == "Ağır Saldırı" and player.Mana < 40:
                    message_text = f"Yeterli Mananız Yok"
                    show_message = True
                    message_start_time = pygame.time.get_ticks()
                elif option == "Pot iç":
                    if player.Pot == 0:
                        message_text = f"Potunuz kalmadı"
                    elif player.Can < 100:
                        change_attribute(player, "Can", 20, "add")
                        change_attribute(player, "Pot", 1, "sub")
                        message_text = f"1 Adet Pot İçtiniz. Canınız 20 arttı"
                    else:
                        message_text = f"Canınız zaten dolu"
                    show_message = True
                    message_start_time = pygame.time.get_ticks()

            elif sira == "enemy":
                if ((random.randint(player_tenacity, 100)) >= 70):
                    message_text = f"{player.İsim} saldırıyı blokladı"
                else:
                    sound = pygame.mixer.Sound(sound_path + '/Damage1.ogg')
                    sound.play(1)
                    change_attribute(player, "Can", player_defence, "sub")
                    message_text = f"{player.İsim} {enemy.İsim}'dan {player_defence:.0f} hasar aldı"
                show_message = True
                message_start_time = pygame.time.get_ticks()
                sira = "player"
        
        pygame.display.flip()

############################################################################################
#                           OYUNUN BAŞLANGIÇ FONKSİYONLARI                                 #
############################################################################################

def main_menu():
    global subtitle_font, subtitle_size, settings, screen, ses
    background = pygame.image.load(image_path + '/main_menu.png')  
    background = pygame.transform.scale(background, (1280, 720))  
    pygame.mixer.music.load(sound_path + '/Main_Menu.ogg')
    pygame.mixer.music.set_volume(ses)
    pygame.mixer.music.play(-1)

    while True:
        screen.blit(background, (0, 0))  
        Cursor(mainMenu)
        option = create_menu(mainMenu)  

        if option == "Oyunu Başlat":
            pygame.mixer.music.stop()
            chapter0()
        elif option == "Ayarlar":
            while True:
                screen.blit(background, (0, 0))  
                Cursor(settingsMenu)
                option = create_menu(settingsMenu)  
                if option == "Tam Ekran":
                    settings["Tam Ekran"] = not settings["Tam Ekran"]
                    if settings["Tam Ekran"]:
                        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((WIDTH, HEIGHT))
                elif option == "Ses":
                    settings["Ses"] = (settings["Ses"] + 10) % 110  
                    ses = settings["Ses"] / 100
                    pygame.mixer.music.set_volume(ses)
                elif option == "Altyazı Boyutu":
                    sizes = ["Küçük", "Orta", "Büyük"]
                    current_index = sizes.index(settings["Altyazı Boyutu"])
                    settings["Altyazı Boyutu"] = sizes[(current_index + 1) % len(sizes)]  
                    subtitle_size = size_mapping[settings["Altyazı Boyutu"]]
                    subtitle_font = pygame.font.Font(None, subtitle_size)
                elif option == "Ana Menüye Dön":
                    break

                pygame.display.flip()
        elif option == "Çıkış":
            pygame.quit()
            sys.exit()
        
        pygame.display.flip()

def exit_menu():
    background = pygame.image.load(image_path + '/main_menu.png')  
    background = pygame.transform.scale(background, (1280, 720))  
    while True:
        screen.blit(background, (0, 0))  
        Cursor(exitMenu)
        option = create_menu(exitMenu)  

        if option == "Ana Menüye Dön":
            main_menu()
        elif option == "İptal":
            town_center()
        pygame.display.flip()

def show_logo():
    logo = pygame.image.load(image_path + '/logo.png')  
    logo_rect = logo.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.fill(BLACK)
    screen.blit(logo, logo_rect)
    pygame.display.update()
    time.sleep(4) 

def game_over():
    global ses
    background = pygame.image.load(image_path + '/Castle.png')  
    background = pygame.transform.scale(background, (1280, 720)) 

    draw_text(f"Tebrikler Bir Başarım Açtınız: WİLL SİZLE GURUR DUYUYOR", WIDTH // 2, HEIGHT // 2, WHITE, font, bg_color=BLACK)
    sound = pygame.mixer.Sound(sound_path + '/Victory1.ogg')
    sound.play(0)
    pygame.display.flip()
    screen.blit(background, (0, 0))  
    time.sleep(5)
    
    while True:
        pygame.mixer.music.load(sound_path + '/game_over.ogg')
        pygame.mixer.music.set_volume(ses)
        pygame.mixer.music.play(-1)
        draw_text("Oyun Bitti. 10 Saniye sonra kapancaktır.", WIDTH // 2, HEIGHT // 2, WHITE, font, bg_color=BLACK)
        pygame.display.flip()
        time.sleep(10)
        pygame.quit()
        sys.exit()

############################################################################################
#                                       OYUNU BAŞLAT                                       #
############################################################################################

show_logo()
main_menu()