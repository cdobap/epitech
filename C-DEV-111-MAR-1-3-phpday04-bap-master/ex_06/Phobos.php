<?php
namespace planet\moon;

include 'Mars.php';

    class Phobos
    {
        private $mars;

        public function getMars()
        {
            return $this->mars;
        }

        public function __construct($objectFromMars)
        {
            if ($objectFromMars instanceof \planet\Mars)
            {
                $this->mars = $objectFromMars;
                echo "Phobos placed in orbit.\n";
            }
            else
            {
                echo "No planet given.\n";
            }
            
        }
        
    }
