<?php

class Gecko
{
    private $name;

    public function __construct($name = null)
    {
        if ($name != null)
        {
        $this->name =$name;
        echo "Hello " . $name . " !\n";
        }
        else
        {
            echo "Hello !\n";
        }
    }
    public function __destruct()
    {
        if ($this->name != null)
        {
            echo "Bye " .$this->getName() ." !\n";
        }
        else 
        {
            echo "Bye !\n";
        }
    }

    public function getName()
    {
        return $this->name;
    }
}


