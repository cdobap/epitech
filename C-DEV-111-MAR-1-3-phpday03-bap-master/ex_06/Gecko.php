<?php

class Gecko
{
    private $name;
    private $Age;
    private $energy = 100;

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

    public function getEnergy()
    {
        return $this->energy;
    }
    /*
    setter
    */
    public function setAge($age)
    {
        $this->Age = $age;
    }
    public function setEnergy($Energy)
    {
      
        $this->energy = $Energy;


        if ($this->energy > 100)
        {
            $this->energy = 100;
        }
        else if ($this->energy < 0)
        {
            $this->energy = 0;
        }
        
    }
    public function gainEnergy($i)
    {
        $this->energy += $i;

        if ($this->energy > 100)
        {
            $this->setEnergy(100);
        }
    }
    public function loseEnergy($i)
    {
        $this->energy -= $i;

        if ($this->energy < 0)
        {
            $this->setEnergy(0);
        }
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

    public function eat($string)
    {
        $meat = "Meat";
        $vegetable = "Vegetable";
        if (strcasecmp($string, $meat) == 0)
        {
            $this->gainEnergy(10);
            echo "Yummy!\n";
        }
        else if (strcasecmp($string, $vegetable) == 0)
        {
            $this->loseEnergy(10);
            echo "Erk!\n";
        }
        else
        {
            echo "I can't eat this.\n";
        }
        
    }
}

