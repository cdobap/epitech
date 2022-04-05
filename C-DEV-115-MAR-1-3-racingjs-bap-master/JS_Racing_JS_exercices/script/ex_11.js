window.onload = function(){   
    let okcookie = document.querySelector('a')    
    let foot = document.querySelector('footer')
    let firstbox = document.querySelectorAll('footer div')[0] 

      
      okcookie.addEventListener('click', () => {      
        document.cookie = "acceptsCookies=true; max-age=86400"

        let replaceDiv = document.createElement('div')
        foot.replaceChild(replaceDiv, firstbox)

        let newDiv = document.createElement('div')          
            foot.appendChild(newDiv)
            newDiv.innerHTML = '<button>Delete cookie</button>'
            
            let btn = document.querySelector('button')
            btn.addEventListener('click', () => {
              document.cookie = "acceptsCookies=true; max-age=-42"
              foot.removeChild(newDiv)
              foot.replaceChild(firstbox, replaceDiv)
            })              
     })
}