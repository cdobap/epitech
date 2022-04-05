
function drawTriangle(numberOfLine)
{
    if(numberOfLine<1 || !Number.isInteger(numberOfLine))
    {
        console.log('param must be a positiv integer');
    }
    else
    { 
            for (let i=1; i<=numberOfLine; i++)
            {
                let j = i;
                let test = '$';
                console.log(test.repeat(j));
            }

    }
}

drawTriangle(8);