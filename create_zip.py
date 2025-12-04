import os
import zipfile

def create_zip():
    version = input("Enter version number (e.g., 1.0, 1.1, 2.0): ").strip()
    
    if not version:
        print("Version number cannot be empty!")
        return
    
    exported_dir = "exported"
    os.makedirs(exported_dir, exist_ok=True)
    
    zip_filename = os.path.join(exported_dir, f"MSE-A-Moogmas-Miracle-{version}.zip")
    
    items_to_zip = [
        "data/",
        "pack.mcmeta",
        "pack.png"
    ]
    
    missing_items = []
    for item in items_to_zip:
        if not os.path.exists(item):
            missing_items.append(item)
    
    if missing_items:
        print(f"Error: The following items were not found:")
        for item in missing_items:
            print(f"  - {item}")
        return
    
    print(f"\nCreating {os.path.basename(zip_filename)} in {exported_dir}/...")
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for item in items_to_zip:
            if os.path.isdir(item):
                for root, dirs, files in os.walk(item):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path)
                        zipf.write(file_path, arcname)
                        print(f"  Added: {arcname}")
            else:
                zipf.write(item, item)
                print(f"  Added: {item}")
    
    print(f"\nSuccessfully created {os.path.basename(zip_filename)} in {exported_dir}/!")
    print(f"File size: {os.path.getsize(zip_filename) / 1024:.2f} KB")

if __name__ == "__main__":
    try:
        create_zip()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nError: {e}")

