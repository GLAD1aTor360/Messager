let z=document.getElementById("hg")
z.addEventListener("click", ()=>{
    window.location.href="/register"
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