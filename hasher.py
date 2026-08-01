import hashlib
import os


def calculate_hash(filename):

    if not os.path.exists(filename):
        raise FileNotFoundError(filename)


    sha256 = hashlib.sha256()


    with open(filename, "rb") as file:

        while chunk := file.read(4096):
            sha256.update(chunk)


    return sha256.hexdigest()



def get_files(path):

    files = []


    if os.path.isfile(path):

        files.append(path)


    elif os.path.isdir(path):

        for root, dirs, filenames in os.walk(path):

            for filename in filenames:

                full_path = os.path.join(
                    root,
                    filename
                )

                files.append(full_path)


    return files