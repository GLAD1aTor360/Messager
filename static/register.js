let z=document.getElementById("hg")
z.addEventListener("click", ()=>{
    window.location.href="/login"
})
let x=document.getElementById("r")
let c=document.getElementById("t")
let co=0
x.addEventListener("click", ()=>{
    if(co===0){
            x.src="/static/icons/hidden.png"
            co=1
            c.type="text"
    }
    else{
        x.src="/static/icons/eye.png"
        co=0
        c.type="password"
    }
})
let x2=document.getElementById("r2")
let c2=document.getElementById("t2")
let co2=0
x2.addEventListener("click", ()=>{
    if(co2===0){
            x2.src="/static/icons/hidden.png"
            co2=1
            c2.type="text"
    }
    else{
        x2.src="/static/icons/eye.png"
        co2=0
        c2.type="password"
    }
})