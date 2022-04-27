<?php

class ErrorReport
{

    function __construct()
    {
        set_error_handler (
            function($errno, $errstr, $errfile, $errline) {
                $ser = new backed();
                $error["Error No"] = $errno;
                $error["Error String"] = $errstr;
                $error["Error File"] = $errfile;
                $error["Error Line"] = $errline;
                $data = $this->ReportDocument("PHP Error Catcher", json_encode($error) );
                $coulmn = ' `session_id`, `action` , `window` , `extra_data`, `tail` ' ;
                $values = "'1','Error','Server New Session','".$data."',NULL";
                $id = $ser->Insert("events",$coulmn,$values);    
            }
        );
    }
    function ReportDocument($name,$stack_trace =null)
    {
        $report['error-name'] = $name;
        $report['request-data'] = $_POST;
        if($stack_trace !== null)
        {
            $report['stack-trace'] = $stack_trace;
        }
        return json_encode($report);
    }

   




}

?>