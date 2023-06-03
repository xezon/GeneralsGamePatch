import os
from pathlib import Path


def run():
    this_dir = os.path.dirname(os.path.realpath(__file__))

    ini_paths = [
        Path(this_dir).joinpath("../../../GameFilesEdited/Data/INI/Speech.ini").absolute().resolve(),
    ]

    dialog_names: list[str] = []

    for ini_path in ini_paths:
        with open(ini_path) as ini_file:
            lines = ini_file.readlines()
            dialog_event_name = ""

            for line in lines:
                line = line.strip().split(";", 1)[0]

                if line.startswith("DialogEvent"):
                    key_value_pair: list[str] = line.split(" ", 1)
                    if len(key_value_pair) != 2:
                        continue

                    value_str = key_value_pair[1]
                    dialog_event_name = value_str.strip()

                elif line.startswith("End"):
                    if dialog_event_name:
                        dialog_names.append(dialog_event_name)
                        dialog_event_name = ""

    out_txt_path = Path(this_dir).joinpath("duplicate_dialogevent.txt").absolute().resolve()
    with open(out_txt_path, "w") as txt_file:
        for index,name in enumerate(dialog_names):
            for index2 in range(index+1, len(dialog_names)):
                if name == dialog_names[index2]:
                    txt_file.write(name)
                    txt_file.write("\n")

    return


if __name__ == "__main__":
    run()