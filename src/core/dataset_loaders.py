def load_raw_text_data(file_path: str) -> str:
    """
    Load raw text data from a given file path.

    Args:
        file_path (str): Path to the dataset file.

    Returns:
        str: The entire content of the file as a string.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            raw_text = f.read()
        return raw_text
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return ""
    except Exception as e:
        print(f"[ERROR] Could not read file {file_path}: {e}")
        return ""