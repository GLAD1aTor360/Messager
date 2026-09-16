const phoneInput = document.querySelector("#phone");

phoneInput.addEventListener("input", function () {

    // Оставляем только цифры
    let numbers = this.value.replace(/\D/g, "");

    // Максимум 10 цифр
    numbers = numbers.slice(0, 10);

    let result = "";

    // Код оператора
    if (numbers.length > 0) {
        result += "(" + numbers.slice(0, 3);
    }

    // Закрываем скобку после трёх цифр
    if (numbers.length >= 3) {
        result += ")";
    }

    // Следующие три цифры
    if (numbers.length > 3) {
        result += " " + numbers.slice(3, 6);
    }

    // Следующие две цифры
    if (numbers.length > 6) {
        result += "-" + numbers.slice(6, 8);
    }

    // Последние две цифры
    if (numbers.length > 8) {
        result += "-" + numbers.slice(8, 10);
    }

    this.value = result;
});