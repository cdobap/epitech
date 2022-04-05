window.onload = function(){   
    let htmlPage = document.querySelector("body")
    let incSize = document.querySelectorAll("footer div button")[0]
    let decSize = document.querySelectorAll("footer div button")[1]

    var i = 16  
    incSize.onclick = function(event){
      i += 1
      htmlPage.style.fontSize = i +"px"     
    }    
    decSize.onclick = function(){
      i -= 1
      htmlPage.style.fontSize = i +"px"     
    }

    let selectlist = document.querySelector('footer div select')
    selectlist.addEventListener('change', (event) =>{
      const color = event.target.value
      document.body.style['background-color'] = color
    })
}