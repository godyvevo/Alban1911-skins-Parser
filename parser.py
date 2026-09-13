```python
import json
import os

# Project root directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SKINS_DIR = os.path.join(BASE_DIR, "skins")
JSON_FILE = os.path.join(BASE_DIR, "resources", "en", "skin_ids.json")


def organize_folders():
    if not os.path.exists(SKINS_DIR) or not os.path.exists(JSON_FILE):
        print("Error: Skins directory or JSON file not found!")
        return

    with open(JSON_FILE, "r", encoding="utf-8") as f:
        skin_data = json.load(f)

    champion_folders = [
        folder
        for folder in os.listdir(SKINS_DIR)
        if os.path.isdir(os.path.join(SKINS_DIR, folder))
    ]
    total_champions = len(champion_folders)

    print(
        f"Found {total_champions} champion folders. Starting process...\n"
        + "-" * 50
    )

    for i, champion_id_str in enumerate(champion_folders, 1):
        old_champion_path = os.path.join(SKINS_DIR, champion_id_str)

        # 1. Rename skin subfolders
        skin_folders = [
            folder
            for folder in os.listdir(old_champion_path)
            if os.path.isdir(os.path.join(old_champion_path, folder))
        ]

        print(
            f"\n[{i}/{total_champions}] Processing Champion Folder ID: "
            f"{champion_id_str}..."
        )

        for skin_id in skin_folders:
            old_skin_path = os.path.join(old_champion_path, skin_id)

            if skin_id in skin_data:
                skin_name = skin_data[skin_id]

                # Remove characters that are invalid in Windows file names
                clean_name = "".join(
                    c for c in skin_name if c.isalnum() or c in (" ", "-", "_", ".")
                ).strip()

                new_skin_path = os.path.join(old_champion_path, clean_name)

                try:
                    os.rename(old_skin_path, new_skin_path)
                    print(f"   -> Skin ({skin_id}) ==> {clean_name}")
                except Exception as e:
                    print(f"   [ERROR] Could not rename skin ({skin_id}): {e}")
            else:
                print(
                    f"   -> Skin ({skin_id}) ==> ID not found in JSON, skipped."
                )

        # 2. Rename the main champion folder
        # Logic: Champion ID * 1000 gives the base skin ID (e.g. 1 -> 1000)
        try:
            base_skin_id = str(int(champion_id_str) * 1000)

            if base_skin_id in skin_data:
                champion_name = skin_data[base_skin_id]

                # Remove characters that are invalid in Windows file names
                clean_champion_name = "".join(
                    c
                    for c in champion_name
                    if c.isalnum() or c in (" ", "-", "_", ".")
                ).strip()

                new_champion_path = os.path.join(
                    SKINS_DIR, clean_champion_name
                )

                os.rename(old_champion_path, new_champion_path)

                print(
                    f" [SUCCESS] Champion folder renamed: "
                    f"{champion_id_str} -> {clean_champion_name}"
                )
            else:
                print(
                    f" [INFO] Base skin ID '{base_skin_id}' for "
                    f"'{champion_id_str}' was not found in the JSON. "
                    "Champion folder name remains unchanged."
                )

        except ValueError:
            # Skip folders whose names are not numeric
            pass


if __name__ == "__main__":
    organize_folders()
```
