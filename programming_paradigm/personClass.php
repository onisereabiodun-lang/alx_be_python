<?php

class Persion
{
    public function __contruct(private string $name, private int $age) {

    }

    public function greet() 
    {
        echo "Hello, my name is " . $this->name;
    }

    public function age()
    {
        echo "I'm " . $this->age . "year old.";
    }

}
