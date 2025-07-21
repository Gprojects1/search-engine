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
Для Windows (через WSL):
CopyRun
wsl --install
sudo apt update && sudo apt install -y g++ cmake python3 python3-pip
2. Сборка C++ приложения
CopyRun
cd cpp_app
mkdir build && cd build
cmake ..
make
3. Установка Python-зависимостей (для тестов)
CopyRun
pip install -r ../requirements.txt