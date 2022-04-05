window.onload = function(){   
    let input = document.querySelectorAll("footer div")[0]
    let output = document.querySelectorAll("footer div")[1]

    let str = ""
    input.addEventListener('keydown', (event) => {

      if(event.key == 'AltGraph' || event.key == 'Shift' || event.key == 'Delete' || event.key == 'Backspace'){
        
      }
      else{
        str +=  event.key  
        output.innerHTML = str
        if(str.substring(0, 3) === '[B]' && str.substring(str.length + -4) === '[/B]'){
         /*  console.log(str.substring(0, 3))
          console.log(str.substring(str.length + -4))   */        
          strB = str.substring(3, str.length + -4)
          output.innerHTML = strB.bold()
        }
        if(str.substring(0, 3) === '[U]' && str.substring(str.length + -4) === '[/U]'){
          strU = str.substring(3, str.length + -4)
          output.innerHTML = '<u>' +strU +'</u>'
        }
        if(str.substring(0, 3) === '[S]' && str.substring(str.length + -4) === '[/S]'){
          strS = str.substring(3, str.length + -4)
          output.innerHTML = '<del>' +strS +'</del>'
        }
        if(str.substring(0, 5) === 'LINK='){         
          /* console.log(str) */                  
          output.innerHTML = '<a href="'+str.substring(5)+'">'+str.substring(5)+'</a>'
        }
        if(str.substring(0, 6) === 'COLOR='){         
          /* console.log(str) */                  
          output.style.color = str.substring(6)
          output.innerHTML = str.substring(6)
        }
      }     
    })
}