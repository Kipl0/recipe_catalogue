// // Santiagos library for validating files

// // ##############################
// function validate(callback){
//     let form = event.target.form
//     if(form == undefined){
//       form = event.target
//     }
    
//     const infoText = document.getElementById("infoText")
//     infoText.innerHTML = ""
//     infoText.classList.add("hidden")

//     const validate_error = "bg-[#FF3F64]"
    
//     console.log(infoText)
//     form.querySelectorAll("[data-validate]").forEach(function(element){ 
//       console.log(element)
//       element.classList.remove("validate_error")
//       element.classList.remove("bg-red-400")
//     })

//     form.querySelectorAll("[data-validate]").forEach( function(element){
//       switch(element.getAttribute("data-validate")){
//         case "str":
//           if( element.value.length < parseInt(element.getAttribute("data-min")) || 
//               element.value.length > parseInt(element.getAttribute("data-max")) 
//           ){
//             element.classList.add("validate_error")
//             element.classList.add("bg-red-400")

//             infoText.innerHTML = `Skal være mellem ${element.getAttribute("data-min")} og ${element.getAttribute("data-max")} karakterer`
//             infoText.classList.remove("hidden")
//           }
//         break;

//         case "int":
//           if( ! /^\d+$/.test(element.value)  ||
//               parseInt(element.value) < parseInt(element.getAttribute("data-min")) || 
//               parseInt(element.value) > parseInt(element.getAttribute("data-max"))
//           ){
//             element.classList.add("validate_error")
//             element.style.backgroundColor = validate_error
//           }
//         break;     

//         case "email":
//           let re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
//           if( ! re.test(element.value.toLowerCase()) ){
//             element.classList.add("validate_error")
//             element.style.backgroundColor = validate_error
//           }
//         break;

//         case "regex":       
//           var regex = new RegExp(element.getAttribute("data-regex"))
//           if( ! regex.test(element.value) ){
//             console.log(element.value)
//             console.log("regex error")
//             element.classList.add("validate_error")
//             element.style.backgroundColor = validate_error
//           }
//         break;

//         case "match":
//           if( element.value != form.querySelector(`[name='${element.getAttribute("data-match-name")}']`).value ){
//             element.classList.add("validate_error")
//             element.style.backgroundColor = validate_error
//           }
//         break;

//       }
//     })
//     if( ! form.querySelector(".validate_error") ){ callback(); return }
//     form.querySelector(".validate_error").focus()
//   }
  