import random

# Eylemler belirlendi
actions = ["taş", "kağıt", "makas"]

# Oyun (game) tanımlandı
def game():
    # Sayaçlar ve skorlara değer atandı
    game_counter = 1
    round_counter = 0
    your_score = 0
    program_score = 0
    
    # Başlangıç mesajı yazıldı
    print("Mini oyuna hoş geldin!\nOyunumuzun adı taş kağıt makas!"
          "\nDünyaca ünlü oldukça basit bir oyun.\nİyi şanslar")

    while True: # Oyun döngüsü
        # Oyuncuya nasıl çıkış yapılacağı söylendi
        user_input = input("Eğer maceramızı başlamadın bitirmek istiyorsan 'exit' yazabilirsin."
                           "\nDevam etmek için ise Enter'a basın").lower()
        if user_input == "exit":
            print("En azından bir tur oynayabilirdik! Neyse, güle güle")
            break
        else:
            print("Öyleyse oyun başlıyor!")
        round_count = int(input("Kaç round oynamak istersin?: "))
        round_counter = 0  # Her yeni oyun için round sayacını sıfırla

        while round_counter < round_count:
            round_counter += 1
            # Oyuncunun ve bilgisayarın seçimlerinin alınması
            player = input("Bir seçim yapın (taş, kağıt, makas): ").lower()
            program = random.choice(actions)
            
            # Oyun ve round sayısı yazılacak
            print("Game number:", game_counter)
            print("Round number:", round_counter)
            
            if player in actions:
                # 9 olasılığı değerlendirilecek
                if player == program:
                    print("Berabere! Program ve oyuncu aynı eylemi seçti.")
                elif (player == "kağıt" and program == "taş") or \
                     (player == "makas" and program == "kağıt") or \
                     (player == "taş" and program == "makas"):
                    print("Bu roundu oyuncu kazandı")
                    your_score += 1
                else:
                    print("Bu roundu program kazandı")
                    program_score += 1

                print("Oyuncunun skoru:", your_score)
                print("Programın skoru:", program_score)

            else:
                print("Geçerli bir değer girin lütfen:(taş, kağıt, makas)")
                round_counter -= 1  # Geçerli seçim yapılmadıysa bu turu tekrarlat
                continue

        if your_score == program_score:
            print("Tüm roundlar sonucu oyun berabere bitti!")
        elif your_score < program_score:
            print("Tüm roundlar sonucu Program kazandı!")
        else:
            print("Tüm roundlar sonucu Oyuncu kazandı!")

        # Tekrar oynama isteği
        play_again = input("Tekrar oynamak ister misin? (evet/hayır) ").lower()
        program_answer = random.choice(["evet", "hayır"])
        # Seçimlere uygun mesajlar yazdırılacak
        if play_again == "hayır" and program_answer == "evet":
            print("Güzel oyundu, vakit ayırdığın için teşekkürler")
            break
        elif play_again == "evet" and program_answer == "hayır":
            print("Program efendi oyuna daha fazla devam etmek istemiyormuş, güle güle!")
            break
        elif play_again == "evet" and program_answer == "evet":
            print("Hadi bir tur daha oynayalım")
            game_counter += 1
            continue
        elif play_again == "hayır" and program_answer == "hayır":
            print("İkinizin de niyeti olmadığına göre, oyun sonlandırılıyor, görüşmek üzere!")
            break
        else:
            print("Lütfen geçerli bir seçim yapınız (evet/hayır)")
            break

# Oyun fonksiyonunu çağır
game()
