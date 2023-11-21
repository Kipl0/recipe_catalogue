function toggle_profile_dropdown() {
    const profile_btn = document.getElementById("profile_btn")
    const profile_dropdown = document.getElementById("profile_dropdown")
    
    profile_btn.addEventListener("click", function() {
        if(profile_dropdown.classList.contains("hidden")) {
            profile_dropdown.classList.remove("hidden")
            profile_dropdown.classList.add("flex")
        }
        else {
            profile_dropdown.classList.remove("flex")
            profile_dropdown.classList.add("hidden")
        }
    })
}

toggle_profile_dropdown()