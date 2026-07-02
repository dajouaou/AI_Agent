const question = $input.first().json.question;

let answer = "";
let confidence = 0;

if (question.toLowerCase().includes("deai")) {

    answer = "DEAI staat voor Data Engineering & Artificial Intelligence.";
    confidence = 95;

} else {

    answer = "Ik weet het antwoord niet met voldoende zekerheid.";
    confidence = 20;

}

return [{
    json: {
        question,
        answer,
        confidence
    }
}];