
// Hent login knappen ved hjælp af id
// CSP forhindre inline onclick functions
const loginButton = document.getElementById("loginButton")

// Tilføj en event listener til knappen
loginButton.addEventListener("click", async function() {
    try {
        const frm = event.target.form
        // console.log(frm)
        const conn = await fetch("/login", {
            method: "POST",
            body: new FormData(frm)
        })

        // Hent response fra API
        const data = await conn.json()
        console.log(data.info)
        if (!conn.ok) {
            showTip("Ugyldigt login")
            return
        }

        // Success
        location.href = "/"

    } catch ({ name, message }) {
        console.log(name)
        console.log(message)
    }
})


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