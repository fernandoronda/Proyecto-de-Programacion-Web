<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];

    if (empty($name) || strlen($name) < 2) {
        echo "El nombre es obligatorio y debe tener al menos 2 caracteres.";
        exit;
    }
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "El correo electrónico no es válido.";
        exit;
    }
    if (!preg_match("/^[0-9]{9,15}$/", $phone)) {
        echo "El teléfono debe contener entre 9 y 15 dígitos.";
        exit;
    }

    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "patagonia_travel";

    $conn = new mysqli($servername, $username, $password, $dbname);

    if ($conn->connect_error) {
        die("Conexión fallida: " . $conn->connect_error);
    }

    $stmt = $conn->prepare("INSERT INTO registros (nombre, email, telefono) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $name, $email, $phone);
    if ($stmt->execute() === TRUE) {
        echo "Registro exitoso";
    } else {
        echo "Error: " . $stmt->error;
    }

    $stmt->close();
    $conn->close();
}
?>