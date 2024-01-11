
function create_recipe() {
    const create_recipe_btn = document.getElementById("create_recipe_btn")

    create_recipe_btn.addEventListener("click", async function() {
        try {
            const frm = event.target.form
            /* eslint-disable */
            sanitizeInputs()

            const conn = await fetch("/opret-opskrift", {
                method: "POST",
                body: new FormData(frm)
            })

            //hent respons fra API
            const data = await conn.json()
            if(!conn.ok) {
                /* eslint-disable */
                showTip("ugyldigt")
                return
            }

            if(conn.ok && data.info == "ok") {
                // Success
                location.href = "/"
            }
            
        } catch ({ name, message }) {
            console.log(name)
            console.log(message)
        }
    })
}

create_recipe()


function show_uploaded_images() {  
    // Hvis billederne i deres kasse, når der er valgt et nyt billede
    // Upload profil banner
    let image_thumbnail = ""
    const image_thumbnail_input = document.getElementById("image_thumbnail_input")

    image_thumbnail_input.addEventListener("change", function() {
        const reader = new FileReader()
        reader.addEventListener("load", () => {
            image_thumbnail = reader.result
            document.getElementById("image_thumbnail").src = image_thumbnail
        })
        reader.readAsDataURL(this.files[0])
    })


} 
// Kald når js filen bliver importeret
show_uploaded_images()



let ingredient_counter = 0
// Ingrediens 
function add_ingredient() {
    const insertIngredient = document.getElementById("insertIngredient")
    insertIngredient.addEventListener("click", function() {
        // const ingredient_ol = document.getElementById("ingredient_ol")
        ingredient_counter += 1

        const ingredient_id = Math.random()
        const ingredient = `
            <li id="${ingredient_id}" class="ml-5">
                <div class="flex items-center">
                    <input type="text" name="ingredient_${ingredient_counter}" placeholder="Ingrediens" class="px-3 py-1 rounded-xl w-full max-w-[300px] " minlength="5" maxlength="30">
                    <svg class="cursor-pointer w-6 h-6 text-current ml-2 delete-ingredient" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V9c0-1.1-.9-2-2-2H8c-1.1 0-2 .9-2 2v10zM18 4h-2.5l-.71-.71c-.18-.18-.44-.29-.7-.29H9.91c-.26 0-.52.11-.70.29L8.5 4H6c-.55 0-1 .45-1 1s.45 1 1 1h12c.55 0 1-.45 1-1s-.45-1-1-1z"/>
                    </svg>
                </div>
            </li>
        `
        document.querySelector("#ingredient_ol").insertAdjacentHTML("beforeend", ingredient)
    })

    // Tilføj en eventlistener til "path" i skraldespands-ikonet ved "mousedown" for at slette li-elementet
    document.addEventListener("click", function(event) {
        if (event.target && event.target.tagName === "path" || event.target.classList.contains("delete-ingredient")) {
            const liToDelete = event.target.closest("li")
            if (liToDelete) {
                liToDelete.remove()
            }
        }
    })
}
add_ingredient()



let step_counter = 0
// Fremgangsmåde 
function add_step() {
    const insertStep = document.getElementById("insertStep")
    insertStep.addEventListener("click", function() {  
        // const step_guide_ol = document.getElementById("step_guide_ol") 
        step_counter += 1
        const step_id = Math.random()
        const step = `
            <li id="${step_id}" class="ml-5">
                <div class="flex items-center">
                <textarea type="text" name="step_${step_counter}" placeholder="Fremgangsmåde" class="px-3 py-1 rounded-xl w-full max-w-[450px] max-h-[100px] md:min-w-[300px]" minlength="5" maxlength="255"></textarea>
                    <svg class="cursor-pointer w-6 h-6 text-current ml-2 delete-step" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V9c0-1.1-.9-2-2-2H8c-1.1 0-2 .9-2 2v10zM18 4h-2.5l-.71-.71c-.18-.18-.44-.29-.7-.29H9.91c-.26 0-.52.11-.70.29L8.5 4H6c-.55 0-1 .45-1 1s.45 1 1 1h12c.55 0 1-.45 1-1s-.45-1-1-1z"/>
                    </svg>
                </div>
            </li>
        `
        document.querySelector("#step_guide_ol").insertAdjacentHTML("beforeend", step)
    })
        // Tilføj en hændelseslytter til "path" i skraldespands-ikonet ved "mousedown" for at slette li-elementet
        document.addEventListener("click", function(event) {
            if (event.target && event.target.tagName === "path" || event.target.classList.contains("delete-step")) {
                const liToDelete = event.target.closest("li")
                if (liToDelete) {
                    liToDelete.remove()
                }
            }
        })
}
add_step()

