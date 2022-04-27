<?php


if(isset($_POST['device'])) // Checking if data is set 
{
    if( $val->CheckExistance($_POST['device']) )
   {   
       if( $val->CheckJSON($_POST['device']) )
           $device =  $_POST['device'];
       else
       {
           $allow = false;
           $data = $error->ReportDocument("Device JSON Parse Error");
       }
   }
   else
   {
       $allow = false;
       $data = $error->ReportDocument("Device Data not set Error");
   }
  
}
else {$allow = false;   $data = $error->ReportDocument("Device Data not set Error");}







?>