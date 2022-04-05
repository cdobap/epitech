<?php


function my_create_continent($continentNameToAdd, &$worldMap)
{    
    if (isset($worldMap[$continentNameToAdd]))
    {
        return $worldMap;
    }
    else
    {
        $worldMap[$continentNameToAdd] = null;    
        return $worldMap;
    }
}

function my_create_country($countryNameToAdd, $continentName, &$worldMap)
{    
    if (isset($worldMap[$continentName][$countryNameToAdd]))
    {
        return $worldMap;
    }
    else
    {
        $worldMap[$continentName][$countryNameToAdd] = null;
        return $worldMap;
    }
}

function my_create_city($cityNameToAdd, $postalCodeOfCityToAdd,
                             $countryName, $continentName, &$worldMap)
{   
    if (isset($worldMap[$continentName][$countryName][$cityNameToAdd])) 
    {
        return $worldMap;
    }
    else
    {
        $worldMap[$continentName][$countryName][$cityNameToAdd] = $postalCodeOfCityToAdd;
        return $worldMap;
    }
}                            




function my_get_countries_of_continent($continentName, $worldMap)
{       
    if (is_array($worldMap[$continentName]))
    {        
       print_r(array_keys($worldMap[$continentName]));      
    }
    else 
    {
        echo "Failure to get continent\n";
        return null;
    }
    

}

function my_get_cities_of_country($countryName, $continentName, $worldMap)
{
    if (isset($worldMap[$continentName][$countryName]))
    {             
        print_r(array_keys($worldMap[$continentName][$countryName])); 
    }
    else 
    {
        echo "Failure to get country\n";
        return null;
    }

}

function my_get_city_postal_code($cityName, $countryName, $continentName, 
                            $worldMap)
{
    if (isset($worldMap[$continentName][$countryName][$cityName]))
    {
        echo $worldMap[$continentName][$countryName][$cityName] ."\n";
    }
    else
    {
        echo "Failure to get city\n";
        return null;
    }
}

