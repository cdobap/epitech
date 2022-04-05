window.onload = function(){   
    let box = document.querySelector('footer div')
  
    box.addEventListener('click', (e) => {   
      color = Math.floor(Math.random() * (1000 - 100) + 100)
      console.log(color)
      box.style.backgroundColor = '#' +color
    }) 
}