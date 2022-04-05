<?php

include_once("Shark.php");

class GreatWhite extends Shark
{

    public function __construct($name, $legs = null, $type = null)
    {
        parent::__construct($name, $legs = null, $type = null);
    }

    public function eat($food)
    {

        if ($food instanceof Animal && $food != $this && !$food instanceof Canary)
        {
            if($food instanceof Shark)
            {
                echo $this->getName() .": The best meal one could wish for." .PHP_EOL;
            }
            else
            {
                echo $this->name ." ate a " .$food->getType() ." named " .$food->name ."." .PHP_EOL;

            }
            
            unset($food);
            
            if ($this->getFrenzy() == true)
            {
                $this->smellBlood(false);
            }
        }
        else if ($food instanceof Canary)
        {
            echo "Next time you try to give me that to eat, I'll eat you instead." .PHP_EOL;
        }
        else if ($food == $this)
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