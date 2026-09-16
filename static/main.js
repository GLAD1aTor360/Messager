let form=document.getElementById("form")
let t=document.getElementById("plus")
let dark=document.getElementById("dark")
if(t!=null && t!=undefined){
    t.addEventListener("click", ()=>{
        dark.hidden=false
    })
}
dark.hidden=true
dark.addEventListener("click", (y)=>{
    if(!form.contains(y.target)){
        dark.hidden=true
    }
})
// let phone=document.getElementById("phone")
// phone.addEventListener("input", (e)=>{
//     if(phone.value.length<4){
//         phone.value="+7 "
//         return
//     }
//     if(!("0123456789".contains(e.key))){
//         phone.value=phone.value.slice(0,phone.value.length-2)
//         return
//     }
// })
let plus19=document.getElementById("plus19")
if(plus19!=null && plus19!=undefined){
    plus19.addEventListener("click", ()=>{
        dark.hidden=false
    })
}
let g=document.getElementById("textarea")
g.addEventListener("input", ()=>{
        g.style.height="auto"
        g.style.height=(g.scrollHeight)+"px"
        g.style.maxHeight="300px"
})

let poisk=document.getElementById("one")
poisk.addEventListener("input", ()=>{
    let te=poisk.value
    for(let x of document.getElementsByClassName("conname")){
        if(x.textContent.contains(te)){
            
        }
    }
})