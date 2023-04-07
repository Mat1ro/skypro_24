from typing import List, Union, TextIO
import re


def get_query(cmd: str, val: str, file: Union[str, List, TextIO]) -> Union[str, List]:
    if cmd == 'filter':
        return list(filter(lambda x: val in x, file))
    if cmd == 'map':
        return '\n'.join([x.split()[int(val)] for x in file])
    if cmd == 'unique':
        return list(set(file))
    if cmd == 'sort':
        is_reverse = val == 'desc'
        return sorted(file, reverse=is_reverse)
    if cmd == 'limit':
        return list(file)[:int(val)]
    if cmd == "regex":
        regexp: re.Pattern = re.compile(val)
        return list(filter(lambda v: regexp.findall(v), file))

    return ''