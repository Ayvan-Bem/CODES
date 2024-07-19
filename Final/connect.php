<?php
$servername="localhost";
$username="root";
$password="";
$database_name="db_reservation";

$conn=mysqli_connect($servername, $username, $password, $database_name);


if(isset($_POST['Submit']))
{
    $Name = $_POST['Name'];
    $Number = $_POST['Number'];
    $Concert = $_POST['Concert'];
    $BOX = $_POST['BOX'];
    $Location = $_POST['Location'];

    $sql_query = "INSERT INTO `tbl_reservation`(`Ticket_Num`, `Name`, `Number`, `Concert`, `BOX`, `Location`)
     VALUES ('0', '$Name', '$Number', '$Concert', '$BOX', '$Location')";

    if (mysqli_query($conn, $sql_query))
    {
        //javascript
        function function_alert($message) {
      
        
            echo "<script>alert('$message');</script>";
        }
          
          
        
        function_alert("Reservation successful, please pay at your designated counter on SM Malls Near You!. Thankyou!");
    }
    else
    {
        echo "Error: " . $sql . "" . mysqli_error($conn);
    }
    mysqli_close($conn);
}
?>