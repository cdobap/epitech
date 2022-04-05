<?php

class Animal
{
    const MAMMAL = 0;
    const FISH = 1;
    const BIRD = 2;

    private $name;
    private $legs;
    private $type;

    public function __construct($name, $numberOgLegs, $type)
    {
        $this->legs = $numberOgLegs;
        $this->setName($name);
        $this->setType($type);
        echo "My name is " .$this->getName() ." and I am a " 
            .$this->getType() ."!\n";
    }

    public function getName()
    {
        return $this->name;
    }
    public function getLegs()
    {
        return $this->legs;
    }
    public function getType()
    {   
        if ($this->type == 0)
        {
            return "mammal";
        }
        else if ($this->type == 1)
        {
            return "fish";
        }
        else if ($this->type == 2)
        {
            return "bird";
        }
    }

    public function setName($name)
    {
        $this->name = $name;
    }
    public function setType($type)
    {
        $this->type = $type;
    }
  
}