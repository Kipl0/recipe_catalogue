// Registrerer brugeren i systemet

async function register() {
    try {
        // Hen event target -> vores form
        const frm = event.target 

        // Lav request til API om at registrerer brugeren
        const conn = await fetch("/opret-bruger", {
            method : "POST",
            body : new FormData(frm)
        })

        // Hent response fra API
        const data = await conn.json()
        if (conn.status == 400) {
            const infoText = document.getElementById("infoText")
            infoText.innerHTML = data.infoText
            infoText.classList.remove("hidden")
            return
        } 
        // Tjek om requestet gik igennem og throw en error
        else if( !conn.ok || data.info != "ok" ) {
            throw new TypeError("Something went wrong")
        }
        const infoText = document.getElementById("infoText")
        infoText.innerHTML = "Bruger oprettet, gå til login"
        infoText.classList.remove("hidden")
    }
    catch({ name, message }) {
        console.log(name)
        console.log(message)
    }
}