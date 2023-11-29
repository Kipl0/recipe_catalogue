
function create_collection() {

    const create_collection_btn = document.getElementById("create_collection_btn")

    create_collection_btn.addEventListener("click", async function() {
        try {
            const frm = event.target.form
            sanitizeInputs()
            
            const conn = await fetch("/opret-samling", {
                method: "POST",
                body: new FormData(frm)
            })
            
            //hent respons fra API
            const data = await conn.json()
            if(!conn.ok) {
                showTip("Kan ikke oprette samling")
                return
            }
            
            if(conn.ok && data.info == "ok") {
                // Success
                location.href = `/${data.username}/samlinger`
            }
            

    } catch ({ name, message }) {
            console.log(name)
            console.log(message)
        }
    })
}

create_collection()


// Vis message til brugere ved forkert login
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
    // Vis billederne i browser, når der er valgt et nyt billede
    let collection_thumbnail = ""
    const collection_thumbnail_input = document.getElementById("collection_thumbnail_input")

    collection_thumbnail_input.addEventListener("change", function() {
        const reader = new FileReader()
        reader.addEventListener("load", () => {
            collection_thumbnail = reader.result
            document.getElementById("collection_thumbnail").src = collection_thumbnail
        })
        reader.readAsDataURL(this.files[0])
    })
} 
// Kald når js filen bliver importeret
show_uploaded_images();