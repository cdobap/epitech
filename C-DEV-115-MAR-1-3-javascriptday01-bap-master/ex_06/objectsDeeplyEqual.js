
function objectsDeeplyEqual(cmp1, cmp2)
{     
    return JSON.stringify(cmp1) === JSON.stringify(cmp2);
}


var obj = {here: {is: 'an'}, object: 2};


console.log(objectsDeeplyEqual(obj, obj));
console.log(objectsDeeplyEqual(obj, {here: 1, object: 2}));
console.log(objectsDeeplyEqual(obj, {here: {is: 'an'}, object: 2}));

