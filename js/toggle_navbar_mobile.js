//  toggle navbar visibility for mobil

function toggle_navbar() {
    const bars = document.getElementById("toggle_navbar_bars")    
    const navbar_ul = document.getElementById("navbar_ul")

    if(navbar_ul.classList.contains("hidden")) {
        navbar_ul.classList.add("flex")
        navbar_ul.classList.remove("hidden")

        bars.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="currentColor" d="M18.36 19.78L12 13.41l-6.36 6.37l-1.42-1.42L10.59 12L4.22 5.64l1.42-1.42L12 10.59l6.36-6.36l1.41 1.41L13.41 12l6.36 6.36z"/></svg>'
        
    } else {
        navbar_ul.classList.add("hidden")
        navbar_ul.classList.remove("flex")
        
        bars.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 14 14"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" d="M13.5 2H.5m13 5H.5m13 5H.5"/></svg>'
    }
}
