
// toggle edit profile - på profil
const toggle_edit_profile_btn = document.getElementById("toggle_edit_profile_btn")

toggle_edit_profile_btn.addEventListener("click", function() {
    const edit_profile = document.getElementById("edit_profile")

    if(edit_profile.classList.contains("fixed")) {
        edit_profile.classList.remove("fixed")
        edit_profile.classList.add("hidden")
    } else {
        edit_profile.classList.remove("hidden")
        edit_profile.classList.add("fixed")
    }
})


// Opdater brugerens oplysninger
const update_profile_btn = document.getElementById("update_profile_btn") // btn

update_profile_btn.addEventListener("click", async function() {
    try {
        const frm = event.target.form
        sanitizeInputs()

        const conn = await fetch("/opdater-profil", {
            method: "PUT",
            body: new FormData(frm)
        })
        
        //hent respons fra API
        const data = await conn.json()
        if(!conn.ok) {
            showTip(data.info)
            return
        }
        
        if(conn.ok && data.info == "ok") {
            // Success
            location.href = `/${data.username}`
        }
        
        } catch ({ name, message }) {
            console.log(name)
            console.log(message)
    }
})


// Vis tip til brugere ved forkert data
function showTip(message) {
    const tip_id = Math.random()
    const tip = `
    <p data-tip-id="${tip_id}" class="flex justify-center w-fit px-8 mx-auto py-4 text-white">
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









// Luk opdater-profil ved klik på "annuller" knap
const cancel_edit_profile_btn = document.getElementById("cancel_edit_profile_btn") // btn

cancel_edit_profile_btn.addEventListener("click", function() {
    const edit_profile = document.getElementById("edit_profile")

    edit_profile.classList.remove("fixed")
    edit_profile.classList.add("hidden")
})