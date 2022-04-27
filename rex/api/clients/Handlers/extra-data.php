<?php

// If data is not there the $data is "No Data" , if there is a data parsing error the $Data is "Data Parse Error"
// if data is there .. The $data is respective data


if(isset($_POST['data'])) // Checking if data is set 
{

    if( $val->CheckExistance($_POST['data']) ) // All other common validation
    {
        if( $val->CheckJSON($_POST['data']) ) // JSON check for JSON
        $data =  $_POST['data'];
        else
        {
            $allow = false;
            $data = $error->ReportDocument("Data JSON Parse Error");
        }
    }
else
{
    $allow = false;
    $data =  $error->ReportDocument("Data Common Validation Error");
}

}
else
{
$allow = false;
$data = $error->ReportDocument("Data not set Error");
}


?>