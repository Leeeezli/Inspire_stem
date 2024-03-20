const randomNumber = math.floor(Math.random() * 100) + 1 ;
let attempt = 0 ;

function checkGuess(){
    const guess = parseint(document.getElementById("guessField").value)
    attempt++;
    if(isNaN(guess) || guess < 1 || guess > 100){
        setMesage("Please enter a valid number between 1 and 100")
        return;
    }
    if (guess === randomNumber){
        setMesage("Congratulation ! Guessed correctly")
        document.getElementById("guessField").disabled = true;
    }else if(guess < randomNumber){
        setMessage("Too low try again")
    }else(
        setMessage("Too hogh try again")
    )
}
function setMessage(message){
    document.getElementById("message").textContent = message;
}