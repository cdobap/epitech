<?php
include 'Animal.php';
class Cat extends Animal
{
    private $color = "grey";

    public function __construct($name, $color = null, $legs = null, $type = null)
    {
        parent::__construct($name, $legs, $type);
         if ($color != null)
        {
            $this->setColor($color);
        } 
        
        $this->legs = 4;
        echo $this->getName() .": MEEEOOWWWW\n";
        
    }
    public function __destruct()
    {
        parent::__destruct();
    }

    public function getColor()
    {
        return $this->color;
    }
    public function setColor($color)
    {
        $this->color = $color;
    }

    public function meow()
    {
        echo $this->getName() ." the " .$this->color ." kitty is meowing.\n";
    }
}