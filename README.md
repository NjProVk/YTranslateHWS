# Instant Translator

An instant text translator utilizing Flask and Helsinki-NLP transformers. As you type into the input field, real-time translations are fetched via AJAX requests.

## 📝 Content

- [Project Structure](#project-structure)
- [Installation and Launch](#installation-and-launch)
  - [Using Docker](#using-docker)
  - [Without Docker](#without-docker)
- [Important Note](#important-note)

<a name="project-structure"></a>
## 📁 Project Structure

- **app.py**: Main Flask server file.
- **hws.py**: Houses translation functions using Helsinki-NLP transformers.
- **Dockerfile**: Instructions for containerizing the app.
- **requirements.txt**: Required dependencies.

<a name="installation-and-launch"></a>
## 🚀 Installation and Launch

<a name="using-docker"></a>
### Using Docker

1. Install Docker.
2. Build the Docker image: 
```bash
docker build -t instant-translator .
```
3. Run:
```bash
docker run -p 8894:8894 instant-translator
```

<a name="without-docker"></a>
### Without Docker

1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Run the Flask app:
```bash
python app.py
```

Visit `http://localhost:8894/` to use the translator.

<a name="important-note"></a>
## ⚠️ Important Note

Ensure you have sufficient RAM. Transformer models can be resource-intensive.


# Мгновенный Переводчик

Мгновенный переводчик текста на Flask и с трансформаторами Helsinki-NLP. При вводе в текстовое поле происходит мгновенный перевод с помощью AJAX-запросов.

## 📝 Содержание

- [Структура Проекта](#структура-проекта)
- [Установка и Запуск](#установка-и-запуск)
  - [С Docker](#с-docker)
  - [Без Docker](#без-docker)
- [Важное Примечание](#важное-примечание)


<a name="структура-проекта"></a>
## 📁 Структура Проекта

- **app.py**: Основной серверный файл Flask.
- **hws.py**: Функции перевода с использованием трансформаторов Helsinki-NLP.
- **Dockerfile**: Инструкции для контейнеризации приложения.
- **requirements.txt**: Необходимые зависимости.

<a name="установка-и-запуск"></a>
## 🚀 Установка и Запуск

<a name="с-docker"></a>
### С Docker

1. Установите Docker.
2. Соберите Docker-образ:
```bash
docker build -t instant-translator .
```
3. Запустите:
```bash
docker run -p 8894:8894 instant-translator
```

<a name="без-docker"></a>
### Без Docker

1. Установите зависимости:
```bash
pip install -r requirements.txt
```
2. Запустите Flask-приложение:
```bash
python app.py
```

Перейдите по адресу `http://localhost:8894/`, чтобы использовать переводчик.

<a name="важное-примечание"></a>
## ⚠️ Важное Примечание

Убедитесь, что у вас достаточно оперативной памяти. Модели трансформеров могут требовать много ресурсов.


