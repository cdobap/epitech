<?php
include_once("Animal.php");
class Shark extends Animal
{   
    private $frenzy = false;

    public function __construct($name, $legs = null, $type = null)
    {
        $legs = 0;
        $type = PARENT::FISH;

        parent::__construct($name, $legs, $type);

        echo "A KILLER IS BORN!" .PHP_EOL;

    }

    public function getFrenzy()
    {
        return $this->frenzy;
    }
    public function smellBlood($bool)
    {
        $this->frenzy = $bool;
        return;
    }

    public function status()
    {
        if ($this->frenzy == true)
        {
            echo $this->name ." is smelling blood and wants to kill." .PHP_EOL;
        }
        else
        {
            echo $this->name ." is swimming peacefully." .PHP_EOL;
        }
    }

    public function eat($animal)
    {
        if ($animal instanceof Animal && $animal != $this)
        {
            echo $this->name ." ate a " .$animal->getType() ." named " .$animal->name ."." .PHP_EOL;
            
            if ($this->frenzy == true)
            {
                $this->smellBlood(false);
            }
            unset($animal);
        }
        else if ($animal == $this)
        {
            return;
        }
        else 
        {
            echo $this->name .": It's not worth my time." .PHP_EOL;
        }
        return;
    }

}