<?php

function my_create_map(...$arrays)
{
   
            foreach ($arrays as $array)
            {        
                if ($array != NULL && count($array) >= 2 )
                {
                $map[$array[0]] = $array[1];
                }                
                else
                {
                    echo "The given arguments aren't valid.\n";
                    return NULL;
                }
            }
            return($map);
               
    
}

