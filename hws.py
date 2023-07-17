from transformers import MarianMTModel, MarianTokenizer


model_name_en = 'Helsinki-NLP/opus-mt-ru-en'
tokenizer_ru_en = MarianTokenizer.from_pretrained(model_name_en)
model_ru_en = MarianMTModel.from_pretrained(model_name_en)

model_name_ru = 'Helsinki-NLP/opus-mt-en-ru'
tokenizer_en_ru = MarianTokenizer.from_pretrained(model_name_ru)
model_en_ru = MarianMTModel.from_pretrained(model_name_ru)


def translate(text, from_lang):
    if from_lang == 'ru':
        inputs = tokenizer_ru_en.encode(text, return_tensors='pt', max_length=10024, truncation=True)
        outputs = model_ru_en.generate(inputs, max_length=10024, num_beams=24, early_stopping=True)
        return [tokenizer_ru_en.decode(t, skip_special_tokens=True) for t in outputs]

    inputs = tokenizer_en_ru.encode(text, return_tensors='pt', max_length=10024, truncation=True)
    outputs = model_en_ru.generate(inputs, max_length=10024, num_beams=24, early_stopping=True)
    return [tokenizer_en_ru.decode(t, skip_special_tokens=True) for t in outputs]
