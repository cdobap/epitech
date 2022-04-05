<?php
include_once("Shark.php");

class BlueShark extends Shark
{


    public function __construct($name, $legs = null, $type = null)
    {
        parent::__construct($name, $legs = null, $type = null);
    }

    public function eat($fish)
    {

        if ($fish->type == Animal::FISH && $fish != $this)
        {
            echo $this->name ." ate a " .$fish->getType() ." named " .$fish->name ."." .PHP_EOL;
            
            if ($this->getFrenzy() == true)
            {
                $this->smellBlood(false);
            }
            unset($fish);
        }
        else if ($fish == $this)
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

