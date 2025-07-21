# search-engine

# Инструкция по установке и запуску count_pairs

## Установка

### Требования
- Компилятор C++ (g++/clang)
- CMake (версия 3.10+)
- Python 3.6+ (для тестов)

### 1. Установка зависимостей

#### Для Ubuntu/Debian:
```bash
sudo apt update
sudo apt install -y g++ cmake python3 python3-pip
```
Для Windows (через WSL):
```bash
wsl --install
sudo apt update && sudo apt install -y g++ cmake python3 python3-pip
```
2. Сборка C++ приложения
```bash
cd cpp_app
mkdir build && cd build
cmake ..
make
```
3. Установка Python-зависимостей (Необходима активация виртуальной среды)
```bash
pip install -r requirements.txt
```
4.  Запуск приложения 
```bash
cd python_app
python main.py <файл> <слово1> <слово2> <макс_расстояние> 
```
5. Запуск тестов
```bash 
cd python_app/tests
behave
```