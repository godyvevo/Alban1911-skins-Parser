import json
import os

# Proje ana dizini
ANA_DIZIN = os.path.dirname(os.path.abspath(__file__))
SKIN_KLASORU = os.path.join(ANA_DIZIN, "skins")
JSON_DOSYASI = os.path.join(ANA_DIZIN, "resources", "tr", "skin_ids.json")


def klasorleri_duzenle():
  if not os.path.exists(SKIN_KLASORU) or not os.path.exists(JSON_DOSYASI):
    print("Hata: Klasör veya JSON dosyası bulunamadı!")
    return

  with open(JSON_DOSYASI, "r", encoding="utf-8") as f:
    skin_verileri = json.load(f)

  sampiyon_klasorleri = [
      k
      for k in os.listdir(SKIN_KLASORU)
      if os.path.isdir(os.path.join(SKIN_KLASORU, k))
  ]
  toplam_sampiyon = len(sampiyon_klasorleri)

  print(
      f"Toplam {toplam_sampiyon} şampiyon klasörü bulundu. İşlem"
      " başlatılıyor...\n"
      + "-" * 50
  )

  for i, sampiyon_id_str in enumerate(sampiyon_klasorleri, 1):
    eski_sampiyon_yolu = os.path.join(SKIN_KLASORU, sampiyon_id_str)

    # 1. Önce içindeki alt kostüm klasörlerini Türkçeleştir
    alt_klasorler = [
        ak
        for ak in os.listdir(eski_sampiyon_yolu)
        if os.path.isdir(os.path.join(eski_sampiyon_yolu, ak))
    ]

    print(
        f"\n[{i}/{toplam_sampiyon}] Şampiyon Klasör ID: {sampiyon_id_str}"
        f" işleniyor..."
    )

    for alt_id in alt_klasorler:
      eski_alt_yol = os.path.join(eski_sampiyon_yolu, alt_id)

      if alt_id in skin_verileri:
        turkce_isim = skin_verileri[alt_id]

        # Windows yasaklı karakter temizliği
        temiz_isim = "".join(
            c for c in turkce_isim if c.isalnum() or c in (" ", "-", "_", ".")
        ).strip()
        yeni_alt_yol = os.path.join(eski_sampiyon_yolu, temiz_isim)

        try:
          os.rename(eski_alt_yol, yeni_alt_yol)
          print(f"   -> Kostüm ({alt_id}) ==> {temiz_isim}")
        except Exception as e:
          print(
              f"   [HATA] Kostüm değiştirilemedi ({alt_id}): {e}"
          )
      else:
        print(f"   -> Kostüm ({alt_id}) ==> JSON içinde bulunamadı, atlandı.")

    # 2. Ana şampiyon klasörünü isimlendir (Örn: "1" -> "Annie")
    # Mantık: Şampiyon ID'sini (örn: 1) 1000 ile çarpınca baz skin ID'sini veriyor (1000)
    try:
      temel_skin_id = str(int(sampiyon_id_str) * 1000)

      if temel_skin_id in skin_verileri:
        sampiyon_adi = skin_verileri[temel_skin_id]

        # Temizlik
        temiz_sampiyon_adi = "".join(
            c for c in sampiyon_adi if c.isalnum() or c in (" ", "-", "_", ".")
        ).strip()
        yeni_sampiyon_yolu = os.path.join(SKIN_KLASORU, temiz_sampiyon_adi)

        os.rename(eski_sampiyon_yolu, yeni_sampiyon_yolu)
        print(
            f" [BAŞARILI] Ana Şampiyon Klasörü Değiştirildi: {sampiyon_id_str}"
            f" -> {temiz_sampiyon_adi}"
        )
      else:
        print(
            f" [BİLGİ] '{sampiyon_id_str}' için temel ID ({temel_skin_id})"
            " JSON'da bulunamadı, ana klasör adı sabit kaldı."
        )
    except ValueError:
        # Klasör adı sayısal değilse
      pass


if __name__ == "__main__":
  klasorleri_duzenle()