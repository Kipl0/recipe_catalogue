
// Hent login knappen ved hjælp af id
// CSP forhindre inline onclick functions
const loginButton = document.getElementById("loginButton")

// Tilføj en event listener til knappen
loginButton.addEventListener("click", async function() {
    try {
        const frm = event.target.form
        console.log("1") 
        console.log("frm", frm) 
        const conn = await fetch("/login", {
            method: "POST",
            body: new FormData(frm)
        })
        console.log("2")
        console.log("conn", conn)

        // Hent response fra API
        const data = await conn.json()
        console.log("3")
        console.log("data", data)
        if (!conn.ok || data.info != "ok") {
            console.log("4")
            showTip(data.info)
            return
        }

        console.log("5")
        console.log(data.info)
        if(conn.ok && data.info == "ok") {
            console.log("6")
            // Success
            location.href = "/"
        }

        console.log("7")
    } catch ({ name, message }) {
        console.log(name)
        console.log("8")
        console.log(message)
    }
})


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