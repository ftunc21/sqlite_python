from kullanıcı_sistemi import *

def print_menu():
    print("""
          1-Giriş Yap
          2-Kayıt Ol
          3-Çıkış
          """)
create_table()

def login_menu(user):
    print(f"""
    {user[1]} {user[2]} {user[3]} Hoşgeldiniz
            
    1-Bir Kullanıcı arama
    2-Tüm Kullanıcıları Listele
    3-Hesap Sil
    4-Çıkış Yap
          
          
          
    """)

while True:
    print_menu()
    secim = input("Seçiminizi yapınız: ")
    if secim == "1":
        username = input("Kullanıcı adınızı giriniz: ")
        password = input("Şifrenizi giriniz: ")
        user = search_user(username)
        if user == None:
            print("Kullanıcı bulunamadı")
            continue
        if password == user[4]:
            while True:
                login_menu(user)
                secim = input("Seçiminizi yapınız: ")
                if secim == "1":
                    username = input("Aranacak kullanıcı adını giriniz: ")
                    user = search_user(username)
                    if user == None:
                        print("Kullanıcı bulunamadı")
                        continue
                    print(f"{user[1]} {user[2]} {user[3]}")
                
                elif secim == "2":
                    print_all()
                elif secim == "3":
                    delete_account(username)
                    print("Hesap silindi")
                    break
                elif secim == "4":
                    break
                else:
                    print("Geçersiz seçim")
    elif secim == "2":
        name = input("Adınızı giriniz: ")
        lastname = input("Soyadınızı giriniz: ")
        username = input("Kullanıcı adınızı giriniz: ")
        password = input("Şifrenizi giriniz: ")
        
        search = search_user(username)
        if search != None:
            print("Bu kullanıcı zaten var")
            continue
        insert(name, lastname, username, password)
        print("Kayıt başarılı")
        
    elif secim == "3":
        break
