window.onload = function(){   
        class Hero{
        name 
        genre
        magic 
        strenght
  
        constructor(name, genre, magic, strenght){
          name = name[0].toUpperCase() + name.substring(1)
          this.name = name 
          this.genre = genre 
          this.magic = magic 
          this.strenght = strenght 
        }        
        
        print(str){
          let e = document.querySelector('footer div')
          e.innerHTML += str
        }

        toString(){          
          if(this.genre == 'guerrier'){
            let str =  '"I am ' +this.name +' the Warrior, I have ' +this.magic 
            +' points in Magic and ' +this.strenght +' in Strenght !" '
            this.print(str)
          }
          if(this.genre == 'mage'){
            let str =  '"I am ' +this.name +' the Wizard, I have ' +this.magic 
            +' points in Magic and ' +this.strenght +' in Strenght !" '
            this.print(str)
          }
        }
      }
      var mage = new Hero("amadeus", "mage", 10, 3);
      var guerrier = new Hero("pontius", "guerrier", 3, 10);      
      mage.toString() 
      guerrier.toString()
}