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
