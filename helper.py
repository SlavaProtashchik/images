import os


def file_output_path(path, sub_folder):
    directory = os.path.dirname(path)
    basename = os.path.basename(path)
    folder_path = f"{directory}/output/{sub_folder}"

    os.makedirs(folder_path, exist_ok=True)

    return f"{folder_path}/{basename}"
