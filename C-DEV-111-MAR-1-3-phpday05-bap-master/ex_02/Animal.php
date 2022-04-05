<?php

class Animal
{
    const MAMMAL = 0;
    const FISH = 1;
    const BIRD = 2;

    private static $numberOfAnimalsAlive = 0;
    private static $numberOfMammals = 0;
    private static $numberOfFishes = 0;
    private static $numberOfBirds = 0;

    private $name;
    private $legs;
    private $type;

    public static function getNumberOfAnimalsAlive()
    {
        if (self::$numberOfAnimalsAlive == 1)
        {
            echo "There is currently " .self::$numberOfAnimalsAlive
                ." animal alive in our world.\n";            
        }
        else
        {
            echo "There are currently " .self::$numberOfAnimalsAlive
                ." animals alive in our world.\n";
        }
        return self::$numberOfAnimalsAlive;
    }

    public static function getNumberOfMammals()
    {
        if (self::$numberOfMammals == 1)
        {
            echo "There is currently " .self::$numberOfMammals
                ." mammal alive in our world.\n";            
        }
        else
        {
            echo "There are currently " .self::$numberOfMammals
                ." mammals alive in our world.\n";
        }
        return self::$numberOfMammals;
    }

    public static function getNumberOfFishes()
    {
        if (self::$numberOfFishes == 1)
        {
            echo "There is currently " .self::$numberOfFishes
                ." fish alive in our world.\n";            
        }
        else if (self::$numberOfFishes == 0)
        {
            echo "There are currently " .self::$numberOfFishes
                ." fish alive in our world.\n"; 
        }
        else
        {
            echo "There are currently " .self::$numberOfFishes
                ." fishes alive in our world.\n";
        }
        return self::$numberOfFishes;
    }

    public static function getNumberOfBirds()
    {
        if (self::$numberOfBirds == 1)
        {
            echo "There is currently " .self::$numberOfBirds
                ." bird alive in our world.\n";            
        }
        else
        {
            echo "There are currently " .self::$numberOfBirds
                ." birds alive in our world.\n";
        }
        return self::$numberOfBirds;
    }


    public function __construct($name, $numberOfLegs, $type)
    {
        $this->legs = $numberOfLegs;
        $this->setName($name);
        $this->setType($type);
        echo "My name is " .$this->getName() ." and I am a " 
            .$this->getType() ."!\n";
        self::$numberOfAnimalsAlive++;
        if ($type == self::MAMMAL)
        {
            self::$numberOfMammals++;
        }
        else if ($type == self::FISH)
        {
            self::$numberOfFishes++;
        }
        else if ($type == self::BIRD)
        {
            self::$numberOfBirds++;
        }
    }

    public function __destruct()
    {
        self::$numberOfAnimalsAlive--;
        if ($this->type == self::MAMMAL)
        {
            self::$numberOfMammals--;
        }
        else if ($this->type == self::FISH)
        {
            self::$numberOfFishes--;
        }
        else if ($this->type == self::BIRD)
        {
            self::$numberOfBirds--;
        }
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