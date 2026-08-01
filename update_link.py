import os
import glob

old_url = "https://firebasestorage.googleapis.com/v0/b/zavor-fe238.firebasestorage.app/o/app%2FZavoR.apk?alt=media&token=0eb9a994-aa87-436d-93e8-aa8019c175c8"
new_url = "https://firebasestorage.googleapis.com/v0/b/zavor-fe238.firebasestorage.app/o/app%2FZavoR.apk?alt=media&token=0eb9a994-aa87-436d-93e8-aa8019c175c8"

for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith(('.html', '.py')):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                if old_url in content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content.replace(old_url, new_url))
                    print(f"Updated {filepath}")
            except Exception as e:
                pass
