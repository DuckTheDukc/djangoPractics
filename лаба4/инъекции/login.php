
<!-- незащищенный вход -->
<?php 
$connect=mysqli_connect(DB_HOST,DB_USERNAME,DB_PASSWORD,DB_NAME);

$query = "SELECT * FROM users WHERE username = '$_POST[username]' AND password = '$_POST[password]'";
$result = mysqli_query($connect, $query);

?>
<!-- защищенный вход -->
<?php

    $pdo = {
        try{
            return new \PDO('mysql:host=' . DB_HOST . ';port=' . DB_PORT . ';charset=utf8;dbname=' . DB_NAME, DB_USERNAME, DB_PASSWORD);
        }catch (\PDOException $e) {
            die("Connection error");
        }
    };

    $stmt = $pdo->prepare("SELECT * FROM user WHERE username=:username AND password=:password ");
    $stmt->execute(['username' => $username, 'password' => $password]);
    return $stmt->fetch(\PDO::FETCH_ASSOC);
?>


