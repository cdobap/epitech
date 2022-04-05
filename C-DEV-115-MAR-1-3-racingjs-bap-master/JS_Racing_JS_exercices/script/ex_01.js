window.onload = function(){
    var messageToEdit = document.querySelector('footer div')
    var newMessage = document.createElement('p')
    newMessage.innerHTML = 'Hello World'
    messageToEdit.parentNode.replaceChild(newMessage, messageToEdit)
    
}