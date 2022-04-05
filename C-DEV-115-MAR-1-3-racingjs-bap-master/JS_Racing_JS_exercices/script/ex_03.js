window.onload = function(){   
  let popup = document.querySelector("footer div")
  popup.onclick = function checkPopup() {    
    if( name = prompt("What is your name")){
      if(confirm("Are you sure " +name +" is your name ?")){
        popup.innerHTML = "Hello " +name
        alert("Hello " + name)
      }
    }
    else{ 
      checkPopup()
    }
  }
}