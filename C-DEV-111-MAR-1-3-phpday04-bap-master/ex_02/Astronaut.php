<?php

class Astronaut
{
    private $name;
    private $snacks;
    private $destination;

    private $id;
    private static $idCount = 0;

    public function __construct($name)
    {
        $this->id = self::$idCount;
        self::$idCount++;
        $this->name = $name;
        $this->snacks = 0;
        $this->destination = null;
        $this->sayReadyForLaunch();
    }


    public function getId()
    {
        return $this->id;
    }
    public function getName()
    {
        return $this->name;
    }    
/* 
    public function getSnacks()
    {
        return $this->snacks;
    }
*/
  
    public function getDestination()
    {
        return $this->destination;
    }
/*
    public function setName($name)
    {
        $this->name = $name;
    }

    public function setSnacks($snacks)
    {
        $this->snacks = $snacks;
    }
    public function setDestination($dest)
    {
        $this->destination = $dest;
    }
*/
    public function sayReadyForLaunch()
    {
        echo $this->name ." ready for launch !\n";
    }

}
