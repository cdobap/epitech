window.onload = function(){   
  let e = document.querySelector("footer div")
    let i = 1
    e.onclick = function() {          
      e.innerHTML = i++
    }
}
