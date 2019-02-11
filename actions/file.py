import re


def file_worker(file) -> list:
    """
    Translate binary file into list of words in brackets
    :param file: binary file from HTTP
    :return: list of words for every line
    """
    if file is None:
        return []
    final_list = []
    for chunk in file.readlines():
        chunk = chunk.decode("utf-8")
        line = str(chunk).rstrip('\n')
        line_context = re.findall("\'(.*?)\'", line)  # pattern: 'matched_text'
        final_list.append(line_context)
    return final_list
