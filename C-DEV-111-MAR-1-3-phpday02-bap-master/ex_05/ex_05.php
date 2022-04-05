<?php

function my_add_elem_map($key, $value, &$map)
{   
    if (isset($map[$key]))
    {
        echo "You have to give good parameters.\n";
    }
    else
    {
        $map[$key] = $value;
        return $map;
    }
}

function my_modify_elem_map($key, $value, &$map)
{
    if (isset($map[$key]))
    {
        $map[$key] = $value;
        return $map;
    }
    else
    {
        echo "You have to give good parameters.\n";
    }
}

function my_delete_elem_map($key, &$map)
{
    if (isset($map[$key]))
    {
        unset($map[$key]);
        return $map;
    }
    else
    {
        echo "You have to give good parameters.\n";
    }
}

function my_is_elem_valid($key, $value, &$map)
{
    if (isset($map[$key]) && $value === $map[$key])
    {
        return true;
    }
    else
    {
        echo "You have to give good parameters.\n";
        return false;
    }
}
