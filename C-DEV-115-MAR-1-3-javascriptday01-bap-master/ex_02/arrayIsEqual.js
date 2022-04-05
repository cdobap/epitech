
function arrayIsEqual(arr1, arr2)
{

   if(arr1.length != arr2.length) return false;

   
   var j = arr1.length;
   
   
   for(i=0; i<j; i++)
   {
      if(arr1[i] !== arr2[i])
      {
         return false;
      }
   }

   return true;
    
}

var a = [3, 4];
var b = [3, 4];

console.log(arrayIsEqual(a,b));
