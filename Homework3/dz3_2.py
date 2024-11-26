import re
import toml

# Регулярные выражения для синтаксиса языка
comment_regex = re.compile(r'{-(.*?)-}', re.DOTALL)
var_regex = re.compile(r'var\s+(\w+)\s+(.*)')
constant_regex = re.compile(r'#{(\w+)}')
array_regex = re.compile(r'\[(.*?)\]', re.DOTALL)
dict_regex = re.compile(r'dict\((.*?)\)', re.DOTALL)

constants = {}


def parse_value(value):
    value = value.strip().rstrip(',')  # Убираем запятую в конце
    # Проверка на числовое значение
    if value.isdigit():
        return int(value)
    # Проверка на строку с экранированными кавычками
    elif value.startswith('"') and value.endswith('"'):
        return value.strip('"').replace('\\"', '"')
    # Проверка на словарь
    elif dict_regex.match(value):
        items = dict_regex.findall(value)[0].split(',')
        result = {}
        for item in items:
            if '=' in item:
                key, val = item.split('=', 1)
                result[key.strip()] = parse_value(val.strip())
        return result
    else:
        return constants.get(value, value)

def process_line(line):
    # Удаление комментариев
    line = comment_regex.sub('', line).strip()
    if not line:
        return ''
    # Обработка объявления переменных
    if var_regex.match(line):
        name, value = var_regex.findall(line)[0]
        constants[name] = parse_value(value)
        return ''
    # Замена констант
    line = constant_regex.sub(lambda x: str(constants.get(x.group(1), x.group(0))), line)
    return line.strip().rstrip(',')  # Убираем лишние запятые

def process_config(config_lines):
    result = {}
    current_key = None
    current_value = []

    for line in config_lines:
        line = line.strip()
        if not line:
            continue
        # Проверка на завершённость структуры
        if line.endswith("("):
            current_key = line.split("=", 1)[0].strip()
            current_value.append(line.split("(", 1)[1].strip())
            continue
        elif current_key:
            if ")" in line:
                current_value.append(line.split(")")[0].strip())
                result[current_key] = parse_value("dict(" + ",".join(current_value) + ")")
                current_key = None
                current_value = []
            else:
                current_value.append(line.strip())
        elif '=' in line:
            key, value = line.split('=', 1)
            result[key.strip()] = parse_value(value.strip())
    return result


def main():
    try:
        with open('input.txt', 'r') as file:
            input_data = file.read()
    except FileNotFoundError:
        print("Файл 'input.txt' не найден.")
        return

    processed_data = []
    for line in input_data.splitlines():
        processed_line = process_line(line)
        if processed_line:
            processed_data.append(processed_line)

    config_result = process_config(processed_data)
    print(toml.dumps(config_result))


if __name__ == '__main__':
    main()
