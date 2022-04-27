<?php

class Validation{

    function CheckJSON($jsonString)
    {
        try{
            json_decode($jsonString ,  $associative=false, $depth=512, JSON_THROW_ON_ERROR);
            return true;
        }
        catch(Exception $e)
        {
            return false;
        }
    }


    function CheckExistance($data)
    {
        if(strcmp($data,"") == 0)
        {
            return false;
        }
        else
        {
            return true;
        }

    }

    function CheckAuthentication()
    {
        if(isset( $_POST['passcode'])){
        $ser = new backed();
        $passwords = $ser->GetDisticntRow("passwords","passcode");
        $notfound = true;
        foreach( $passwords as $password)
        {
            if(strcmp($password['passcode'], $_POST['passcode']) == 0)
            {
                return true;
                $notfound = false;
            }

        }
        if($notfound)
        {
            return false;
        }

    }
    else
    {return false;}
        

    
    }


}

?>