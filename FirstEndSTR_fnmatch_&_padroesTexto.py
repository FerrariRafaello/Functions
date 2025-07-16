import re
from fnmatch import fnmatch, fnmatchcase

def check_file_extension(filename: str, extension: str = ".txt") -> bool:
    return filename.endswith(extension)

def check_file_start(filename: str, start_str: str) -> bool:
    return filename.startswith(start_str)

def filename_pattern_match(filename: str, pattern: str) -> bool:
    return fnmatch(filename, pattern)

def filename_pattern_case_sensitive(filename: str, pattern: str) -> bool:
    return fnmatchcase(filename, pattern)

def regex_match_date(text: str) -> bool:
    date_pattern = re.compile(r"\d+/\d+/\d+")
    return bool(date_pattern.match(text))

def regex_find_dates(text: str) -> list:
    date_pattern = re.compile(r"\d+/\d+/\d+")
    return date_pattern.findall(text)

def exact_regex_match(text: str) -> bool:
    pattern = re.compile(r"(\d+)/(\d+)/(\d+)$")
    return bool(pattern.match(text))

def read_file_and_find_txt(file_path: str):
    with open(file_path, "r") as file:
        content = file.read()
    txt_pattern = re.compile(r"\w+\.txt")
    return txt_pattern.findall(content)


# Example usage:
if __name__ == "__main__":
    fname = "arquivo.txt"
    print("Ends with .txt:", check_file_extension(fname))
    print("Starts with 'arq':", check_file_start(fname, "arq"))
    print("fnmatch '*.txt':", filename_pattern_match(fname, "*.txt"))
    print("fnmatchcase '*.TXT' case sensitive:", filename_pattern_case_sensitive(fname, "*.TXT"))

    sample_text = "11/04/2010"
    print("Regex date match:", regex_match_date(sample_text))

    random_text = "blablabla 12/11/2010, adadsada 10/10/1994"
    print("Dates found:", regex_find_dates(random_text))

    print("Exact regex match end:", exact_regex_match("27/12/1987marcos"))
    print("Exact regex match correct:", exact_regex_match("27/12/1987"))


