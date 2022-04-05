<?php


class Astronaut
{
    private $name;
    private $snacks;
    
    private $destination;
    private $onMission = false;
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
    public function __destruct()
    {
        if ($this->destination != null)
        {
            echo $this->name .": Mission aborted !\n";
        }
        else 
        {
            echo $this->name .": I may have done nothing, but I have " 
                .$this->getSnacks() ." Mars to eat at least !\n";
        }
    }

    public function getId()
    {
        return $this->id;
    }

    public function getIdCount()
    {
        return self::$id;
    }
    public function getName()
    {        
        return $this->name;
    }     
    public function getSnacks()
    {
        return $this->snacks;
    }  
    public function getDestination()
    {
        return $this->destination;
    }
    public function getOnMission()
    {
        return $this->onMission;
    }
    
    public function setSnacks($snack)
    {
        $this->snacks = $snack;
    }
    public function setDestination($dest)
    {
        $this->destination = $dest;

    }
    public function setOnMission($bool)
    {
        $this->onMission = $bool;
    }

    public function eatSnack()
    {
        $this->snacks++;
    }
    public function doActions($param = null)
    {
        if ($param == null)
        {
            echo $this->getName() .": Nothing to do.\n";
        }
        else if ($param instanceof \planet\Mars)
        {
            echo $this->getName() .": started a mission !\n";
            $this->setDestination($param);
            $this->setOnMission(true);
        }
        else if ($param instanceof \chocolate\Mars)
        {
            $this->eatSnack();
            echo $this->getName() ." is eating mars number " .$param->getId() .".\n";
        }
    }


    public function sayReadyForLaunch()
    {
        echo $this->name ." ready for launch !\n";
    }

}
