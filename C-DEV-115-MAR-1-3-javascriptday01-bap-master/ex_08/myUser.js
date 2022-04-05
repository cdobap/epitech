
class myUser
{

    name = 'Bernard';
    age = 42;

    constructor(name, age)
    {
        if(name === null || isNaN(age) || age < 1)
        {
            console.log('bad params');
        }

        this.name = name;
        this.age = age;
    }

    printMe()
    {
        console.log('Hello, my name is ' + this.name + ' and I am '
                    + this.age + ' years old.');
    }
}

/* export { myUser }; */

albert = new myUser('Albert', 99);

albert.printMe();

