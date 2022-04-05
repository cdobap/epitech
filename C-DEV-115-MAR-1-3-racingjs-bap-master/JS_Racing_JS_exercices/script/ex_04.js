window.onload = function(){   
    let e = document.querySelector("html")
    let elt = document.querySelector("footer div")
  
    let str = ""
    e.addEventListener('keydown', (event) => {
      str +=  event.key  
      if(str.length > 42){
        sub = str.substr(-42)
        elt.innerHTML = sub
        console.log(sub.length)
      }   
      else{
        elt.innerHTML = str 
      } 
    })
}