document.addEventListener('DOMContentLoaded', function () {
    // Din eksisterende JavaScript-kode her
    let the_timer

    // Hide
    function hideSearchResults() {
        clearTimeout(the_timer)
        the_timer = setTimeout(async function () {
            document.querySelector("#search_results").classList.add("hidden")
        }, 700)
    }

    function search() {
        clearTimeout(the_timer)

        const frm = event.target.form

        the_timer = setTimeout(async function () {
            const conn = await fetch("/search-recipe", {
                method: "POST",
                body: new FormData(frm),
            })

            const data = await conn.json()
            let results = ""

            document.querySelector("#search_results").innerHTML = ""
            data.forEach((item) => {
                results += `<a href="/${item.recipe_name}" class="flex flex-col px-4 py-3 hover:bg-[#c7bbb8]">
                                <section class="flex items-center gap-6">
                                    <img src="/images/recipe_thumbnails/${item.recipe_thumbnail}" alt="" class="w-12 rounded-full aspect-square">
                                    <section >
                                        <div>${item.recipe_name}</div>         
                                    </section>
                                </section>
                            </a>
                            `
            })

            document
                .querySelector("#search_results")
                .insertAdjacentHTML("afterbegin", results)

            document.querySelector("#search_results").classList.remove("hidden")
            document.querySelector("#search_results").classList.add("flex")
        }, 500)
    }

    // Add event listeners
    document.getElementById('searchInput').addEventListener('input', search)
    document.getElementById('searchInput').addEventListener('blur', hideSearchResults)
})
