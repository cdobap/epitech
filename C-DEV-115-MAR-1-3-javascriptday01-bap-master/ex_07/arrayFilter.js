
function arrayFilter(array, test)
{
    var result = [];
    for(var element of array)
    {        
        if(test(element) == true)
        {
            result.push(element);
        }
    }
    return result;
}


// Your implementation
// Use this to test
var toFilter = [1, 2, 3, 4, 5, 6, 7, 8, 9];
// the anonymous function is the test your filtering function will use to
// make decision
var passed = arrayFilter(toFilter, function (value) {
return value % 3 === 0;
});
console.log(passed);

