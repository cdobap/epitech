<?php
include_once("Animal.php");
class Canary extends Animal
{
    private $eggs;

    public function __construct($name, $legs = null, $type = null)
    {
        $legs = 2;
        $type = PARENT::BIRD;
        parent::__construct($name, $legs, $type);
        $this->eggs = 0;
        
        echo "Yellow and smart? Here I am!" .PHP_EOL;
    }

    public function getEggsCount()
    {
        return $this->eggs;
    }

    public function layEgg()
    {
        $this->eggs++;
    }


}