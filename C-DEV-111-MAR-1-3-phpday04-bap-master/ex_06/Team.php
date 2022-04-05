<?php
include 'Astronaut.php';
class Team
{
    private $name;
    private $arrayAstronauts;
    

    public function __construct($teamName)
    {
        $this->name = $teamName;
    }

    public function getName()
    {
        return $this->name;
    }
    public function getAstronauts()
    {
        return $this->arrayAstronauts;
    }

    public function add($astronaut)
    {
        if ($astronaut instanceof Astronaut)
        {
            array_push($this->arrayAstronauts, $astronaut);
        }
        else 
        {
            echo $this->name .": Sorry, you are not part of the team.\n";
        }
    }

    public function remove($astronaut)
    {
        $key = array_search($astronaut, $this->arrayAstronauts);
        unset($this->arrayAstronauts[$key]);
    }

/*
a tester
*/


    public function countMembers()
    {
        $count = count($this->arrayAstronauts);
        return $count;
    }
/*
????
  ,  ,   . 
*/
    public function showMembers()
    {   
        if ($this->arrayAstronauts != null)
        {
            echo $this->name .": ";
            foreach ($this->arrayAstronauts as $astronaut)
            {
                echo $astronaut->getName() ." ";
                $bool = $astronaut->getOnMission();
                if ($bool = true)
                {
                    echo "on mission, ";
                }
                else 
                {
                    echo $astronaut->getName() ." on standby, ";
                }
            }
            echo ".\n";
        }
    }

}