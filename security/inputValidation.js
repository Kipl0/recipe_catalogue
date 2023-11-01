
function sanitizeInputs() {
    const inputFields = document.querySelectorAll('input[type="text"], input[type="password"], textare')
    
    inputFields.forEach(function(inputField) {
        let inputValue = inputField.value
        var sanitizedInput = DOMPurify.sanitize(inputValue)
    })
}

// brug sanitizedInput til at sætte videre