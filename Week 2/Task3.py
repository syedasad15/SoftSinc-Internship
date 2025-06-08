def write_to_file(file_path, content, mode='a'):
    try:
        with open(file_path, mode, encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")


def read_from_file(file_path):

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return ""
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return ""

contents = read_from_file("activity.log")

print("File Contents:\n", contents)