
// toggle edit profile - på profil

function edit_profile() {
    const edit_profile = document.getElementById("edit_profile")

    if(edit_profile.classList.contains("fixed")) {
        edit_profile.classList.remove("fixed")
        edit_profile.classList.add("hidden")
    } else {
        edit_profile.classList.remove("hidden")
        edit_profile.classList.add("fixed")
    }
}