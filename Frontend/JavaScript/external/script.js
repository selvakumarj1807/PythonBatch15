function getValues() {
    inputArea = document.getElementById("contactForm");
    outputArea = document.getElementById("output");

    inputValues = inputArea.getElementsByTagName("input");
    outputValues = outputArea.getElementsByTagName("p");

    /*
    outputValues[0].innerHTML = inputValues[0].value;
    outputValues[1].innerHTML = inputValues[1].value;
    outputValues[2].innerHTML = inputValues[2].value;
    outputValues[3].innerHTML = inputValues[3].value;
    */

    for (i = 0; i < inputValues.length; i++) {
        outputValues[i].innerHTML = inputValues[i].value;
    }
}