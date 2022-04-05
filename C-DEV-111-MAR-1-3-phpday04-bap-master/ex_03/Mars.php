<?php

namespace chocolate
{

    class Mars
    {
        private $id;
        private static $idCount = 0;
        
        public function getId()
        {
            return $this->id;
        }    
    
        public static function getIdCount()
        {
            return self::$idCount;
        }
    
        public function __construct()
        {
            $this->id = self::$idCount;
            self::$idCount++;
        }
    }

}

namespace planet
{
    class Mars
    {
        private $size;
        private $id;
        private static $idCount = 0;

        public function getId()
        {
            return $this->id;
        }
        public static function getIdCount()
        {
            return self::$idCount;
        }

        public function __construct($size = null)
        {            
            $this->id = self::$idCount;
            self::$idCount++;
            
            if ($size != null)
            {
               
                $this->setSize($size);
            }
        }

        public function getSize()
        {
            return $this->size;
        }

        public function setSize($size)
        {
            $this->size = $size;
        }
    }

}
