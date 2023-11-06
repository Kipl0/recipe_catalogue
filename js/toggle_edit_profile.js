
// toggle edit profile - på profil
function edit_profile() {
    const edit_profile = document.getElementById("edit_profile")
    const toggle_edit_profile = document.getElementById("toggle_edit_profile") // btn

    toggle_edit_profile.addEventListener("click", function() {

        
        if(edit_profile.classList.contains("fixed")) {
            edit_profile.classList.remove("fixed")
            edit_profile.classList.add("hidden")
        } else {
            edit_profile.classList.remove("hidden")
            edit_profile.classList.add("fixed")
        }
    })
}
edit_profile()


function update_edit_profile() {
    const edit_profile = document.getElementById("edit_profile")
    const update_edit_profile = document.getElementById("update_edit_profile") // btn

    update_edit_profile.addEventListener("click", function() {

        
        if(edit_profile.classList.contains("fixed")) {
            edit_profile.classList.remove("fixed")
            edit_profile.classList.add("hidden")
        } else {
            edit_profile.classList.remove("hidden")
            edit_profile.classList.add("fixed")
        }
    })
}
update_edit_profile()


function cancel_edit_profile() {
    const edit_profile = document.getElementById("edit_profile")
    const cancel_edit_profile = document.getElementById("cancel_edit_profile") // btn

    cancel_edit_profile.addEventListener("click", function() {

        
        if(edit_profile.classList.contains("fixed")) {
            edit_profile.classList.remove("fixed")
            edit_profile.classList.add("hidden")
        } else {
            edit_profile.classList.remove("hidden")
            edit_profile.classList.add("fixed")
        }
    })
}
cancel_edit_profile()