const likeForms = document.querySelectorAll('.like-form')

// Add a submit event listener to each form
likeForms.forEach(function (form) {
    form.addEventListener('submit', async function (event) {
        event.preventDefault()

        const form_id_split = form.id.split("form_like_recipe_")
        const recipe_id = form_id_split[1]

        try {
            const frm = form
            const conn = await fetch("/like-opskrift", {
                method: "POST",
                body: new FormData(frm)
            })
    
            //hent respons fra API
            const data = await conn.json()
            if(!conn.ok) {
                console.log("Kan ikke like opskrift")
                return
            }
    
            // Success
            if(conn.ok && data.info == "ok") {
                const unsolid_hrt = document.getElementById(`unsolid_hrt_${recipe_id}`)
                const solid_hrt = document.getElementById(`solid_hrt_${recipe_id}`)

                if (unsolid_hrt.classList.contains("hidden")){
                    unsolid_hrt.classList.remove("hidden")
                    solid_hrt.classList.add("hidden")
                }
                else {
                    solid_hrt.classList.remove("hidden")
                    unsolid_hrt.classList.add("hidden")
                }
            }

        } catch ({ name, message }) {
            console.log(name)
            console.log(message)
        }        
    })
})
