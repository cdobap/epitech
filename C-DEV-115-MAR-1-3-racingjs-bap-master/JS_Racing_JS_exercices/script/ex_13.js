window.onload = function(){   
    let area = document.querySelector('footer div')

    area.innerHTML = '<img name="img12" style="width: 100%" src="' +localStorage.getItem('ex12_img') +'">'
    
    img = document.querySelector('img')
    
    img.addEventListener('click', ()=>{
      localStorage.removeItem('ex12_img')
    })
    
    
    area.addEventListener('mouseover', ()=>{
      function loop(){
        let i = img.style.width.slice(0, -1)
        let j = i*0.95
        console.log(j)
        img.style.width = j +'%'
      }
      let decrease = setInterval(loop, 1000)
      area.addEventListener('mouseleave', ()=>{
        clearInterval(decrease)
        img.style.width = '100%'
      })
    })  
}