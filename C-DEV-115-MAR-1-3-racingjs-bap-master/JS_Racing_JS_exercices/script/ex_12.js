window.onload = function(){   
    let area = document.querySelector('footer div')
    
    console.log(window.localStorage)
    
    localStorage.setItem('ex12_img', 'https://www.coding-academy.fr/wp-content/uploads/2017/10/CODING_LOGO_CMJN.png')
    area.innerHTML = '<img style="width: 200px" src="' +localStorage.getItem('ex12_img') +'">'
}