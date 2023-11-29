function sanitizeInputs() { 
    const inputFields = document.querySelectorAll('input[type="text"], input[type="password"], textarea')
    
    inputFields.forEach(function(inputField) { 
        let inputValue = inputField.value
        
        var sanitizedInput = DOMPurify.sanitize(inputValue)
        
        if(inputValue != sanitizedInput){
            console.log("OBS! Denne: " + inputValue + " blev ændret til: " + sanitizedInput)
        }
        // Brug sanitizedInput her eller returnér det, afhængigt af hvad du vil gøre
    })
}