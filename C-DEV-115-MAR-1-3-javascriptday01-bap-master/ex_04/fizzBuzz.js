
function fizzBuzz()
{
    var result = '';


    for (i=1; i<=20; i++)
    {
        if(i%3==0 && i%5!=0 )
        {
            result += 'Fizz, ';
        }
        else if(i%5==0 && i%3!=0 )
        {
            result += 'Buzz, ';
        }
        else if(i%5==0 && i%3==0 )
        {
            result += 'FizzBuzz, ';
        }
        else
        {
            result += i + ', ';
        }

    }

    result = result.slice(0, -2);
    
    console.log(result);
}

fizzBuzz();