
function range(start, end, step)
{
    if(step === undefined)
    {
        var step = 1;
    }

    var result = [start];

    if(step > 0)
    {
        for(var i = start; i < end; i)
        {              
            i += step;     
            
            if (i > end)
            {
                return result;
            }
            result.push(i);        
        }
        return result;
    }
    else
    {
        for(var i = start; i > end; i)
        {              
            i += step;   
            
            if (i < end)
            {
                return result;
            }
            result.push(i);        
        }
        return result;
    }
}



console.log(range(1, 10, 2));

console.log(range(19, 22));

console.log(range(5, 2, -1));
