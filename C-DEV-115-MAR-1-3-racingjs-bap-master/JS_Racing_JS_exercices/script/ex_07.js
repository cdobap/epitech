window.onload = function(){   

    var canvas = document.querySelector('canvas')
    var ctx = canvas.getContext('2d')
  
      ctx.fillStyle = '#fff'
      ctx.beginPath()
      ctx.moveTo(6, 6)
      ctx.lineTo(14, 10)
      ctx.lineTo(6, 14)
      ctx.closePath()
  
      ctx.lineWidth = 1
      ctx.strokeStyle = '#fff'
      ctx.stroke()
  
  
   var pause = document.querySelectorAll('button')[0]
   var bstop = document.querySelectorAll('button')[1]
   var mute = document.querySelectorAll('button')[2]
  
  /*  https://dl.espressif.com/dl/audio/ff-16b-1c-44100hz.ogg */
   let audio = new Audio('example.ogg')
   
    canvas.addEventListener('click', (e) => {
      audio.loop = true
      audio.play()    
      
    })
    
    bstop.addEventListener('click', (e) => {
      audio.pause()
      audio.currentTime = 0
    })
    
    pause.addEventListener('click', (e) => {
      audio.pause()
    })
    
    mute.addEventListener('click', (e) => {   
      if(audio.muted == false){
        audio.muted = true  
        mute.innerHTML = "Unmute"     
      }   
      else{
        audio.muted = false
        mute.innerHTML = "Mute" 
      } 
    })

}