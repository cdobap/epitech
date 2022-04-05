window.onload = function(){   
    let dropzone = document.querySelectorAll('footer div')[0]
    let canvas = document.querySelector('canvas')
    let writezone = document.querySelectorAll('footer div')[1]    
             
    var active = false
    var currentX = 0
    var currentY = 0
    var initialX
    var initialY    
    
    dropzone.addEventListener("mousedown", dragStart)
    dropzone.addEventListener("mousemove", drag)
    dropzone.addEventListener("mouseup", dragEnd)
    
    function dragStart(e) {      
      initialX = e.clientX - currentX // 700   700  0
      initialY = e.clientY - currentY       
    if (e.target === canvas) {
          active = true
        }
    }
    
    function drag(e) {
        if (active) {      
            currentX = e.clientX - initialX  //  100   800    700
            currentY = e.clientY - initialY        
            setTranslate(currentX, currentY, canvas)     
        }     
    }
    function setTranslate(xPos, yPos, el) {
        el.style.transform = "translate(" + xPos + "px, " + yPos + "px)"
    }         
    
    function dragEnd(e) {
        active = false
        if (e.target === canvas) {
            writezone.innerHTML = 'New coordinates => {x:'+e.clientX +', y:'+e.clientY+'}'
        }
    }          
}