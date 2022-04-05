window.onload = function(){   
    let result = document.querySelector('.result')
    let buttons = document.querySelector('.buttons')   

    let i = 0
    let op = "+"
    let j = 0 

    buttons.addEventListener('click', (e) => {
      if (e.target.matches('div')) {
        if(e.target.innerText == '0' || 
            e.target.innerText == '1' || 
            e.target.innerText == '2' || 
            e.target.innerText == '3' || 
            e.target.innerText == '4' || 
            e.target.innerText == '5' || 
            e.target.innerText == '6' || 
            e.target.innerText == '7' || 
            e.target.innerText == '8' || 
            e.target.innerText == '9')
        {
          if(op == '+'){
            i = e.target.innerText
            result.textContent = i      
            j += Number(e.target.innerText)   
            console.log(i)      
          }
          if(op == '-'){
            i = e.target.innerText
            result.textContent = i      
            j -= Number(e.target.innerText)   
            console.log(i)      
          }
          if(op == '/'){
            i = e.target.innerText
            result.textContent = i      
            j /= Number(e.target.innerText)   
            console.log(i)      
          }
          if(op == 'x'){
            i = e.target.innerText
            result.textContent = i      
            j *= Number(e.target.innerText)   
            console.log(i)      
          }
          if(op == '%'){
            i = e.target.innerText
            result.textContent = i      
            j %= Number(e.target.innerText)   
            console.log(i)      
          }
        }
        if(e.target.innerText == '+' || 
            e.target.innerText == '-' ||
            e.target.innerText == '/' || 
            e.target.innerText == 'x' || 
            e.target.innerText == '%'  )
        {        
          op = e.target.innerText
          result.textContent = op        
          console.log(op) 
        }
        if(e.target.innerText == '='){          
          console.log(j)
          result.textContent = j
        }
        if(e.target.innerText == 'C'){    
          j = 0      
          result.textContent = j
          console.log(j)
        }
      }      
    })
}