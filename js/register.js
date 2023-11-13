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


// Vis message til brugere ved forkert login
function showTip(message) {
    const tip_id = Math.random()
    const tip = `
    <p data-tip-id="${tip_id}" class="flex justify-center w-fit px-8 mx-auto py-3 mb-4 text-white bg-red-400 rounded-md">
       ${message}
    </p>
    `
    document.querySelector("#tips").insertAdjacentHTML("afterbegin", tip)
    setTimeout(function() {
        document.querySelector(`[data-tip-id='${tip_id}']`).remove()
    }, 3000)
}

function show_uploaded_images() {  
    // Hvis billederne i deres kasse, når der er valgt et nyt billede
    // Upload profil billede
    let uploaded_profil_pic = ""
    const uploaded_profil_pic_input = document.getElementById("uploaded_profil_pic_input")

    uploaded_profil_pic_input.addEventListener("change", function() {
        const reader = new FileReader()
        reader.addEventListener("load", () => {
            uploaded_profil_pic = reader.result
            document.getElementById("uploaded_profil_pic").src = uploaded_profil_pic
        })
        reader.readAsDataURL(this.files[0])
    })


    // Upload profil banner
    let uploaded_banner = ""
    const uploaded_banner_input = document.getElementById("uploaded_banner_input")

    uploaded_banner_input.addEventListener("change", function() {
        const reader = new FileReader()
        reader.addEventListener("load", () => {
        uploaded_banner = reader.result
        document.getElementById("uploaded_banner").src = uploaded_banner
        })
        reader.readAsDataURL(this.files[0])
    })

}
  
  // Kald når js filen bliver importeret
  show_uploaded_images()