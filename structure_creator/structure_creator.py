import json
from pathlib import Path


def load_config():
    try:
        with open('config.json',encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data

    except FileNotFoundError:
        print("File config.json is not found in current directory")


def create_structure(data: dict = None):

    if data:
        for folder in data["folders"]:
            for idx, file in enumerate(folder["top_files"]):
                file_name = f'{str(idx + 1).zfill(2)}00_{file["file_name"]}.md'
                path = Path(folder["name"])
                path.mkdir(parents=True, exist_ok=True)
                filepath = path / file_name

                if not filepath.is_file():
                    with filepath.open("w", encoding="utf-8") as f:
                        f.write(file["content"])
                else:
                    print(f'{filepath} already exists!')
                #TODO: put into funcion and wrap in if devices exist
                for i, d in enumerate(data["devices"]):
                    file_name_device = f'{str(idx + 1).zfill(2)}{str(i + 1).zfill(2)}_{file["file_name"]}_device{i + 1}.md'
                    device_path = Path(folder["name"], file_name_device)

                    if not device_path.is_file():
                        with device_path.open("w", encoding="utf-8") as f:
                            f.write(f'### {d}\n\nТекст\n')
                    else:
                        print(f'{device_path} already exists!')

        appendix_path = Path('appendix')
        appendix_path.mkdir(parents=True, exist_ok=True)
        appendix_file = appendix_path / data["appendix_file"]

        if not appendix_file.is_file():
            with appendix_file.open("w", encoding="utf-8") as f:
                f.write(data["appendix_content"])
        else:
            print(f'{appendix_file} already exists!')


if __name__ == '__main__':
    config = load_config()
    create_structure(config)
