import re
from pathlib import Path

path_regex = re.compile(r'^.+?("[^"]+?")[^"]+?$')

result_file_path = Path(__file__).parent
result_file_path = '%s/result.txt' % result_file_path
result_file_path = Path(result_file_path)
result_file = open(result_file_path, 'w')
result_file.write('')
result_file.close()

result_set = {}

log_file_path = Path(__file__).parent
log_file_path = '%s/access.log' % log_file_path
log_file_path = Path(log_file_path)
if log_file_path.exists():
    log_file = open(log_file_path, 'r')
    for line in log_file:
        path_search_result = path_regex.search(line)
        if path_search_result is not None:
            match_result = path_search_result.group(1)
            if match_result in result_set:
                result_set[match_result] += 1
            else:
                result_set[match_result] = 1
    log_file.close()

    result_set = dict(sorted(result_set.items(), key=lambda item: item[1]))

    result_file = open(result_file_path, 'a')

    for key in result_set:
        result_file.write('[' + str(result_set[key]) + ']')
        result_file.write(' ')
        result_file.write(key)
        result_file.write('\n')

    result_file.close()
