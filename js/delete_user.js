const deleteForms = document.querySelectorAll('.delete-form')


// Add a submit event listener to each form
deleteForms.forEach(function (form) {
    form.addEventListener('click', function (event) {
        event.preventDefault()

        const form_id_split = form.id.split("form_delete_user_")
        const user_id = form_id_split[1]

        const trashcan = document.getElementById(`trashcan_${user_id}`)
        trashcan.classList.add("hidden")
        trashcan.classList.remove("flex")


        // knapperne der faktisk gør noget.
        const buttons_container = document.getElementById(`buttons_con_${user_id}`)

        buttons_container.classList.remove("hidden")
        buttons_container.classList.add("flex")

        const confirm = document.getElementById(`confirm_${user_id}`)
        const cancel = document.getElementById(`cancel_${user_id}`)


        // Cancel knappen
        cancel.addEventListener('click', function() {
            buttons_container.classList.add("hidden")
            buttons_container.classList.remove("flex")
            
            trashcan.classList.add("flex")
            trashcan.classList.add("tester")
            trashcan.classList.remove("hidden")
        })
        
        // Den ville ikke skifte uden en timeout, det gik "for hurtigt"
        cancel.addEventListener('click', function() {            
            setTimeout(function() {
                buttons_container.classList.add("hidden")
                buttons_container.classList.remove("flex")
            }, 10)
            
            setTimeout(function() {
                trashcan.classList.add("flex")
                trashcan.classList.remove("hidden")
            }, 10)
        })
        
        
        confirm.addEventListener('click', async function() {            
            try {
                const frm = form
                const conn = await fetch("/delete-user", {
                    method: "POST",
                    body: new FormData(frm)
                })
        
                //hent respons fra API
                const data = await conn.json()
                if(!conn.ok) {
                    console.log("Kan ikke like følge bruger")
                    return
                }
        
                // Success
                if(conn.ok && data.info == "ok") {
                    const user_card = document.getElementById(`user_card_${user_id}`)
                    user_card.classList.add("hidden")
                    user_card.classList.remove("flex")

                    setTimeout(function() {
                        buttons_container.classList.add("hidden")
                        buttons_container.classList.remove("flex")
                    }, 10)
                    
                    setTimeout(function() {
                        trashcan.classList.add("flex")
                        trashcan.classList.remove("hidden")
                    }, 10)
                }

            } catch ({ name, message }) {
                console.log(name)
                console.log(message)
            }        
        })
    })
})
