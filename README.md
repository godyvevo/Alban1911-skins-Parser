# Alban1911 Skins Parser

A Python script that automatically renames Alban1911 League of Legends skin folders using skin IDs and Turkish champion/skin names.

## Features

* Automatically renames champion folders.
* Automatically renames skin folders.
* Uses `skin_ids.json` for ID-to-name mapping.
* Converts champion IDs to their base skin IDs.
* Removes characters that are invalid in Windows file names.
* Skips skin IDs that are not found in the JSON file.

## Folder Structure

The script expects the following structure:

```text
project/
├── ayristirici.py
├── skins/
│   ├── 1/
│   │   ├── 1000/
│   │   └── 1001/
│   └── ...
└── resources/
    └── tr/
        └── skin_ids.json
```

## Usage

1. Place the `skins` folder next to `ayristirici.py`.
2. Make sure `resources/tr/skin_ids.json` exists.
3. Run:

```bash
python ayristirici.py
```

The script will automatically rename the champion and skin folders according to the names found in `skin_ids.json`.

## Notes

This script is intended for organizing Alban1911 skin files by replacing numeric IDs with readable Turkish names.

The `skin_ids.json` file is not authored by this project. Please respect the original source and any applicable licensing terms.

## How It Works

The script uses the `skin_ids.json` file as an ID-to-name mapping.

1. It scans the `skins` directory and detects all champion folders.
2. For each champion folder, it checks the skin subfolders and reads their IDs.
3. Each skin ID is searched in `skin_ids.json`.
4. When a matching ID is found, the numeric skin folder is renamed to its corresponding Turkish skin name.
5. The champion ID is multiplied by `1000` to determine its base skin ID.
6. The base skin ID is also searched in `skin_ids.json` and used to rename the champion folder.
7. Characters that are not valid in Windows file names are removed automatically.
8. IDs that are not present in the JSON file are skipped without stopping the program.

# Alban1911 Skins Parser

Alban1911 League of Legends skin klasörlerini, skin ID'lerini kullanarak Türkçe şampiyon ve kostüm isimleriyle otomatik olarak yeniden adlandıran bir Python scriptidir.

## Özellikler

* Şampiyon klasörlerini otomatik olarak yeniden adlandırır.
* Kostüm klasörlerini otomatik olarak yeniden adlandırır.
* ID → isim eşleştirmesi için `skin_ids.json` kullanır.
* Şampiyon ID'lerini temel kostüm ID'lerine dönüştürür.
* Windows dosya adlarında kullanılamayan karakterleri otomatik olarak temizler.
* JSON dosyasında bulunmayan skin ID'lerini atlar.

## Klasör Yapısı

Script aşağıdaki klasör yapısını bekler:

```text
project/
├── ayristirici.py
├── skins/
│   ├── 1/
│   │   ├── 1000/
│   │   └── 1001/
│   └── ...
└── resources/
    └── tr/
        └── skin_ids.json
```

## Kullanım

1. `skins` klasörünü `ayristirici.py` dosyasının yanına koyun.
2. `resources/tr/skin_ids.json` dosyasının mevcut olduğundan emin olun.
3. Scripti çalıştırın:

```bash
python ayristirici.py
```

Script, `skin_ids.json` içerisinde bulunan isimlere göre şampiyon ve kostüm klasörlerini otomatik olarak yeniden adlandıracaktır.

## Notlar

Bu script, Alban1911 skin dosyalarını sayısal ID'lerden okunabilir Türkçe isimlere dönüştürerek düzenlemek amacıyla hazırlanmıştır.

`skin_ids.json` bu proje tarafından oluşturulmamıştır. Lütfen orijinal kaynağa ve geçerli lisans koşullarına uygun şekilde kullanın.

## Nasıl Çalışır?

Script, `skin_ids.json` dosyasını bir ID → isim eşleştirme tablosu olarak kullanır.

1. `skins` klasörünü tarar ve tüm şampiyon klasörlerini bulur.
2. Her şampiyon klasörünün içindeki kostüm klasörlerini kontrol eder ve klasör adlarını ID olarak alır.
3. Her kostüm ID'sini `skin_ids.json` içerisinde arar.
4. Eşleşen bir ID bulunduğunda, sayısal kostüm klasörünü karşılık gelen Türkçe kostüm adıyla yeniden adlandırır.
5. Şampiyon ID'sini `1000` ile çarparak temel kostüm ID'sini oluşturur.
6. Oluşturulan temel kostüm ID'sini `skin_ids.json` içerisinde arar ve bulunan ismi şampiyon klasörünü yeniden adlandırmak için kullanır.
7. Windows dosya adlarında geçersiz olan karakterleri otomatik olarak temizler.
8. JSON dosyasında bulunmayan ID'leri hata vermeden atlar ve sonraki klasöre devam eder.

Script, skin dosyalarının içeriğini değiştirmez. Yalnızca ilgili şampiyon ve kostüm klasörlerinin adlarını değiştirir.


### Example

Before:

```text
skins/
├── 1/
│   ├── 1001/
│   ├── 1002/
│   └── 1003/
└── 2/
    ├── 2001/
    └── 2002/
```

After:

```text
skins/
├── Annie/
│   ├── Gothic Annie/
│   ├── Red Riding Annie/
│   └── Woad Annie/
└── Olaf/
    ├── Forsaken Olaf/
    └── ...
```

The script does not modify the skin files themselves. It only renames the corresponding folders.

## Türkçe - Nasıl Çalışır?

Script, şampiyon ve kostüm ID'lerini isimlere dönüştürmek için `skin_ids.json` dosyasını bir eşleştirme tablosu olarak kullanır.

1. `skins` klasörünü tarar ve içerisindeki tüm şampiyon klasörlerini bulur.
2. Her şampiyon klasörünün içindeki kostüm klasörlerini kontrol eder ve klasör adlarını ID olarak alır.
3. Her kostüm ID'sini `skin_ids.json` içerisinde arar.
4. Eşleşen bir ID bulunduğunda, sayısal kostüm klasörünü JSON dosyasındaki Türkçe kostüm adıyla yeniden adlandırır.
5. Şampiyon ID'sini `1000` ile çarparak temel kostüm ID'sini oluşturur.
6. Oluşturulan temel kostüm ID'sini de `skin_ids.json` içerisinde arar ve bulunan adı şampiyon klasörünü yeniden adlandırmak için kullanır.
7. Windows dosya adlarında kullanılamayan karakterleri otomatik olarak temizler.
8. JSON dosyasında bulunmayan ID'leri hata vermeden atlar ve sonraki klasöre devam eder.

### Örnek

**Önce:**

```text
skins/
├── 1/
│   ├── 1001/
│   ├── 1002/
│   └── 1003/
└── 2/
    ├── 2001/
    └── 2002/
```

**Sonra:**

```text
skins/
├── Annie/
│   ├── Kostüm Adı 1/
│   ├── Kostüm Adı 2/
│   └── Kostüm Adı 3/
└── Olaf/
    ├── Kostüm Adı 1/
    └── Kostüm Adı 2/
```

Script, kostüm dosyalarının içeriğini değiştirmez. Yalnızca şampiyon ve kostüm klasörlerinin adlarını düzenler.

## Scripts

### `ayristirici.py`
Uses `resources/tr/skin_ids.json` to rename champion and skin folders with Turkish names.

### `parser.py`
Uses `resources/en/skin_ids.json` to rename champion and skin folders with English names.

## License

This project is licensed under the MIT License.
