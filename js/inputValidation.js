function sanitizeInputs() {  // eslint-disable-line no-unused-vars
    const inputFields = document.querySelectorAll('input[type="text"], input[type="password"], textarea')
    
    inputFields.forEach(function(inputField) { 
        let inputValue = inputField.value
        /* eslint-disable */
        var sanitizedInput = DOMPurify.sanitize(inputValue)
        
        if(inputValue != sanitizedInput){
            console.log("OBS! Denne: " + inputValue + " blev ændret til: " + sanitizedInput)
        }
    })
}