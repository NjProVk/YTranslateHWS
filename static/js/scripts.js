const textFromTranslate = document.getElementsByClassName('original')[0];
const textToTranslate = document.getElementById('translate');
const loader = document.querySelector('.loader');
const overlay = document.querySelector('.overlay');

let start_num = 0;
let end_num = 0;


function debounce(func, delay) {
    let debounceTimer;
    return function() {
        const context = this;
        const args = arguments;
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(() => func.apply(context, args), delay);
    };
}


function checkStatus() {
    end_num += 1

    if (start_num === end_num) {
        loader.style.visibility = 'hidden';
        overlay.style.visibility = 'hidden';
    }
}


function getTranslateNow() {

    if (!textFromTranslate.value || textFromTranslate.value.replace(/\s/g, '').length <= 1) {
        return false;
    }

    start_num += 1
    loader.style.visibility = 'visible';
    overlay.style.visibility = 'visible';

    let fromToLanguage = document.getElementById('lang');

    fetch('http://localhost:8894/translate', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            text: textFromTranslate.value,
            'language': fromToLanguage.value
        })
    })
    .then(response => response.json())
    .then(data => {
        textToTranslate.value = data.value;
        checkStatus()
    })
    .catch((error) => {
        console.error('Error:', error)
        checkStatus()
    });
}

let debouncedTranslate = debounce(getTranslateNow, 500);
