<?php


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

