import subprocess
import os
import shutil
import sys

def count_pairs(file_path, word1, word2, max_distance):
    abs_file_path = os.path.abspath(file_path)
    print(f"Поиск файла: {abs_file_path}") 
    
    if not os.path.exists(abs_file_path):
        raise FileNotFoundError(f"Файл не найден: {abs_file_path}")

    cpp_app = os.path.join(
        os.path.dirname(__file__), 
        "..", 
        "cpp_app", 
        "build", 
        "count_pairs"
    )
    
    if not os.path.exists(cpp_app):
        raise FileNotFoundError(f"C++ программа не найдена: {cpp_app}")

    try:
        result = subprocess.run(
            [cpp_app, abs_file_path, word1, word2, str(max_distance)],
            capture_output=True,
            text=True,
            encoding='utf-8',
            check=True
        )
        return int(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Ошибка C++ программы: {e.stderr}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Использование: python main.py <файл> <слово1> <слово2> <расстояние>")
        sys.exit(1)
    
    try:
        result = count_pairs(sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]))
        print(result)
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)