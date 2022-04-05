<?php

class Gecko
{
    private $name;
    private $Age;

    public function __construct($name = null, $age = null)
    {
        if ($name != null)
        {
        $this->name =$name;
        echo "Hello " . $name . " !\n";
        }
        else
        {
            echo "Hello !\n";
        }
        $this->setAge($age);
    }
    public function __destruct()
    {
        if ($this->name != null)
        {
            echo "Bye " .$this->getName() ." !\n";
        }
        else 
        {
            echo "Bye !\n";
        }
    }

    /*
    getter
    */
    public function getName()
    {
        return $this->name;
    }

    public function getAge()
    {
        return $this->Age;
    }

    /*
    setter
    */
    public function setAge($age)
    {
        $this->Age = $age;
    }


    /*
    */
    public function status()
    {
        switch ($this->Age)
        {
            case 0:
                echo "Unborn Gecko\n";
                break;
            case 1:
            case 2:
                echo "Baby Gecko\n";
                break;
            case 3:
            case 4:
            case 5:
            case 6:
            case 7:
            case 8:
            case 9:
            case 10:
                echo "Adult Gecko\n";
                break;
            case 11:
            case 12:
            case 13:
                echo "Old Gecko\n";
                break;
            default:
                echo "Impossible Gecko\n";
            
        }
    }

    public function hello($speech)
    {
        if (is_string($speech))
        {
            if ($this->name != null)
            {
            echo "Hello " . $speech . ", I'm " . $this->getName() . "!\n";
            }
            else
            {
                echo "Hello " .$speech ."!\n";
            }
        }
        else if (is_int($speech))
        {
            for ($i = 0; $i < $speech; $i++)
            {
                if ($this->name != null)
                {
                echo "Hello, I'm " .$this->getName() ."!\n";
                }
                else
                {
                echo "Hello !\n";
                }
            }
        }
        /*
        else    
        {
        }
        */
    }
}

