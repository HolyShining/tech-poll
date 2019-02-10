import re


def file_worker(file) -> list:
    if file is None:
        return []
    final_list = []
    for chunk in file.readlines():
        chunk = chunk.decode("utf-8")
        line = str(chunk).rstrip('\n')
        line_context = re.findall("\'(.*?)\'", line)
        final_list.append(line_context)
    return final_list
