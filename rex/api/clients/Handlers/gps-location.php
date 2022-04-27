<?php



if(isset($_POST['gps_loc'])) // Checking if data is set 
{
    if( $val->CheckExistance($_POST['gps_loc']) ) // Checking all other validation
        {
            if( $val->CheckJSON($_POST['gps_loc']) ) //Checking JSON 
                $gps_loc =  $_POST['gps_loc'];
            else
            {
                $allow = false;
                $data = $error->ReportDocument("GPS Location Parse Error");
            }
        }
        else
        {
            $allow = false;
            $data = $error->ReportDocument("GPS Location Validation Error");
        }
   
}
 else {$allow = false;  $data = $error->ReportDocument("Empty GPS Locaition Data");}


 


?>