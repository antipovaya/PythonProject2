



import warnings

warnings.filterwarnings('ignore')



with open('__init__.py', 'a', encoding='utf-8') as file:
    file.write('def rename_files (desired_name, num_digits, source_ext, target_ext, name_range=None):')


with open("__init__.py", "r") as init_file:
    code = init_file.read()

function_names = [
    "def rename_files"
]

for func_name in function_names:
    if func_name not in code:
        print(f"Функция {func_name} не найдена в файле __init__.py")
    else:
        print(f"Функция {func_name} найдена в файле __init__.py")