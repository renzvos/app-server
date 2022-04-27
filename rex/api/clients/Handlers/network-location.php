<?php




if(isset($_POST['net_loc'])) // Checking if data is set 
{

 if( $val->CheckExistance($_POST['net_loc']) ) // Checking all other validation
{
    
    if( $val->CheckJSON($_POST['net_loc']) )
        $net_loc =  $_POST['net_loc'];
    else
    {
        $allow = false;
        $data =  $data = $error->ReportDocument("Network Location JSON Parse Error");
    }
}else {$allow = false;   $data = $error->ReportDocument("Network Location Common Validation Error");;}

}
else{ $allow = false; $data = $error->ReportDocument("Network Location not set Error");; }





?>