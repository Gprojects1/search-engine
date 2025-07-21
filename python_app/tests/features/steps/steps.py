from behave import *
import subprocess
import os
from pathlib import Path

CPP_APP_PATH = (
    Path(__file__).parent.parent.parent.parent  
    / ".."  
    / "cpp_app" 
    / "build" 
    / "count_pairs"
).resolve()

print(f"Путь к count_pairs: {CPP_APP_PATH}")

@given('подготовили тестовый файл "{filename}"')
def step_prepare_test_file(context, filename):
    context.test_dir = Path(__file__).parent / "test_files"
    context.test_dir.mkdir(exist_ok=True)
    context.test_file = context.test_dir / filename
    
    test_content = (
        "налоги на доходы физических лиц в России, "
        "налоги на доходы физических лиц в Казахстане"
    )
    context.test_file.write_text(test_content, encoding="utf-8")

@when('запускаем приложение count_pairs с недостаточным числом аргументов')
def step_run_with_few_args(context):
    try:
        context.process = subprocess.run(
            [str(CPP_APP_PATH)],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )
    except Exception as e:
        context.error = str(e)
        raise

@when('ищем пару слов "{word1}" и "{word2}" на расстоянии, не превышающем {distance:d} слов')
def step_search_pair(context, word1, word2, distance):
    try:
        context.process = subprocess.run(
            [str(CPP_APP_PATH), str(context.test_file), word1, word2, str(distance)],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )
        context.output = context.process.stdout.strip()
    except Exception as e:
        context.error = str(e)
        raise

@then('получаем сообщение об ошибке')
def step_check_error(context):
    assert hasattr(context, 'process'), "Приложение не было запущено"
    assert context.process.returncode != 0, "Ожидалась ошибка, но программа завершилась успешно"
    assert "Usage" in context.process.stderr, "Нет ожидаемого сообщения об ошибке"

@then('находим {expected_count:d} такую пару в тестовом файле')
def step_check_pair_count(context, expected_count):
    assert hasattr(context, 'process'), "Приложение не было запущено"
    assert context.process.returncode == 0, f"Ошибка выполнения: {context.process.stderr}"
    assert context.output == str(expected_count), \
        f"Ожидалось {expected_count}, получено {context.output}"
    
@then('находим 0 таких пар в тестовом файле')
def step_impl(context):
    assert context.process.returncode == 0, f"Ошибка: {context.process.stderr}"
    assert context.output == "0", \
        f"Ожидалось 0, получено {context.output}"

@then('находим 2 такие пары в тестовом файле')
def step_impl(context):
    assert context.process.returncode == 0, f"Ошибка: {context.process.stderr}"
    assert context.output == "2", \
        f"Ожидалось 2, получено {context.output}"