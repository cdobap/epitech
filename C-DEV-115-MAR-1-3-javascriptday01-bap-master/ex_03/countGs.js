
function countGs(str)
{
    var count = 0;

    const split_str = str.split('');


    for(i = 0; i < split_str.length; i++)
    {
        if(split_str[i] == split_str[i].toUpperCase()) /*compte toutes les majuscules*/
        {
            if(split_str[i] === 'G') /*compte seulement les G*/
            {
                count++;
            }
        }

    }
    return count;
}

console.log(countGs('abcgGggGeaGfdsGG'));
